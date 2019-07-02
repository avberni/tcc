import os
import pydicom
import Data
import shutil
from datetime import timedelta, datetime


class ParPatientImage(object):

    def __init__(self, name):
        self.name = name
        self.namePathFile = []


class Search(object):

    def __init__(self):
        self.dirLoadContents = ""
        self.dirSaveContents = ""
        self.dataStartContents = ""
        self.dataEndContents = ""
        self.listPatImg = []
        self.db = Data.DBManipulation()

    def work_list(self):

        datestart = datetime.strptime(self.dataStartContents.get(), '%Y/%m/%d').date()
        dateend = datetime.strptime(self.dataEndContents.get(), '%Y/%m/%d').date()

        while (dateend >= datestart) :

            try :
                # procura na pasta especifica com  a data
                dcm_load_path = self.dirLoadContents.get()
                dcm_load_path += "/" + datestart.strftime('%Y/%m/%d')

                #lista todas as fotos
                images_path = os.listdir(dcm_load_path)

                for n, image in enumerate(images_path):

                    try:
                        pathfile = os.path.join(dcm_load_path, image)
                        ds = pydicom.read_file(pathfile)

                        print(image)
                        print(ds)

                        self.insertPatient(pathfile,ds)
                        self.insertImage(image,ds)

                    except pydicom.errors.InvalidDicomError:
                        print("InvalidDicomError")
                    except AttributeError :
                        print("AttributeError")


                datestart = datestart + timedelta(days=1)

            except FileNotFoundError :
                print("FileNotFoundError")
                datestart = dateend + timedelta(days=1)

    def saveImage(self) :

        dcm_save_path = self.dirSaveContents.get() + "/save"

        if os.path.isdir(dcm_save_path):
            print("pasta DCM ja existe")
        else:
            os.makedirs(dcm_save_path)

        for n, obj in enumerate(self.listPatImg):
            for image in obj.listImage :
                ds = pydicom.read_file(image)
                shutil.copy2(ds.filename, dcm_save_path)

    def insertPatient(self,pathfile,dicom):

        patname = dicom.PatientName
        displayname = str(patname.given_name + " " + patname.family_name).lower()

        listDate = list(dicom.PatientBirthDate)
        patbirthdate = listDate[6] + listDate[7] + "/" + listDate[4] + listDate[5] + "/" + listDate[0] + listDate[1] + listDate[2] + listDate[3]
        patbirthdate = datetime.strptime(patbirthdate, '%d/%m/%Y').date()

        self.insertPatImag(displayname, pathfile)

        if len(self.db.patientSearch(displayname)) == 0:
            patient = Data.Patient(displayname, patbirthdate)
            self.db.insert(patient)

    def insertPatImag(self, namepatient, pathfile):

        try:
            patitent = list(filter(lambda patient : patient.name == namepatient, self.listPatImg))

            if (len(patitent) != 0) :
                patitent[0].namePathFile.append(pathfile)
            else:
                obj = ParPatientImage(namepatient)
                obj.namePathFile.append(pathfile)
                self.listPatImg.append(obj)
        except :
            print("ALGUM ERRO")

    def insertImage(self,file,dicom):

        eyesectionvalue = 0  # EYSECTION = 1 (Fundo de olho)

        try :
            for eyesection in dicom[0x0040, 0x0555] :
                if eyesection[0x0040, 0xa043][0][0x0008, 0x0100].value == "Eye section" :
                    eyesectionvalue = eyesection[0x0040, 0xa30a].value
                    break
        except KeyError :
            eyesectionvalue = 2

        listDate = list(dicom.StudyDate)
        dateStudy = listDate[6] + listDate[7] + "/" + listDate[4] + listDate[5] + "/" + listDate[0] + listDate[1] + listDate[2] + listDate[3]
        dateStudy = datetime.strptime(dateStudy, '%d/%m/%Y').date()

        if len(self.db.imageSearch(file)) == 0:
            img = Data.Image(file, eyesectionvalue, dicom.HorizontalFieldOfView, dicom.ImageLaterality, dateStudy)
            self.db.insert(img)