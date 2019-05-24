# import os
# import cv2
# import pathlib
# import random
# import IPython.display as display
# import tensorflow as tf

# # make it True if you want in PNG format
PNG = False

class Train(object):

    dirLoadContents = ""
    attributions = ""
    data_root = ""

    def main(self):

        # self.data_root = tf.keras.utils.get_file('flower_photos','https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz',untar=True)
        # self.data_root = pathlib.Path(self.data_root)
        # print(self.data_root)
        #
        # for item in self.data_root.iterdir():
        #     print(item)
        #
        # all_image_paths = list(self.data_root.glob('*/*'))
        # all_image_paths = [str(path) for path in all_image_paths]
        # random.shuffle(all_image_paths)
        #
        # image_count = len(all_image_paths)
        # print(image_count)
        #
        # self.attributions = (self.data_root / "LICENSE.txt").read_text(encoding="utf8").splitlines()[4:]
        # self.attributions = [line.split(' CC-BY') for line in self.attributions]
        # self.attributions = dict(self.attributions)
        #
        # for n in range(3):
        #     image_path = random.choice(all_image_paths)
        #     display.display(display.Image(image_path))
        #     print(image_path)
        #     print(self.caption_image(image_path))
        #     print()

        print("ok")
