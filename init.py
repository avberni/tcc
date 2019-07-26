# import Windows
#
# def main(args):
#     appProc = Windows.MainDialogs()
#     appProc.execute()
#     return 0
#
# if __name__ == '__main__':
#     import sys
#
#     sys.exit(main(sys.argv))

import encodings

# import tensorflow as tf
#
# filename = "C:\\Users\\dell\\Desktop\\tcc\\teste.jpg"
#
# filenames = tf.constant(['C:\\Users\\dell\\Desktop\\tcc\\teste.jpg'])
# labels = tf.constant([0])
#
# # step 2: create a dataset returning slices of `filenames`
# dataset = tf.data.Dataset.from_tensor_slices((filenames, labels))
#
# # step 3: parse every image in the dataset using `map`
# def _parse_function(filename, label):
#     image_string = tf.read_file(filename)
#     image_decoded = tf.image.decode_jpeg(image_string, channels=3)
#     image = tf.cast(image_decoded, tf.float32)
#     return image, label
#
# dataset = dataset.map(_parse_function)
# dataset = dataset.batch(2)
#
# # step 4: create iterator and final input tensor
# iterator = dataset.make_one_shot_iterator()
# images, labels = iterator.get_next()
#
# sess = tf.Session()
#
# print(sess.run([images, labels]))
#
#
# sess.close()

# import pathlib
# import random
# import IPython.display as display
# import tensorflow as tf
# import numpy as np
# import PIL.Image as Image
#
#
# data_root = tf.keras.utils.get_file('flower_photos','https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz',untar=True)
# data_root = pathlib.Path(data_root)
# #print(data_root)
#
# image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)
# image_data = image_generator.flow_from_directory(str(data_root))
#
# for image_batch,label_batch in image_data:
#   print("Image batch shape: ", image_batch.shape)
#   print("Labe batch shape: ", label_batch.shape)
#   break
#
# print("ok")
#
# features_extractor_layer = layers.Lambda(feature_extractor, input_shape=IMAGE_SIZE+[3])
#
# model = tf.keras.Sequential([
#   features_extractor_layer,
#   layers.Dense(image_data.num_classes, activation='softmax')
# ])
# model.summary()

# import tensorflow as tf
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# #
# #
# # sess = tf.Session()
# #
# #
# #
# # sess.close()
#
# import numpy as np
# import pathlib
# import random
#
#
# data_root = os.path.abspath("C:/Users/andre/Desktop/tcc_dados/JPEG")
# # print(data_root)
# data_root = pathlib.Path(data_root)
# # print(data_root)
# #
# # for item in data_root.iterdir():
# #   print(item)
# #
# # all_image_paths = list(data_root.glob('*/*'))
# # all_image_paths = [str(path) for path in all_image_paths]
# # random.shuffle(all_image_paths)
# #
# # image_count = len(all_image_paths)
# # print(image_count)
# #
# #
# # label_names = sorted(item.name for item in data_root.glob('*/') if item.is_dir())
# # print(label_names)
# #
# # label_to_index = dict((name, index) for index,name in enumerate(label_names))
# # print(label_to_index)
# #
# # all_image_labels = [label_to_index[pathlib.Path(path).parent.name] for path in all_image_paths]
# #
# # print("First 24 labels indices: ", all_image_labels[:24])
#
# # image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)
# # image_data = image_generator.flow_from_directory(str(data_root))
# # print(image_data)

# import numpy as np
# import cv2
#
# img1 = cv2.imread("C:/Users/andre/Desktop/tcc_dados/JPEG/jpeg0/teste1.jpg",cv2.IMREAD_UNCHANGED)
# img2 = cv2.imread("C:/Users/andre/Desktop/tcc_dados/JPEG/jpeg0/teste2.png",cv2.IMREAD_UNCHANGED)
#
# ima = img1 - img2
#
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',ima)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#import Data
from datetime import datetime,date

#db = Data.DBManipulation()

# print(Data.EXTERNA)
#
#pat = Data.Patient("Andrews",32,date(2009, 10, 25))
#
# db.insert(pat)
#
# ima = Data.Image("teste",Data.EXTERNA,30,"D")


