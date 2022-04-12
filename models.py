from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, UniqueConstraint, select, \
    ForeignKeyConstraint
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
    countries = relationship("Country")

    # def __init__(self, entered_continent: str):
    #     self.entered_continent: str = entered_continent

    def __repr__(self):
        return f"Continent(id={self.continent_id!r}, " \
               f"name={self.continent!r})"

    # def add_new_continent(self):
    #     session = Session()
    #
    #     # Check to see if the entered_continent exists
    #     query = (select(Continent.continent)
    #              .where(Continent.continent == self.entered_continent)
    #              )
    #     result = session.execute(query)
    #     check_continent = result.scalar()
    #
    #     # Does the entered_country exist in the entered_continent
    #     if check_continent is not None:
    #         print(f"The entered_continent of {self.entered_continent} has already been discovered.")
    #         return
    #
    #     new_continent = self.entered_continent
    #
    #     session.add(new_continent)
    #     session.flush()
    #     session.commit()


class Country(Base):
    # def __init__(self, entered_continent, entered_country):
    #     self.entered_continent = entered_continent
    #     self.entered_country = entered_country

    __tablename__ = 'country'
    country_id = Column(Integer, primary_key=True)
    continent_id = Column(Integer, ForeignKey('continent.continent_id'), nullable=False)
    country = Column(String(length=50))
    # test = relationship("Continent", back_populates="countries")  # Added from example, may not matter.

    # UniqueConstraint('continent_id', 'country')

    def __repr__(self):
        return f"Country(id={self.country_id!r}, " \
               f"continent_id={self.continent_id!r}, " \
               f"name={self.country!r})"


class AddToTable(Base):
    def add_new_country(entered_continent: str, entered_country: str):

        session = Session()

        # Check to see if the entered_continent exists
        query = (select(Country.country)
                 .where(Country.country == entered_country)
                 )
        result = session.execute(query)
        check_country = result.scalar()

        # Does the entered_country exist in the entered_continent
        if check_country is not None:
            print(f"The country of {entered_country} has already been discovered.")
            return

        # Get continent_id from continent table
        query = (select(Continent.continent_id)
                 .where(Continent.continent == entered_continent))
        result = session.execute(query)
        entered_continent_id = result.scalar()

        new_country = Country(continent_id=entered_continent_id, country=entered_country)

        session.add(new_country)
        session.flush()
        session.commit()


# def add_new_country(session, entered_continent, entered_country):
#
#     # Check if entered_country exists
#     entered_country = (
#         session.query(Country)
#         .join(Continent)
#         .filter(Country.entered_country == entered_country)
#         .filter(
#             and_(
#                 Continent.entered_continent == entered_continent
#             )
#         )
#         .one_or_none()
#     )
#
#     # Does the entered_country exist in the entered_continent
#     if entered_country is not None:
#         return
#
#     # Get the entered_country in the entered_continent
#     entered_country = (
#         session.query(Country)
#         .join(Continent)
#         .filter(Country.entered_country == entered_country)
#         .filter(
#             and_(
#                 Continent.entered_continent == entered_continent
#             )
#         )
#         .one_or_none()
#     )
#     # Create new entered_country if needed
#     if entered_country is None:
#         entered_country = Country(entered_country=entered_country)
#
#     # Get the Continent
#     entered_continent = (
#         session.query(Continent)
#         .filter(
#             and_(
#                 Continent.entered_continent == entered_continent
#             )
#         )
#         .one_or_none()
#     )
#     # Do we need to create the entered_continent
#     if entered_continent is None:
#         entered_continent = Continent(entered_continent == entered_continent)
#         session.add(entered_continent)
#
#     # Initialize the entered_country relationships
#     entered_country.entered_continent = entered_continent
#     session.add(entered_country)
#
#     # Commit to the database
#     session.commit()
#
#

########################################################################################################################

# # Enter a New Continent
# inst = Continent(entered_continent="Unknown")
# inst.add_new_continent()

# Enter a New Country
add_new_country(entered_continent='North America', entered_country="USA")



