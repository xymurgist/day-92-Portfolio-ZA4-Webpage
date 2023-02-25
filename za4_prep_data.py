from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import re


def create_weapons_list():
    """"Accepts list of weapons from scrape_za4_website(), filters results, returns the list"""
    try:
        with open('weapons_names.txt', 'r') as file:
            weapons_data = file.read()
            # print('Opening file...')
    except FileNotFoundError:
        elements_list = scrape_za4_website()
        with open('weapons_names.txt', 'w') as file:
            for weapon in elements_list:
                if weapon.text == 'Zombie Mech' or weapon.text == 'Zombdroid Soldier':
                    pass
                else:
                    file.write(f'{weapon.text}\n')

        with open('weapons_names.txt', 'r') as file:
            weapons_data = file.read()
            # print('File created...')
    finally:
        weapons_names = weapons_data.split('\n')
        weapons_list = weapons_names[:-1]
        return weapons_list


def scrape_za4_website():
    """Use Selenium to scrape SAS:ZA4 website to create and return a list of weapons; returned to create_weapons_file()"""

    # invoke webdriver and navigate to "SAS" homepage
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://saszombieassault.fandom.com/wiki/SAS:_Zombie_Assault_4')

    # navigate to "Weapons" webpage
    weapons_page_link = driver.find_element(By.LINK_TEXT, 'weapons')
    weapons_page_link.click()

    # search list of weapons to include only regular weapons that players can use (i.e., not npc-only, exclusive, nor purchasable)
    # I haven't yet figured out how to combine the two following search statements; is it possible?; is it advised?
    weapons_search_following = '//*[@id="Pistols_3"]/a/following::li/a'
    weapons_search_preceding = '//*[@id="Championship_Exclusive"]/a/preceding::li/a'
    weapons_links_following = driver.find_elements(By.XPATH, weapons_search_following)
    weapons_links_preceding = driver.find_elements(By.XPATH, weapons_search_preceding)

    # compare weapons lists and filter for intersecting items
    elements_list = [value for value in weapons_links_following if value in weapons_links_preceding]
    return elements_list


def scrape_weapon_table(weapon_name):
    """Use weapon_name with Pandas to scrape weapon's properties table; this will combine a pair of nested dicts inside one dict"""

    weapon_page = weapon_name.replace(' ', '_')
    ##### ===== TEST SINGLE WEAPON HERE; need to indent the TRY under the IF ===== #####
    # if weapon_name == 'HVM 001':
    try:
        weapon_table_df = pd.read_html(f'https://saszombieassault.fandom.com/wiki/{weapon_page}', match=weapon_name)
    except:
        print(f'{weapon_page} caused an error...')
    else:
        df_table_scraped = weapon_table_df[0]
        json_from_df = df_table_scraped.to_json(orient='columns', indent=4)
        dict_from_json = json.loads(json_from_df)

    return(dict_from_json)


def zip_dict_pairs(dict_from_json):
    """Create two lists from each dict, remove the first two unsused keys, then zip the two lists into one dict
    where the value from the first list becomes the key for its corresponding value from the second list
    then dump to a string for further formatting"""
    column1 = list(dict_from_json.values())[0].copy()
    column2 = list(dict_from_json.values())[1].copy()
    del column1['0']
    del column1['1']
    del column2['0']
    del column2['1']

    headers_list = []
    for val in column1.values():
        headers_list.append(val)

    data_list = []
    for val in column2.values():
        data_list.append(val)

    zipped_dict = dict(zip(headers_list, data_list))
    str_from_dict = json.dumps(zipped_dict)
    return str_from_dict


