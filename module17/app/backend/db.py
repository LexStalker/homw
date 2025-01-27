from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

from sqlalchemy import create_engine
engine = create_engine("sqlite:///taskmanager.db", echo=True)

class Base(DeclarativeBase):
    pass
