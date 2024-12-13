from src.locators.sales_order_locators import SalesOrderLocators
from src.pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from src.utils.logger import Logger


class SalesOrderPage(BasePage):
    # Configuração do logger para a classe
    logger = Logger.get_logger(
        name="SalesOrderPage", log_file="logs/sales_order_page.log"
    )

    def select_option(self):
        """
        Clica na opção de Sales Order.
        """
        try:
            self.logger.info("Selecionando a opção de Sales Order...")
            self.click(SalesOrderLocators.SALES_ORDER_CLICK)
            self.logger.info("Opção de Sales Order selecionada com sucesso.")
        except Exception as e:
            self.logger.error(f"Erro ao selecionar a opção de Sales Order: {e}")
            raise

    def select_rows(self, rows: int):
        """
        Seleciona o número de linhas exibidas na tabela.
        """
        try:
            self.logger.info(f"Selecionando {rows} linhas na tabela...")
            dropdown = self.find_element(SalesOrderLocators.SELECT_ROWS_DROPDOWN)
            select = Select(dropdown)
            select.select_by_value(str(rows))
            self.logger.info(f"{rows} linhas selecionadas com sucesso.")
        except Exception as e:
            self.logger.error(f"Erro ao selecionar {rows} linhas na tabela: {e}")
            raise

    def process_single_sales_order(self, row):
        """
        Processa uma única linha da tabela de pedidos.

        :param row: WebElement representando uma linha na tabela.
        :return: Tuple contendo (order_id, tracking_numbers, row_element).
        """
        try:
            status = row.find_element(*SalesOrderLocators.STATUS_COLUMN).text
            self.logger.info(f"Processando linha com status: {status}")
            if status in ["Confirmed", "Delivery Outstanding"]:
                expand_icon = row.find_element(*SalesOrderLocators.EXPAND_ICON)
                expand_icon.click()
                self.logger.debug("Expandiu sub-tabela com sucesso.")

                sub_rows = self.find_elements(SalesOrderLocators.SUB_TABLE_ROWS)
                tracking_numbers = []
                for sub_row in sub_rows:
                    tracking_number = sub_row.find_element(
                        *SalesOrderLocators.TRACKING_COLUMN
                    ).text
                    tracking_numbers.append(tracking_number)
                    self.logger.debug(f"Tracking number encontrado: {tracking_number}")

                self.logger.info("Processamento da linha concluído.")
                return tracking_numbers, row
            self.logger.info("Linha ignorada devido ao status incompatível.")
            return None, None
        except Exception as e:
            self.logger.error(f"Erro ao processar a linha: {e}")
            raise

    def click_generate_invoice(self, row):
        """
        Clica no botão Generate Invoice para uma linha específica.
        """
        try:
            self.logger.info("Clicando no botão Generate Invoice...")
            generate_invoice_button = row.find_element(
                *SalesOrderLocators.GENERATE_INVOICE_BUTTON
            )
            generate_invoice_button.click()
            self.logger.info("Botão Generate Invoice clicado com sucesso.")
        except Exception as e:
            self.logger.error(f"Erro ao clicar no botão Generate Invoice: {e}")
            raise

    def click_close(self, row):
        """
        Clica no botão Close para uma linha específica.
        """
        try:
            self.logger.info("Clicando no botão Close...")
            close_button = row.find_element(*SalesOrderLocators.CLOSE_BUTTON)
            close_button.click()
            self.logger.info("Botão Close clicado com sucesso.")
        except Exception as e:
            self.logger.error(f"Erro ao clicar no botão Close: {e}")
            raise
