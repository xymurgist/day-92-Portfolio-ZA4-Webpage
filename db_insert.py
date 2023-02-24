from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
import db_schema as schema


# Insert data into table
with Session(schema.engine) as session:
    spongebob = schema.Weapons(
        name="spongebob",
        fullname="Spongebob Squarepants",

    )
    sandy = schema.Weapons(
        name="sandy",
        fullname="Sandy Cheeks",

    )
    patrick = schema.Weapons(name="patrick", fullname="Patrick Star")
    session.add_all([spongebob, sandy, patrick])
    session.commit()


# Select data from table
session = Session(schema.engine)
stmt = select(schema.Weapons).where(schema.Weapons.name.in_(["spongebob", "sandy"]))
for weapon in session.scalars(stmt):
    print(weapon)

