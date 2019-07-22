import pydicom
import os
import cv2
import Data
import xlrd
from datetime import datetime


class Sort(object):

    def __init__(self):
        self.dirLoadContents = ""
        self.dirSaveContents = ""
        self.format = 'png'
        self.db = Data.DBManipulation()
        self.listImageSelected = []
        self.listNameXML = []
        self.namePatient = ""
        self.datePatient = None
        self.eyePosition = ''
        self.fileName = ""
        self.imagem = None
        self.dicom = None
        self.listDateXML = []

    def work_imagens(self):

        self.listSelected()

        images_path = os.listdir(self.dirLoadContents.get())

        try:

            for n, image in enumerate(images_path):

                ds = pydicom.read_file(os.path.join(self.dirLoadContents.get(), image))
                self.dicom = ds
                namefile = image.split('.dcm')[0]

                if self.listImageSelected.__contains__(namefile):

                    image = image.replace('.dcm', '.' + self.format)
                    self.imagem = image
                    self.insertImage(namefile)

                    path = self.dirSaveContents.get() + '/' + self.format + str(0)

                    if not (os.path.isdir(path)):
                        os.makedirs(path)
                    cv2.imwrite(os.path.join(path, self.imagem), cv2.cvtColor(self.dicom.pixel_array, cv2.COLOR_RGB2BGR))


        except pydicom.errors.InvalidDicomError:
            print("erro de dicom")

    def insertImage(self,file):

        listDate = list(self.dicom.StudyDate)
        dateStudy = listDate[6] + listDate[7] + "/" + listDate[4] + listDate[5] + "/" + listDate[0] + listDate[1] + listDate[2] + listDate[3]
        dateStudy = datetime.strptime(dateStudy, '%d/%m/%Y').date()

        img = self.db.imageSearch(file)

        if len(img) == 0:

            self.fileName = file
            anglevalue  = 60
            laterality = 'L'

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
                laterality = self.dicom.Laterality


            img = Data.Image(file, 0, anglevalue, laterality, dateStudy)
            self.eyePosition = laterality
            self.db.insert(img)
            patient = self.insertPatient()
            self.insertPatIma(patient,img)
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

        if type(patient) is list :
            patient = patient[0]

        return patient

    def insertPatIma(self,patient,image):

        #union = self.db.examSearch(patient,image)

        #if len(union) == 0 :
        value = self.isCatarata()
        #print(str(value) + "    " +  self.fileName + "     " +self.namePatient + "    " + str(self.datePatient))
        exame = Data.Exam(patient,image,value)
        self.db.insert(exame)


    def listSelected(self):

        images_path = os.listdir("C:/Users/andre/Desktop/tcc_dados/Aprovados")

        for n, image in enumerate(images_path):
            namefile = image.split('.jpg')[0]
            self.listImageSelected.append(namefile)

    def isCatarata(self):

        # 0 = False     1 = True
        ret = 0
        book = xlrd.open_workbook("C:/Users/andre/Desktop/tcc_dados/laudos.xlsx")
        sh = book.sheet_by_index(0)

        find = self.findPatient(book)

        if find != -1:
            line = find + 1

            retL = sh.cell_value(rowx=line, colx=8)
            retR = sh.cell_value(rowx=line, colx=5)

            if retL == 0 and retR == 0:
                ret = sh.cell_value(rowx=line, colx=11)
                print(self.namePatient)
                images_path = "C:/Users/andre/Desktop/tcc_dados/FFTCatarata"
                cv2.imwrite(os.path.join(images_path, self.imagem),cv2.cvtColor(self.dicom.pixel_array, cv2.COLOR_RGB2BGR))

            elif self.eyePosition == 'L':
                ret = retL
                images_path = "C:/Users/andre/Desktop/tcc_dados/ComCatarata"
                cv2.imwrite(os.path.join(images_path, self.imagem), cv2.cvtColor(self.dicom.pixel_array, cv2.COLOR_RGB2BGR))
            else:
                ret = retR
                images_path = "C:/Users/andre/Desktop/tcc_dados/ComCatarata"
                cv2.imwrite(os.path.join(images_path, self.imagem),cv2.cvtColor(self.dicom.pixel_array, cv2.COLOR_RGB2BGR))
        else :
            ret = 0
            images_path = "C:/Users/andre/Desktop/tcc_dados/SemCatarata"
            cv2.imwrite(os.path.join(images_path, self.imagem), cv2.cvtColor(self.dicom.pixel_array, cv2.COLOR_RGB2BGR))

            arquivo = open('nome.txt', 'r')
            conteudo = arquivo.readlines()
            conteudo.append(self.namePatient + '\n')

            arquivo = open('nome.txt', 'w')
            arquivo.writelines(conteudo)
            arquivo.close()

        return ret

    def createNameListXML(self,book):

        sh = book.sheet_by_index(0)

        for i in range(1,sh.nrows):
            nameXML = sh.cell_value(rowx=i, colx=2).split()
            self.listNameXML.append(str(nameXML).lower())
            py_date = xlrd.xldate.xldate_as_datetime(sh.cell_value(rowx=i, colx=4),book.datemode).date()
            self.listDateXML.append(py_date)


    def findPatient(self,book):

        if len(self.listNameXML) == 0 :
            self.createNameListXML(book)

        find = -1

        pat = self.namePatient.split()

        for i, item in enumerate(self.listNameXML):
            if item.__contains__(pat[0]) and item.__contains__(pat[1]):
                if self.listDateXML[i] == self.datePatient:
                    find = i
                    break
        return find