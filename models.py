# Filename: models.py
# This contains Metadata Table Objects
# And Add to Table logic
########################################################################################################################
# 1 - Imports
from typing import Optional

from sqlalchemy import Column, Integer, String, Date, Float, and_
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


# wsl.continent
class Continent(Base):
    __tablename__ = 'continent'
    continent_id = Column(Integer, primary_key=True)
    continent = Column(String(length=20), unique=True)
    countries = relationship("Country")

    def __repr__(self):
        return f"Continent(id={self.continent_id!r}, " \
               f"name={self.continent!r})"


# wsl.country
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


# wsl.region
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


# wsl.city
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


# wsl.break
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
    events = relationship("Event")

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



# wsl.surfers
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
    heat_surfers = relationship("HeatSurfers")

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


# wsl.tour
class Tour(Base):
    __tablename__ = 'tour'
    tour_id = Column(Integer, primary_key=True)
    year = Column(Integer)
    gender = Column(String(length=6))
    tour_type = Column(String(length=50), nullable=False)
    tour_name = Column(String(length=50), nullable=False)
    events = relationship("Event")

    def __repr__(self):
        return f"tour_id={self.tour_id!r}, " \
               f"year={self.year!r}, " \
               f"gender={self.gender!r}, " \
               f"tour_type={self.tour_type!r}, " \
               f"tour_name={self.tour_name!r}"


# wsl.event
class Event(Base):
    __tablename__ = 'event'
    event_id = Column(Integer, primary_key=True)
    event_name = Column(String(length=50), nullable=False)
    tour_id = Column(Integer, ForeignKey('tour.tour_id'), nullable=False)
    stop_nbr = Column(Integer)
    break_id = Column(Integer, ForeignKey('break.break_id'), nullable=False)
    open_date = Column(Date)
    close_date = Column(Date)
    heat_details = relationship("HeatDetails")

    def __repr__(self):
        return f"event_id={self.event_id!r}, " \
               f"event_name={self.event_name!r}, " \
               f"tour_id={self.tour_id!r}, " \
               f"stop_nbr={self.stop_nbr!r}, " \
               f"break_id={self.break_id!r}, " \
               f"open_date={self.open_date!r}, " \
               f"close_date={self.close_date!r}"


# wsl.round
class Round(Base):
    __tablename__ = 'round'
    round_id = Column(Integer, primary_key=True)
    round = Column(String(length=32), nullable=False)
    heat_details = relationship("HeatDetails")

    def __repr__(self):
        return f"round_id={self.round_id!r}, " \
               f"round={self.even!r}"


# wsl.heat_details
class HeatDetails(Base):
    __tablename__ = 'heat_details'
    heat_id = Column(Integer, primary_key=True)
    heat_nbr = Column(String(length=10), nullable=False)
    event_id = Column(Integer, ForeignKey('event.event_id'), nullable=False)
    round_id = Column(Integer, ForeignKey('round.round_id'), nullable=False)
    wind = Column(String(length=32))
    heat_date = Column(Date)
    duration = Column(Integer)
    wave_min = Column(Integer)
    wave_max = Column(Integer)
    heat_surfers = relationship("HeatSurfers")
    heat_results = relationship("HeatResults")

    def repr__(self):
        return f"heat_id={self.heat_id!r}, " \
               f"heat_nbr={self.heat_nbr}, " \
               f"event_id={self.event_id!r}, " \
               f"round_id={self.round_id!r}, " \
               f"wind={self.wind!r}, " \
               f"heat_date={self.heat_date!r}, " \
               f"duration={self.duration!r}, " \
               f"wave_min={self.wave_min!r}, " \
               f"wave_max={self.wave_max!r}"


# wsl.heat_surfers
class HeatSurfers(Base):
    __tablename__ = 'heat_surfers'
    surfer_heat_id = Column(Integer, primary_key=True)
    heat_id = Column(Integer, ForeignKey('heat_details.heat_id'), nullable=False)
    surfer_id = Column(Integer, ForeignKey('surfers.surfer_id'), nullable=False)
    surfer_results = relationship("HeatResults")

    def __repr__(self):
        return f"surfer_heat_id={self.surfer_heat_id!r}, " \
               f"heat_id={self.heat_id!r}, " \
               f"surfer_id={self.surfer_id!r}"


