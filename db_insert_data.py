from sqlalchemy.orm import Session
from db_engine import engine as engine
from db_schema import Weapons as Weapons
from za4_weapon_class import Weapon as weapon_props


# Insert data into table
with Session(engine) as session:
    for prop in weapon_props.set_weapon_props():
        weapon = Weapons(
            ammo_cost_black = prop.ammo_cost_black,
            ammo_cost_black_high_damage = prop.ammo_cost_black_high_damage,
            ammo_cost_red = prop.ammo_cost_red,
            ammo_cost_red_high_damage = prop.ammo_cost_red_high_damage,
            ammo_cost_standard = prop.ammo_cost_standard,
            ammo_cost_standard_high_damage = prop.ammo_cost_standard_high_damage,
            ammo_quantity_black = prop.ammo_quantity_black,
            ammo_quantity_black_high_damage = prop.ammo_quantity_black_high_damage,
            ammo_quantity_red = prop.ammo_quantity_red,
            ammo_quantity_red_high_damage = prop.ammo_quantity_red_high_damage,
            ammo_quantity_standard = prop.ammo_quantity_standard,
            ammo_quantity_standard_high_damage = prop.ammo_quantity_standard_high_damage,
            approx_drop_level_red = prop.approx_drop_level_red,
            approx_drop_level_standard = prop.approx_drop_level_standard,
            augmented_dps_black = prop.augmented_dps_black,
            augmented_dps_red = prop.augmented_dps_red,
            augmented_dps_standard = prop.augmented_dps_standard,
            augmented_pierce_dps_red = prop.augmented_pierce_dps_red,
            augmented_pierce_dps_standard = prop.augmented_pierce_dps_standard,
            blast_radius = prop.blast_radius,
            capacity_red = prop.capacity_red,
            capacity_standard = prop.capacity_standard,
            crafting_cost_alloy_black = prop.crafting_cost_alloy_black,
            crafting_cost_alloy_red = prop.crafting_cost_alloy_red,
            crafting_cost_alloy_standard = prop.crafting_cost_alloy_standard,
            crafting_cost_cash_black = prop.crafting_cost_cash_black,
            crafting_cost_cash_red = prop.crafting_cost_cash_red,
            crafting_cost_cash_standard = prop.crafting_cost_cash_standard,
            damage_type = prop.damage_type,
            damage_pellet_black = prop.damage_pellet_black,
            damage_pellet_red = prop.damage_pellet_red,
            damage_pellet_standard = prop.damage_pellet_standard,
            dot_pellet_black = prop.dot_pellet_black,
            dot_pellet_duration = prop.dot_pellet_duration,
            dot_pellet_red = prop.dot_pellet_red,
            dot_pellet_standard = prop.dot_pellet_standard,
            firing_mode = prop.firing_mode,
            manufacturer = prop.manufacturer,
            movement = prop.movement,
            pellets_shot = prop.pellets_shot,
            pierce_black = prop.pierce_black,
            pierce_dps_black = prop.pierce_dps_black,
            pierce_dps_red = prop.pierce_dps_red,
            pierce_dps_standard = prop.pierce_dps_standard,
            pierce_red = prop.pierce_red,
            pierce_standard = prop.pierce_standard,
            rate_of_fire = prop.rate_of_fire,
            reload_time = prop.reload_time,
            single_dps_black = prop.single_dps_black,
            single_dps_red = prop.single_dps_red,
            single_dps_standard = prop.single_dps_standard,
            weapon_class = prop.weapon_class,
            weapon_name = prop.weapon_name,
        )

        session.add_all([weapon])
        session.commit()
