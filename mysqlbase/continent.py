from sqlalchemy import Column, String, Integer, Date
from base import Base


# Create and map the Continent table
class Continent(Base):
    __tablename__ = 'continent'

    continent_id = Column(Integer, primary_key=True)
    continent = Column(String(length=30))

    def __init__(self, continent):
        self.continent = continent