# wsl.heat_results
class HeatResults(Base):
    __tablename__ = 'heat_results'
    heat_result_id = Column(Integer, primary_key=True)
    heat_id = Column(Integer, ForeignKey('heat_details.heat_id'), nullable=False)
    surfer_in_heat_id = Column(Integer, ForeignKey('heat_surfers.surfer_heat_id'), nullable=False)
    pick_to_win_percent = Column(Float)
    jersey_color = Column(String(length=32))
    status = Column(String(length=12))
    wave_1 = Column(Float)
    wave_2 = Column(Float)
    wave_3 = Column(Float)
    wave_4 = Column(Float)
    wave_5 = Column(Float)
    wave_6 = Column(Float)
    wave_7 = Column(Float)
    wave_8 = Column(Float)
    wave_9 = Column(Float)
    wave_10 = Column(Float)
    wave_11 = Column(Float)
    wave_12 = Column(Float)
    wave_13 = Column(Float)
    wave_14 = Column(Float)
    wave_15 = Column(Float)

    def __repr__(self):
        return f"heat_result_id={self.heat_result_id!r}, " \
               f"heat_id={self.heat_id!r}, " \
               f"surfer_in_heat_id={self.surfer_in_heat_id!r}, " \
               f"pick_to_win_percent={self.pick_to_win_percent!r}, " \
               f"jersey_color={self.jersey_color!r}, " \
               f"status={self.status!r}, " \
               f"wave_1={self.wave_1!r}, " \
               f"wave_2={self.wave_2!r}, " \
               f"wave_3={self.wave_3!r}, " \
               f"wave_4={self.wave_4!r}, " \
               f"wave_5={self.wave_5!r}, " \
               f"wave_6={self.wave_6!r}, " \
               f"wave_7={self.wave_7!r}, " \
               f"wave_8={self.wave_8!r}, " \
               f"wave_9={self.wave_9!r}, " \
               f"wave_10={self.wave_10!r}, " \
               f"wave_11={self.wave_11!r}, " \
               f"wave_12={self.wave_12!r}, " \
               f"wave_13={self.wave_13!r}, " \
               f"wave_14={self.wave_14!r}, " \
               f"wave_15={self.wave_15!r}"


#######################################################################################################################
# 4.0 - Table Manipulation

