import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#Configure stuff for headless browser
options = Options()
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
#options.add_argument("--headless")
options.add_argument('log-level=2')
options.add_argument("window-size=1400,600")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Chromedriver\chromedriver.exe')
driver.implicitly_wait(10)
print ("Headless Chrome Initialized")

urls = []
sitios = ['http://www.congresonayarit.mx/diputados-pan/','http://www.congresonayarit.mx/diputados-pri/','http://www.congresonayarit.mx/diputados-prd/','http://www.congresonayarit.mx/diputados-pt/','http://www.congresonayarit.mx/diputados-morena/','http://www.congresonayarit.mx/diputados-mc/','http://www.congresonayarit.mx/diputados-nueva-alianza']
for sitio in sitios:
    driver.get(sitio)
    diputados = driver.find_elements_by_class_name('vc_btn3-color-juicy-pink')
    for diputado in diputados:
        urls.append(diputado.get_attribute('href'))
 
driver.close()
print ('Driver has been closed.')
print (urls)
for url in urls:
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    nombre = soup.find("h1", attrs={"class": "title"}).text
    distrito_stuff = soup.find("h3").text.lower()
    if 'proporcional' in distrito_stuff:
        distrito = 'RP'
    elif ' i,' in distrito_stuff:
        distrito = '1'
    elif ' ii,' in distrito_stuff:
        distrito = '2'
    elif ' iii,' in distrito_stuff:
        distrito = '3'
    elif ' iv,' in distrito_stuff:
        distrito = '4'
    elif ' v,' in distrito_stuff:
        distrito = '5'
    elif ' vi,' in distrito_stuff:
        distrito = '6'
    elif ' vii,' in distrito_stuff:
        distrito = '7'
    elif ' viii,' in distrito_stuff:
        distrito = '8'
    elif ' ix,' in distrito_stuff:
        distrito = '9'
    elif ' x,' in distrito_stuff:
        distrito = '10'
    elif ' xi,' in distrito_stuff:
        distrito = '11'
    elif ' xii,' in distrito_stuff:
        distrito = '12'
    elif ' xiii,' in distrito_stuff:
        distrito = '13'
    elif ' xiv,' in distrito_stuff:
        distrito = '14'
    elif ' xv,' in distrito_stuff:
        distrito = '15'
    elif ' xvi,' in distrito_stuff:
        distrito = '16'
    elif ' xvii,' in distrito_stuff:
        distrito = '17'
    elif ' xviii,' in distrito_stuff:
        distrito = '18'
    elif ' xix,' in distrito_stuff:
        distrito = '19'
    elif ' xx,' in distrito_stuff:
        distrito = '20'
    else:
        distrito = ''
    imagen = soup.find("img", attrs={"class": "vc_single_image-img attachment-thumbnail"}).attrs['src']
    contacto =  soup.find("div", attrs={"class": "vc_tta-panel-body"})
    email_stuff = contacto.findAll("span")[0].text.split(' ')
    for stuff in email_stuff:
        if '@congresonayarit.mx' in stuff:
            email = stuff
    telefono = contacto.findAll("span")[1].text.split('(')[1].replace(')','').replace(' ','')
    resultados = [nombre,imagen,'Nayarit',distrito,email,telefono]
    with open(r'nayarit.csv', 'a',encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(resultados)
    try:
        file_object = open('nayarit.csv', 'r',encoding='UTF-8')
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
            file_object = open('nayarit.csv', 'w',encoding='UTF-8')
            for line in data:
                str1 = ','.join(line)
                file_object.write(str1+"\n")
            file_object.close() 
    except Exception as e:
        print (e)