from enum import Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, func,Date,Table
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

NAMEDATABASE = 'sqlite:///rop.db'
BASE = declarative_base()
#Imagem type
EXTERNA = 0
FUNDO = 1
LF = 2

class Exam(BASE):

    __tablename__ = 'Exame'

    id = Column(Integer,primary_key=True)
    patient_id = Column(Integer, ForeignKey('Paciente.id'))
    patient = relationship("Patient", backref="Exam")
    image_id = Column(Integer, ForeignKey('Imagem.id'))
    image = relationship("Image", backref="Exam")
    cataract = Column(String)

    def __init__(self,patient,image,cataract):
        self.patient = patient
        self.image = image
        self.cataract = cataract


class Image(BASE):

    __tablename__ = 'Imagem'

    id = Column(Integer, primary_key=True)
    fileName = Column(String, index=True)
    imageType = Column(Integer,nullable=False)
    angle = Column(Integer)
    eyePos = Column(String,nullable=False)

    def __init__(self, fileName, imageType, angle,eyePos):
        self.fileName = fileName
        self.imageType = imageType
        self.angle = angle
        self.eyePos = eyePos

    def __str__(self):
        return self.fileName + "," + self.type + "," + self.angle


class Patient(BASE):

    __tablename__ = 'Paciente'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    age = Column(Integer)
    birthDate = Column(Date,nullable=False)

    def __init__(self, name, age, birthDate):
        self.name = name
        self.age = age
        self.birthDate = birthDate

    def __srt__(self):
        return self.name + "," + self.age + "," + self.birthDate


class DBManipulation(object):

    def __init__(self):
        self.engine = create_engine(NAMEDATABASE)
        BASE.metadata.create_all(self.engine)

    def session(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def closeSession(self):
        self.session.close_all_session()

    def insert(self,item):
        DBManipulation.session(self)
        self.session.add(item)
        self.session.commit()
        self.session.close_all()