# import os
# import pydicom
# import shutil
#
# dcm_load_path = "C:/Users/andre/Desktop/tcc_dados/ds"
#
# images_path = os.listdir(dcm_load_path)
#
# for n, image in enumerate(images_path) :
#
#
#     pathfile = os.path.join(dcm_load_path, image)
#     ds = pydicom.read_file(pathfile)
#
#     bir = ds.PatientBirthDate
#     path_date = ds.PatientName
#
#     la = ds.ImageLaterality
#     ll = ds.HorizontalFieldOfView
#     ls = ds.StudyDate
#
#     try :
#         for eyesection in ds[0x0040, 0x0555] :
#             if eyesection[0x0040, 0xa043][0][0x0008, 0x0100].value == "Eye section":
#                 eyesectionvalue = eyesection[0x0040, 0xa30a].value
#                 break
#     except KeyError :
#         eyesectionvalue = 2
#
#
#     print(pathfile)
#     print(bir)
#     print("\n\n")
#     print(pathfile)
#     print(eyesectionvalue)
#     print(ll)
#     print(la)
#     print(ls)
#
#     print("----------------------------------------------")
#
#     dcm_load_path = "C:/Users/andre/Desktop/tcc_dados/a"
#
#     shutil.copy2(pathfile, dcm_load_path)
#     #print(ds)
#     print("ERRO")

# import os
# import pydicom
# import cv2
#
#
# dcm_load_path = "C:/Users/andre/Desktop/tcc_dados/ds"
#
# images_path = os.listdir(dcm_load_path)
#
# for n, image in enumerate(images_path):
#
#     pathfile = os.path.join(dcm_load_path, image)
#     ds = pydicom.read_file(pathfile)
#
#     image2 = image.replace('.dcm', '.' + 'png')
#     image3 = image.replace('.dcm', '.' + 'jpg')
#
#     dcm_load_path = "C:/Users/andre/Desktop/tcc_dados/a"
#
#     path2 = os.path.join(dcm_load_path, image2)
#     cv2.imwrite(path2, cv2.cvtColor(ds.pixel_array, cv2.COLOR_RGB2BGR))
#
#     path3 = os.path.join(dcm_load_path, image3)
#     cv2.imwrite(path3, cv2.cvtColor(ds.pixel_array, cv2.COLOR_RGB2BGR))
#
#
#
#     i = cv2.imread(path2,cv2.IMREAD_UNCHANGED)
#     ii = cv2.imread(path3, cv2.IMREAD_UNCHANGED)
#
#
#     a = ds.pixel_array - i
#     aa = ds.pixel_array - ii
#     aaa = i - ii
#
#
#
#     cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#     cv2.imshow('image', a)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#     cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#     cv2.imshow('image', aa)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#     cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#     cv2.imshow('image', aaa)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# lista = [10,10,20,10]
#
# for i, item in enumerate(lista):
#     if item == 10:
#         print(i)
#
# import xlrd
# book = xlrd.open_workbook("C:/Users/andre/Desktop/tcc_dados/laudos.xlsx")
# sh = book.sheet_by_index(0)
#
# listNameXML = []
#
# for i in range(1, sh.nrows) :
#     nameXML = sh.cell_value(rowx=i, colx=2).split()
#     listNameXML.append(str(nameXML).lower())
#     print(listNameXML[-1])

# import pydicom
#
# images_path = "C:/Users/andre/Desktop/tcc_dados/26/1.2.276.0.75.2.1.20.0.3.180731122248561.1174051.27557.dcm"
#
# ds = pydicom.read_file(images_path)
# print(ds)
#
# # try:
# #     print(ds.Laterality)
# # except Exception as e:
# #     print(e)
#
# try :
#     for anglesection in ds[0x0040, 0x0555] :
#         if anglesection[0x0040, 0xa043][0][0x0008, 0x0100].value == "Angle" :
#             anglevalue = anglesection[0x0040, 0xa30a].value
#             break
# except KeyError :
#     print("ERROR")
#     anglevalue = 30
#
# print(anglevalue)


# arquivo = open('nome.txt', 'r') # Abra o arquivo (leitura)
# conteudo = arquivo.readlines()
# conteudo.append('Nova linha' + '\n')   # insira seu conteúdo
#
# arquivo = open('nome.txt', 'w') # Abre novamente o arquivo (escrita)
# arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
#
# arquivo.close()

# lista = []
#
# arquivo = open('nome.txt', 'r')
#
# for line in arquivo:
#     if not lista.__contains__(line):
#         lista.append(line)
#
# arquivo.close()
#
# print(len(lista))
# for nome in lista:
#     arquivo = open('nome2.txt', 'r')
#     conteudo = arquivo.readlines()
#     conteudo.append(nome)
#
#     arquivo = open('nome2.txt', 'w')
#     arquivo.writelines(conteudo)
#     arquivo.close()

# import re
#
# nome = input('Qual o seu nome completo? ')
#
# if re.search('enzo', nome, re.IGNORECASE):
#     print("A string tem o nome Enzo")
# else:
#     print("A string não tem o nome Enzo")