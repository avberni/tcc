from enum import Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

NAMEDATABASE = 'sqlite:///rop.db'
BASE = declarative_base()
EXTERNA = 0
FUNDO = 1
LF = 2


class Image(BASE):

    __tablename__ = 'Imagem'

    id = Column(Integer, primary_key=True)
    fileName = Column(String, index=True)
    type = Column(Integer)
    angle = Column(Integer)
    patient_id = Column(Integer, ForeignKey('Paciente.id'))
    patient = relationship("Patient", backref="Imagem")

    def __init__(self, fileName, type, angle, people):
        self.fileName = fileName
        self.type = type
        self.angle = angle
        self.people = people

    def __str__(self):
        return self.fileName + "," + self.type + "," + self.angle


class Patient(BASE):

    __tablename__ = 'Paciente'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    age = Column(Integer)
    dateBirth = Column(DateTime, default=datetime.utcnow())

    def __init__(self, name, age, dateBirth):
        self.name = name
        self.age = age
        self.birthDate = dateBirth

    def __srt__(self):
        return self.name + "," + self.age + "," + self.birthDate


class InitDataBase(object):

    def __init__(self):
        self.engine = create_engine(NAMEDATABASE)
        BASE.metadata.create_all(self.engine)


class DBManipulation(object):

    def __init__(self):
        self.db = InitDataBase()

    def session(self):
        Session = sessionmaker(bind=self.db.engine)
        self.session = Session()

    def closeSession(self):
        self.session.close_all_session()

    def insertPeople(self):
        DBManipulation.session(self)
        newPeople = Patient("Andrews", 10, datetime(1988, 10, 1))
        self.session.add(newPeople)
        self.session.commit()
        self.session.close_all()

    def insertImage(self):
        DBManipulation.session(self)
        newPeople = Patient("Andrews", 10, func.now())
        newImage = Image("Teste", EXTERNA, 30, newPeople)
        self.session.add(newPeople)
        self.session.add(newImage)
        self.session.commit()
        self.session.close_all()

    # def insertPeople(self,people):
    #
    #     newPeople = db.Peolple(name="OTO", age=20)
