from django.shortcuts import render
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from .models import Usuarios, Usuario_endereco


# Create your views here.
def driver_linkedin():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    PATH  = "C:\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.linkedin.com/")
    driver.maximize_window()
    return driver


def login_search ():
    driver = driver_linkedin()
    sleep(4)
    username = driver.find_element_by_xpath('//*[@id="session_key"]').send_keys("vso1997@gmail.com")
    sleep(4)
    password = driver.find_element_by_xpath('//*[@id="session_password"]').send_keys("Torvi321")
    btn = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div[2]/form/button').click()
    sleep(20)
    pesquisa = driver.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input').send_keys('gerente',Keys.ENTER)
    sleep(3)
    botao_pessoas = driver.find_elements_by_class_name('artdeco-pill')
    sleep(5)
    for x in range(0,len(botao_pessoas)):
        button_pessoas = botao_pessoas[0]
    sleep(5)
    button_pessoas.click()
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


def scrap(request):
    driver = login_search()
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
    driver = login_search()
    sleep(5)
    filtro_lateral(driver)
    sleep(5)
    save_info(driver)
    sleep(5)
    seleciona_pais = driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[1]/label/p/span[1]').click()
    sleep(5)
    seleciona_profissao = driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[2]/ul/li[7]/fieldset/div/ul/li[2]/label/p/span[1]').click()
    sleep(5)
    exibir_resultado = driver.find_element_by_xpath('//*[@id="artdeco-modal-outlet"]/div/div/div[3]/div/button[2]').click()
    sleep(5)


def scrap_saude_maranhao(request):
    driver = login_search()
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


