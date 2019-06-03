import os
import pydicom
import Data
import shutil
from datetime import date,timedelta,datetime

class ParPatientImage(object):

    def __init__(self,name):
        self.name      = name
        self.namePathImagem = []

class Search(object):

    dirLoadContents    = ""
    dirSaveContents    = ""
    dataStartContents  = ""
    dataEndContents    = ""
    listPatImg = []

    def work_list(self):

        datestart = self.dataStartContents.get()
        dateend = self.dataStartContents.get()

        while(dateend >= datestart):

            try:
                # procura na pasta especifica data
                dcm_load_path = self.dirLoadContents.get()
                dcm_load_path += "/" + datetime.strptime(datestart, '%Y/%m/%d').strftime('%Y/%m/%d')

                # procura as fotos especificas
                images_path = os.listdir(dcm_load_path)

                for n, image in enumerate(images_path):

                    try:
                        ds = pydicom.read_file(os.path.join(dcm_load_path, image))

                        pat_name = ds.PatientName
                        display_name = str(pat_name.given_name + " " + pat_name.family_name).lower()

                        self.insertPatImag(display_name,image,dcm_load_path)

                    except pydicom.errors.InvalidDicomError:
                        print("InvalidDicomError")
                    except AttributeError:
                        print("AttributeError")

                #Gravar Imagens
                datestart = datestart + timedelta(days=1)

            except FileNotFoundError:
                print("FileNotFoundError")

    def insertPatImag(self,namePatient,image,dcm_load_path):

        try:
            obj = ParPatientImage(namePatient)
            patitent = list(filter(lambda a: a.name == namePatient,self.listPatImg))

            if (len(patitent) != 0):
                patitent[0].namePathImagem.append(os.path.join(dcm_load_path, image))
            else:
                obj.namePathImagem.append(os.path.join(dcm_load_path, image))

        except:
            print("ALGUM ERRO")

    def insertDB(self):
        print("INSER IMAGEM E PACINTE")

    def saveImage(self):

        dcm_save_path = self.dirSaveContents.get() + "/save"

        if os.path.isdir(dcm_save_path):
            print("pasta DCM ja existe")
        else:
            os.makedirs(dcm_save_path)

        for n,obj in enumerate(self.listPatImg):
            for image in obj.listImage:
                ds = pydicom.read_file(image)
                shutil.copy2(ds.filename, dcm_save_path)