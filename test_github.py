import pytest
from automacao import iniciar_navegador, scroll_ate_final, clicar_sign_up

@pytest.fixture
def setup_teardown():
    """Prepara o navegador para os testes."""
    driver = iniciar_navegador()
    yield driver
    driver.quit()

def test_scroll_pagina(setup_teardown):
    """Testa se o scroll até o final da página funciona."""
    driver = setup_teardown
    footer = scroll_ate_final(driver)
    assert footer.is_displayed(), "Scroll não chegou ao final da página!"

def test_abrir_tela_login(setup_teardown):
    """Testa se a tela de login é aberta corretamente."""
    driver = setup_teardown
    campo_login = clicar_sign_up(driver)
    assert campo_login.is_displayed(), "Tela de login não foi aberta!"