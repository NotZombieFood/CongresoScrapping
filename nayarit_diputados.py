from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

urls = ['http://www.congresonayarit.mx/dip-ana-yusara-ramirez-salazar/', 'http://www.congresonayarit.mx/dip-heriberto-castaneda-ulloa/', 'http://www.congresonayarit.mx/dip-javier-hiram-mercado-zamora/', 'http://www.congresonayarit.mx/dip-jose-antonio-barajas-lopez/', 'http://www.congresonayarit.mx/dip-juan-carlos-covarrubias-garcia/', 'http://www.congresonayarit.mx/dip-leopoldo-dominguez-gonzalez/', 'http://www.congresonayarit.mx/dip-librado-casas-ledesma/', 'http://www.congresonayarit.mx/dip-rodolfo-pedroza-ramirez/', 'http://www.congresonayarit.mx/dip-rosa-mirna-mora-romano/', 'http://www.congresonayarit.mx/dip-adahan-casas-rivas/', 'http://www.congresonayarit.mx/dip-avelino-aguirre-marcelo/', 'http://www.congresonayarit.mx/dip-j-carlos-rios-lara/', 'http://www.congresonayarit.mx/dip-jesus-armando-velez-macias/', 'http://www.congresonayarit.mx/dip-karla-gabriela-flores-parra/', 'http://www.congresonayarit.mx/dip-lucio-santana-zuniga/', 'http://www.congresonayarit.mx/dip-mariafernanda-belloso-cayeros/', 'http://www.congresonayarit.mx/dip-nelida-ivonne-sabrina-diaz-tejeda/', 'http://www.congresonayarit.mx/dip-adan-zamora-romero/', 'http://www.congresonayarit.mx/dip-eduardo-lugo-lopez/', 'http://www.congresonayarit.mx/dip-erika-leticia-jimenez-aldaco/', 'http://www.congresonayarit.mx/dip-ismael-dunalds-ventura/', 'http://www.congresonayarit.mx/dip-ma-de-la-luz-verdin-manjarrez/', 'http://www.congresonayarit.mx/dip-margarita-moran-flores/', 'http://www.congresonayarit.mx/dip-jorge-armando-ortiz-rodriguez/', 'http://www.congresonayarit.mx/dip-marisol-sanchez-navarro/', 'http://www.congresonayarit.mx/dip-pedro-roberto-perez-gomez/', 'http://www.congresonayarit.mx/dip-claudia-cruz-dionisio/', 'http://www.congresonayarit.mx/dip-manuel-ramon-salcedo-osuna/', 'http://www.congresonayarit.mx/dip-julieta-mejia-ibanez/', 'http://www.congresonayarit.mx/dip-manuel-navarro-garcia/']

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