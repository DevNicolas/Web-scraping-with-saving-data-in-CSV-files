import  csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://scholar.google.es/citations?user=GlM971cAAAAJ&hl=es&oi=ao") #here puts the url od the page
bsObj = BeautifulSoup(html, "lxml")
content_all = bsObj.findAll("table", {"id": "gsc_a_t"}) #find the father structure that contains your info
info = bsObj.findAll("tr") # specify what find in the structure to save
print(content_all)
print(info)
csvFile = open("prueba2.csv", "wt", newline='') #create the csv file to save the info
writer = csv.writer(csvFile)
try:
    for i in info:
        csvRow = []
        for cell in i.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()