def regex_weapon_str(weapon_str):
    """Use regex to remove unnecessary characters, mitigate inconsistencies,
    and separate multiple values with commas, then convert str to dict with json.loads"""

    # the order of the following regex should be preserved; otherwise it will likely error
    remove_hvm = re.sub(r',|\s\[\?\]|for|\.0|\srps|%|\s\(Premium\sAmmo\)|\ssec', r'', weapon_str)
    replace_hvm = re.sub(r',(\d)', r'\1', remove_hvm)
    remove_trailblazer = re.sub(r'\s\d+\s\(Mobile\)|\s&|Works like a ', r'', replace_hvm)
    replace_trailblazer = re.sub(r'Semi-', r'Semi ', remove_trailblazer)
    remove_poison_claw = re.sub(r'\sover\s(\d)', r' \1', replace_trailblazer)
    remove_ria_313 = re.sub(r'PC:\s|Mobile:\s\d+|PC Mobile ', r'', remove_poison_claw)
    remove_cm_225 = re.sub(r'(Full)-(Auto)', r'\1 \2', remove_ria_313)
    remove_mustang = re.sub(r'\(\d+/clip\)', r'', remove_cm_225)
    remove_ria_7 = re.sub(r'\(\d+\.\d+kg\)', r'', remove_mustang)
    remove_ria_T7 = re.sub(r'/(\d)', r' \1', remove_ria_7)
    remove_ronson_65a = re.sub(r'fro', r'', remove_ria_T7)
    remove_cm_gigavolt = re.sub(r'(\d)onds', r'\1', remove_ronson_65a)
    remove_cm_440_titan = re.sub(r'Flash: 7 8 ', r'8', remove_cm_gigavolt)
    remove_cm_451_starburst = re.sub(r'\([Ss]team\)', r'', remove_cm_440_titan)
    replace_cm_451_starburst = re.sub(r'XXXX|XX00', r'0', remove_cm_451_starburst)
    remove_heartburn = re.sub(r'\sStandard|\sRPS', r'', replace_cm_451_starburst)
    remove_hardthorn = re.sub(r'\(Steam Version\)|\(mobile\)|\(6 on mobile\)', r'', remove_heartburn)
    replace_hardthorn = re.sub(r'6\s+(8)', r'\1', remove_hardthorn)
    remove_1887_shockfield = re.sub(r'\s/|\(\d+/mag\)|Still works like a ', r'', replace_hardthorn)
    remove_tombstone = re.sub(r'or\s400', r'', remove_1887_shockfield)
    remove_proposition = re.sub(r'\(400 in mobile\)|\(\d+kg\)', r'', remove_tombstone)
    replace_cm_800_jupiter = re.sub(r'(6)\s+/\s+', r'\1', remove_proposition)
    remove_t101_feldhaubitz = re.sub(r'\s+0.8\s+\(Mobile\)', r'', replace_cm_800_jupiter)
    remove_shredder = re.sub(r'\[2 Rps Mobile\]|24 \[MOBILE\]\s', r'', remove_t101_feldhaubitz)

    replace_free = re.sub(r'Free\s\sunlimited', r'0  0', remove_shredder)
    remove_x_period = re.sub(r'x\.', r'x', replace_free)
    correct_spaces = re.sub(r'\s+', r' ', remove_x_period)
    add_commas_btwn_digits = re.sub(r'\s(\d)', r', \1', correct_spaces)
    add_commas_btwn_quotes = re.sub(r'"\s"', r'", "', add_commas_btwn_digits)

    regex_complete = add_commas_btwn_quotes
    # print(f'Regex: {regex_complete}')
    weapon_dict = json.loads(regex_complete)
    return weapon_dict


def values_to_lists(weapon_dict):
    """Split each value with commas into a list"""
    for key in weapon_dict:
        if re.search(r',', weapon_dict[key]) is None:
            pass
        else:
            weapon_dict[key] = weapon_dict[key].split(', ')
    return weapon_dict


def values_to_int(values_as_lists):
    """Scan each value and list-items. If it is integer-like, convert to integer, else leave as a str"""
    for key in values_as_lists:
        value = values_as_lists[key]
        if type(value) == list:
            for item in value:
                # print(f'Item: {item}')
                if type(item) == str and re.match(r'-?\d+', item):
                    try:
                        value[value.index(item)] = int(item)
                    except ValueError:
                        value[value.index(item)] = float(item)
                else:
                    value[value.index(item)] = item
        elif type(value) == str and re.match(r'-?\d+', value):
            # print(f'Str to Int: {value}')
            try:
                values_as_lists[key] = int(value)
            except ValueError:    
                values_as_lists[key] = float(value)
        else:
            pass
    return values_as_lists


