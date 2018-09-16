from bs4 import BeautifulSoup
import requests, csv

url = 'http://congresogro.gob.mx/inicio/diputados/'
http_request = requests.get(url)
html = http_request.content
soup = BeautifulSoup(html, "html.parser")
contenedor = soup.find("div", attrs={"class": "card-content"})
diputados = contenedor.findAll("tr")
for diputado in diputados[1:]:
    elementos = diputado.findAll('td')
    nombre = elementos[0].text
    try:
        distrito = int(elementos[1].text)
    except:
        distrito = 'RP'
    try:
        imagen = 'http://congresogro.gob.mx/inicio/diputados/' + diputado.find('img',attrs={"class":"foto"}).attrs['src'].replace(' ','%20')
    except:
        imagen = 'http://www.diverfarming.eu/images/img/static/equipo/avatar-generico.png'
    resultados = [nombre,imagen,'Guerrero',distrito,'','']
    with open(r'guerrero.csv', 'a',encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(resultados)
    try:
        file_object = open('guerrero.csv', 'r',encoding='UTF-8')
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
            file_object = open('guerrero.csv', 'w',encoding='UTF-8')
            for line in data:
                str1 = ','.join(line)
                file_object.write(str1+"\n")
            file_object.close() 
    except Exception as e:
        print (e)

