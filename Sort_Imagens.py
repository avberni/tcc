import pydicom
import os
import cv2
import Data
import xlrd
from PIL import Image, ImageFile
from datetime import datetime

ImageFile.LOAD_TRUNCATED_IMAGES = True

class Sort(object):

    def __init__(self):
        self.dirLoadContents = ""
        self.dirSaveContents = ""
        self.format = 'jpg'
        self.db = Data.DBManipulation()
        self.namePatient = ""
        self.datePatient = None
        self.eyePosition = ''
        self.imagem = None
        self.dicom = None
        self.listNameXML = []
        self.listDateXML = []

    def work_imagens(self):

        listImageSelected = self.listSelected()

        images_path = os.listdir(self.dirLoadContents.get())

        try:

            for n, image in enumerate(images_path):

                ds = pydicom.read_file(os.path.join(self.dirLoadContents.get(), image))
                self.dicom = ds
                namefile = image.split('.dcm')[0]


                if listImageSelected.__contains__(namefile):

                    image = image.replace('.dcm', '.' + self.format)


                    self.imagem = image
                    self.insertImage(namefile)

                # path = self.dirSaveContents.get() + '/' + self.format + str(0)
                #
                # if not (os.path.isdir(path)):
                #     os.makedirs(path)
                #
                # cv2.imwrite(os.path.join(path, self.imagem), cv2.cvtColor(self.dicom.pixel_array, cv2.COLOR_RGB2BGR))


        except pydicom.errors.InvalidDicomError:
            print("erro de dicom")

    def insertImage(self,nameFile):

        listDate = list(self.dicom.StudyDate)
        dateStudy = listDate[6] + listDate[7] + "/" + listDate[4] + listDate[5] + "/" + listDate[0] + listDate[1] + listDate[2] + listDate[3]
        dateStudy = datetime.strptime(dateStudy, '%d/%m/%Y').date()

        imgListDB = self.db.imageSearch(nameFile)

        if len(imgListDB) == 0:

            anglevalue  = 60

            try :
                for anglesection in self.dicom[0x0040, 0x0555] :
                    if anglesection[0x0040, 0xa043][0][0x0008, 0x0100].value == "Angle":
                        anglevalue = anglesection[0x0040, 0xa30a].value
                        break
            except KeyError :
                anglevalue = 30

            try:
                laterality = self.dicom.ImageLaterality
            except AttributeError:
                #Necessário por causa do tipo de DICOM
                laterality = self.dicom.Laterality


            img = Data.Image(nameFile, 0, anglevalue, laterality, dateStudy)
            self.eyePosition = laterality
            self.db.insert(img)
            patient = self.insertPatient()
            self.insertExame(patient,img)
        #else:
            #print("Imagem ja exite")


    def insertPatient(self):

        patname = self.dicom.PatientName
        displayname = str(patname.given_name + " " + patname.family_name).lower()
        self.namePatient = displayname

        listDate = list(self.dicom.PatientBirthDate)
        patbirthdate = listDate[6] + listDate[7] + "/" + listDate[4] + listDate[5] + "/" + listDate[0] + listDate[1] + listDate[2] + listDate[3]
        patbirthdate = datetime.strptime(patbirthdate, '%d/%m/%Y').date()
        self.datePatient = patbirthdate

        patient = self.db.patientSearch(displayname, patbirthdate)

        if len(patient) == 0:
            patient = Data.Patient(displayname, patbirthdate)
            self.db.insert(patient)
        else:
            patient = patient[0]

        # if type(patient) is list:
        #     patient = patient[0]

        return patient

    def insertExame(self,patient,image):

        values,review = self.report()
        exame = Data.Exam(patient,image,values,review)
        self.db.insert(exame)


    def listSelected(self):

        listImageSelected = []
        images_path = os.listdir("C:/Users/dell/Desktop/tcc_dados/erros/ComCatarata")

        for n, image in enumerate(images_path):
            namefile = image.split('.png')[0]
            listImageSelected.append(namefile)

            # arquivo = open('nome.txt', 'r') # Abra o arquivo (leitura)
            # conteudo = arquivo.readlines()
            # conteudo.append( image + '\n')   # insira seu conteúdo
            #
            # arquivo = open('nome.txt', 'w') # Abre novamente o arquivo (escrita)
            # arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
            #
            # arquivo.close()

        return listImageSelected

    def report(self):

        # 0 = False     1 = True
        ret = []
        review = False
        book = xlrd.open_workbook("C:/Users/dell/Desktop/tcc_dados/laudos.xlsx")
        sh = book.sheet_by_index(0)

        find = self.findPatient(book)

        if find != -1:
            line = find + 1

            retR = sh.cell_value(rowx=line, colx=5)
            retL = sh.cell_value(rowx=line, colx=8)
            retH = sh.cell_value(rowx=line, colx=11)

            if sh.cell_value(rowx=line, colx=5) == "":
                print(sh.cell_value(rowx=line, colx=2))
                retR = False

            if sh.cell_value(rowx=line, colx=8) == "":
                print(sh.cell_value(rowx=line, colx=2))
                retR = False

            ret.append(bool(retR))
            ret.append(sh.cell_value(rowx=line, colx=6))
            ret.append(sh.cell_value(rowx=line, colx=7))
            ret.append(bool(retL))
            ret.append(sh.cell_value(rowx=line, colx=9))
            ret.append(sh.cell_value(rowx=line, colx=10))
            ret.append(bool(retH))
            ret.append(sh.cell_value(rowx=line, colx=12))
            ret.append(sh.cell_value(rowx=line, colx=13))

            if (bool(retL) is False and bool(retR) is False and bool(retH) is True) or ((bool(retL) is True or bool(retR) is True) and bool(retH) is False):

                # if self.isIncipiente(sh) and self.isLente(sh):
                #     images_path = "C:/Users/dell/Desktop/tcc_dados/IncipienteLente"
                #     if not os.path.isdir(images_path):
                #         os.makedirs(images_path)
                #     cv2.imwrite(os.path.join(images_path, self.imagem),cv2.cvtColor(self.dicom.pixel_array, cv2.COLOR_RGB2BGR))
                # else:
                images_path = "C:/Users/dell/Desktop/tcc_dados/Revisao"

                if not os.path.isdir(images_path) :
                    os.makedirs(images_path)
                cv2.imwrite(os.path.join(images_path, self.imagem),cv2.cvtColor(self.dicom.pixel_array, cv2.COLOR_RGB2BGR))

                review = True

            elif (bool(retL) is True or bool(retR) is True) and (bool(retH) is True):
                #deposi exclui o tipo
                images_path = "C:/Users/dell/Desktop/tcc_dados/ComCatarata"
                if not os.path.isdir(images_path):
                    os.makedirs(images_path)

                cv2.imwrite(os.path.join(images_path, self.imagem), cv2.cvtColor(self.dicom.pixel_array, cv2.COLOR_RGB2BGR))
            else:
                images_path = "C:/Users/dell/Desktop/tcc_dados/SemCatarata"
                if not os.path.isdir(images_path):
                    os.makedirs(images_path)

                cv2.imwrite(os.path.join(images_path, self.imagem),cv2.cvtColor(self.dicom.pixel_array, cv2.COLOR_RGB2BGR))

        else :

            for i in range(0,9):
                ret.append(0)

            images_path = "C:/Users/dell/Desktop/tcc_dados/SemBanco"
            if not os.path.isdir(images_path):
                os.makedirs(images_path)

            try:
                cv2.imwrite(os.path.join(images_path, self.imagem), cv2.cvtColor(self.dicom.pixel_array, cv2.COLOR_RGB2BGR))
            except Exception:
                print(self.imagem)

        return ret,review

    def findPatient(self,book):

        if len(self.listNameXML) == 0 :
            self.createNameListXML(book)

        find = -1

        pat = self.namePatient.split()

        for i, item in enumerate(self.listNameXML):
            if item.__contains__(pat[0]) and item.__contains__(pat[1]):
                #print(self.listDateXML[i] + " ==  " + self.datePatient)
                if self.listDateXML[i] == self.datePatient:
                    find = i
                    break
        return find

    def createNameListXML(self, book):

        sh = book.sheet_by_index(0)

        for i in range(1, sh.nrows):
            nameXML = sh.cell_value(rowx=i, colx=2).split()
            self.listNameXML.append(str(nameXML).lower())
            py_date = xlrd.xldate.xldate_as_datetime(sh.cell_value(rowx=i, colx=4), book.datemode).date()
            self.listDateXML.append(py_date)

    def isIncipiente(self,datePatient):
        ret = False
        return ret

    def isLente(self):
        ret = False
        return ret