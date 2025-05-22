from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def recupera_texto(elemento):
    return elemento.get_attribute('value')


driver.get("https://github.com/login")

campo_login = driver.find_element(By.ID, "login_field")
campo_login.send_keys("Janio-Almeida")

campo_senha = driver.find_element(By.ID, "password")
campo_senha.send_keys("senha_correta")

btn_login = driver.find_element(By.NAME, "commit")


print(recupera_texto(btn_login))

btn_login.click()

time.sleep(5)

driver.quit()