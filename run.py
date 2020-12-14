#!usr/bin/env python3
import os
import requests

DESC_PATH = "supplier-data/descriptions/"
FIELDS = ["name","weight", "description", "image_name"]
URL = "/"

def add_fruit(data):
    r = requests.post(URL,data = data)

if __name__=="__main__":
    unittest.main()
    for text_file in listdir(DESC_PATH):
        data = {}
        for i, line in enumerate(text_file.readline()):
            if i==1:
                data[FIELDS[i]]=int(line)
            else:
                data[FIELDS[i]] = line
        add_fruit(data)
            