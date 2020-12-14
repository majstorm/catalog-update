#!/usr/bin/env python3
import os
import datetime
import reports

DESC_PATH = "supplier-data/descriptions/"
ATTACHMENT = '/tmp/processed.pdf'


if __name__=="__main__":
    fruits = []
    for text_file in listdir(DESC_PATH):
        data = {}
        for i, line in enumerate(text_file.readline()):
            if i==1:
                data[FIELDS[i]]=int(line)
            else:
                data[FIELDS[i]] = line
        fruits.append((data))

    reports.generate_report(attachment, title, paragraph)