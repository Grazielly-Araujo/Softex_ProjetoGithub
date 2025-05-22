from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def iniciar_navegador():
    """Configura e inicia o navegador."""
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://github.com")
    return driver

def scroll_ate_final(driver):
    """Rola a página até o final."""
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    return driver.find_element(By.CSS_SELECTOR, "footer[class='footer']")

def clicar_sign_up(driver):
    driver.find_element(By.CSS_SELECTOR, "BUTTON").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login_field"))
    )
    return driver.find_element(By.ID, "login_field")