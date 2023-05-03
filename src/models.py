import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastName = Column(String(200), nullable=False)
    email = Column(String(200))
    password = Column(String(200))
    user_name = Column(String(200))
    created_date = Column(DateTime)



class Planet(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    climate = Column(String(80))
    diameter = Column(Integer)
    terrain = Column(String(80))
    description = Column(String(250))
    url = Column(String(80), unique=True)



class Character(Base):
    __tablename__= 'character'
    id = Column(String(60), primary_key=True)
    description = Column(String(250))
    gender = Column(String(60))
    mass = Column(Integer)
    name = Column(String(60))
    url = Column(String(80), unique=True)



class Favorites(Base):
    __tablename__= 'favorites'
    id = Column(Integer, primary_key=True)    
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('character.id'))





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
