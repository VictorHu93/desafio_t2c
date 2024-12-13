from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from src.utils.web_manager import WebManager
from src.utils.logger import Logger


class BasePage:
    def __init__(self, driver=None, name="BasePage"):
        """
        Inicializa a BasePage com o WebDriver fornecido ou reutiliza o singleton.
        """
        self.driver = driver if driver else WebManager().get_webdriver()
        self.logger = Logger.get_logger(name, log_file=f"logs/{name.lower()}.log")

    def find_element(self, locator, timeout=10):
        """
        Encontra um elemento no DOM, aguardando até que esteja visível.

        :param locator: Localizador do elemento (By, value).
        :param timeout: Tempo máximo de espera.
        :return: WebElement encontrado.
        """
        self.logger.debug(f"Buscando elemento: {locator}")
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            self.logger.debug(f"Elemento encontrado: {locator}")
            return element
        except Exception as e:
            self.logger.error(f"Erro ao encontrar elemento {locator}: {e}")
            raise

    def find_elements(self, locator, timeout=10):
        """
        Encontra múltiplos elementos no DOM, aguardando até que estejam presentes.

        :param locator: Localizador dos elementos (By, value).
        :param timeout: Tempo máximo de espera.
        :return: Lista de WebElements encontrados.
        """
        self.logger.debug(f"Buscando múltiplos elementos: {locator}")
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            self.logger.debug(f"Elementos encontrados: {locator}")
            return elements
        except Exception as e:
            self.logger.error(f"Erro ao encontrar múltiplos elementos {locator}: {e}")
            raise

    def send_keys(self, value, locator):
        """
        Envia texto para um elemento localizado.

        :param value: Texto a ser enviado.
        :param locator: Localizador do elemento.
        """
        self.logger.debug(f"Enviando texto '{value}' para o elemento: {locator}")
        try:
            element = self.find_element(locator)
            element.send_keys(value)
            self.logger.info(f"Texto enviado com sucesso para {locator}")
        except Exception as e:
            self.logger.error(f"Erro ao enviar texto para {locator}: {e}")
            raise

    def click(self, locator):
        """
        Clica em um elemento localizado.

        :param locator: Localizador do elemento.
        """
        self.logger.debug(f"Clicando no elemento: {locator}")
        try:
            element = self.find_element(locator)
            element.click()
            self.logger.info(f"Elemento clicado com sucesso: {locator}")
        except Exception as e:
            self.logger.error(f"Erro ao clicar no elemento {locator}: {e}")
            raise

    def select_by_value(self, value, locator):
        """
        Seleciona um valor em um dropdown.

        :param value: Valor a ser selecionado.
        :param locator: Localizador do dropdown.
        """
        self.logger.debug(f"Selecionando valor '{value}' no dropdown: {locator}")
        try:
            select = Select(self.find_element(locator))
            select.select_by_value(str(value))
            self.logger.info(f"Valor '{value}' selecionado com sucesso em {locator}")
        except Exception as e:
            self.logger.error(f"Erro ao selecionar valor em {locator}: {e}")
            raise

    def get_text(self, locator):
        """
        Obtém o texto de um elemento.

        :param locator: Localizador do elemento.
        :return: Texto do elemento.
        """
        self.logger.debug(f"Obtendo texto do elemento: {locator}")
        try:
            text = self.find_element(locator).text
            self.logger.debug(f"Texto obtido de {locator}: {text}")
            return text
        except Exception as e:
            self.logger.error(f"Erro ao obter texto de {locator}: {e}")
            raise

    def get_html(self, locator):
        """
        Obtém o HTML interno de um elemento.

        :param locator: Localizador do elemento.
        :return: HTML interno do elemento.
        """
        self.logger.debug(f"Obtendo HTML do elemento: {locator}")
        try:
            html = self.find_element(locator).get_attribute("innerHTML")
            self.logger.debug(f"HTML obtido de {locator}: {html}")
            return html
        except Exception as e:
            self.logger.error(f"Erro ao obter HTML de {locator}: {e}")
            raise

    def open(self, url):
        """
        Abre uma URL no navegador.

        :param url: URL a ser aberta.
        """
        self.logger.info(f"Abrindo a URL: {url}")
        try:
            self.driver.get(url)
            self.logger.info(f"URL aberta com sucesso: {url}")
        except Exception as e:
            self.logger.error(f"Erro ao abrir a URL {url}: {e}")
            raise
