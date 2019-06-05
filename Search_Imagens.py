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

    def work_list(self):

        datestart = self.dataStartContents
        dateend = self.dataStartContents

        while (dateend >= datestart) :

            try :
                # procura na pasta especifica data
                dcm_load_path = self.dirLoadContents.get()
                dcm_load_path += "/" + datetime.strptime(datestart, '%Y/%m/%d').strftime('%Y/%m/%d')

                # procura as fotos especificas
                images_path = os.listdir(dcm_load_path)

                for n, image in enumerate(images_path):

                    try:
                        pathfile = os.path.join(dcm_load_path, image)
                        ds = pydicom.read_file(pathfile)

                        pat_name = ds.PatientName
                        display_name = str(pat_name.given_name + " " + pat_name.family_name).lower()

                        self.insertPatImag(display_name, pathfile)

                    except pydicom.errors.InvalidDicomError:
                        print("InvalidDicomError")
                    except AttributeError :
                        print("AttributeError")

                # Gravar Imagens
                datestart = datestart + timedelta(days=1)

            except FileNotFoundError :
                print("FileNotFoundError")

    def insertPatImag(self, namepatient, pathfile):

        try:
            patitent = list(filter(lambda a : a.name == namepatient, self.listPatImg))

            if (len(patitent) != 0) :
                patitent[0].namePathFile.append(pathfile)
            else:
                obj = ParPatientImage(namepatient)
                obj.namePathFile.append(pathfile)

        except :
            print("ALGUM ERRO")

    def insertDB(self) :
        print("INSER IMAGEM E PACINTE")

    def saveImage(self) :

        dcm_save_path = self.dirSaveContents.get() + "/save"

        if os.path.isdir(dcm_save_path) :
            print("pasta DCM ja existe")
        else :
            os.makedirs(dcm_save_path)

        for n, obj in enumerate(self.listPatImg):
            for image in obj.listImage :
                ds = pydicom.read_file(image)
                shutil.copy2(ds.filename, dcm_save_path)
