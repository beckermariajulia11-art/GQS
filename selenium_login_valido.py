"""CT-001: autenticação com credenciais válidas."""

# Os fluxos de CT-001 e CT-002 são intencionalmente paralelos.
# pylint: disable=duplicate-code

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()  # pylint: disable=not-callable
try:
    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)
    usuario = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    usuario.send_keys("tomsmith")
    senha = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    senha.send_keys("SuperSecretPassword!")
    botao = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=submit]"))
    )
    botao.click()

    mensagem = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text
    url_observada = driver.current_url

    assert "You logged into a secure area!" in mensagem
    assert url_observada.endswith("/secure")

    print("URL observada:", url_observada)
    print("Texto observado:", mensagem)
    print("CT-001 APROVADO:", mensagem)
finally:
    driver.quit()
