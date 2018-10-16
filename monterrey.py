# clase boton btn btn-default btn-block


from bs4 import BeautifulSoup
import requests, csv

url = 'http://www.hcnl.gob.mx/organizacion/diputados.php'
http_request = requests.get(url)
html = http_request.content
soup = BeautifulSoup(html, "html.parser")
botones = soup.findAll("a", attrs={"class": "btn btn-default btn-block"})
for boton in botones:
    url_partido = 'http://www.hcnl.gob.mx/organizacion/' + boton.attrs['href']
    http_request = requests.get(url_partido)
    html = http_request.content
    sitioPartido = BeautifulSoup(html, "html.parser")
    diputados = sitioPartido.findAll('div',attrs={"class":"list-group-item"})
    for diputado in diputados:
        nombre = diputado.find('h4',attrs={'class':'media-heading'}).text.title()
        distrito = diputado.findAll('div',attrs={'class':'col-md-2'})[1].text.replace('\n','').replace('\t','').split(':')[1]
        imagen = diputado.find('img').attrs['src']
        resultados = [nombre,imagen,'Nuevo León',distrito,'','']
        with open(r'nl.csv', 'a',encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(resultados)
        try:
            file_object = open('nl.csv', 'r',encoding='UTF-8')
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
                file_object = open('nl.csv', 'w',encoding='UTF-8')
                for line in data:
                    str1 = ','.join(line)
                    file_object.write(str1+"\n")
                file_object.close() 
        except Exception as e:
            print (e)

