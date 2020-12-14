#!/usr/bin/env python3
import psutil
import emails
import shutil
import requests

FROM = "automation@example.com"
TO = "student-00-8e7de78efaaa@example.com"
subject = ""
BODY = "Please check your system and resolve the issue as soon as possible."

cpu = psutil.cpu_percent(interval=1)
memory = shutil.disk_usage('/')
ram = psutil.virtual_memory()
#print(cpu)
#print(memory)
#print(ram)


err=False
r = requests.get('http://localhost')
print(100*memory.free/memory.total, cpu, ram.available >> 20)
if r.status_code=="404":
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    err=True
elif (100*memory.free/memory.total)<20.0:
    subject = "Error - Available disk space is less than 20%"
    err=True
elif (ram.available >>20)<500:
    subject = "Error - Available memory is less than 500MB"
    err=True
elif cpu>80.0:
    subject = "Error - CPU usage is over 80%"
    err=True
if err:
    emails.generate_email(FROM, TO, subject, BODY)
    print("sent report!")
    err=False
