import os
import pydicom
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
                        patname = ds.PatientName
                        displayname = str(patname.given_name + " " + patname.family_name).lower()

                        eyesectionvalue = 0

                        try:
                            for eyesection in ds[0x0040, 0x0555] :
                                if eyesection[0x0040, 0xa043][0][0x0008, 0x0100].value == "Eye section" :
                                    eyesectionvalue = eyesection[0x0040, 0xa30a].value
                                    break
                        except KeyError :
                            eyesectionvalue = 2

                        if eyesectionvalue == 0:
                            self.listPatImg.append(displayname)

                    except pydicom.errors.InvalidDicomError:
                        print("InvalidDicomError")
                    except AttributeError :
                        print("AttributeError")

                self.searchAgain(dcm_load_path)

                datestart = datestart + timedelta(days=1)

            except FileNotFoundError :
                print("FileNotFoundError")
                datestart = dateend + timedelta(days=1)

    def searchAgain(self,dcmpath):

        images_path = os.listdir(dcmpath)

        for n, image in enumerate(images_path):

            try:
                pathfile = os.path.join(dcmpath, image)
                ds = pydicom.read_file(pathfile)
                patname = ds.PatientName
                displayname = str(patname.given_name + " " + patname.family_name).lower()

                if self.listPatImg.__contains__(displayname):
                    print("Achou")

                dcm_save_path = self.dirSaveContents.get() + "/save"

                if os.path.isdir(dcm_save_path):
                    print("pasta DCM ja existe")
                else:
                    os.makedirs(dcm_save_path)

                shutil.copy2(ds.filename, dcm_save_path)

            except pydicom.errors.InvalidDicomError:
                print("InvalidDicomError")
            except AttributeError:
                print("AttributeError")