from typing import Optional
from sqlmodel import select


def add_beer_to_database() -> bool:
    with get_session() as session:

    return True
