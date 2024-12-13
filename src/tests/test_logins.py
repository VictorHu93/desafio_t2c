import pytest
from unittest.mock import patch, MagicMock
from src.pages.login_page import LoginPage
from src.locators.login_locators import LoginLocators


@pytest.fixture
def mock_base_page_find_element():
    """
    Fixture que substitui o método find_element da BasePage com um mock.
    """
    with patch("src.pages.base_page.BasePage.find_element") as mock:
        yield mock


@pytest.fixture
def mock_element():
    """
    Fixture para simular um elemento retornado pelo find_element.
    """
    return MagicMock()


def test_pre_login_success(mock_base_page_find_element, mock_element):
    """
    Testa o pré-login com sucesso.
    """
    # Configuração do mock
    mock_element = MagicMock()
    mock_base_page_find_element.return_value = mock_element

    # Ação
    login_page = LoginPage()
    login_page.pre_login()

    # Verificação
    assert mock_base_page_find_element.call_args_list == [
        ((LoginLocators.PRE_BUTTON_CLICK,),),
        ((LoginLocators.PRE_USERNAME_FIELD,),),
        ((LoginLocators.PRE_BUTTON_NEXT_CLICK,),),
        ((LoginLocators.PRE_PASSWORD_FIELD,),),
        ((LoginLocators.PRE_LOGIN_BUTTON,),),
    ], "Os locators do pré-login não foram usados corretamente."

    assert mock_element.click.call_count == 3, "Os cliques esperados não ocorreram."
    assert mock_element.send_keys.call_count == 2, "Os envios de texto esperados não ocorreram."



def test_login_success(mock_base_page_find_element, mock_element):
    """
    Testa o login com sucesso.
    """
    # Configuração do mock
    mock_base_page_find_element.return_value = mock_element

    # Ação
    login_page = LoginPage()
    login_page.login()

    # Verificação
    assert mock_base_page_find_element.call_args_list == [
        ((LoginLocators.USERNAME_FIELD,),),
        ((LoginLocators.PASSWORD_FIELD,),),
        ((LoginLocators.LOGIN_BUTTON,),),
    ], "Os locators do login não foram usados corretamente."
    assert mock_element.send_keys.call_count == 2, "Os envios de chaves esperados não ocorreram."
    assert mock_element.click.call_count == 1, "O clique esperado não ocorreu."


def test_login_failure_invalid_user(mock_base_page_find_element, mock_element):
    """
    Testa o caso de falha de login devido a usuário inválido.
    """
    # Configuração do mock para simular mensagem de erro
    mock_element.text = "Invalid username or password"
    mock_base_page_find_element.return_value = mock_element

    # Ação
    login_page = LoginPage()
    login_page.login()

    # Verificação
    assert mock_base_page_find_element.call_args_list == [
        ((LoginLocators.USERNAME_FIELD,),),
        ((LoginLocators.PASSWORD_FIELD,),),
        ((LoginLocators.LOGIN_BUTTON,),),
    ], "Os locators do login não foram usados corretamente."
    assert mock_element.text == "Invalid username or password", "A mensagem de erro não corresponde ao esperado."


