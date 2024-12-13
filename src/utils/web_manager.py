from selenium import webdriver
from src.utils.logger import Logger


class WebManager:
    """
    Gerencia as instâncias do WebDriver.
    """

    _driver = None  # Singleton padrão

    def __init__(self):
        self.logger = Logger.get_logger(
            name="WebManager", log_file="logs/web_manager.log"
        )
        self.options = webdriver.ChromeOptions()

    def get_webdriver(self):
        """
        Retorna a instância única do WebDriver (singleton).
        """
        if WebManager._driver is None:
            self.logger.info("Inicializando o WebDriver singleton...")
            WebManager._driver = webdriver.Chrome(options=self.options)
        else:
            self.logger.info("Reutilizando o WebDriver singleton existente.")
        return WebManager._driver

    def get_new_webdriver(self):
        """
        Cria e retorna uma nova instância do WebDriver.
        """
        self.logger.info("Inicializando uma nova instância do WebDriver...")
        return webdriver.Chrome(options=self.options)

    @staticmethod
    def quit_webdriver(driver=None):
        """
        Fecha o WebDriver e redefine a instância (opcional).
        """
        logger = Logger.get_logger(name="WebManager", log_file="logs/web_manager.log")
        if driver:  # Fecha uma instância específica
            logger.info(f"Fechando a instância do WebDriver: {driver}")
            driver.quit()
        elif WebManager._driver:  # Fecha o singleton
            logger.info("Fechando o WebDriver singleton...")
            WebManager._driver.quit()
            WebManager._driver = None
