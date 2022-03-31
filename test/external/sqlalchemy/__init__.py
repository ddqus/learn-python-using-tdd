import os

from sqlalchemy import create_engine, Column, MetaData, Table, Integer
from sqlalchemy.orm import sessionmaker

db_url = os.getenv("SQLITE_DB_URL")
engine = create_engine(db_url, echo=True)
Session = sessionmaker(engine)

meta = MetaData()

home = Table(
    "home",
    meta,
    Column("id", Integer, primary_key=True),
)
