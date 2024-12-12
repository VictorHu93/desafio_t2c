from src.locators.login_locators import LoginLocators
from src.pages.base_page import BasePage
from src.config.environment.login import USER, PASSWORD, PRE_USER, PRE_PASSWORD

class LoginPage(BasePage):
    
    def pre_login(self):
        self.click(LoginLocators.PRE_BUTTON_COKIES)
        self.click(LoginLocators.PRE_BUTTON_CLICK)
        self.send_keys(PRE_USER, LoginLocators.PRE_USERNAME_FIELD)
        self.click(LoginLocators.PRE_BUTTON_NEXT_CLICK)
        self.send_keys(PRE_PASSWORD, LoginLocators.PRE_PASSWORD_FIELD)
        self.click(LoginLocators.PRE_LOGIN_BUTTON)
        
    def login(self):
        self.send_keys(USER, LoginLocators.USERNEAME_FIELD)
        self.send_keys(PASSWORD, LoginLocators.PASSWORD_FIELD)
        self.click(LoginLocators.LOGIN_BUTTON)
        