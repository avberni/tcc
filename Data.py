from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import sessionmaker, relationship

NAMEDATABASE = 'sqlite:///catarata.db'
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
    cristalino_od = Column(Boolean)
    outros_od = Column(String)
    alteracoes_estruturas_com_alteracao_od = Column(String)
    cristalino_oe = Column(Boolean)
    outros_oe = Column(String)
    alteracoes_estruturas_com_alteracao_oe = Column(String)
    cataract = Column(Boolean)
    hipotese_catarata_descricao  = Column(String)
    conduta_detalhamento_conduta = Column(String)
    review = Column(Boolean)


    def __init__(self,patient,image,var,review):
        self.patient = patient
        self.image = image
        self.cristalino_od = bool(var[0])
        self.outros_od = var[1]
        self.alteracoes_estruturas_com_alteracao_od = var[2]
        self.cristalino_oe = bool(var[3])
        self.outros_oe = var[4]
        self.alteracoes_estruturas_com_alteracao_oe = var[5]
        self.cataract = bool(var[6])
        self.hipotese_catarata_descricao = var[7]
        self.conduta_detalhamento_conduta = var[8]
        self.review = bool(review)

class Image(BASE):

    __tablename__ = 'Imagem'

    id = Column(Integer, primary_key=True)
    fileName = Column(String, index=True)
    imageType = Column(Integer, nullable=False)
    angle = Column(Integer, nullable=False)
    eyePos = Column(String, nullable=False)
    dateExam = Column(Date, nullable=False)

    def __init__(self, fileName, imageType, angle,eyePos, dataExam):
        self.fileName = fileName
        self.imageType = imageType
        self.angle = angle
        self.eyePos = eyePos
        self.dateExam = dataExam

    def __str__(self):
        return self.fileName + "," + self.type + "," + self.angle

    def __getFileName__(self):
        return self.fileName

class Patient(BASE):

    __tablename__ = 'Paciente'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    birthDate = Column(Date,nullable=False)

    def __init__(self, name, birthDate):
        self.name = name
        self.birthDate = birthDate

    def __srt__(self):
        return self.name + "," + self.birthDate

    def __getName__(self):
        return self.name

class DBManipulation(object):

    def __init__(self):
        self.engine = create_engine(NAMEDATABASE)
        BASE.metadata.create_all(self.engine)

    def session(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def closeSession(self):
        self.session.close_all_session()

    def insert(self, item):
        DBManipulation.session(self)
        self.session.add(item)
        self.session.commit()
        self.session.close_all()

    def patientSearch(self, patName,patbirthdate):
        DBManipulation.session(self)
        ret = self.session.query(Patient).filter(Patient.name == patName, Patient.birthDate == patbirthdate).all()
        self.session.close_all()
        return ret

    def imageSearch(self, fileName):
        DBManipulation.session(self)
        ret = self.session.query(Image).filter(Image.fileName == fileName).all()
        self.session.close_all()
        return ret

    def examSearch(self,patient,image):
        DBManipulation.session(self)
        #ret = self.session.query(Exam).filter(Exam.patient.name == patient.name,Exam.image.fileName == image.fileName).all()
        ret = self.session.query(Exam.patient_id,Exam.image_id).filter(Patient.name == patient.name, Image.fileName == image.fileName).all()
        self.session.close_all()
        return ret