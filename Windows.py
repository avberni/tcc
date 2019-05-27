#import tkinter as tk
from tkinter import *
import tkinter.filedialog as file
import os
from datetime import datetime
import Search_Imagens
import Sort_Imagens
import Train_Imagens


Search_Ima = Search_Imagens.Search()
Sort_Ima   = Sort_Imagens.Sort()
Train_Ima  = Train_Imagens.Train()
PADX = 5
PADY = 5

class MainDialogs(object):

    AppName = "Main"
    CurrDir = os.getcwd()

    def __init__(self,**kw):

        self.root = Tk()
        self.root.title(self.AppName)
        self.root.resizable(width=False, height=False)

        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.root.winfo_screenwidth() / 3 - windowWidth / 3)
        positionDown = int(self.root.winfo_screenheight() / 3 - windowHeight / 3)

        # Positions the window in the center of the page.
        self.root.geometry("+{}+{}".format(positionRight, positionDown))

        self.findBtn = Button(self.root, text="Procura", command=self.finddialogs,height=5,width=10,justify=CENTER)
        self.findBtn.grid(row=0, column=0, padx=PADX, pady=PADY)

        self.sortBtn = Button(self.root, text="Separa", command=self.sortdialogs,height=5,width=10,justify=CENTER)
        self.sortBtn.grid(row=0, column=1, padx=PADX, pady=PADY)

        self.treineBtn = Button(self.root, text="Treina", command=self.traindialogs, height=5,width=10,justify=CENTER)
        self.treineBtn.grid(row=0, column=2, padx=PADX, pady=PADY)

        self.testBtn = Button(self.root, text="Testa", command=self.testedialogs, height=5,width=10,justify=CENTER)
        self.testBtn.grid(row=0, column=3, padx=PADX, pady=PADY)


    def execute(self):
        self.root.mainloop()

    def finddialogs(self):
        self.root.destroy()
        appProc = FindDialogs()
        appProc.execute()

    def sortdialogs(self):
        self.root.destroy()
        appProc = SortDialogs()
        appProc.execute()

    def traindialogs(self):
        self.root.destroy()
        appProc = TrainDialogs()
        appProc.execute()

    def testedialogs(self):
        self.root.destroy()
        appProc = MainDialogs()
        appProc.execute()



