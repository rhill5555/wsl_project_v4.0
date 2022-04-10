from sqlalchemy import Column, String, Integer, Date
from base import Base


# Create and map the Country table
class Country(Base):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True)
    continent = Column(String(length=30))

    def __init__(self, country):
        self.country = country