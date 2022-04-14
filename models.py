# Filename: models.py
# This contains Metadata Table Objects
# And Add to Table logic
########################################################################################################################
# 1 - Imports
from typing import Optional

from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy import create_engine, select, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# 2 - Connection to mysql and create base

# 2.1 - Connection String
conn_str = 'mysql+pymysql://Heather:#LAwaItly19@localhost:3306/wsl'

# 2.2 - SQLAlchemy engine that will interact with mysql database
engine = create_engine(conn_str, echo=True)

# 2.3 - SQLAlchemy ORM session that binds to the engine
Session = sessionmaker(bind=engine)

# 2.4 - Base MetaData Object
Base = declarative_base()

########################################################################################################################
# 3.0 - MetaData Table Object


class Continent(Base):
    __tablename__ = 'continent'
    continent_id = Column(Integer, primary_key=True)
    continent = Column(String(length=20), unique=True)
    countries = relationship("Country")

    def __repr__(self):
        return f"Continent(id={self.continent_id!r}, " \
               f"name={self.continent!r})"


class Country(Base):
    __tablename__ = 'country'
    country_id = Column(Integer, primary_key=True)
    country = Column(String(length=50))
    continent_id = Column(Integer, ForeignKey('continent.continent_id'), nullable=False)
    regions = relationship("Region")
    surfers = relationship("Surfers")

    def __repr__(self):
        return f"Country(id={self.country_id!r}, " \
               f"continent_id={self.continent_id!r}, " \
               f"name={self.country!r})"


class Region(Base):
    __tablename__ = 'region'
    region_id = Column(Integer, primary_key=True)
    region = Column(String(length=50))
    country_id = Column(Integer, ForeignKey('country.country_id'), nullable=False)
    cities = relationship("City")
    break_names = relationship("Break")

    def __repr__(self):
        return f"Region(id={self.region_id!r}, " \
               f"country_id={self.country_id!r}, " \
               f"name={self.region!r}"


class City(Base):
    __tablename__ = 'city'
    city_id = Column(Integer, primary_key=True)
    city = Column(String(length=50))
    region_id = Column(Integer, ForeignKey('region.region_id'), nullable=False)
    surfers = relationship("Surfers")

    def __repr__(self):
        return f"City(city_id={self.city_id!r}, " \
               f"region_id={self.region_id!r}, " \
               f"name={self.city!r}"


class Break(Base):
    __tablename__ = 'break'
    break_id = Column(Integer, primary_key=True)
    break_name = Column(String(50))
    region_id = Column(Integer, ForeignKey('region.region_id'), nullable=False)
    break_type = Column(String(length=32))
    reliability = Column(String(length=32))
    ability = Column(String(length=32))
    shoulder_burn = Column(String(length=32))
    clean = Column(Float)
    blown_out = Column(Float)
    too_small = Column(Float)

    def __repr__(self):
        return f"Break(break_id={self.break_id!r}, " \
               f"break_name={self.break_name!r}, " \
               f"region_id={self.region_id!r} ", \
               f"break_type={self.break_type!r}, " \
               f"reliability={self.reliability!r}, " \
               f"ability={self.ability!r}, " \
               f"shoulder_burn={self.shoulder_burn!r}, " \
               f"clean={self.clean!r}, " \
               f"blown_out={self.blown_out!r}, " \
               f"too_small={self.too_small!r}, " \


class Surfers(Base):
    __tablename__ = 'surfers'
    surfer_id = Column(Integer, primary_key=True)
    gender = Column(String(length=6), nullable=False)
    first_name = Column(String(length=50), nullable=False)
    last_name = Column(String(length=50), nullable=False)
    stance = Column(String(length=10))
    rep_country_id = Column(Integer, ForeignKey('country.country_id'), nullable=False)
    birthday = Column(Date)
    height = Column(Integer)
    weight = Column(Integer)
    first_season = Column(Integer)
    first_tour = Column(String(length=50))
    home_city_id = Column(Integer, ForeignKey('city.city_id'), nullable=False)

    def __repr__(self):
        return f"surfer_id={self.surfer_id!r}, " \
               f"gender={self.gender!r}, " \
               f"first_name={self.first_name!r}, " \
               f"last_name={self.last_name!r}, " \
               f"stance={self.stance!r}, " \
               f"rep_country_id={self.rep_country_id!r}, " \
               f"birthday={self.birthday!r}, " \
               f"height={self.height!r}, " \
               f"weight={self.weight!r}, " \
               f"first_season={self.first_season!r}, " \
               f"first_tour={self.first_tour!r}, " \
               f"home_city_id={self.home_city_id!r}"