class FindDialogs(object):

    AppName = "Extrair fotos"
    FrameWidth = 200
    FrameHeight = 100
    CurrDir = os.getcwd()

    def __init__(self, **kw):

        self.root = Tk()
        self.root.title(self.AppName)
        self.root.resizable(width=False,height=False)

        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        # print("Width", windowWidth, "Height", windowHeight)

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.root.winfo_screenwidth() / 3 - windowWidth / 3)
        positionDown = int(self.root.winfo_screenheight() / 3 - windowHeight / 3)

        # Positions the window in the center of the page.
        self.root.geometry("+{}+{}".format(positionRight, positionDown))
        self.create_widget_find()

    def execute(self):
        self.root.mainloop()

    def create_widget_find(self):

        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y")

        self.dataStartFrame = Frame(self.root)
        self.dataEndFrame   = Frame(self.root)

        self.dataStartLabel = Label(self.dataStartFrame,text="Data Inicio:")
        self.dataEndLabel   = Label(self.dataEndFrame,text="Data Fim:")
        self.dirLoadLabel   = Label(self.root, text="Selecione diretorio das fotos:")
        self.dirSaveLabel   = Label(self.root, text="Selecione diretorio para savar as fotos:")

        self.dataStartLabel.grid(sticky=W)
        self.dataEndLabel.grid(sticky=W)
        self.dirLoadLabel.grid(sticky=W,row=1,column=0,padx=PADX,pady=PADY)
        self.dirSaveLabel.grid(sticky=W,row=2,column=0,padx=PADX,pady=PADY)

        self.dataStartContents = StringVar(value=date_time)
        self.dataEndContents = StringVar(value=date_time)
        self.dirLoadContents = StringVar()
        self.dirSaveContents = StringVar()

        self.dataStartEntry = Entry(self.dataStartFrame,width=23,textvariable=self.dataStartContents)
        self.dataEndEntry   = Entry(self.dataEndFrame, width=22,textvariable=self.dataEndContents)
        self.dirLoadEntry = Entry(self.root, width=31,textvariable=self.dirLoadContents)
        self.dirSaveEntry = Entry(self.root, width=31,textvariable=self.dirSaveContents)

        self.dataStartEntry.grid(row=0,column=1)
        self.dataEndEntry.grid(row=0, column=1)

        #main principal
        self.dataStartFrame.grid(row=0,column=0)
        self.dataEndFrame.grid(row=0, column=1)
        self.dirLoadEntry.grid(row=1, column=1)
        self.dirSaveEntry.grid(row=2, column=1)

        self.dirLoadBtn = Button(self.root, text="Select", command=self.file_directory_load)
        self.dirSaveBtn = Button(self.root, text="Select", command=self.file_directory_save)

        self.dirLoadBtn.grid(row=1, column=2,padx=PADX,pady=PADY)
        self.dirSaveBtn.grid(row=2, column=2,padx=PADX,pady=PADY)

        Search_Ima.dataStartContents = self.dataStartContents
        Search_Ima.dataEndContents   = self.dataEndContents
        Search_Ima.dirLoadContents   = self.dirLoadContents
        Search_Ima.dirSaveContents   = self.dirSaveContents

        self.okBtn = Button(self.root, text="OK", command=self.ok, width=5)
        self.okBtn.grid(row=3, column=1,sticky=E,padx=PADX,pady=PADY)

        self.backBtn = Button(self.root, text="Voltar", command=self.voltar,width=5)
        self.backBtn.grid(row=3, column=2)

    def file_directory_load(self):

        try:
            temp = file.askdirectory(parent=self.root, initialdir=self.CurrDir, title='Path')
            self.dirLoadContents.set(temp)
        except AttributeError:
            print("Vazio")

    def file_directory_save(self):

        try:
            temp = file.askdirectory(parent=self.root, initialdir=self.CurrDir, title='Path')
            self.dirSaveContents.set(temp)
        except AttributeError:
            print("Vazio")

    def file_select(self):

        try:
            temp = file.askopenfilename(parent=self.root, initialdir=self.CurrDir, title='File',filetypes=[('Todos arquivos', '.*')])
            self.fileContents.set(temp)
        except AttributeError:
            print("Vazio")

    def ok(self):
        self.root.destroy()
        Search_Ima.work_list()

    def voltar(self):

        self.root.destroy()
        appProc = MainDialogs()
        appProc.execute()


