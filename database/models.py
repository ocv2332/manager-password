from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Password(Base):
    __tablename__ = "password"

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
