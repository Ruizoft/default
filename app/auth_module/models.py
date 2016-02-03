# -*- coding: utf-8 -*-
from app import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey,Float
from sqlalchemy.orm import relationship

class User(Base):

    __tablename__ = 'users'

    # User Name
    id = Column(Integer, primary_key=True)

    name    = Column(String(128),  nullable=False)

    # Identification Data: email & password
    email    = Column(String(128),  nullable=False,
                                            unique=True)
    password = Column(String(192),  nullable=False)

    tipo = Column(Integer,  nullable=False)

    created_by = Column(Integer,  nullable=True)

    child = relationship("Teacher")


    
    # Authorisation Data: role & status

    # New instance instantiation procedure
    def __init__(self, values={}):

        for k,v in values.iteritems():
            setattr(self, k, v)

    def to_json(self):
        output = dict()
        for field in dir(self):
            if not field.startswith('_') and field != "metadata" and not field.startswith("child") and not field.startswith('D') and not field.startswith('to'):
                output[field] = getattr(self, field)
            elif field.startswith('D') and getattr(user, field) != None:
                    output[field] = getattr(self, field).isoformat()
        return output

    def __repr__(self):
        return '%s' % (self.id)

class Teacher(Base):

    __tablename__ = 'teachers'

    # User Name
    id = Column(Integer, primary_key=True)

    user_id  = Column(Integer, ForeignKey("users.id"), nullable=False)

    descripcion    = Column(String(250),  nullable=True,
                                            unique=False)
    celular    = Column(String(250),  nullable=True,
                                            unique=False)
    cedula    = Column(String(250),  nullable=True,
                                            unique=False)
    telefono    = Column(String(250),  nullable=True,
                                            unique=False)
    foto    = Column(String(250),  nullable=True,
                                            unique=False)
    Dbirthdate    = Column(Date(),  nullable=True,
                                            unique=False)
   

    # New instance instantiation procedure
    def __init__(self, values={}):

        for k,v in values.iteritems():
            setattr(self, k, v)

    def to_json(self, name, email):
        output = dict()
        for field in dir(self):
            if not field.startswith('_') and field != "metadata" and not field.startswith("child") and not field.startswith('D') and not field.startswith('to'):
                output[field] = getattr(self, field)
            elif field.startswith('D') and getattr(self, field) != None:
                    output[field] = getattr(self, field).isoformat()
        output['name'] = name
        output['email'] = email
        return output

    def __repr__(self):
        return '%s' % (self.id)


class Admin(Base):

    __tablename__ = 'admins'

    # User Name
    id = Column(Integer, primary_key=True)

    user_id  = Column(Integer, ForeignKey("users.id"), nullable=False)

    celular    = Column(String(250),  nullable=True,
                                            unique=False)
    cedula    = Column(String(250),  nullable=True,
                                            unique=False)
    telefono    = Column(String(250),  nullable=True,
                                            unique=False)
    foto    = Column(String(250),  nullable=True,
                                            unique=False)
    Dbirthdate    = Column(Date(),  nullable=True,
                                            unique=False)
   

    # New instance instantiation procedure
    def __init__(self, values={}):

        for k,v in values.iteritems():
            setattr(self, k, v)

    def to_json(self, name, email):
        output = dict()
        for field in dir(self):
            if not field.startswith('_') and field != "metadata" and not field.startswith("child") and not field.startswith('D') and not field.startswith('to'):
                output[field] = getattr(self, field)
            elif field.startswith('D') and getattr(self, field) != None:
                    output[field] = getattr(self, field).isoformat()
        output['name'] = name
        output['email'] = email
        return output

    def __repr__(self):
        return '%s' % (self.id)