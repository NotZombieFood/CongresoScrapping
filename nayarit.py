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
    print (url)
    distrito_h3 = soup.findAll("h3")
    for distrito_stuff in distrito_h3:
        if 'proporcional' in distrito_stuff.text.lower():
            distrito = 'RP'
            break
        elif ' i,' in distrito_stuff.text.lower():
            distrito = '1'
            break
        elif ' ii,' in distrito_stuff.text.lower():
            distrito = '2'
            break
        elif ' iii,' in distrito_stuff.text.lower():
            distrito = '3'
            break
        elif ' iv,' in distrito_stuff.text.lower():
            distrito = '4'
            break
        elif ' v,' in distrito_stuff.text.lower():
            distrito = '5'
            break
        elif ' vi,' in distrito_stuff.text.lower():
            distrito = '6'
            break
        elif ' vii,' in distrito_stuff.text.lower():
            distrito = '7'
            break
        elif ' viii,' in distrito_stuff.text.lower():
            distrito = '8'
            break
        elif ' ix,' in distrito_stuff.text.lower():
            distrito = '9'
            break
        elif ' x,' in distrito_stuff.text.lower():
            distrito = '10'
            break
        elif ' xi,' in distrito_stuff.text.lower():
            distrito = '11'
            break
        elif ' xii,' in distrito_stuff.text.lower():
            distrito = '12'
            break
        elif ' xiii,' in distrito_stuff.text.lower():
            distrito = '13'
            break
        elif ' xiv,' in distrito_stuff.text.lower():
            distrito = '14'
            break
        elif ' xv,' in distrito_stuff.text.lower():
            distrito = '15'
            break
        elif ' xvi,' in distrito_stuff.text.lower():
            distrito = '16'
            break
        elif ' xvii,' in distrito_stuff.text.lower():
            distrito = '17'
            break
        elif ' xviii,' in distrito_stuff.text.lower():
            distrito = '18'
            break
        elif ' xix,' in distrito_stuff.text.lower():
            distrito = '19'
            break
        elif ' xx,' in distrito_stuff.text.lower():
            distrito = '20'
            break
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