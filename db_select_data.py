from sqlalchemy import select
from sqlalchemy.orm import Session
from db_engine import engine as engine
from db_schema import Weapons as Weapons

session = Session(engine)
stmt = select(Weapons)
result = session.scalars(stmt)


def all_weapons_properties():
    for prop in result:
        yield prop
