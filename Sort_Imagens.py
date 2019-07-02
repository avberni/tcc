import pydicom
import os
import cv2


class Sort(object):

    def __init__(self):
        self.dirLoadContents = ""
        self.dirSaveContents = ""
        self.format = 'png'

    def work_imagens(self):

        images_path = os.listdir(self.dirLoadContents.get())

        try:

            for n, image in enumerate(images_path):

                ds = pydicom.read_file(os.path.join(self.dirLoadContents.get(), image))

                # print(ds)

                image = image.replace('.dcm', '.' + self.format)

                eyesectionvalue = 0  # EYSECTION = 1 (Fundo de olho)

                try:
                    for eyesection in ds[0x0040, 0x0555]:
                        if eyesection[0x0040, 0xa043][0][0x0008, 0x0100].value == "Eye section":
                            eyesectionvalue = eyesection[0x0040, 0xa30a].value
                            break
                except KeyError:
                    eyesectionvalue = 2

                path = self.dirSaveContents.get() + '/' + self.format + str(eyesectionvalue)

                if not (os.path.isdir(path)):
                    os.makedirs(path)

                cv2.imwrite(os.path.join(path, image), cv2.cvtColor(ds.pixel_array, cv2.COLOR_RGB2BGR))

        except pydicom.errors.InvalidDicomError:
            print("erro de dicom")
