#!/usr/bin/env python3
from PIL import Image
from os import listdir
from os.path import isfile, join
import unittest

PATH = "~/supplier-data/images/"

class TestImageTransform(unittest.TestCase):
    def test_bad_file(self):
        self.assertEqual(image_transform("/"), "Not an Image")
    def test_correct_file(self):
        self.assertEqual(image_transform("file_example_TIFF_1MB",""),"Image saved successfuly!")

def image_transform(img_src, img_path=""):
    try:
        img = Image.open(join(img_path,img_src))
    except:
        return("Not an Image")
    img_res = img.resize((600,400))
    try:
        img_res.convert('RGB').save(img_src, "jpeg")
    except:
        return("Could not save image")
    return "Image saved successfuly!"
    

if __name__=="__main__":
    unittest.main()
    for file_img in listdir(PATH):
        if isfile(join(PATH,file_img)):
            image_transform(file_img,PATH)
