from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker

from . import db_url, meta

engine = create_engine(db_url, echo=True)
Session = sessionmaker(engine)
meta.create_all(engine)


def test_table_exist():
    with Session() as session:
        rows = session.execute("SELECT name FROM sqlite_master").all()

    assert rows[0][0] == "home"


def test_escape():
    escaped = String("").literal_processor(dialect=engine.dialect)(value="'a")
    assert escaped == "'''a'"


def test_escape_tuple():
    id = ("1", "'2")
    escaped_id = ",".join(
        [String("").literal_processor(dialect=engine.dialect)(value=k) for k in id]
    )
    assert escaped_id == "'1','''2'"


def test_in_with_manual_escape():
    id = ("1", "'2")
    escaped_id = ",".join(
        [String("").literal_processor(dialect=engine.dialect)(value=k) for k in id]
    )

    with Session() as session:
        sql = f"SELECT * FROM home WHERE id IN ({escaped_id})"
        rows = session.execute(sql).all()

    assert not rows