def map_values_to_keys(values_as_int):
    """Convert dict into lists to manipulate strings. For any value that is a list, 
    alter the key with meaningful strings, then pair with the associated list-item.
    Lastly, convert all list pairs into key:value pairs in a dict"""
    
    combo_lists = []

    for key in values_as_int:
        value = values_as_int[key]
        count = 1
        add_string = ''
        items_split = []

        # if value is not a list, create a list with the key and value
        if type(value) != list:
            if key == 'Approx Drop Level' or key == 'Augmented DPS' or key == 'Augmented Pierce DPS' or key == 'Capacity' or key == 'Damage/Pellet' or key == 'Pierce' or key == 'Pierce DPS' or key == 'Single DPS':
                key_changed = key + ' ' + 'Standard'
                items_split = list((key_changed, value))
                combo_lists.append(items_split)
            else:
                items_split = list((key, value))
                combo_lists.append(items_split)

        #if the value is a list, refactor each key so it can be used across each of its values, then pair the new key and its associated value
        elif key == 'Ammo Cost':
            key_cost = 'Ammo Cost'
            key_quantity = 'Ammo Quantity'
            
            if len(value) == 8:
                for item in value:
                    if count == 1 or count == 2 or count == 5 or count == 6:
                        add_string = 'Standard'
                    elif count == 3 or count == 4 or count == 7 or count == 8:
                        add_string = 'Red'

                    if count % 2 == 0:
                        key = key_quantity
                    else:
                        key = key_cost

                    if count == 5 or count == 6 or count == 7 or count == 8:
                        add_string = add_string + ' ' + 'High Damage'

                    count += 1
                    key_changed = key + ' ' + add_string
                    items_split = list((key_changed, item))
                    combo_lists.append(items_split)

            elif len(value) == 12:
                for item in value:
                    if count == 1 or count == 2 or count == 7 or count == 8:
                        add_string = 'Standard'
                    elif count == 3 or count == 4 or count == 9 or count == 10:
                        add_string = 'Red'
                    elif count == 5 or count == 6 or count == 11 or count == 12:
                        add_string = 'Black'

                    if count % 2 == 0:
                        key = key_quantity
                    else:
                        key = key_cost

                    if count == 7 or count == 8 or count == 9 or count == 10 or count == 11 or count == 12:
                        add_string = add_string + ' ' + 'High Damage'

                    count += 1
                    key_changed = key + ' ' + add_string
                    items_split = list((key_changed, item))
                    combo_lists.append(items_split)

        elif key == 'Crafting Cost':
            if len(value) == 4:
                for item in value:
                    if count == 1 or count == 2:
                        add_string = 'Cash'
                    elif count == 3 or count == 4:
                        add_string = 'Alloy'

                    if count == 1 or count == 3:
                        add_string = add_string + ' ' + 'Standard'
                    elif count == 2 or count == 4:
                        add_string = add_string + ' ' + 'Red'

                    count += 1
                    key_changed = key + ' ' + add_string
                    items_split = list((key_changed, item))
                    combo_lists.append(items_split)

            elif len(value) == 6:
                for item in value:
                    if count == 1 or count == 2 or count == 3:
                        add_string = 'Cash'
                    elif count == 4 or count == 5 or count == 6:
                        add_string = 'Alloy'

                    if count == 1 or count == 4:
                        add_string = add_string + ' ' + 'Standard'
                    elif count == 2 or count == 5:
                        add_string = add_string + ' ' + 'Red'
                    elif count == 3 or count == 6:
                        add_string = add_string + ' ' + 'Black'

                    count += 1
                    key_changed = key + ' ' + add_string
                    items_split = list((key_changed, item))
                    combo_lists.append(items_split)

        elif key == 'Total DoT/Pellet':
            key = 'DoT/Pellet'
            if len(value) == 4 and value[1] == 2:
                del value[1]
            
            if len(value) == 3:
                value.insert(1, value[0])

            if len(value) == 6:
                del value[3]
                del value[1]

            for item in value:
                if count == 1:
                    add_string = 'Standard'
                elif count == 2:
                    add_string = 'Red'
                elif count == 3:
                    add_string = 'Black'
                elif count == 4:
                    add_string = 'Duration'

                count += 1
                key_changed = key + ' ' + add_string
                items_split = list((key_changed, item))
                combo_lists.append(items_split)

        elif key == 'Single DPS' or key == 'Pierce DPS' or key == 'Augmented DPS' or key == 'Augmented Pierce DPS':
            if len(value) == 4:
                for item in value:
                    if count == 1:
                        add_string = 'Standard'
                    elif count == 2:
                        add_string = 'Red'
                    elif count == 3 or count == 4:
                        pass

                    count += 1
                    key_changed = key + ' ' + add_string
                    items_split = list((key_changed, item))
                    combo_lists.append(items_split)
            else:
                for item in value:
                    if count == 1:
                        add_string = 'Standard'
                    elif count == 2:
                        add_string = 'Red'
                    elif count == 3:
                        add_string = 'Black'

                    count += 1
                    key_changed = key + ' ' + add_string
                    items_split = list((key_changed, item))
                    combo_lists.append(items_split)

        else:
            for item in value:
                if count == 1:
                    add_string = 'Standard'
                elif count == 2:
                    add_string = 'Red'
                elif count == 3:
                    add_string = 'Black'

                count += 1
                key_changed = key + ' ' + add_string
                items_split = list((key_changed, item))
                combo_lists.append(items_split)
    # print(f'Combo Lists >>>\n{combo_lists}')

    # convert each list in combo_lists into key:value pairs for dictionary
    final_weapon_dict = {}
    for item in combo_lists:
        key_name = item[0]
        item_value = item[1]
        final_weapon_dict[key_name] = item_value
        if 'Ammo Used' in final_weapon_dict:
            del final_weapon_dict['Ammo Used']
    return final_weapon_dict


