from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

conn_str = 'mysql+pymysql://Heather:#LAwaItly19@localhost:3306/wsl'

# SQLAlchemy engine that will interact with mysql database
engine = create_engine(conn_str)

# SQLAlchemy ORM session that binds to the engine
Session = sessionmaker(bind=engine)

# Base class for our class definitions
Base = declarative_base()
