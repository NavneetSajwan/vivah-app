
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Initialize SQLAlchemy with SQLite
DATABASE_URL = "sqlite:///./vivah.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Define the database models based on the schema

# Auxiliary Tables

class Religion(Base):
    __tablename__ = "religions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Caste(Base):
    __tablename__ = "castes"
    id = Column(Integer, primary_key=True, index=True)
    religion_id = Column(Integer, ForeignKey('religions.id'))
    name = Column(String, index=True)

class MotherTongue(Base):
    __tablename__ = "mother_tongues"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, index=True)
    country_id = Column(Integer, ForeignKey('countries.id'))
    name = Column(String, index=True)

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    state_id = Column(Integer, ForeignKey('states.id'))
    name = Column(String, index=True)

# Main User Tables

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    registration_date = Column(Date)

class BasicInfo(Base):
    __tablename__ = "basic_info"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    full_name = Column(String, index=True)
    gender = Column(String, index=True)
    date_of_birth = Column(Date)
    marital_status = Column(String, index=True)
    religion_id = Column(Integer, ForeignKey('religions.id'))
    caste_id = Column(Integer, ForeignKey('castes.id'))
    mother_tongue_id = Column(Integer, ForeignKey('mother_tongues.id'))
    country_id = Column(Integer, ForeignKey('countries.id'))
    state_id = Column(Integer, ForeignKey('states.id'))
    city_id = Column(Integer, ForeignKey('cities.id'))

# ... More tables/models can be added based on the schema as needed

# Create the tables in the SQLite database
Base.metadata.create_all(bind=engine)
