import json
from pprint import pprint

class Weapon:
  def __init__(self, **kw):
    self.ammo_cost_black = kw.get('Ammo Cost Black', '0')
    self.ammo_cost_black_high_damage = kw.get('Ammo Cost Black High Damage', '0')
    self.ammo_cost_red = kw.get('Ammo Cost Red', '0')
    self.ammo_cost_red_high_damage = kw.get('Ammo Cost Red High Damage', '0')
    self.ammo_cost_standard = kw.get('Ammo Cost Standard', '0')
    self.ammo_cost_standard_high_damage = kw.get('Ammo Cost Standard High Damage', '0')
    self.ammo_quantity_black = kw.get('Ammo Quantity Black', '0')
    self.ammo_quantity_black_high_damage = kw.get('Ammo Quantity Black High Damage', '0')
    self.ammo_quantity_red = kw.get('Ammo Quantity Red', '0')
    self.ammo_quantity_red_high_damage = kw.get('Ammo Quantity Red High Damage', '0')
    self.ammo_quantity_standard = kw.get('Ammo Quantity Standard', '0')
    self.ammo_quantity_standard_high_damage = kw.get('Ammo Quantity Standard High Damage', '0')
    self.approx_drop_level = kw.get('Approx Drop Level', '0')
    self.approx_drop_level_red = kw.get('Approx Drop Level Red', '0')
    self.approx_drop_level_standard = kw.get('Approx Drop Level Standard', '0')
    self.augmented_dps = kw.get('Augmented DPS', '0')
    self.augmented_dps_black = kw.get('Augmented DPS Black', '0')
    self.augmented_dps_red = kw.get('Augmented DPS Red', '0')
    self.augmented_dps_standard = kw.get('Augmented DPS Standard', '0')
    self.augmented_pierce_dps = kw.get('Augmented Pierce DPS', '0')
    self.augmented_pierce_dps_red = kw.get('Augmented Pierce DPS Red', '0')
    self.augmented_pierce_dps_standard = kw.get('Augmented Pierce DPS Standard', '0')
    self.blast_radius = kw.get('Blast Radius', '0')
    self.capacity = kw.get('Capacity', '0')
    self.capacity_red = kw.get('Capacity Red', '0')
    self.capacity_standard = kw.get('Capacity Standard', '0')
    self.crafting_cost_alloy_black = kw.get('Crafting Cost Alloy Black', '0')
    self.crafting_cost_alloy_red = kw.get('Crafting Cost Alloy Red', '0')
    self.crafting_cost_alloy_standard = kw.get('Crafting Cost Alloy Standard', '0')
    self.crafting_cost_cash_black = kw.get('Crafting Cost Cash Black', '0')
    self.crafting_cost_cash_red = kw.get('Crafting Cost Cash Red', '0')
    self.crafting_cost_cash_standard = kw.get('Crafting Cost Cash Standard', '0')
    self.damage_pellet = kw.get('Damage/Pellet', '0')
    self.damage_pellet_black = kw.get('Damage/Pellet Black', '0')
    self.damage_pellet_red = kw.get('Damage/Pellet Red', '0')
    self.damage_pellet_standard = kw.get('Damage/Pellet Standard', '0')
    self.damage_type = kw.get('Damage Type', 'n/a') # string
    self.dot_pellet_black = kw.get('DoT/Pellet Black', '0')
    self.dot_pellet_duration = kw.get('DoT/Pellet Duration', '0')
    self.dot_pellet_red = kw.get('DoT/Pellet Red', '0')
    self.dot_pellet_standard = kw.get('DoT/Pellet Standard', '0')
    self.firing_mode = kw.get('Firing Mode', 'n/a') # string
    self.manufacturer = kw.get('Manufacturer', 'n/a') # string
    self.movement = kw.get('Movement', '0')
    self.pellets_shot = kw.get('Pellets/shot', '0')
    self.pierce = kw.get('Pierce', '0')
    self.pierce_black = kw.get('Pierce Black', '0')
    self.pierce_dps = kw.get('Pierce DPS', '0')
    self.pierce_dps_black = kw.get('Pierce DPS Black', '0')
    self.pierce_dps_red = kw.get('Pierce DPS Red', '0')
    self.pierce_dps_standard = kw.get('Pierce DPS Standard', '0')
    self.pierce_red = kw.get('Pierce Red', '0')
    self.pierce_standard = kw.get('Pierce Standard', '0')
    self.rate_of_fire = kw.get('Rate of Fire', '0')
    self.reload_time = kw.get('Reload Time', '0')
    self.single_dps = kw.get('Single DPS', '0')
    self.single_dps_black = kw.get('Single DPS Black', '0')
    self.single_dps_red = kw.get('Single DPS Red', '0')
    self.single_dps_standard = kw.get('Single DPS Standard', '0')
    self.weapon_class = kw.get('Weapon Class', 'n/a') # string
    self.weapon_name = kw.get('Weapon Name', 'n/a') # string

with open('all_weapons.json', 'r') as file:
  weapons = json.load(file)

for key in weapons:
  if key == 'HVM 001':
    props = weapons[key]

weapon = Weapon(**props)
pprint(vars(weapon))

