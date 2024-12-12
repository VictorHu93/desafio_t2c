from selenium import webdriver

class WebManager:
    _driver = None  # Atributo de classe para garantir uma única instância

    def __init__(self):
        self.options = webdriver.ChromeOptions()

    def get_webdriver(self):
        """
        Retorna a instância única do WebDriver.
        """
        if WebManager._driver is None:
            WebManager._driver = webdriver.Chrome(options=self.options)
        return WebManager._driver

    @staticmethod
    def quit_webdriver():
        """
        Fecha o WebDriver e redefine a instância.
        """
        if WebManager._driver:
            WebManager._driver.quit()
            WebManager._driver = None
