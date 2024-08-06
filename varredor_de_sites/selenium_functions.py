from driver_function import iniciar_driver
from selenium.webdriver.support import expected_conditions as condicoes_esperadas
from selenium.webdriver.common.by import By

driver, wait = iniciar_driver()

def logar_shopee(driver, wait):

    # Navegar até o site https://shopee.com.br/buyer/login
    driver.get("https://shopee.com.br/buyer/login")
    # Localizar o campo usuario
    campo_usuario = wait.until(condicoes_esperadas.element_to_be_clickable((By.NAME, "loginKey")))
    print(f"Campo usuario localizado")
    # Inserir usuario
    # Localicar o campo senha
    # Inserir senha
    # Localizer botão "Entrar"
    # Clicar botão "Entrar"
