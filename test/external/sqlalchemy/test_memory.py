from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import db_url, meta

engine = create_engine(db_url, echo=True)
Session = sessionmaker(engine)
meta.create_all(engine)


def test_memory_create():
    with Session() as session:
        rows = session.execute("SELECT name FROM sqlite_master").all()

    assert rows[0][0] == "home"


def test_exist_table_in_other_method():
    with Session() as session:
        rows = session.execute("SELECT name FROM sqlite_master").all()

    assert rows[0][0] == "home"


def test_table_not_exist_in_new_engine():
    engine2 = create_engine(db_url, echo=True)
    Session2 = sessionmaker(engine2)

    with Session2() as session:
        rows = session.execute("SELECT name FROM sqlite_master").all()

    assert len(rows) == 0
