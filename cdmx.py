from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

url = 'http://www.aldf.gob.mx/conoce-tu-diputado-105-1.html'
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
partidos = soup.findAll("a", attrs={"class": "list-group-item"})
for partido in partidos: 
    url_partido  = 'http://www.aldf.gob.mx/' + partido.attrs['href']
    html_partido = urlopen(url_partido).read()
    soup_partido = BeautifulSoup(html_partido, "html.parser")
    div_diputados = soup_partido.find("div", attrs={"class": "lista-diputados"})
    diputados = div_diputados.findAll('li')
    for diputado in diputados:
        nombre = diputado.find('span',attrs={"class": "nombre"}).text.split(' ')[1]
        imagen = diputado.find("img", attrs={"class": "retrato"}).attrs['src']
        nombre = senador.find("div", attrs={"class": "panel-heading"}).text.replace('\n','')
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