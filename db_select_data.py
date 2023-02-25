from sqlalchemy.orm import Session
from sqlalchemy import select
from db_engine import engine as engine
from db_schema import Weapons as Weapons

session = Session(engine)

stmt = select(Weapons).where(Weapons.name.in_(["spongebob", "sandy"]))

for user in session.scalars(stmt):
    print(user)


# Select data from table
# session = Session(schema.engine)
# stmt = select(schema.Weapons).where(schema.Weapons.name.in_(["spongebob", "sandy"]))
# for weapon in session.scalars(stmt):
#     print(weapon)
