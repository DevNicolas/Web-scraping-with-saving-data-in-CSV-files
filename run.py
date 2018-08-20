import  csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://scholar.google.es/citations?user=GlM971cAAAAJ&hl=es&oi=ao") #here puts the url of the page
bsObj = BeautifulSoup(html,"html.parser")
content_all = bsObj.findAll("table", {"id": "gsc_a_t"}) #find the father structure that contains your info
info = bsObj.findAll("tr") # specify what find in the structure to save
grafica = bsObj.findAll("div", {"class": "gsc_md_hist_b"})
csvFile = open("prueba2.csv", "wt", newline='') #create the csv file to save the info
writer = csv.writer(csvFile)
try:
    for i in info: #create a for to save all the info that will be find
        csvRow = []
        for cell in i.findAll(['td', 'th']):
            csvRow.append(cell.get_text()) #and put it in a list
            writer.writerow(csvRow)

    for año in grafica:
        csvRow.append(año.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()


