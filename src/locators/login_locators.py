from selenium.webdriver.common.by import By


class LoginLocators:
    """
    Localizadores para os elementos relacionados ao login, incluindo pré-login.
    """

    # Localizadores para o pré-login
    PRE_BUTTON_COKIES = (
        By.ID,
        "onetrust-accept-btn-handler",
    )  # Botão para aceitar cookies
    PRE_BUTTON_CLICK = (
        By.XPATH,
        "//button[text()='Community login']",
    )  # Botão de login da comunidade
    PRE_USERNAME_FIELD = (
        By.ID,
        "43:2;a",
    )  # Campo para inserir o nome de usuário no pré-login
    PRE_BUTTON_NEXT_CLICK = (
        By.XPATH,
        "//button[text()='Next']",
    )  # Botão "Next" do pré-login
    PRE_PASSWORD_FIELD = (
        By.CLASS_NAME,
        "textbox.input.sfdc_passwordinput.sfdc.input",
    )  # Campo para inserir a senha no pré-login
    PRE_LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Log in']",
    )  # Botão "Log in" do pré-login

    # Localizadores para o login principal
    USERNAME_FIELD = (
        By.ID,
        "salesOrderInputEmail",
    )  # Campo para inserir o e-mail de login
    PASSWORD_FIELD = (
        By.ID,
        "salesOrderInputPassword",
    )  # Campo para inserir a senha de login
    LOGIN_BUTTON = (By.CLASS_NAME, "btn-user")  # Botão para realizar o login
