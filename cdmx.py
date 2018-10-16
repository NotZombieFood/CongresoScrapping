from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

def roman_to_int(roman, values={'M': 1000, 'D': 500, 'C': 100, 'L': 50, 
                                'X': 10, 'V': 5, 'I': 1}):
    """Convert from Roman numerals to an integer."""
    numbers = []
    for char in roman:
        numbers.append(values[char]) 
    total = 0
    if len(numbers) == 1:
        return numbers[0]
    else:
        for num1, num2 in zip(numbers, numbers[1:]):
            if num1 >= num2:
                total += num1
            else:
                total -= num1
        return total + num2

diputados_guardados = []
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
        #print (diputado.find('span',attrs={"class": "nombre"}).text)
        nombre = diputado.find('span',attrs={"class": "nombre"}).text
        imagen = diputado.find("img", attrs={"class": "retrato"}).attrs['src']
        #print (diputado.find('span',attrs={"class": "cargo"}).text.split(' ')[1])
        if 'Proporcional' in diputado.find('span',attrs={"class": "cargo"}).text or 'Minor' in diputado.find('span',attrs={"class": "cargo"}).text:
            distrito = 'RP'
        else:
            distrito = roman_to_int(diputado.find('span',attrs={"class": "cargo"}).text.split(' ')[1])
        enlace = 'http://www.aldf.gob.mx/' +  diputado.find("a", attrs={"class": 'btn-agregar-diputado'}).attrs['href']
        html_diputado = urlopen(enlace).read()
        soup_diputado = BeautifulSoup(html_diputado, "html.parser")
        li_diputado = soup_diputado.findAll('li')
        correo = ''
        telefono = '51301900'
        for li in li_diputado:
            if 'Contacto' in li.text:
                mini_lis = li.findAll('li')
                for mini_li in mini_lis:
                    if '@aldf.gob.mx' in mini_li.text:
                        correo = mini_li.text.replace('Correo: ','')
                    if 'Extensión' in mini_li.text:
                        magic_string = mini_li.text.replace('Extensión: ','').replace(' ','')
                        if magic_string != '':
                            telefono = telefono + 'Ext.' + magic_string
        if nombre not in diputados_guardados:
            diputados_guardados.append(nombre)
            resultados = [nombre.replace("\n",""),imagen,'Ciudad de México',distrito,correo.replace("\n",""),telefono]
        with open(r'cdmx.csv', 'a',encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(resultados)
        try:
            file_object = open('cdmx.csv', 'r',encoding='UTF-8')
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
                file_object = open('cdmx.csv', 'w',encoding='UTF-8')
                for line in data:
                    str1 = ','.join(line)
                    file_object.write(str1+"\n")
                file_object.close() 
        except Exception as e:
            print (e)

        
