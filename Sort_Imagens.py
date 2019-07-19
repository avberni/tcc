import pydicom
import os
import cv2
import Data
from datetime import datetime


class Sort(object):

    def __init__(self):
        self.dirLoadContents = ""
        self.dirSaveContents = ""
        self.format = 'png'
        self.db = Data.DBManipulation()

    def work_imagens(self):

        images_path = os.listdir(self.dirLoadContents.get())

        try:

            for n, image in enumerate(images_path):

                ds = pydicom.read_file(os.path.join(self.dirLoadContents.get(), image))

                image = image.replace('.dcm', '.' + self.format)

                eyesectionvalue = 0  # EYSECTION = 1 (Fundo de olho)

                try:
                    for eyesection in ds[0x0040, 0x0555]:
                        if eyesection[0x0040, 0xa043][0][0x0008, 0x0100].value == "Eye section":
                            eyesectionvalue = eyesection[0x0040, 0xa30a].value
                            break
                except KeyError:
                    eyesectionvalue = 2

                path = self.dirSaveContents.get() + '/' + self.format + str(eyesectionvalue)

                if not (os.path.isdir(path)):
                    os.makedirs(path)

                cv2.imwrite(os.path.join(path, image), cv2.cvtColor(ds.pixel_array, cv2.COLOR_RGB2BGR))

        except pydicom.errors.InvalidDicomError:
            print("erro de dicom")

    # def insertPatient(self,pathfile,dicom):
    #
    #     patname = dicom.PatientName
    #     displayname = str(patname.given_name + " " + patname.family_name).lower()
    #
    #     listDate = list(dicom.PatientBirthDate)
    #     patbirthdate = listDate[6] + listDate[7] + "/" + listDate[4] + listDate[5] + "/" + listDate[0] + listDate[1] + listDate[2] + listDate[3]
    #     patbirthdate = datetime.strptime(patbirthdate, '%d/%m/%Y').date()
    #
    #     self.insertPatImag(displayname, pathfile)
    #
    #     if len(self.db.patientSearch(displayname,patbirthdate)) == 0:
    #         patient = Data.Patient(displayname, patbirthdate)
    #         self.db.insert(patient)
    #     else:
    #         print("Paciente ja existe")
    #
    # def insertPatImag(self, namepatient, pathfile):
    #
    #     try:
    #         patitent = list(filter(lambda patient : patient.name == namepatient, self.listPatImg))
    #
    #         if (len(patitent) != 0) :
    #             patitent[0].namePathFile.append(pathfile)
    #         else:
    #             obj = ParPatientImage(namepatient)
    #             obj.namePathFile.append(pathfile)
    #             self.listPatImg.append(obj)
    #     except :
    #         print("ALGUM ERRO")
    #
    # def insertImage(self,file,dicom):
    #
    #     eyesectionvalue = 0  # EYSECTION = 1 (Fundo de olho)
    #
    #     try :
    #         for eyesection in dicom[0x0040, 0x0555] :
    #             if eyesection[0x0040, 0xa043][0][0x0008, 0x0100].value == "Eye section" :
    #                 eyesectionvalue = eyesection[0x0040, 0xa30a].value
    #                 break
    #     except KeyError :
    #         eyesectionvalue = 2
    #
    #     listDate = list(dicom.StudyDate)
    #     dateStudy = listDate[6] + listDate[7] + "/" + listDate[4] + listDate[5] + "/" + listDate[0] + listDate[1] + listDate[2] + listDate[3]
    #     dateStudy = datetime.strptime(dateStudy, '%d/%m/%Y').date()
    #
    #     if len(self.db.imageSearch(file)) == 0:
    #         img = Data.Image(file, eyesectionvalue, dicom.HorizontalFieldOfView, dicom.ImageLaterality, dateStudy)
    #         self.db.insert(img)
    #     else:
    #         print("Imagem ja exite")
    #