from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--headless")
options.add_argument("window-size=1400,600")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Utility\BrowserDrivers\chromedriver.exe')
driver.implicitly_wait(5)
urls = []
sitio = 'https://google.com'
driver.get(sitio)
print ("Headless Chrome Initialized")
diputados = driver.find_elements_by_class_name('vc_btn3-color-juicy-pink')
for diputado in diputados:
    urls.append(diputado.get_attribute('href'))

driver.close()