def prepare_data():
    all_weapons_dict = {}
    weapons_list = create_weapons_list()
    # print(f'Weapons List: {weapons_list}')
    for weapon_name in weapons_list:
        print(f'\n===Working on: {weapon_name} ===')
        if weapon_name == 'RIA 20 PARA':
            weapon_name = 'RIA 20 Para'
        if weapon_name == 'Sub-Light COM2':
            weapon_name = 'Sub-light COM2'
        if weapon_name == 'Rancor Hotspot':
            weapon_name = 'Hotspot'

        dict_from_json = scrape_weapon_table(weapon_name)
        # print(f'Dict from JSON: {dict_from_json}')

        if dict_from_json != None:
            weapon_str = zip_dict_pairs(dict_from_json)
            # print(f'Weapon Str: {weapon_str}\n')
            weapon_dict = regex_weapon_str(weapon_str)
            # print(f'Weapon Dict: {weapon_dict}\n')
            values_as_lists = values_to_lists(weapon_dict)
            # print(f'VasList: {values_as_lists}\n')
            values_as_int = values_to_int(values_as_lists)
            # print(f'VasInt: {values_as_int}\n')
            final_weapon_dict = map_values_to_keys(values_as_int)
            # print(f'Final Dict: {final_weapon_dict}\n')
        else:
            pass
            # print(f"Skipping {weapon_name}")
        final_weapon_dict['Weapon Name'] = weapon_name
        all_weapons_dict[weapon_name] = final_weapon_dict
    
    # save the full dict to a json file; eventually save to db instead
    with open('all_weapons.json', 'w') as file:
        json.dump(all_weapons_dict, file, indent=4)
        print('\n=== Complete weapons file created... ===\n')


# start data preparation
prepare_data()
