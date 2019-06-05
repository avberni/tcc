import Windows

def main(args):
    appProc = Windows.MainDialogs()
    appProc.execute()
    return 0

if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))

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

# db = Database.DBManipulation()
#
# #db.insertPeople()
# db.insertImage()
#
# a = 1.strftime('%Y/%m/%d')

# from datetime import date,timedelta,datetime
#
# now = date.today()
#
# datestart = now + timedelta(days=1)
#
# op = str(datestart)
#
# op2 = datetime.strptime(op, '%Y-%m-%d')
#
# print(op2)

# numeros = [1,2,3,4,5,6,7,8,9]
#
# a = filter(lambda a: a > 4,numeros)
#
# print(list(a))

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

