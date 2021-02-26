from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import math

percoQuantasVezes = #Quantas Vezes você quer poder perder ?

def getNumMoedas():
    coins = driver.find_element_by_class_name("user-saldo")
    coins = coins.text
    coins = coins.replace(".", "")
    sleep(2)
    return coins

def calcNumBase(coins):
    coins = int(coins)
    valorBaseAux = math.log(coins,2)
    valorBase = valorBaseAux - (percoQuantasVezes + 1)
    valorBase = math.pow(2,valorBase)
    valorBase = int(valorBase)
    return valorBase


def logarTwitch():
    link = driver.find_element_by_css_selector('a.twitch')
    link.click()
    sleep(5)

def ApostaRoleta(valorBase):
    autoBet = driver.find_element_by_xpath("/html/body/app-root/div/app-roulette/div[2]/div[5]/div/div/div/div/button")
    autoBet.click()
    sleep(2)
    campo1 = driver.find_element_by_xpath("/html/body/app-root/div/app-roulette/div[2]/div[5]/div/div/div/div[2]/label[1]/input").clear()
    campo1 = driver.find_element_by_xpath("/html/body/app-root/div/app-roulette/div[2]/div[5]/div/div/div/div[2]/label[1]/input")
    campo1.send_keys(valorBase)

    campo2 = driver.find_element_by_xpath("/html/body/app-root/div/app-roulette/div[2]/div[5]/div/div/div/div[2]/select/option[7]")
    campo2.click()

    campo3 = driver.find_element_by_xpath('/html/body/app-root/div/app-roulette/div[2]/div[5]/div/div/div/div[2]/div[1]/select/option[1]')
    campo3.click()

    campo4 = driver.find_element_by_xpath('/html/body/app-root/div/app-roulette/div[2]/div[5]/div/div/div/div[2]/div[2]/label/input').clear()
    campo4 = driver.find_element_by_xpath('/html/body/app-root/div/app-roulette/div[2]/div[5]/div/div/div/div[2]/div[2]/label/input')
    campo4.send_keys(4)

    campo5 = driver.find_element_by_xpath('/html/body/app-root/div/app-roulette/div[2]/div[5]/div/div/div/div[2]/div[3]/input').clear()
    campo5 = driver.find_element_by_xpath('/html/body/app-root/div/app-roulette/div[2]/div[5]/div/div/div/div[2]/div[3]/input')
    campo5.send_keys(percoQuantasVezes)

    ligar = driver.find_element_by_xpath('/html/body/app-root/div/app-roulette/div[2]/div[5]/div/div/div/div[2]/button')
    ligar.click()




options = webdriver.ChromeOptions() 

options.add_argument("user-data-dir=C:\\Users\\YOUR-COMPUTER-NAME\\AppData\\Local\\Google\\Chrome\\AutoBot") #Diretório até o seu Chrome
options.add_argument('--profile-directory=Profile 1')
options.add_argument("start-maximized")



driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver.exe", chrome_options=options)

#acessar site
driver.get("https://johnpittertv.com/")
sleep(5)

#logar
logarTwitch()

#numero de moedas
coins = getNumMoedas()

valorBase = calcNumBase(coins)
driver.get("https://johnpittertv.com/roleta")
sleep(2)
ApostaRoleta(valorBase)



