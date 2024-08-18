import time
import schedule
import pickle
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar o navegador fora da função para mantê-lo aberto
service = Service('/Users/bortotti/Downloads/Projeto-python/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service)

# Verifica se os cookies de sessão já foram salvos
if os.path.exists("whatsapp_session.pkl"):
    # Carregar os cookies salvos
    driver.get('https://web.whatsapp.com/')
    time.sleep(10)
    with open("whatsapp_session.pkl", "rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
    driver.refresh()
else:
    # Primeira vez: fazer login e salvar os cookies
    driver.get('https://web.whatsapp.com/')
    time.sleep(30)  # Tempo para escanear o QR Code manualmente
    # Salvar os cookies de sessão
    with open("whatsapp_session.pkl", "wb") as f:
        pickle.dump(driver.get_cookies(), f)

def enviar_texto(contato, mensagem):
    # Procura o contato/grupo pelo nome
    search_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )
    search_box.click()
    search_box.send_keys(contato)
    search_box.send_keys(Keys.RETURN)

    # Espera o campo de mensagem de texto estar disponível e envia a mensagem
    message_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @data-tab="10"]'))
    )
    message_box.click()
    message_box.send_keys(mensagem)
    message_box.send_keys(Keys.RETURN)

def enviar_arquivo(contato, caminho_arquivo):
    # Procura o contato/grupo pelo nome
    search_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )
    search_box.click()
    search_box.send_keys(contato)
    search_box.send_keys(Keys.RETURN)

    # Anexa e envia o arquivo
    attachment_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@title="Anexar"]'))
    )
    attachment_box.click()
    
    time.sleep(1)  # Pequeno atraso para abrir a janela de seleção de arquivo
    
    file_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//input[@accept="*"]'))
    )
    file_input.send_keys(caminho_arquivo)  # Especifique o caminho para o seu arquivo

    time.sleep(1)  # Pequeno atraso para a seleção do arquivo
    
    send_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]'))
    )
    send_button.click()

def enviar_mensagem(tipo, contato, conteudo):
    if tipo == "texto":
        enviar_texto(contato, conteudo)
    elif tipo == "arquivo":
        enviar_arquivo(contato, conteudo)
    else:
        print("Tipo de envio inválido. Use 'texto' ou 'arquivo'.")

# Exemplo de agendamento para enviar um texto ou arquivo
schedule.every(1).seconds.do(enviar_mensagem, tipo="texto", contato="MARI", conteudo="Te Amo.")
# schedule.every(5).seconds.do(enviar_mensagem, tipo="arquivo", contato="MARI", conteudo="/Users/bortotti/Downloads/Modelo_Envio.xlsm")

# Mantém o script em execução para executar o agendamento
while True:
    schedule.run_pending()
    time.sleep(1)