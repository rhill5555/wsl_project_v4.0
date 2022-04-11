from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, UniqueConstraint, select
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


conn_str = 'mysql+pymysql://Heather:#LAwaItly19@localhost:3306/wsl'

# SQLAlchemy engine that will interact with mysql database
engine = create_engine(conn_str, echo=True)

# SQLAlchemy ORM session that binds to the engine
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Continent(Base):
    __tablename__ = 'continent'
    continent_id = Column(Integer, primary_key=True)
    continent = Column(String(length=20), unique=True)
    countries = relationship("Country", backref=backref("continent"))

    def __repr__(self):
        return f"Continent(id={self.continent_id!r}, " \
               f"name={self.continent!r})"


class Country(Base):
    __tablename__ = 'country'
    country_id = Column(Integer, primary_key=True)
    continent_id = Column(Integer, ForeignKey("continent.continent_id"))
    country = Column(String(length=50))

    UniqueConstraint('continent_id', 'country')

    def __repr__(self):
        return f"Country(id={self.country_id!r}, " \
               f"continent_id={self.continent_id!r}, " \
               f"name={self.country!r})"


def add_new_continent(continent):
    session = Session()

    # Check to see if the continent exists
    query = (select(Continent.continent)
             .where(Continent.continent == continent)
             )
    result = session.execute(query)
    check_continent = result.scalar()


    # Does the country exist in the continent
    if check_continent is not None:
        print(f"The continent of {continent} has already been discovered.")
        return

    new_continent = Continent(continent=f'{continent}')

    session.add(new_continent)
    session.flush()
    session.commit()

# def add_new_country(session, continent, country):
#
#     # Check if country exists
#     country = (
#         session.query(Country)
#         .join(Continent)
#         .filter(Country.country == country)
#         .filter(
#             and_(
#                 Continent.continent == continent
#             )
#         )
#         .one_or_none()
#     )
#
#     # Does the country exist in the continent
#     if country is not None:
#         return
#
#     # Get the country in the continent
#     country = (
#         session.query(Country)
#         .join(Continent)
#         .filter(Country.country == country)
#         .filter(
#             and_(
#                 Continent.continent == continent
#             )
#         )
#         .one_or_none()
#     )
#     # Create new country if needed
#     if country is None:
#         country = Country(country=country)
#
#     # Get the Continent
#     continent = (
#         session.query(Continent)
#         .filter(
#             and_(
#                 Continent.continent == continent
#             )
#         )
#         .one_or_none()
#     )
#     # Do we need to create the continent
#     if continent is None:
#         continent = Continent(continent == continent)
#         session.add(continent)
#
#     # Initialize the country relationships
#     country.continent = continent
#     session.add(country)
#
#     # Commit to the database
#     session.commit()
#
#

########################################################################################################################


# add_new_continent(continent='Unknown')
