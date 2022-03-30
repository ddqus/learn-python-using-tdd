import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text, table, column, select

db_url = os.getenv("SQLITE_DB_URL")

engine = create_engine(db_url)
Session = sessionmaker(engine)


def test_db_url():
    assert db_url
    assert db_url.startswith("sqlite://")


def test_engine():
    assert engine
    with Session() as session:
        rows = session.execute("SELECT * FROM sqlite_master WHERE type='table'").all()
    assert not rows


def test_statement():
    assert str(text("SELECT 2 WHERE 1=:x")) == "SELECT 2 WHERE 1=:x"

    t = table("t", column("x"))
    s = select([t]).where(t.c.x == "'2")
    compiled = s.compile(compile_kwargs={"literal_binds": True})
    assert str(compiled) == "SELECT t.x \nFROM t \nWHERE t.x = '''2'"


def test_literal_binds():
    vals = (1, 2, 3)
    keys = ",".join([f":{k}" for k in vals])
    sql = text(f"SELECT 1 WHERE 2 IN ({keys})")
    assert str(sql.compile(compile_kwargs={"literal_binds": True})) == \
           "SELECT 1 WHERE 2 IN (NULL,NULL,NULL)"
