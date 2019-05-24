from enum import Enum
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy import create_engine, Column,Integer,String,DateTime,ForeignKey,func
from sqlalchemy.orm import sessionmaker,relationship
from datetime import datetime

NAMEDATABASE = 'sqlite:///rope.db'
BASE = declarative_base()

class Type_Image(Enum):
    EXTERNA = 0
    FUNDO   = 1
    LF      = 2

    def describe(self):
        return self.name,self.value

class Image(BASE):

    __tablename__ = 'Imagem'

    id = Column(Integer, primary_key=True)
    fileName = Column(String,index=True)
    type = Column(Integer)
    angle = Column(Integer)
    people_id = Column(Integer, ForeignKey('Pessoa.id'))
    people = relationship("People",backref="Imagem")

    def __init__(self, fileName, type, angle,people):
        self.fileName = fileName
        self.type     = type
        self.angle    = angle
        self.people   = people

    def toSting(self):
        return self.fileName + "," + self.type + "," + self.angle

class People(BASE):

    __tablename__ = 'Pessoa'

    id        = Column(Integer,primary_key=True)
    name      = Column(String,index=True)
    age       = Column(Integer)
    dateBirth = Column(DateTime,default=datetime.datetime.utcnow())

    def __init__(self, name, age, dateBirth):
        self.name = name
        self.age = age
        self.birthDate = dateBirth

    def __srt__(self):
        return self.name + "," + self.age + "," + self.birthDate


class InitDataBase(object):

    engine = create_engine(NAMEDATABASE)
    BASE.metadata.create_all(engine)


class DBManipulation(object):

    db = InitDataBase()

    def session(self):

        Session = sessionmaker(bind=DBManipulation.db.engine)
        self.session = Session()

    def closeSession(self):
        self.session.close_all_session()

    def insertPeople(self):

        DBManipulation.session(self)
        newPeople = People("Andrews",10 ,datetime(1988,10,1))
        self.session.add(newPeople)
        self.session.commit()
        self.session.close_all()

    def insertImage(self):

        DBManipulation.session(self)
        newPeople = People("Andrews", 10,func.now())
        newImage  = Image("Teste",Type_Image.EXTERNA.value,30,newPeople)
        self.session.add(newPeople)
        self.session.add(newImage)
        self.session.commit()
        self.session.close_all()


    # def insertPeople(self,people):
    #
    #     newPeople = db.Peolple(name="OTO", age=20)