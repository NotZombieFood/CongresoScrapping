from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

senadores = 'http://www.senado.gob.mx/64/senadores'
html = urlopen(senadores).read()
soup = BeautifulSoup(html, "html.parser")
paneles = soup.findAll("div", attrs={"class": "panel-SG"})
for senador in paneles: 
    nombre = senador.find("div", attrs={"class": "panel-heading"}).text.replace('\n','')
    estado = senador.find("div", attrs={"class": "panel-footer"}).text.replace('\n','')
    imagen = 'http://www.senado.gob.mx' + senador.find("img", attrs={"class": "img-rounded"}).attrs['src']
    parrafos = senador.findAll("p", attrs={"class": "text-left"})
    email = 'No encontrado'
    telefono = 'No encontrado'
    for parrafo in parrafos:
        if 'Tel:' in parrafo.text:
            enlaces = parrafo.findAll('a')
            for enlace in enlaces:
                if 'mailto' in enlace.attrs['href']:
                    email = enlace.attrs['href'].replace('mailto:','')
                elif 'tel' in enlace.attrs['href']:
                    telefono = enlace.attrs['href'].replace('tel:','')
    resultados = [nombre,imagen,estado,email,telefono]
    with open(r'senadores.csv', 'a',encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(resultados)
    try:
        file_object = open('senadores.csv', 'r',encoding='UTF-8')
        lines = csv.reader(file_object, delimiter=',', quotechar='"')
        flag = 0
        data=[]
        for line in lines:
            if line == []:
                flag =1
                continue
            else:
                data.append(line)
        file_object.close()
        if flag ==1: #if blank line is present in file
            file_object = open('senadores.csv', 'w',encoding='UTF-8')
            for line in data:
                str1 = ','.join(line)
                file_object.write(str1+"\n")
            file_object.close() 
    except Exception as e:
        print (e)