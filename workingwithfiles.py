#!/usr/bin/env python3

file = open(textfile.txt)
# Opens the file
print(file.readline())
# Reads oneline in the file
print(file.read())
#reads the whole file
file.close()
#closes the files

with open("spider.txt") as file:
    print(file.readline())


with open("textfile.txt") as file:
    for line in file:
        print(line.upper())

with open("textfile.txt") as file:
    for line in file:
        print(line.strip().upper())

# The second one is to take out extra white space with the strip function.

file = open(textfile.txt)
lines = file.readlines()
file.close()
lines.sort()
print(lines)

with open("textfile.txt", "w") as file:
    file.write("it was a dark and story night")
# The w is opening the file in write mode.  r is read-only but is the default  a is to append to a file and r+ is read/write
#file.write displays letter count and the end if it runs successfully
#https://docs.python.org/3/library/functions.html#open
#OS module will be used heavly.  Basically like being on the commandline.

import os
os.remove("novel.txt")
os.rename("first_draft.txt" , "Finished.txt")
os.path.exists("finished_masterpiece.txt")
os.path.exists("deshaonlamar.txt")

os.path.getsize("deshaon.txt")
os.path.getmtime("deshaon.txt")

# can use relevant and obsolute paths
os.path.abspath("deshaon.txt")

print(os.getcwd())
os.mkdir("new_dir")
os.chdir("new_dir")
print(os.getcwd())

os.mkdir("newer_dir")
os.rmdir("newer_dir")

os.listdir("website")
#['images', 'index.html', 'favicon.ico']
dir = "website"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

# THis script above determines of object is a files or a directory.

#CVS files
#Parseing a file
import csv
file = open("csv_file.txt")
csv_file = csv.reader(file)

for row in cvs_file:
    name, phone, role = row
    print("name: {}, phone: {}, Role: {}".format(name, phone, role))

f.close()

hosts = [["workstation.local", "192.168.1.1"], ["webserver.cloud", "10.1.1.1"]]

with open('textfile.txt', 'w') as hosts_csv:
    write = csv.writer(hosts_cvs)
    writer.writerows(hosts)

#cat host_cvs.txt

























