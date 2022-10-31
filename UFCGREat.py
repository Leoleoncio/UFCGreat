import site
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
teste = 'TestLinkOpenSource'

urlMain = 'https://testlink.org'

try:
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)

    navegador.get(urlMain)
    navegador.maximize_window()
    navegador.find_element(
        By.XPATH, '/html/body/div/div[3]/div/a[3]').click()
    site = requests.get(urlMain, headers=headers)
    soupMain = soup = BeautifulSoup(site.content, 'html.parser')
    dados = soupMain.find(
        'div', class_='jumbotron').get_text().strip().replace(' ', '')
    print(dados)
    assert 'TestLinkOpenSource' in dados
    print('deu certo')
except:
    print(f'o site nao ta pegando ')
else:
    print('o site ta pegando')

linkGit = soupMain.find_all('a', href=True)

for sopa in linkGit:
    try:
        assert 'git' in sopa['href']
        siteGit = sopa['href']
    except:
        pass


site = requests.get(siteGit, headers=headers)
soupGit = BeautifulSoup(site.content, 'html.parser')
testGit = soupGit.find('a', class_='url fn').get_text()
try:
    assert teste in testGit
    print('tudo acaba bem quando termina bem')
except:
    print('deu tudo errado')
navegador.find_element(
    By.XPATH, '/html/body/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]').send_keys('Leoleoncio')
navegador.find_element(
    By.XPATH, '//*[@id="jump-to-suggestion-search-global"]/a/div[2]').click()
navegador.find_element(
    By.XPATH, '/html/body/div[4]/main/div/div[2]/nav[1]/a[10]').click()
Leoneee = WebDriverWait(navegador, 20).until(EC.element_to_be_clickable(
    (By.XPATH, f'//*[@id="user_search_results"]/div/div/div[2]/div[1]/div[1]/a[1]')))
navegador.execute_script('arguments[0].click()', Leoneee)
sleep(10)
