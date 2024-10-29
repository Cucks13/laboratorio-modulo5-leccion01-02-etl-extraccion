from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium import webdriver # type: ignore
from time import sleep

def magic(parametros, url):
    for i in parametros:
        carga_datos_ine(i, url)


def carga_datos_ine(p, url):

    child = str(p[1])
    
    chrome_options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": "C:\\Users\\almaz\\Hackio\\laboratoriohackio\\laboratorio-modulo5-leccion01-etl-extraccion\\data\\ine", 
        "download.prompt_for_download": False, 
        "directory_upgrade": True, 
        "safebrowsing.enabled": True
    }

    chrome_options.add_experimental_option("prefs", prefs)

    

    driver = webdriver.Chrome(chrome_options)
    driver.get(url)
    sleep(5)
    driver.find_element('css selector','#aceptarCookie').click()
    driver.implicitly_wait(10)
    driver.find_element("css selector", f'#periodo > option:nth-child({child})').click()
    driver.implicitly_wait(10)
    driver.find_element("css selector", '#botonConsulSele').click()
    driver.implicitly_wait(10)
    driver.find_element('xpath','/html/body/div[1]/main/ul/li/div/div/form[2]/button').click()
    driver.implicitly_wait(10)
    sleep(5)
    try:
        driver.find_element('xpath','//*[@id="export"]/ul/li[4]/label').click()
    except:
        print("Error al clickear en la descarga del csv, probamos otra vez, hasta que no este en popup")
        carga_datos_ine(p, url)

    sleep(5)
    driver.close()

