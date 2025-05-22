import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup_teardown():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def recupera_texto(elemento):
    return elemento.get_attribute('value') or elemento.text

def test_login_github(setup_teardown):
    driver = setup_teardown
    driver.get("https://github.com/login")

    campo_login = driver.find_element(By.ID, "login_field")
    campo_login.send_keys("Janio-Almeida")

    campo_senha = driver.find_element(By.ID, "password")
    campo_senha.send_keys("senha_correta") 
    btn_login = driver.find_element(By.NAME, "commit")
    texto_botao = recupera_texto(btn_login)
    print("Texto do botão:", texto_botao)

    assert "Sign in" in texto_botao

    btn_login.click()

    assert "login" not in driver.current_url.lower()

def test_login_invalido(setup_teardown):
    driver = setup_teardown
    driver.get("https://github.com/login")

    campo_login = driver.find_element(By.ID, "login_field")
    campo_login.send_keys("Janio-Almeida")

    campo_senha = driver.find_element(By.ID, "password")
    campo_senha.send_keys("senha_errada")

    btn_login = driver.find_element(By.NAME, "commit")
    texto_botao = recupera_texto(btn_login)
    print("Texto do botão:", texto_botao)

    assert "Sign in" in texto_botao

    btn_login.click()

    erro = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "flash-error"))
    )
    print("Texto encontrado:", erro.text)
    assert "Nome de usuário ou senha incorretos." in erro.text 
