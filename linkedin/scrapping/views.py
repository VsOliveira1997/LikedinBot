import numpy as np
from django.shortcuts import render
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from .models import Usuarios, Usuario_endereco
import json
import pandas as pd


# Auxiliares
def driver_linkedin():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    PATH  = "C:\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.linkedin.com/")
    driver.maximize_window()
    return driver

def login_search (palavra_busca, botao_click):
    driver = driver_linkedin()
    sleep(8)
    driver.find_element_by_xpath('//*[@id="session_key"]').send_keys("")
    sleep(8)
    driver.find_element_by_xpath('//*[@id="session_password"]').send_keys("")
    sleep(8)
    driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div[2]/form/button').click()
    sleep(20)
    driver.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input').send_keys(palavra_busca,Keys.ENTER)
    sleep(3)
    if botao_click == 'pessoas':
        botao_pessoas = driver.find_elements_by_class_name('artdeco-pill')
        sleep(5)
        for x in range(0,len(botao_pessoas)):
            button_pessoas = botao_pessoas[0]
        sleep(5)
        button_pessoas.click()
    elif botao_click == 'empresas':
        botao_empresa = driver.find_elements_by_class_name('artdeco-pill')
        sleep(5)
        for x in range(0,len(botao_empresa)):
            button_empresa = botao_empresa[3]
        sleep(5)
        button_empresa.click()
    return driver

def filtro_lateral(driver):
    sleep(5)
    botaos_navbar = driver.find_elements_by_class_name('artdeco-pill--2')
    sleep(5)
    for x in range(0,len(botaos_navbar)):
        botao_todos_filtros = botaos_navbar[4]
    sleep(7)
    botao_todos_filtros.click()
    sleep(5)

def save_info(driver):
    contar_pessoas = 0
    for i in range (1, 11):
        sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        paginas = driver.find_elements_by_class_name('artdeco-pagination__indicator--number')
        nome = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[2]/ul/li/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]')
        endereco = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[2]/ul/li/div/div/div[2]/div[1]/div[2]/div/div[2]')
        for y in range(0,len(nome)):
            usuario_endereco = Usuario_endereco(nome=nome[y].text, endereco=endereco[y].text)
            contar_pessoas += 1
            if contar_pessoas < 31:
                usuario_endereco.save()
            else:
                break
        sleep(5)
        if i == 10:
            return("sucesso")
        else:
            paginas[i].click()





# Executaveis na url

def scrap(request):
    driver = login_search('gerente', 'pessoas')
    sleep(4)
    for i in range (1, 11):
        sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        paginas = driver.find_elements_by_class_name('artdeco-pagination__indicator--number')
        nome = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[2]/ul/li/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]')
        for y in range(0,len(nome)):
            nomes = Usuarios(nome=nome[y].text)
            nomes.save()

        sleep(5)
        if i == 10:
            return("sucesso")
        else:
            paginas[i].click()

def scrap_endereco (request):
    driver = login_search('gerente', 'pessoas')
    sleep(5)
    filtro_lateral(driver)
    sleep(5)
    save_info(driver)
    sleep(5)
    driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[1]/label/p/span[1]').click()
    sleep(5)
    driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[2]/ul/li[7]/fieldset/div/ul/li[2]/label/p/span[1]').click()
    sleep(5)
    driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[3]/div/button[2]').click()
    sleep(5)

def scrap_saude_maranhao(request):
    driver = login_search('gerente', 'pessoas')
    filtro_lateral(driver)
    sleep(3)
    driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[6]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[6]/div/div/input').send_keys('Maranhão')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[6]/div/div/input').send_keys(Keys.ARROW_DOWN)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[6]/div/div/input').send_keys(Keys.ENTER)
    sleep(5)
    driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[2]/ul/li[7]/fieldset/div/ul/li[6]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[2]/ul/li[7]/fieldset/div/ul/li[6]/div/div/input').send_keys('Saúde')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[2]/ul/li[7]/fieldset/div/ul/li[6]/div/div/input').send_keys(Keys.ARROW_DOWN)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[2]/ul/li[7]/fieldset/div/ul/li[6]/div/div/input').send_keys(Keys.ENTER)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[3]/div/button[2]').click()
    sleep(5)
    save_info(driver)

def diretor_empresas(request):
    driver = login_search('', 'empresas')
    filtro_lateral(driver)
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/ul/li[2]/fieldset/div/ul/li[2]/label/p/span[1]').click()
    sleep(5)
    driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[5]/label/p/span[1]').click()
    sleep(5)
    driver.find_element_by_xpath('// *[ @ id = "artdeco-modal-outlet"] / div / div / div[3] / div / button[2]').click()
    sleep(5)
    items = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[2]/ul/li/div/div/div[2]/div/div[1]/div/span/span/a')
    links = []
    botoes_company = []
    for i in range(len(items)):
        links.append(items[i].get_attribute('href'))
    for link in links:
        driver.get(link)
        sleep(7)
        driver.get(link+'people/')
        sleep(7)
        driver.find_element_by_xpath('//*[@id="people-search-keywords"]').send_keys('manager', Keys.ENTER)
        sleep(7)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(7)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(7)
        nome = driver.find_elements_by_xpath('//*[@id="main"]/div[2]/div/div[2]/div/ul/li/section/div/div/div[2]/div[1]')
        cargo = driver.find_elements_by_xpath('//*[@id="main"]/div[2]/div/div[2]/div/ul/li/section/div/div/div[2]/div[3]')
        data = {
        }
        for w in range(len(nome)):
            data['nome'] = nome[w].text
            data['cargo'] = cargo[w].text
            with open('dados.json', 'a') as f:
                json.dump(data, f, indent=2)
            if data['nome'] != None:
                df = pd.DataFrame([data])
                df.to_csv('dados_final.csv', mode='a', index=False)