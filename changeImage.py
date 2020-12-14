#!/usr/bin/env python3
from PIL import Image
from os import listdir
from os.path import isfile, join
import unittest

PATH = "/home/student-00-8e7de78efaaa/supplier-data/images/"

class TestImageTransform(unittest.TestCase):
    def test_bad_file(self):
        self.assertEqual(image_transform("/"), "Not an Image")
    def test_correct_file(self):
        self.assertEqual(image_transform("file_example_TIFF_1MB",""),"Image saved successfuly!")

def image_transform(img_src, img_path=""):
    try:
        img = Image.open(join(img_path,img_src))
        img_res = img.resize((600,400))
        print(join(img_path, img_src[:-5]))
        img_res.convert('RGB').save(join(img_path,img_src[:-5])+".jpeg", "jpeg")
    except:
        print("Could not save image")
    print("Image saved successfuly!")


if __name__=="__main__":
    #unittest.main()
    for file_img in listdir(PATH):
        if isfile(join(PATH,file_img)):
            image_transform(file_img,PATH)