from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """SQLAlchemy's DeclarativeBase class for mapping"""
    pass


class Weapons(Base):
    """Maps the Weapons table's columns for use by Base to create the table and columns"""
    __tablename__ = "weapons"

    id: Mapped[int] = mapped_column(primary_key=True)
    ammo_cost_black: Mapped[int]
    ammo_cost_black_high_damage: Mapped[int]
    ammo_cost_red: Mapped[int]
    ammo_cost_red_high_damage: Mapped[int]
    ammo_cost_standard: Mapped[int]
    ammo_cost_standard_high_damage: Mapped[int]
    ammo_quantity_black: Mapped[int]
    ammo_quantity_black_high_damage: Mapped[int]
    ammo_quantity_red: Mapped[int]
    ammo_quantity_red_high_damage: Mapped[int]
    ammo_quantity_standard: Mapped[int]
    ammo_quantity_standard_high_damage: Mapped[int]
    approx_drop_level: Mapped[int]
    approx_drop_level_red: Mapped[int]
    approx_drop_level_standard: Mapped[int]
    augmented_dps: Mapped[int]
    augmented_dps_black: Mapped[int]
    augmented_dps_red: Mapped[int]
    augmented_dps_standard: Mapped[int]
    augmented_pierce_dps: Mapped[int]
    augmented_pierce_dps_red: Mapped[int]
    augmented_pierce_dps_standard: Mapped[int]
    blast_radius: Mapped[int]
    capacity: Mapped[int]
    capacity_red: Mapped[int]
    capacity_standard: Mapped[int]
    crafting_cost_alloy_black: Mapped[int]
    crafting_cost_alloy_red: Mapped[int]
    crafting_cost_alloy_standard: Mapped[int]
    crafting_cost_cash_black: Mapped[int]
    crafting_cost_cash_red: Mapped[int]
    crafting_cost_cash_standard: Mapped[int]
    damage_type: Mapped[str] = mapped_column(String(15))
    damage_pellet: Mapped[int]
    damage_pellet_black: Mapped[int]
    damage_pellet_red: Mapped[int]
    damage_pellet_standard: Mapped[int]
    dot_pellet_black: Mapped[int]
    dot_pellet_duration: Mapped[int]
    dot_pellet_red: Mapped[int]
    dot_pellet_standard: Mapped[int]
    firing_mode: Mapped[str] = mapped_column(String(30))
    manufacturer: Mapped[str] = mapped_column(String(35))
    movement: Mapped[int]
    pellets_shot: Mapped[int]
    pierce: Mapped[int]
    pierce_black: Mapped[int]
    pierce_dps: Mapped[int]
    pierce_dps_black: Mapped[int]
    pierce_dps_red: Mapped[int]
    pierce_dps_standard: Mapped[int]
    pierce_red: Mapped[int]
    pierce_standard: Mapped[int]
    rate_of_fire: Mapped[int]
    reload_time: Mapped[int]
    single_dps: Mapped[int]
    single_dps_black: Mapped[int]
    single_dps_red: Mapped[int]
    single_dps_standard: Mapped[int]
    weapon_class: Mapped[str] = mapped_column(String(15))
    weapon_name: Mapped[str] = mapped_column(String(25))


    def __repr__(self) -> str:
        return f"Weapons(id={self.id!r}, weapon_name={self.weapon_name!r})"


# Connects to database and creates the Weapons table with columns
engine = create_engine('postgresql://localhost/za4')
Base.metadata.create_all(engine)

