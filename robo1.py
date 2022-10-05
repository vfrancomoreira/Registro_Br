""" 
import pdb; pdb.set_trace()  # Pausa o programa em meio código para interagir com CMD
Atráves do CMD busque por resultados e o [índice] das palavras em negrito exibidas no terminal.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Controla as teclas
import time  # Espera de execução
import xlrd

print("Iniciando nosso robô...\n")

# Criando um arquivo 'txt'
arq = open('resultado.txt', 'w')

driver = webdriver.Edge('D:\edgedriver_win64\msedgedriver.exe')  # Abrir o navegador
driver.get("https://registro.br/")  # Entrar no site

dominios = ['roboscompython.com.br', 'udemy.com', 'uol.com.br', 'pythoncurso.com']

for dominio in dominios:
    pesquisa = driver.find_element_by_id('is-avail-field') # Entra na barra de pesquisa atráves do 'id' da página.
    pesquisa.clear()  # Limpando a barra de pesquisa
    pesquisa.send_keys(dominio)  # Mandando dados para a barra
    pesquisa.send_keys(Keys.RETURN)  # Aperta enter 
    time.sleep(2)
    resultados = driver.find_elements_by_tag_name('strong')  # Percorre todos strong
    texto = f"Status domínio {dominio}: {resultados[4].text}.\n"
    arq.write(texto)

arq.close() # Fecha arquivo 'txt'
driver.close() # Fecha navegador
