import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=False)
    email = Column(String(100), nullable=False, unique=True)
    name = Column(String(25), nullable=False, unique=False)
    last_name = Column(String(25), nullable=False, unique=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id')) 
    user = relationship('User', back_populates='favorites')


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False, unique=True)
    height = Column(Integer, nullable=False, unique=False)
    mass = Column(Integer, nullable=False, unique=False)
    hair_color = Column(String(15), nullable=False, unique=False)
    skin_color = Column(String(15), nullable=False, unique=False)
    eye_color = Column(String(15), nullable=False, unique=False)
    birth_year = Column(String(15), nullable=False, unique=False)
    gender = Column(String(15), nullable=False, unique=False)
    favorite_id = Column(Integer, ForeignKey('favorites.id'))
    favorite = relationship('Favorites', back_populates='character')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False, unique=True)
    rotation_period = Column(Integer, nullable=False, unique=False)
    orbital_period = Column(Integer, nullable=False, unique=False)
    diameter = Column(Integer, nullable=False, unique=False)
    climate = Column(String(15), nullable=False, unique=False)
    gravity = Column(String(15), nullable=False, unique=False)
    terrain = Column(String(15), nullable=False, unique=False)
    population = Column(Integer, nullable=False, unique=False)
    favorite_id = Column(Integer, ForeignKey('favorites.id'))
    favorite = relationship('Favorites', back_populates='planet')
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
