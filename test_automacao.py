from selenium import webdriver  # controlar navegador
from selenium.webdriver.chrome.service import Service # iniciar Chrome com driver
from selenium.webdriver.common.keys import Keys #importar keys
from selenium.webdriver.common.by import By  # localizar elementos (ID, CSS, etc.)
from selenium.webdriver.support.ui import Select # lidar com <select>
from selenium.webdriver.common.alert import Alert # lidar com alertas
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait # espera explícita
from webdriver_manager.chrome import ChromeDriverManager
import pytest # biblioteca de testes
import time # biblioteca de testes

@pytest.fixture
def setup_teardown_home(): 
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://github.com/")
    driver.implicitly_wait(10)
    time.sleep(2)

    yield driver
    driver.quit()

@pytest.fixture
def setup_teardown_login():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://github.com/login")
    
    WebDriverWait(driver, 30).until(
        lambda driver: driver.current_url == "https://github.com/") #Timeout Implicito, espera até eu logar manualmente e ser redirecionado para home
    
    yield driver
    driver.quit()



def test_keyboard_navigation(setup_teardown_home): #setup que começa na pag inicial
    driver = setup_teardown_home
    body = driver.find_element(By.TAG_NAME, "body")

    body.send_keys(Keys.TAB) #simulação de um clique no tab usando o send keys no BODY, e passando como parâmetro KEYS com a tecla TAB
    time.sleep(1)

    active_element = driver.execute_script("return document.activeElement") #método para executar js e usar propriedade DOM, para pegar o elemento que está em foco na página
    active_element_value = active_element.get_attribute("value")

    assert active_element_value != "body"



def test_invalid_user_to_repository(setup_teardown_login): #setup que começa na pag de login
    driver = setup_teardown_login
    driver.get("https://github.com/CodeByBia/teste-github/settings/access") #direciona para acesso no repositório

    btn_add = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#dialog-show-add-access-dialog-user')) #espera até que a opção de adicionar apareça
    )
    btn_add.click()

    input_user = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.js-repo-add-access-search-input')) #espera até que o input para adicionar user apareça e o armazena
    )
    input_user.send_keys("userinvalido123") #escrevemos o user INVÁLIDO no input

    btn_confirm_add = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit'].Button--primary")) #espera até que o botão de adicionar apareça e o armazena
    )

    time.sleep(3) 
    assert btn_confirm_add.is_enabled() == False #conferimos se o botão de adicionar está desabilitado