class Tour(Base):
    __tablename__ = 'tour'
    tour_id = Column(Integer, primary_key=True)
    year = Column(Integer)
    gender = Column(String(length=6))
    tour_type = Column(String(length=50), nullable=False)
    tour_name = Column(String(length=50), nullable=False)

    def __repr__(self):
        return f"tour_id={self.tour_id!r}, " \
               f"year={self.year!r}, " \
               f"gender={self.gender!r}, " \
               f"tour_type={self.tour_type!r}, " \
               f"tour_name={self.tour_name!r}"

########################################################################################################################
# 4.0 - Table Manipulation


class AddLocation:
    def __init__(self,
                 entered_continent: str,
                 entered_country: str,
                 entered_region: Optional[str] = None,
                 entered_city: Optional[str] = None,
                 entered_break_name: Optional[str] = None,
                 entered_break_type: Optional[str] = None,
                 entered_reliability: Optional[str] = None,
                 entered_ability: Optional[str] = None,
                 entered_shoulder_burn: Optional[str] = None,
                 entered_clean: Optional[float] = 0,
                 entered_blown_out: Optional[float] = 0,
                 entered_too_small: Optional[float] = 0):

        self.entered_continent = entered_continent
        self.entered_country = entered_country
        self.entered_region: Optional[str] = entered_region
        self.entered_city: Optional[str] = entered_city
        self.entered_break_name: Optional[str] = entered_break_name
        self.entered_break_type: Optional[str] = entered_break_type
        self.entered_reliability: Optional[str] = entered_reliability
        self.entered_ability: Optional[str] = entered_ability
        self.entered_shoulder_burn: Optional[str] = entered_shoulder_burn
        self.entered_clean: Optional[float] = entered_clean
        self.entered_blown_out: Optional[float] = entered_blown_out
        self.entered_too_small: Optional[float] = entered_too_small

    def add_new_country(self):
        session = Session()

        # Check to see if the entered_continent exists
        query = (select(Country.country)
                 .where(Country.country == self.entered_country)
                 )
        result = session.execute(query)
        check_country = result.scalar()

        # Does the entered_country exist in the entered_continent
        if check_country is not None:
            print(f"The country of {self.entered_country} has already been discovered.")
            return

        # Get continent_id from continent table
        query = (select(Continent.continent_id)
                 .where(Continent.continent == self.entered_continent))
        result = session.execute(query)
        entered_continent_id = result.scalar()

        new_country = Country(continent_id=entered_continent_id, country=self.entered_country)

        session.add(new_country)
        session.flush()
        session.commit()

    def add_new_region(self):
        session = Session()

        # Since entered_region is not required check to see if it has been entered
        if self.entered_region is None:
            print(f"You didn't enter a region.")
            return

        self.add_new_country()

        # Check to see if the entered_region exists
        query = (select(Region.region)
                 .where(Region.region == self.entered_region)
                 )
        result = session.execute(query)
        check_region = result.scalar()

        # Does the entered_region exist in the entered_continent
        if check_region is not None:
            print(f"The region of {self.entered_region} "
                  f"in the country of {self.entered_country} has already been discovered.")
            return

        # Get country_id from continent table
        query = (select(Country.country_id)
                 .where(Country.country == self.entered_country))
        result = session.execute(query)
        entered_country_id = result.scalar()

        new_region = Region(country_id=entered_country_id, region=self.entered_region)

        session.add(new_region)
        session.flush()
        session.commit()

    def add_new_city(self):
        session = Session()

        # Since entered_region is not required check to see if it has been entered
        if self.entered_region is None:
            print('')
            print(f"You didn't enter a region.")
            print('')
            return

        # Since entered_city is not required check to see if it has been entered
        if self.entered_city is None:
            print('')
            print(f"You didn't enter a city.")
            print('')
            return

        # Add Country and Region if necessary
        self.add_new_region()

        # Check to see if the entered_cityexists
        query = (select(City.city)
                 .where(City.city == self.entered_city)
                 )
        result = session.execute(query)
        check_city = result.scalar()

        # Does the entered_region exist in the entered_continent
        if check_city is not None:
            print('')
            print(f"The city of {self.entered_city} "
                  f"in {self.entered_region}, {self.entered_country} has already been discovered.")
            print('')
            return

        # Get region_id from continent table
        query = (select(Region.region_id)
                 .where(Region.region == self.entered_region))
        result = session.execute(query)
        entered_region_id = result.scalar()

        new_city = City(region_id=entered_region_id, city=self.entered_city)

        session.add(new_city)
        session.flush()
        session.commit()

    def add_new_break(self):
        session = Session()

        # Since entered_region is not required check to see if it has been entered
        if self.entered_region is None:
            print('')
            print(f"You didn't enter a region.")
            print('')
            return

        # Since entered_break is not required check to see if it has been entered
        if self.entered_break_name is None:
            print('')
            print(f"You didn't enter a break name.")
            print('')
            return

        # Add Country and Region if necessary
        self.add_new_region()

        # Check to see if the entered_break exists
        query = (select(Break.break_name)
                 .where(Break.break_name == self.entered_break_name)
                 )
        result = session.execute(query)
        check_break_name = result.scalar()

        # Does the entered_region exist in the entered_continent
        if check_break_name is not None:
            print('')
            print(f"The wave at {self.entered_break_name} "
                  f"in {self.entered_region}, {self.entered_country} has already been discovered.")
            print('')
            return

        # Get region_id from continent table
        query = (select(Region.region_id)
                 .where(Region.region == self.entered_region))
        result = session.execute(query)
        entered_region_id = result.scalar()

        new_break = Break(break_name=self.entered_break_name,
                          region_id=entered_region_id,
                          break_type=self.entered_break_type,
                          reliability=self.entered_reliability,
                          ability=self.entered_ability,
                          shoulder_burn=self.entered_shoulder_burn,
                          clean=self.entered_clean,
                          blown_out=self.entered_blown_out,
                          too_small=self.entered_too_small)

        session.add(new_break)
        session.flush()
        session.commit()


