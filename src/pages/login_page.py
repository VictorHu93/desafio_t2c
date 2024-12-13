from src.locators.login_locators import LoginLocators
from src.pages.base_page import BasePage
from src.config.environment.login import USER, PASSWORD, PRE_USER, PRE_PASSWORD
from src.utils.logger import Logger


class LoginPage(BasePage):
    # Configuração do logger para a classe
    logger = Logger.get_logger(name="LoginPage", log_file="logs/login_page.log")
    
    def handle_cookies(self):
        self.click(LoginLocators.PRE_BUTTON_COKIES)
        self.logger.debug("Aceitou os cookies.")

    def pre_login(self):
        """
        Executa o pré-login utilizando as credenciais de pré-autenticação.
        """
        self.logger.info("Iniciando o pré-login...")
        try:
            self.click(LoginLocators.PRE_BUTTON_CLICK)
            self.logger.debug("Clicou no botão 'Community login'.")
            self.send_keys(PRE_USER, LoginLocators.PRE_USERNAME_FIELD)
            self.logger.debug("Inseriu o pré-usuário.")
            self.click(LoginLocators.PRE_BUTTON_NEXT_CLICK)
            self.logger.debug("Clicou no botão 'Next'.")
            self.send_keys(PRE_PASSWORD, LoginLocators.PRE_PASSWORD_FIELD)
            self.logger.debug("Inseriu a pré-senha.")
            self.click(LoginLocators.PRE_LOGIN_BUTTON)
            self.logger.info("Pré-login concluído com sucesso.")
        except Exception as e:
            self.logger.error(f"Erro durante o pré-login: {e}")
            raise

    def login(self):
        """
        Realiza o login principal utilizando as credenciais do usuário.
        """
        self.logger.info("Iniciando o login principal...")
        try:
            self.send_keys(USER, LoginLocators.USERNAME_FIELD)
            self.logger.debug("Inseriu o usuário.")
            self.send_keys(PASSWORD, LoginLocators.PASSWORD_FIELD)
            self.logger.debug("Inseriu a senha.")
            self.click(LoginLocators.LOGIN_BUTTON)
            self.logger.info("Login principal concluído com sucesso.")
        except Exception as e:
            self.logger.error(f"Erro durante o login principal: {e}")
            raise
