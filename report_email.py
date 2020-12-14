#!/usr/bin/env python3
import os
from datetime import date
import reports
import emails
from os import listdir
from os.path import join

DESC_PATH = "supplier-data/descriptions/"
ATTACHMENT = '/tmp/processed.pdf'
FROM = "automation@example.com"
TO = "student-00-8e7de78efaaa@example.com"
SUBJECT = "Upload Completed - Online Fruit Store"
BODY = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
FIELDS = ["name", "weight", "description","image_name"]

if __name__=="__main__":
    paragraph="<br/>"
    fruits = []
    for text_file in listdir(DESC_PATH):
        data = {}
        with open(join(DESC_PATH, text_file),"r") as file:
            for i, line in enumerate(file):
                print(i,line)
                if i==0:
                    paragraph+="name: "+line +"<br/>"
                    data[FIELDS[i]] = line
                elif i==1:
                    paragraph+="weight: "+line +"<br/>"
                    data[FIELDS[i]]=int(line.split(" ")[0])
                else:
                    data[FIELDS[i]] = line
        file.close()
        paragraph+="<br/>"
        fruits.append((data))

    title = "Processed Update on {}".format(date.today().strftime("%B %d, %Y"))

    reports.generate_report(ATTACHMENT, title, paragraph)

    emails.generate_email(FROM, TO, SUBJECT, BODY, ATTACHMENT)
