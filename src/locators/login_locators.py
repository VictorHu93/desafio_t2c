from selenium.webdriver.common.by import By

class LoginLocators:
    
    PRE_BUTTON_COKIES = (By.ID, 'onetrust-accept-btn-handler')
    PRE_BUTTON_CLICK = (By.XPATH, "//button[text()='Community login']")
    PRE_USERNAME_FIELD = (By.ID, '43:2;a')
    PRE_BUTTON_NEXT_CLICK = (By.XPATH, "//button[text()='Next']")
    PRE_PASSWORD_FIELD = (By.CLASS_NAME, 'textbox.input.sfdc_passwordinput.sfdc.input')
    PRE_LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")
    
    USERNEAME_FIELD = (By.ID, 'salesOrderInputEmail')
    PASSWORD_FIELD = (By.ID, 'salesOrderInputPassword')
    LOGIN_BUTTON = (By.CLASS_NAME, 'btn-user')