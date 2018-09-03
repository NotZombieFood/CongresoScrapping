from bs4 import BeautifulSoup
import requests, csv, re

class_link = 'linkVerde' 
base_url = 'http://sitl.diputados.gob.mx/LXIV_leg'
url = 'http://sitl.diputados.gob.mx/LXIV_leg/listado_diputados_gpnp.php'
http_request = requests.get(url)
page = http_request.content
soup = BeautifulSoup(page, "html.parser")
diputados = soup.findAll("tr")[4].findAll("tr")
for diputado in diputados[4:]:
    diputado_url = 'http://sitl.diputados.gob.mx/LXIV_leg/' + diputado.find("a", attrs={"class": "linkVerde"}).attrs['href']
    textos = diputado.findAll("td", attrs={"class": "textoNegro"})
    #nombre = re.sub(r'\d+','',textos[0].text).replace('\xa0','')
    estado = re.sub(r'\d+','',textos[1].text).replace('\xa0','')
    distrito = re.sub(r'.*\s+','',textos[2].text).replace('\xa0','')
    diputado_http = requests.get(diputado_url)
    diputado_web = diputado_http.content
    moreSoup = BeautifulSoup(diputado_web,'html.parser')
    nombre =  moreSoup.find("center").text
    imagen = 'http://sitl.diputados.gob.mx/LXIV_leg/' +  moreSoup.find("img",attrs={'class':'fotodip'}).attrs['src'][2:]
    tipo_elecction =  moreSoup.findAll("td",attrs={'class':'textocurri',"width":"470"})[0].text
    email = moreSoup.findAll("td",attrs={'class':'textocurri',"width":"470"})[2].text
    if email == ' ':
        email = 'Email no registrado'
    resultados = [nombre,imagen,email, tipo_elecction, distrito, estado, diputado_url]
    with open(r'diputados.csv', 'a',encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(resultados)
    try:
        file_object = open('diputados.csv', 'r',encoding='UTF-8')
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
            file_object = open('diputados.csv', 'w',encoding='UTF-8')
            for line in data:
                str1 = ','.join(line)
                file_object.write(str1+"\n")
            file_object.close() 
    except Exception as e:
        print (e)