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
# a = 1
