import time
import schedule
import pywhatkit as kit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def enviar_arquivo():
    # Configurar o Selenium e abrir o WhatsApp Web
    driver = webdriver.Chrome(executable_path='/Users/bortotti/Downloads/Projeto-python/chromedriver_mac_arm64')  # Especifique o caminho para o chromedriver
    driver.get('https://web.whatsapp.com/')
    
    # Tempo para escanear o QR Code
    time.sleep(15)  # Ajuste conforme necessário

    # Procura o contato/grupo pelo nome
    contato = 'LEMBRETES'
    search_box = driver.find_element('xpath', '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(contato)
    search_box.send_keys(Keys.RETURN)

    # Anexa e envia o arquivo
    attachment_box = driver.find_element('xpath', '//div[@title="Anexar"]')
    attachment_box.click()
    
    time.sleep(1)  # Pequeno atraso para abrir a janela de seleção de arquivo
    
    file_input = driver.find_element('xpath', '//input[@accept="*"]')
    file_input.send_keys('/Users/bortotti/Downloads/Projeto-python/chromedriver_mac_arm64/LICENSE.chromedriver')  # Especifique o caminho para o seu arquivo

    time.sleep(1)  # Pequeno atraso para a seleção do arquivo
    
    send_button = driver.find_element('xpath', '//span[@data-icon="send"]')
    send_button.click()

    # Feche o navegador após 