# Check to see if fields were entered and add to mysql tables
class AddLocation:
    def __init__(self,
                 entered_continent: Optional[str] = None,
                 entered_country: Optional[str] = None,
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

        self.entered_continent: Optional[str] = entered_continent
        self.entered_country: Optional[str] = entered_country
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

    word = 'Input Error'
    char = '='
    width = 50

    def was_continent_entered(self):
        if self.entered_continent is None or self.entered_continent == '':
            no_entry_error = (f"\n{self.word:{self.char}^{self.width}}\n" 
                              f"You seem a little lost. What continent are you on?\n" 
                              f"Continent cannot be None or an empty string.\n"
                              f"Your Entered: {self.entered_continent}")
        raise ValueError(no_entry_error)

    def was_country_entered(self):
        session = Session()

        # Check to see if a country was entered
        # If a country was entered does it already exist on the entered continent?
        if self.entered_continent is None or self.entered_continent == '':
            print(f"You seem a little lost. You're on the continent of {self.entered_continent}.")
            print(f"What country are you in?")
            return
        else:
            query = (select(Country.country_id)
                     .join(Continent, Continent.continent_id == Country.continent_id)
                     .where(and_(
                                  Continent.continent == self.entered_continent,
                                  Country.country == self.entered_country
                                )))
            result = session.execute(query)
            check_country = result.scalar()

            # Did the query return a country? If so it has already been added to wsl.country
            if check_country is not None:
                print(f"The country, {self.entered_country} "
                      f"has already been discovered on the continent, {self.entered_continent}.")
                return

    def was_region_entered(self):
        session = Session()

        # Check to see if a region was entered
        # If a region was entered does it already exist in the entered country and continent?
        if self.entered_region is None or self.entered_region == '':
            print(f"You seem a little lost. ")
            print(f"You are in the country, {self.entered_country} on the continent of {self.entered_continent}.")
            print(f"What region are you in? You entered: {self.entered_region}.")
            return
        else:
            # Does the entered region exist in the entered country on the entered continent?
            query = (select(Region.region_id)
                     .join(Country, Country.country_id == Region.country_id)
                     .join(Continent, Continent.continent_id == Country.continent_id)
                     .where(and_(
                                  Continent.continent == self.entered_continent,
                                  Country.country == self.entered_country,
                                  Region.region == self.entered_region
                                )))

            result = session.execute(query)
            check_region = result.scalar()

            # Did the query return a region? If so it has already been added to wsl.region.
            if check_region is not None:
                print(f"The region, {self.entered_region} in the country, {self.entered_country} "
                      f"on the continent, {self.entered_country} has already been discovered.")
                return

    def was_city_entered(self):
        session = Session()

        # Check to see if a city was entered
        # If a city was entered does it already exist in wsl.city for the entered region, country, and continent?
        if self.entered_city is None or self.entered_city == '':
            print(f"You seem a little lost. ")
            print(f"You are in {self.entered_region}, {self.entered_country} "
                  f"on the continent of {self.entered_continent}.")
            print(f"What city are you in? You entered: {self.entered_city}.")
            return
        else:
            # Does the entered city exist in the entered region, country, and continent?
            query = (select(City.city_id)
                     .join(Region, Region.region_id == City.region_id)
                     .join(Country, Country.country_id == Region.country_id)
                     .join(Continent, Continent.continent_id == Country.continent_id)
                     .where(and_(
                                  Continent.continent == self.entered_continent,
                                  Country.country == self.entered_country,
                                  Region.region == self.entered_region,
                                  City.city == self.entered_city
                                )))

            result = session.execute(query)
            check_city = result.scalar()

            # Did the query return a city? If so it has already been added to wsl.city
            if check_city is not None:
                print(f"{self.entered_city}, {self.entered_region}, {self.entered_country} "
                      f"on the continent of {self.entered_continent} has already been discovered.")
            return

    def was_break_name_entered(self):
        session = Session()

        # Check to see if a break name was entered
        # If a break name was entered does it already exist in wsl.break for the entered region, country, and continent?
        if self.entered_break_name is None or self.entered_break_name == '':
            print(f"You seem a little lost. ")
            print(f"You are in {self.entered_region}, {self.entered_country} "
                  f"on the continent of {self.entered_continent}.")
            print(f"What break are you at? You entered: {self.entered_break_name}.")
            return
        else:
            # Does the entered break exist in the entered region, country, and continent?
            query = (select(Break.break_id)
                     .join(Region, Region.region_id == Break.region_id)
                     .join(Country, Country.country_id == Region.country_id)
                     .join(Continent, Continent.continent_id == Country.continent_id)
                     .where(and_(
                                 Continent.continent == self.entered_continent,
                                 Country.country == self.entered_country,
                                 Region.region == self.entered_region,
                                 Break.break_name == self.entered_break_name
                                )))

            result = session.execute(query)
            check_break = result.scalar()

            # Did the query return a break? If so it has already been added to wsl.break
            if check_break is not None:
                print(f"The wave at {self.entered_break_name} in "
                      f"{self.entered_region}, {self.entered_country} "
                      f"on the continent of {self.entered_continent} has already been discovered.")
            return

    def add_new_country(self):
        session = Session()

        # Was a continent entered?
        self.was_continent_entered()

        # Was a country entered?
        self.was_country_entered()

        # Get continent_id from continent table
        query = (select(Continent.continent_id)
                 .where(Continent.continent == self.entered_continent))
        result = session.execute(query)
        entered_continent_id = result.scalar()

        # Create an instance of the Country class to add to wsl.country
        new_country = Country(continent_id=entered_continent_id,
                              country=self.entered_country)

        # Add the new country.
        session.add(new_country)
        session.flush()
        session.commit()

    def add_new_region(self):
        session = Session()

        # Was a continent entered?
        self.was_continent_entered()

        # Was a country entered?
        self.was_country_entered()

        # If a valid country was entered and does not already exist add it to wsl.country
        self.add_new_country()

        # Was a region entered?
        self.was_region_entered()

        # Get country_id from continent table
        # We need to run this query again incase a new country was added when checking the entered country
        query = (select(Country.country_id)
                 .join(Continent, Continent.continent_id == Country.continent_id)
                 .where(and_(
                              Continent.continent == self.entered_continent,
                              Country.country == self.entered_country
                            )))

        result = session.execute(query)
        entered_country_id = result.scalar()\

        # Create an instance of the Region class to add the new region to wsl.region.
        new_region = Region(country_id=entered_country_id,
                            region=self.entered_region)

        # Add the new region
        session.add(new_region)
        session.flush()
        session.commit()

    def add_new_city(self):
        session = Session()

        # Was a continent entered?
        self.was_continent_entered()

        # Was a country entered?
        self.was_country_entered()

        # If a valid country was entered and does not already exist add it to wsl.country
        self.add_new_country()

        # Was a region entered?
        self.was_region_entered()

        # If a valid region was entered and does not already exist add it to wsl.region
        self.add_new_region()

        # Was a city entered?
        self.was_city_entered()

        # Get region_id from continent table
        query = (select(Region.region_id)
                 .join(Country, Country.country_id == Region.country_id)
                 .join(Continent, Continent.continent_id == Country.continent_id)
                 .where(and_(
                             Region.region == self.entered_region,
                             Country.country == self.entered_country,
                             Continent.continent == self.entered_continent
                             )))
        result = session.execute(query)
        entered_region_id = result.scalar()

        new_city = City(region_id=entered_region_id,
                        city=self.entered_city)

        session.add(new_city)
        session.flush()
        session.commit()

    def add_new_break(self):
        session = Session()

        # Was a continent entered?
        self.was_continent_entered()

        # Was a country entered?
        self.was_country_entered()

        # If a valid country was entered and does not already exist add it to wsl.country
        self.add_new_country()

        # Was a region entered?
        self.was_region_entered()

        # If a valid region was entered and does not already exist add it to wsl.region
        self.add_new_region()

        # Was a city entered?
        self.was_break_name_entered()

        # Get region_id from continent table
        query = (select(Region.region_id)
                 .join(Country, Country.country_id == Region.country_id)
                 .join(Continent, Continent.continent_id == Country.continent_id)
                 .where(and_(
                  Region.region == self.entered_region,
                  Country.country == self.entered_country,
                  Continent.continent == self.entered_continent
                 )))
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


# class AddSurfer:
#     def __init__(self,
#                  entered_gender: str = None,
#                  entered_first_name: str = None,
#                  entered_last_name: str = None,
#                  entered_stance: Optional[str] = None,
#                  entered_rep_country: str = None,
#                  entered_birthday: Optional = None,
#                  entered_height: Optional[int] = None,
#                  entered_weight: Optional[int] = None,
#                  entered_first_season: Optional[int] = None,
#                  entered_first_tour: Optional[str] = None,
#                  entered_home_country: Optional[str] = None,
#                  entered_home_region: Optional[str] = None,
#                  entered_home_city: Optional[str] = None
#                  ):
#
#         self.entered_gender: str = entered_gender
#         self.entered_first_name: str = entered_first_name
#         self.entered_last_name: str = entered_last_name
#         self.entered_stance: Optional[str] = entered_stance
#         self.entered_rep_country: str = entered_rep_country
#         self.entered_birthday: Optional = entered_birthday
#         self.entered_height: Optional[int] = entered_height
#         self.entered_weight: Optional[int] = entered_weight
#         self.entered_first_season: Optional[int] = entered_first_season
#         self.entered_first_tour: Optional[str] = entered_first_tour
#         self.entered_home_country: Optional[str] = entered_home_country
#         self.entered_home_region: Optional[str] = entered_home_region
#         self.entered_home_city: Optional[str] = entered_home_city
#
#     def add_new_surfer(self):
#         session = Session()
#
#         # Check that gender is entered
#         if self.entered_gender is None or self.entered_gender == '':
#             print(f"You have to choose a gender because of biology and shit.")
#             return
#
#         # Check that first_name is entered
#         if self.entered_first_name is None or self.entered_first_name == '':
#             print(f"What is the surfer's first name?")
#             return
#
#         # Check that last_name is entered
#         if self.entered_last_name is None or self.entered_last_name == '':
#             print(f"What is the surfer's last name?")
#             return
#
#         # Check that a rep country is entered
#         if self.entered_rep_country is None or self.entered_rep_country == '':
#             print(f"What country is the surfer representing?")
#             return
#
#         # If a home city is entered check that a home region is entered
#         city_is_entered = self.entered_home_city is not None
#         region_is_none = self.entered_home_region is None
#         region_is_empty = self.entered_home_region == ''
#         if city_is_entered and (region_is_none or region_is_empty):
#             print(f"What region is the surfer's home town in?")
#             return
#
#         # If a home city is entered check that a home country is entered
#         country_is_none = self.entered_home_country is None
#         country_is_empty = self.entered_home_country == ''
#         if city_is_entered and (country_is_none or country_is_empty):
#             print(f"What country is the surfer's home town in?")
#             return
#
#         # Check to see if the entered_surfer exists
#         query = (select(Surfers.surfer_id)
#                  .join(Country, Country.country_id == Surfers.rep_country_id)
#                  .where(and_(
#                              Surfers.gender == self.entered_gender,
#                              Surfers.first_name == self.entered_first_name,
#                              Surfers.last_name == self.entered_last_name,
#                              Country.country == self.entered_rep_country
#                             )))
#         result = session.execute(query)
#         check_surfer = result.scalar()
#
#         if check_surfer is not None:
#             print(f"{self.entered_first_name} {self.entered_last_name} "
#                   f"of {self.entered_rep_country} has already been added.")
#             return
#
#         # Get country_id from the country table
#         query = (select(Country.country_id)
#                  .where(Country.country == self.entered_rep_country))
#         result = session.execute(query)
#         entered_rep_country_id = result.scalar()
#
#         # Get city_id from the city table
#         if self.entered_home_city is None or self.entered_home_city == '':
#             entered_city_id = None
#         else:
#             query = (select(City.city_id)
#                      .join(Region, Region.region_id == City.region_id)
#                      .join(Country, Country.country_id == Region.country_id)
#                      .where(and_(
#                                  City.city == self.entered_home_city,
#                                  Region.region == self.entered_home_region,
#                                  Country.country == self.entered_home_country
#                                 )))
#             result = session.execute(query)
#             entered_city_id = result.scalar()
#
#         new_surfer = Surfers(gender=self.entered_gender,
#                              first_name=self.entered_first_name,
#                              last_name=self.entered_last_name,
#                              stance=self.entered_stance,
#                              rep_country_id=entered_rep_country_id,
#                              birthday=self.entered_birthday,
#                              height=self.entered_height,
#                              weight=self.entered_weight,
#                              first_season=self.entered_first_season,
#                              first_tour=self.entered_first_tour,
#                              home_city_id=entered_city_id)
#
#         session.add(new_surfer)
#         session.flush()
#         session.commit()
#
#
# class AddTour:
#     def __init__(self,
#                  entered_year: Optional[int] = None,
#                  entered_gender: Optional[str] = None,
#                  entered_tour_type: Optional[str] = None,
#                  entered_tour_name: Optional[str] = None,
#                  entered_event_name: Optional[str] = None,
#                  entered_stop_nbr: Optional[int] = None,
#                  entered_country: Optional[str] = None,
#                  entered_region: Optional[str] = None,
#                  entered_break_name: Optional[str] = None,
#                  entered_open_date: Optional = None,
#                  entered_close_date: Optional = None,
#                  entered_round: Optional[str] = None,
#                  entered_heat_nbr: Optional[str] = None,
#                  entered_wind: Optional[str] = None,
#                  entered_heat_date: Optional = None,
#                  entered_duration: Optional[int] = None,
#                  entered_wave_min: Optional[int] = None,
#                  entered_wave_max: Optional[int] = None,
#                  entered_pick_to_win_percent: Optional[float] = None,
#                  entered_jersey_color: Optional[str] = None,
#                  entered_status: Optional[str] = None,
#                  entered_wave_1: Optional[float] = None,
#                  entered_wave_2: Optional[float] = None,
#                  entered_wave_3: Optional[float] = None,
#                  entered_wave_4: Optional[float] = None,
#                  entered_wave_5: Optional[float] = None,
#                  entered_wave_6: Optional[float] = None,
#                  entered_wave_7: Optional[float] = None,
#                  entered_wave_8: Optional[float] = None,
#                  entered_wave_9: Optional[float] = None,
#                  entered_wave_10: Optional[float] = None,
#                  entered_wave_11: Optional[float] = None,
#                  entered_wave_12: Optional[float] = None,
#                  entered_wave_13: Optional[float] = None,
#                  entered_wave_14: Optional[float] = None,
#                  entered_wave_15: Optional[float] = None):
#
#         self.entered_year: Optional[int] = entered_year
#         self.entered_gender: Optional[str] = entered_gender
#         self.entered_tour_type: Optional[str] = entered_tour_type
#         self.entered_tour_name: Optional[str] = entered_tour_name
#         self.entered_event_name: Optional[str] = entered_event_name
#         self.entered_stop_nbr: Optional[int] = entered_stop_nbr
#         self.entered_country: Optional[str] = entered_country
#         self.entered_region: Optional[str] = entered_region
#         self.entered_break_name: Optional[str] = entered_break_name
#         self.entered_open_date: Optional = entered_open_date
#         self.entered_close_date: Optional = entered_close_date
#         self.entered_round: Optional[str] = entered_round
#         self.entered_heat_nbr: Optional[str] = entered_heat_nbr
#         self.entered_wind: Optional[str] = entered_wind
#         self.entered_heat_date: Optional = entered_heat_date
#         self.entered_duration: Optional[int] = entered_duration
#         self.entered_wave_min: Optional[int] = entered_wave_min
#         self.entered_wave_max: Optional[int] = entered_wave_max
#         self.entered_pick_to_win_percent: Optional[float] = entered_pick_to_win_percent
#         self.entered_jersey_color: Optional[str] = entered_jersey_color
#         self.entered_status: Optional[str] = entered_status
#         self.entered_wave_1: Optional[float] = entered_wave_1
#         self.entered_wave_2: Optional[float] = entered_wave_2
#         self.entered_wave_3: Optional[float] = entered_wave_3
#         self.entered_wave_4: Optional[float] = entered_wave_4
#         self.entered_wave_5: Optional[float] = entered_wave_5
#         self.entered_wave_6: Optional[float] = entered_wave_6
#         self.entered_wave_7: Optional[float] = entered_wave_7
#         self.entered_wave_8: Optional[float] = entered_wave_8
#         self.entered_wave_9: Optional[float] = entered_wave_9
#         self.entered_wave_10: Optional[float] = entered_wave_10
#         self.entered_wave_11: Optional[float] = entered_wave_11
#         self.entered_wave_12: Optional[float] = entered_wave_12
#         self.entered_wave_13: Optional[float] = entered_wave_13
#         self.entered_wave_14: Optional[float] = entered_wave_14
#         self.entered_wave_15: Optional[float] = entered_wave_15
#
#     def add_new_tour(self):
#         session = Session()
#
#         # Check that the tour type has been entered
#         if self.entered_tour_type is None or self.entered_tour_type == '':
#             print(f"What type of tour is being added?")
#             return
#
#         # Check that a year has been entered
#         if self.entered_year is None or self.entered_year == '':
#             print(f"What year did this tour take place?")
#             return
#
#         # Check to see if the tour already exists
#         query = (select(Tour.tour_id)
#                  .where(and_(
#                              Tour.year == self.entered_year,
#                              Tour.gender == self.entered_gender,
#                              Tour.tour_type == self.entered_tour_type
#                             )))
#
#         result = session.execute(query)
#         check_tour = result.scalar()
#
#         # Does the entered_country exist in the entered_continent
#         if check_tour is not None:
#             print(f"The {self.entered_year} {self.entered_gender}s {self.entered_tour_type} has already been added.")
#             return
#
#         entered_tour_name = f"{self.entered_year} {self.entered_gender}s {self.entered_tour_type}"
#
#         new_tour = Tour(year=self.entered_year,
#                         gender=self.entered_gender,
#                         tour_type=self.entered_tour_type,
#                         tour_name=entered_tour_name)
#
#         session.add(new_tour)
#         session.flush()
#         session.commit()
#
#     def add_new_event(self):
#         session = Session()
#
#         # Check that the tour name has been entered
#         if self.entered_tour_name is None or self.entered_tour_name == '':
#             print(f"Which tour are you trying to add an event to?")
#             return
#
#         # Check that the event name has been added
#         if self.entered_event_name is None or self.entered_event_name == '':
#             print(f"What is the name of the event you are adding?")
#             return
#
#         # Check that the stop number has been added
#         if self.entered_stop_nbr is None:
#             print(f"What stop number is this event? You entered: {self.entered_stop_nbr}")
#             return
#
#         # Check that the Country, Region, and Break were added
#         if self.entered_country is None or self.entered_country == '':
#             print(f"What country was this even in?")
#             return
#
#         if self.entered_region is None or self.entered_region == '':
#             print(f"What region of {self.entered_country} was this event in?")
#             return
#
#         if self.entered_break_name is None or self.entered_break_name == '':
#             print(f"What is the name of the break?")
#             return
#
#         # Check to see if the entered_event exists in the entered_tour
#         query = (select(Event.event_name)
#                  .join(Tour, Tour.tour_id == Tour.tour_id)
#                  .where(
#                  and_(
#                       Tour.tour_name == self.entered_tour_name,
#                       Event.stop_nbr == self.entered_stop_nbr
#                       )))
#
#         result = session.execute(query)
#         check_event = result.scalar()
#
#         # Does the entered_event exist in the entered_tour
#         if check_event is not None:
#             print(f"The event {self.entered_event_name} "
#                   f"in the {self.entered_tour_name} has already been added.")
#             return
#
#         # Get tour_id from tour table
#         query = (select(Tour.tour_id)
#                  .where(Tour.tour_name == self.entered_tour_name))
#         result = session.execute(query)
#         entered_tour_id = result.scalar()
#
#         # Get break_id from break table
#         query = (select(Break.break_id)
#                  .join(Region, Break.region_id == Region.region_id)
#                  .join(Country, Region.country_id == Country.country_id)
#                  .where(and_(
#                              Break.break_name == self.entered_break_name,
#                              Region.region == self.entered_region,
#                              Country.country == self.entered_country
#                             )))
#         result = session.execute(query)
#         entered_break_id = result.scalar()
#
#         new_event = Event(event_name=self.entered_event_name,
#                           tour_id=entered_tour_id,
#                           stop_nbr=self.entered_stop_nbr,
#                           break_id=entered_break_id,
#                           open_date=self.entered_open_date,
#                           close_date=self.entered_close_date)
#
#         session.add(new_event)
#         session.flush()
#         session.commit()
#
#     def add_new_round(self):
#         session = Session()
#
#         # Check that text is entered for round
#         if self.entered_round is None or self.entered_round == '':
#             print(f"What is the name of the round you are creating?")
#             return
#
#         # Create an instance of the Round class to add to wsl.round
#         new_round = Round(round=self.entered_round)
#
#         session.add(new_round)
#         session.flush()
#         session.commit()
#
#     def add_new_heat_details(self):
#         session = Session()
#
#         # Check to see if tour name is entered
#         if self.entered_tour_name is None or self.entered_tour_name == '':
#             print(f"Which tour are you trying to add an event to?")
#             return
#
#
#         # Check to see if event name is entered
#         if self.entered_event_name is None or self.entered_event_name == '':
#             print(f"What is the name of the event you are adding?")
#             return
#         else:
#             # If it is entered see if it exists for the tour entered
#             query = (select(Event.event_name)
#                 .join(Tour, Tour.tour_id == Tour.tour_id)
#                 .where(
#                 and_(
#                     Tour.tour_name == self.entered_tour_name,
#                     Event.stop_nbr == self.entered_stop_nbr
#                 )))
#
#             result = session.execute(query)
#             check_event = result.scalar()
#
#             # Does the entered_event exist in the entered_tour
#             if check_event is not None:
#                 print(f"The event {self.entered_event_name} "
#                       f"in the {self.entered_tour_name} has already been added.")
#                 return
#
#
#         # Check to see if round is entered
#         # Get Round id
#
#
#         # Check to see if heat nbr is entered for tour, event, round above
#
#     def add_new_surfers_to_heat(self):
#         session = Session()
#
#         # Check to see if tour name is entered
#         if self.entered_tour_name is None or self.entered_tour_name == '':
#             print(f"Which tour are you trying to add an event to?")
#             return
#
#
#         # Check to see if event name is entered for tour entered
#
#
#         # Check to see if round is entered
#
#
#         # Check to see id heat nbr is ented for tour, event, and round
#         # Get Heat id
#
#
#         # Check if surfer first and last name is entered
#         # Get Surfer id
#
#     def add_new_heat_results(self):
#         session = Session()
#
#         # Check to see if tour is entered
#         if self.entered_tour_name is None or self.entered_tour_name == '':
#             print(f"Which tour are you trying to add an event to?")
#             return
#
#         # Check to see if event is entered for tour entered
#
#
#         # Check to see if round is entered
#
#
#         # Check to see that heat nbr is entered
#         # Get Heat id
#
#
#         # Check to see if surfer first and last name is entered
#         # Get surfer id
#

########################################################################################################################
# 5.0 - Testing


# Enter a New Country
inst = AddLocation(
                   entered_country="Australia")
inst.add_new_country()


# # Enter a New Region
# inst = AddLocation(entered_continent='North America',
#                    entered_country='Australia',
#                    entered_region='North Carolina')
#
# inst.add_new_region()


# # Enter a New City
# inst = AddLocation(entered_continent='North America',
#                    entered_country='USA',
#                    entered_region='California',
#                    entered_city='North Shore')
#
# inst.add_new_city()

# # Enter a New Break
# inst = AddLocation(entered_continent='North America',
#                    entered_country='California',
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

# # Enter a New Surfer
# inst = AddSurfer(entered_gender='Male',
#                  entered_first_name='John John',
#                  entered_last_name='Florence',
#                  entered_stance='Regular',
#                  entered_rep_country='Hawaii',
#                  entered_birthday='1992-10-18',
#                  entered_height=168,
#                  entered_weight=79,
#                  entered_first_season=2008,
#                  entered_first_tour='Qualifying Series',
#                  entered_home_country='Hawaii',
#                  entered_home_region='Oahu',
#                  entered_home_city='North Shore')
# inst.add_new_surfer()

# # Enter a New Tour
# inst = AddTour(entered_year=2022,
#                entered_gender='Men',
#                entered_tour_type='Championship Tour')
# inst.add_new_tour()

# # Enter a New Event
# inst = AddTour(entered_tour_name='2022 Mens Championship Tour',
#                entered_event_name='Billabong Prop Pipeline',
#                entered_stop_nbr=1,
#                entered_country='Hawaii',
#                entered_region='Oahu',
#                entered_break_name='Pipeline',
#                entered_open_date='2022-01-29',
#                entered_close_date='2022-02-10')
# inst.add_new_event()
