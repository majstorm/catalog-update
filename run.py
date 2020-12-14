#!/usr/bin/env python3
import os
import requests
from os import listdir
from os.path import join

DESC_PATH = "/home/student-00-8e7de78efaaa/supplier-data/descriptions/"
FIELDS = ["name","weight", "description", "image_name"]
URL = "http://35.239.10.233/fruits/"

def add_fruit(data):
    r = requests.post(URL,data = data)
    print(r.status_code)

if __name__=="__main__":
    #unittest.main()
    for text_file in listdir(DESC_PATH):
        data = {}
        with open(join(DESC_PATH,text_file),"r") as file:
            for i, line in enumerate(file):
                print(line)
                if i==1:
                    data[FIELDS[i]]=int(line.split(" ")[0])
                else:
                    data[FIELDS[i]] = line
            data["image_name"] = text_file[:-4]+".jpeg"
            print(data)
        file.close
        add_fruit(data)
