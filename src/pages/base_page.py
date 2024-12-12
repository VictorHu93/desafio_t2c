from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from src.utils.web_manager import WebManager

class BasePage:
    def __init__(self):
        self.__driver = WebManager().get_webdriver()

    def find_element(self, locator, timeout: float = 10):
        return WebDriverWait(self.__driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def find_elements(self, locator, timeout: float = 10):
        return WebDriverWait(self.__driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def send_keys(self, value: str, locator):
        self.find_element(locator).send_keys(value)

    def click(self, locator):
        self.find_element(locator).click()

    def select_by_value(self, value: str, locator):
        Select(self.find_element(locator)).select_by_value(str(value))

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_html(self, locator):
        return self.find_element(locator).get_attribute("innerHTML")

    def open(self, url: str):
        self.__driver.get(url)
