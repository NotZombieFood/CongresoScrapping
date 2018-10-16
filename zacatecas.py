# clase distrito = distrito
# clase nombre = nomdip
#col-md-2

from bs4 import BeautifulSoup
import requests, csv

url = 'http://www.congresozac.gob.mx'
http_request = requests.get(url)
html = http_request.content
soup = BeautifulSoup(html, "html.parser")
contenedores = soup.findAll("div", attrs={"class": "col-md-2"})
for contenedor in contenedores:
    nombre = contenedor.find("div", attrs={"class": "nomdip"}).text
    distrito_prev = contenedor.find("span", attrs={"class": "distrito"}).text.lower()
    if 'prop' in distrito_prev:
        distrito = 'RP'
    elif 'xviii' in distrito_prev:
        distrito = '18'
    elif 'xvii' in distrito_prev:
        distrito = '17'
    elif 'xvi' in distrito_prev:
        distrito = '16'
    elif 'xv' in distrito_prev:
        distrito = '15'
    elif 'xiv' in distrito_prev:
        distrito = '14'
    elif 'xiii' in distrito_prev:
        distrito = '13'
    elif 'xii' in distrito_prev:
        distrito = '12'
    elif 'xi' in distrito_prev:
        distrito = '11'
    elif 'x' in distrito_prev:
        distrito = '10'
    elif 'ix' in distrito_prev:
        distrito = '9'
    elif 'viii' in distrito_prev:
        distrito = '8'
    elif 'vii' in distrito_prev:
        distrito = '7'
    elif 'vi' in distrito_prev:
        distrito = '6'
    elif 'v' in distrito_prev:
        distrito = '5'
    elif 'iv' in distrito_prev:
        distrito = '4'
    elif 'iii' in distrito_prev:
        distrito = '3'
    elif 'ii' in distrito_prev:
        distrito = '2'
    elif 'i' in distrito_prev:
        distrito = '1'
    else:
        distrito = ''
    imagen = url + contenedor.find('img').attrs['src']
    resultados = [nombre,imagen,'Zacatecas',distrito,'','']
    with open(r'zacatecas.csv', 'a',encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(resultados)
    try:
        file_object = open('zacatecas.csv', 'r',encoding='UTF-8')
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
            file_object = open('zacatecas.csv', 'w',encoding='UTF-8')
            for line in data:
                str1 = ','.join(line)
                file_object.write(str1+"\n")
            file_object.close() 
    except Exception as e:
        print (e)