class SortDialogs(object):

    AppName = "Separa fotos"
    FrameWidth = 1000
    FrameHeight = 400
    CurrDir = os.getcwd()

    def __init__(self, **kw):

        self.root = Tk()
        self.root.title(self.AppName)
        #self.root.geometry('%dx%d+%d+%d' % (self.FrameWidth, self.FrameHeight, self.root.winfo_screenwidth() / 4, self.root.winfo_screenheight() / 4))

        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        # print("Width", windowWidth, "Height", windowHeight)

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.root.winfo_screenwidth() / 3 - windowWidth / 3)
        positionDown = int(self.root.winfo_screenheight() / 3 - windowHeight / 3)

        # Positions the window in the center of the page.
        self.root.geometry("+{}+{}".format(positionRight, positionDown))

        self.create_dialog_sort()

    def create_dialog_sort(self):

        self.dirLoadContents = StringVar()
        self.dirSaveContents = StringVar()

        self.dirLoadLabel = Label(self.root, text="Selecione diretorio DCM:")
        self.dirSaveLabel = Label(self.root, text="Selecione diretorio para salvar JPEG:")

        self.dirLoadLabel.grid(sticky=W, padx=PADX,pady=PADY)
        self.dirSaveLabel.grid(sticky=W, padx=PADX,pady=PADY)

        self.dirLoadEntry = Entry(self.root, width=30,textvariable=self.dirLoadContents)
        self.dirSaveEntry = Entry(self.root, width=30,textvariable=self.dirSaveContents)

        self.dirLoadEntry.grid(row=0, column=1, padx=PADX,pady=PADY)
        self.dirSaveEntry.grid(row=1, column=1, padx=PADX,pady=PADY)

        self.dirLoadBtn = Button(self.root, text="Select", command=self.file_directory_load)
        self.dirSaveBtn = Button(self.root, text="Select", command=self.file_directory_save)

        self.dirLoadBtn.grid(row=0, column=2, padx=PADX,pady=PADY)
        self.dirSaveBtn.grid(row=1, column=2, padx=PADX,pady=PADY)

        Sort_Ima.dirLoadContents = self.dirLoadContents
        Sort_Ima.dirSaveContents = self.dirSaveContents

        self.okBtn = Button(self.root, text="OK", command=self.ok, width=5)
        self.okBtn.grid(row=2, column=1, sticky=E, padx=PADX,pady=PADY)

        self.backBtn = Button(self.root, text="Voltar", command=self.voltar, width=5)
        self.backBtn.grid(row=2, column=2, padx=PADX,pady=PADY)

        #self.status = tk.Label(self.root, text="Loading", bd=1, relief=SUNKEN, anchor=E)
        #self.status.grid(row=3, column=0, padx=5, pady=5)

    def ok(self):
        #self.root.destroy()
        Sort_Ima.work_imagens()

    def voltar(self):
        self.root.destroy()
        appProc = MainDialogs()
        appProc.execute()

    def execute(self):
        self.root.mainloop()

    def file_directory_load(self):

        try:
            temp = file.askdirectory(parent=self.root, initialdir=self.CurrDir, title='Path')
            self.dirLoadContents.set(temp)
        except AttributeError:
            print("Vazio")

    def file_directory_save(self):

        try:
            temp = file.askdirectory(parent=self.root, initialdir=self.CurrDir, title='Path')
            self.dirSaveContents.set(temp)
        except AttributeError:
            print("Vazio")


class TrainDialogs(object):

    AppName = "Treinar"
    FrameWidth = 1000
    FrameHeight = 400
    CurrDir = os.getcwd()

    def __init__(self, **kw):
        self.root = Tk()
        self.root.title(self.AppName)

        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.root.winfo_screenwidth() / 3 - windowWidth / 3)
        positionDown = int(self.root.winfo_screenheight() / 3 - windowHeight / 3)

        # Positions the window in the center of the page.
        self.root.geometry("+{}+{}".format(positionRight, positionDown))
        self.create_dialog_train()

    def create_dialog_train(self):

        self.dirLoadLabel = Label(self.root, text="Selecione diretorio com as fotos JPEG:")

        self.dirLoadLabel.grid(sticky=W, padx=PADX,pady=PADY)

        self.dirLoadEntry = Entry(self.root, width=30)

        self.dirLoadEntry.grid(row=0, column=1, padx=PADX,pady=PADY)

        self.dirLoadBtn = Button(self.root, text="Select", command=self.file_directory_load)

        self.dirLoadBtn.grid(row=0, column=2, padx=PADX,pady=PADY)

        self.dirLoadContents = StringVar()

        self.dirLoadEntry["textvariable"] = self.dirLoadContents
        Train_Ima.dirLoadContents = self.dirLoadContents

        self.okBtn = Button(self.root, text="OK", command=self.ok, width=5)
        self.okBtn.grid(row=1, column=1, sticky=E, padx=PADX,pady=PADY)

        self.backBtn = Button(self.root, text="Voltar", command=self.voltar, width=5)
        self.backBtn.grid(row=1, column=2, padx=PADX,pady=PADY)



    def ok(self):
        #self.root.destroy()
        Train_Ima.main()

    def voltar(self):
        self.root.destroy()
        appProc = MainDialogs()
        appProc.execute()

    def execute(self):
        self.root.mainloop()

    def file_directory_load(self):

        try:
            temp = file.askdirectory(parent=self.root, initialdir=self.CurrDir, title='Path')
            self.dirLoadContents.set(temp)
        except AttributeError:
            print("Vazio")