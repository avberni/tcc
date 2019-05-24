import os
import pydicom
import Data
import shutil

class Search(object):


    dirLoadContents    = ""
    dirSaveContents    = ""
    dataStartContents  = ""
    dataEndContents    = ""
    listOfPeople = []

    def work_list(self):

        dateStart = self.dataStartContents.get().split("/")
        dateEnd = self.dataStartContents.get().split("/")

        #for


    def search_folder(self, Patiens):

        dcm_save_path = self.dirSaveContents.get() + "/save"

        if os.path.isdir(dcm_save_path):
            print("pasta DCM ja existe")
        else:
            os.makedirs(dcm_save_path)

        for index, patien in enumerate(Patiens):

            try:
                #procura na pasta especifica data
                dcm_load_path = self.dirLoadContents.get()
                dcm_load_path += "/" + str(patien[0][0]) + "/" + str(patien[0][1]) + "/" + str(patien[0][2])

                try:

                    # procura as fotos especificas
                    images_path = os.listdir(dcm_load_path)

                    for namepatien in enumerate(patien[1]):

                        #namepatien é um tupla [index, Nome]
                        name_split = namepatien[1].split()
                        
                        first_last_name = str(name_split[0] + " " + name_split[-1])

                        for n, image in enumerate(images_path):

                            try:
                                ds = pydicom.read_file(os.path.join(dcm_load_path, image))

                                pat_name = ds.PatientName
                                display_name = str(pat_name.given_name + " " + pat_name.family_name)

                                if display_name.lower() == first_last_name.lower():
                                    print("Achou")
                                    shutil.copy2(ds.filename,dcm_save_path)

                            except pydicom.errors.InvalidDicomError:
                                print("erro de dicom")
                            except AttributeError:
                                print("Erro no DS")
                                print(n)

                except FileNotFoundError:
                    print("Path not Found")

            except TypeError:
                print("de lista")