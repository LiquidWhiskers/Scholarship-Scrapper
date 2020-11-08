
import csv
from bs4 import BeautifulSoup
mypath = "E:\\Downloads\\New folder\\"
from os import listdir
from os.path import isfile, join
directory = listdir(mypath)
print(directory)
files = []
for file in directory:
    path = mypath + file
    if isfile(path):
        files.append(path)
print (files)
output = []
for file in files:
    file = open(file)
    soup = BeautifulSoup(file, 'html.parser')
    soup = soup.find("div", {"class": "searchResults lastField"})
    data = soup.findAll("div", {"class": "searchResultOption bottomBrdrThin left"})
    for entry in range(len(data)):
        info = []
        entry = data[entry]
        title = entry.h3.a.get_text()
        info.append(title)
        
        fields = entry.findAll("div", {"class": "searchResultOptionField copySm left clearBoth"})
        for value in fields:
            value = value.find("div", {"class": "left"})
            text = value.get_text()
            info.append(text)
        output.append(info)

with open('data.csv','w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for entry in range(len(output)):
        print(output[entry])
        writer.writerow(output[entry])
        
    




