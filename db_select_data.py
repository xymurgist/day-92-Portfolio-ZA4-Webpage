from sqlalchemy.orm import Session
from sqlalchemy import select
from db_engine import engine as engine
from db_schema import Weapons as Weapons

session = Session(engine)

# Select data from table

stmt = select(Weapons)
# stmt = select(Weapons).where(Weapons.weapon_name == "HVM 001")
result = session.execute(stmt)
for item in result.scalars():
    print(item.manufacturer)
# print(result.all())

result2 = session.scalars(stmt)
for item in result2:
    print(item.weapon_name)
# print(result2.all())