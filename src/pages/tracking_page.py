import time
from src.locators.tracking_locators import TrackingLocators
from src.locators.login_locators import LoginLocators
from src.pages.base_page import BasePage
from src.config.environment.login import PRE_USER, PRE_PASSWORD
from src.utils.logger import Logger


class TrackingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.get_logger(
            name="TrackingPage", log_file="logs/tracking_page.log"
        )
    
    def hadle_cookies(self):
        self.click(LoginLocators.PRE_BUTTON_COKIES)
        self.logger.debug("Aceitando cookies.")

    def pre_login_tracking(self):
        """
        Realiza o pré-login na página de rastreamento.
        """
        self.logger.info("Iniciando pré-login na página de rastreamento.")
        try:
            self.click(LoginLocators.PRE_BUTTON_CLICK)
            self.logger.debug("Clicando no botão de login.")
            self.send_keys(PRE_USER, LoginLocators.PRE_USERNAME_FIELD)
            self.logger.debug(f"Preenchendo o campo de usuário com: {PRE_USER}.")
            self.click(LoginLocators.PRE_BUTTON_NEXT_CLICK)
            self.logger.debug("Clicando em próximo no login.")
            self.send_keys(PRE_PASSWORD, LoginLocators.PRE_PASSWORD_FIELD)
            self.logger.debug("Preenchendo o campo de senha.")
            self.click(LoginLocators.PRE_LOGIN_BUTTON)
            self.logger.info("Login concluído com sucesso.")
        except Exception as e:
            self.logger.error(f"Erro durante o pré-login: {e}")
            raise

    def search_tracking(self, tracking_number):
        """
        Realiza a busca de rastreamento usando o número de rastreamento.

        :param tracking_number: Número de rastreamento a ser pesquisado.
        """
        self.logger.info(f"Buscando número de rastreamento: {tracking_number}.")
        try:
            self.send_keys(tracking_number, TrackingLocators.SEARCH_FIELD)
            self.click(TrackingLocators.SEARCH_BUTTON)
            self.logger.info("Busca realizada com sucesso.")
        except Exception as e:
            self.logger.error(f"Erro ao buscar o número de rastreamento: {e}")
            raise

    def validate_tracking_number(self, tracking_number):
        """
        Valida se o número de rastreamento exibido na tabela corresponde ao esperado.

        :param tracking_number: Número de rastreamento esperado.
        :return: True se os números corresponderem, False caso contrário.
        """
        self.logger.info(f"Validando número de rastreamento: {tracking_number}.")
        try:
            displayed_tracking_number = self.get_text(
                TrackingLocators.TRACKING_NUMBER_FIELD
            ).strip()
            if displayed_tracking_number == tracking_number:
                self.logger.info("Número de rastreamento validado com sucesso.")
                return True
            else:
                self.logger.warning(
                    f"Número de rastreamento inconsistente: esperado {tracking_number}, encontrado {displayed_tracking_number}."
                )
                return False
        except Exception as e:
            self.logger.error(
                f"Erro durante a validação do número de rastreamento: {e}"
            )
            raise

    def verify_all_delivered(self, tracking_numbers):
        """
        Verifica se todos os itens têm o status 'Delivered'.

        :param tracking_numbers: Lista de números de rastreamento.
        :return: True se todos forem 'Delivered', False caso contrário.
        """
        self.logger.info("Verificando status de entrega para os itens.")
        try:
            for tracking_number in tracking_numbers:
                self.logger.debug(
                    f"Verificando número de rastreamento: {tracking_number}."
                )
                search_field = self.find_element(TrackingLocators.SEARCH_FIELD)
                if search_field:
                    search_field.clear()
                    self.search_tracking(tracking_number)
                    time.sleep(3)  # Pode ser ajustado com uma espera explícita

                if self.validate_tracking_number(tracking_number):
                    status = self.get_text(
                        TrackingLocators.SCHEDULED_DELIVERY_FIELD
                    ).strip()
                    self.logger.info(
                        f"Status encontrado para {tracking_number}: {status}."
                    )
                    if status != "Delivered":
                        self.logger.warning(
                            f"Item com status diferente de 'Delivered': {status}."
                        )
                        return False
                else:
                    self.logger.error(
                        f"Validação falhou para o número de rastreamento: {tracking_number}."
                    )
                    return False
            self.logger.info("Todos os itens possuem o status 'Delivered'.")
            return True
        except Exception as e:
            self.logger.error(f"Erro durante a verificação dos status de entrega: {e}")
            raise
