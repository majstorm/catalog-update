#!/usr/bin/env python3
import requests
from os import listdir
from os.path import isfile, join

URL = "http://35.239.10.233/upload/"
PATH = "/home/student-00-8e7de78efaaa/supplier-data/images/"

def image_upload(file_img):
    with open(join(PATH,file_img),'rb') as img:
        r = requests.post(URL,files={'file':img})
        print(r.status_code)
    img.close()

if __name__=="__main__":
    #unittest.main()
    for file_img in listdir(PATH):
        if isfile(join(PATH,file_img)) and file_img.endswith(".jpeg"):
            image_upload(file_img)
