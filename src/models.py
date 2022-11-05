import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

myModel = declarative_base()


class User(myModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    username = Column(String(255))
    user_state = Column(String(255))
    admin = Column(Boolean())
    password = Column(String(255))#el password nunca debe serializarse

class Character(myModel):
    __tablename__ = 'charachter'

    uid = Column(Integer, primary_key=True)
    name = Column(String(255))
    gender = Column(String(255))
    height = Column(String(255))
    birth_year = Column(String(255))
    hair_color = Column(String(255))
    skin_color = Column(String(255))
    eye_color = Column(String(255))
    birth_year = Column(Integer)
    gender = Column(String(255))
    homeworld = Column(String(255), ForeignKey('planets.id'))
    films = Column(String(255), ForeignKey('films.id'))
    species = Column(String(255), ForeignKey('species.id'))
    vehicles = Column(String(255), ForeignKey('vehicles.id'))
    starships = Column(String(255), ForeignKey('starships.id'))
    created = Column(Integer)
    edited = Column(Integer)
    url = Column(String(255))

    # def deleteCharacter(id):
    #     charachter = Character.query.get(id)
    #     session.delete(charachter)
    #     session.commit()
    #     return {"Message": "Character was delete"}


class Planets(myModel):
    __tablename__ = 'planets'

    uid = Column(Integer, primary_key=True)
    name = Column(String(255))
    diameter = Column(Integer)
    climate = Column(String(255))
    gravity = Column(Numeric(5,4))
    terrain = Column(String(255))
    population = Column(Integer)

class Vehicles(myModel):
    __tablename__ = 'vehicles'

    uid = Column(Integer, primary_key=True)
    name = Column(String(255))
    url = Column(String(255))

class Species(myModel):
    __tablename__ = 'species'

    uid = Column(Integer, primary_key=True)
    name = Column(String(255))
    url = Column(String(255))

class Starships(myModel):
    __tablename__ = 'starships'

    uid = Column(Integer, primary_key=True)
    name = Column(String(255))
    url = Column(String(255))

class Favorites(myModel):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    charachter_id = Column(Integer, ForeignKey('charachter.u id'))
    planets_id = Column(Integer, ForeignKey('planets.uid'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.uid'))
    species_id = Column(Integer, ForeignKey('species.uid'))
    starships_id = Column(Integer, ForeignKey('starships.uid'))
    User = relationship("User")
    Favorite_planets = relationship("Planets")
    Favorite_charachter = relationship("Character")
    Favorite_species = relationship("Species")
    Favorite_films = relationship("Films")


    # def to_dict(self):
    #         return {}


# Draw from SQLAlchemy myModel
render_er(myModel, 'DiagramaCuatro.png')
