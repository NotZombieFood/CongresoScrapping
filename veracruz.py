from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

url = 'http://www.legisver.gob.mx/Inicio.php?p=legis'
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
diputados = soup.findAll("div", attrs={"class": "col l5 m4 s5"})

urls = []
for diputado in diputados[1:]:
    urls.append("http://www.legisver.gob.mx/" + diputado.findChild().get_attribute_list("onclick")[0].split("'")[1])

for enlace in urls:
    html = urlopen(enlace).read()
    soup = BeautifulSoup(html, "html.parser")
    imagen = "http://www.legisver.gob.mx/" + soup.find("div", attrs={"class": "backImage"}).findChild().attrs['src']
    resultados = soup.findAll("div", attrs={"class": "col l7 m7 s7"})
    telefono = resultados[len(resultados)-2].text.replace("\n","") + "Ext." + resultados[len(resultados)-1].text.replace("\n","")
    for resultado in resultados:
        if "legisver.gob.mx" in resultado.text:
            email = resultado.text
            break
    for resultado in resultados:
        if 'proporcional' in resultado.text.lower():
            distrito = 'RP'
            break
        elif ' i.' in resultado.text.lower():
            distrito = '1'
            break
        elif ' ii.' in resultado.text.lower():
            distrito = '2'
            break
        elif ' iii.' in resultado.text.lower():
            distrito = '3'
            break
        elif ' iv.' in resultado.text.lower():
            distrito = '4'
            break
        elif ' v.' in resultado.text.lower():
            distrito = '5'
            break
        elif ' vi.' in resultado.text.lower():
            distrito = '6'
            break
        elif ' vii.' in resultado.text.lower():
            distrito = '7'
            break
        elif ' viii.' in resultado.text.lower():
            distrito = '8'
            break
        elif ' ix.' in resultado.text.lower():
            distrito = '9'
            break
        elif ' x.' in resultado.text.lower():
            distrito = '10'
            break
        elif ' xi.' in resultado.text.lower():
            distrito = '11'
            break
        elif ' xii.' in resultado.text.lower():
            distrito = '12'
            break
        elif ' xiii.' in resultado.text.lower():
            distrito = '13'
            break
        elif ' xiv.' in resultado.text.lower():
            distrito = '14'
            break
        elif ' xv.' in resultado.text.lower():
            distrito = '15'
            break
        elif ' xvi.' in resultado.text.lower():
            distrito = '16'
            break
        elif ' xvii.' in resultado.text.lower():
            distrito = '17'
            break
        elif ' xviii.' in resultado.text.lower():
            distrito = '18'
            break
        elif ' xix.' in resultado.text.lower():
            distrito = '19'
            break
        elif ' xx.' in resultado.text.lower():
            distrito = '20'
            break
        elif ' xxi.' in resultado.text.lower():
            distrito = '11'
            break
        elif ' xxii.' in resultado.text.lower():
            distrito = '12'
            break
        elif ' xxiii.' in resultado.text.lower():
            distrito = '13'
            break
        elif ' xxiv.' in resultado.text.lower():
            distrito = '14'
            break
        elif ' xxv.' in resultado.text.lower():
            distrito = '15'
            break
        elif ' xxvi.' in resultado.text.lower():
            distrito = '16'
            break
        elif ' xxvii.' in resultado.text.lower():
            distrito = '17'
            break
        elif ' xxviii.' in resultado.text.lower():
            distrito = '18'
            break
        elif ' xxix.' in resultado.text.lower():
            distrito = '19'
            break
        elif ' xxx.' in resultado.text.lower():
            distrito = '20'
            break
        else:
            distrito = ''
    nombre = soup.find("h5").text
    resultados = [nombre,imagen,'Veracruz',distrito,email,telefono]
    with open(r'veracruz.csv', 'a',encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(resultados)
    try:
        file_object = open('veracruz.csv', 'r',encoding='UTF-8')
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
            file_object = open('veracruz.csv', 'w',encoding='UTF-8')
            for line in data:
                str1 = ','.join(line)
                file_object.write(str1+"\n")
            file_object.close() 
    except Exception as e:
        print (e)