class AddSurfer:
    def __init__(self,
                 entered_gender: str = None,
                 entered_first_name: str = None,
                 entered_last_name: str = None,
                 entered_stance: str = None,
                 entered_rep_country: str = None,
                 entered_birthday=None,
                 entered_height: int = None,
                 entered_weight: int = None,
                 entered_first_season: int = None,
                 entered_first_tour: str = None,
                 entered_home_city: str = None
                 ):

        self.entered_gender: str = entered_gender
        self.entered_first_name: str = entered_first_name
        self.entered_last_name: str = entered_last_name
        self.entered_stance: str = entered_stance
        self.entered_rep_country: str = entered_rep_country
        self.entered_birthday = entered_birthday
        self.entered_height: int = entered_height
        self.entered_weight: int = entered_weight
        self.entered_first_season: int = entered_first_season
        self.entered_first_tour: str = entered_first_tour
        self.entered_home_city: str = entered_home_city

    def add_new_surfer(self):
        session = Session()

        # Check to see if the entered_continent exists
        query = (select(Surfers.surfer_id)
                 .where(Surfers.gender == self.entered_gender)
                 .and_(Surfers.first_name == self.entered_first_name)
                 .and_(Surfers.last_name == self.entered_last_name)
                 .and_(Surfers.rep_country_id == self.entered_rep_country)
                 )
        result = session.execute(query)
        check_surfer = result.scalar()

        # Does the entered_country exist in the entered_continent
        if check_surfer is not None:
            print(f"{self.entered_first_name} {self.entered_last_name} of {self.entered_rep_country} has already been added.")
            return

        # Get country_id from the country table
        query = (select(Country.country_id)
                 .where(Country.country == self.entered_rep_country))
        result = session.execute(query)
        entered_country_id = result.scalar()

        # Get city_id from the city table
        query = (select(City.city_id)
                 .where(City.city == self.entered_home_city))
        result = session.execute(query)
        entered_city_id = result.scalar()

        new_surfer = Surfers(gender=self.entered_gender,
                             first_name=self.entered_first_name,
                             last_name=self.entered_last_name,
                             stance=self.entered_stance,
                             rep_country_id=entered_country_id,
                             birthday=self.entered_birthday,
                             height=self.entered_height,
                             weight=self.entered_weight,
                             first_season=self.entered_first_season,
                             first_tour=self.entered_first_tour,
                             home_city_id=entered_city_id)

        session.add(new_surfer)
        session.flush()
        session.commit()

########################################################################################################################
# 5.0 - Testing

# # Enter a New Country
# inst = AddLocation(entered_continent='Oceania', entered_country="Australia")
# inst.add_new_country()

# # Enter a New Region
# inst = AddLocation(entered_continent='North America',
#                   entered_country='Hawaii',
#                   entered_region='Oahu')
#
# inst.add_new_region()


# # Enter a New City
# inst = AddLocation(entered_continent='North America',
#                   entered_country='Hawaii',
#                   entered_region='Oahu',
#                   entered_city='North Shore')
#
# inst.add_new_city()

# # Enter a New Break
# inst = AddLocation(entered_continent='North America',
#                    entered_country='Hawaii',
#                    entered_region='Oahu',
#                    entered_break_name='Pipeline',
#                    entered_break_type='Reef',
#                    entered_reliability='Consistent',
#                    entered_ability=None,
#                    entered_shoulder_burn=None,
#                    entered_clean=44,
#                    entered_blown_out=36,
#                    entered_too_small=20)
#
# inst.add_new_break()

# Enter a New Surfer
inst = AddSurfer()