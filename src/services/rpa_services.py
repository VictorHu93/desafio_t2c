from src.utils.logger import Logger
from src.utils.web_manager import WebManager
from src.pages.tracking_page import TrackingPage
from src.locators.sales_order_locators import SalesOrderLocators


class RPAService:
    def __init__(self, login_page, sales_order_page, tracking_repository):
        """
        Inicializa o serviço RPA com as páginas necessárias.
        """
        self.logger = Logger.get_logger(
            name="RPAService", log_file="logs/rpa_service.log"
        )
        self.login_page = login_page
        self.sales_order_page = sales_order_page
        self.tracking_repository = tracking_repository

    def execute(self, url_sales_order, url_track):
        """
        Executa o fluxo principal do RPA.

        :param url_sales_order: URL da página de pedidos.
        :param url_track: URL para rastreamento.
        """
        first_driver = None
        second_driver = None
        try:
            # Configuração do primeiro WebDriver para Sales Order
            first_driver = WebManager().get_webdriver()
            self.login_page.driver = first_driver
            self.sales_order_page.driver = first_driver

            # Realiza login e navega para a página de pedidos
            self._perform_login(url_sales_order)

            # Configuração do segundo WebDriver para Tracking
            second_driver = WebManager().get_new_webdriver()
            tracking_page = TrackingPage(second_driver)

            # Login e navegação no rastreamento
            tracking_page.open(url_track)
            tracking_page.hadle_cookies()
            tracking_page.pre_login_tracking()

            # Processamento de pedidos
            self._process_orders(tracking_page)

        except Exception as e:
            self.logger.error(f"Erro durante a execução do RPA: {e}")
            raise
        finally:
            self._cleanup_drivers(first_driver, second_driver)

    def _perform_login(self, url_sales_order):
        """
        Realiza o login na página de pedidos.
        """
        self.logger.info(f"Abrindo a página de pedidos: {url_sales_order}")
        self.login_page.open(url_sales_order)
        self.logger.info("Realizando o pré-login...")
        self.login_page.handle_cookies()
        self.login_page.pre_login()
        self.logger.info("Realizando o login...")
        self.login_page.login()

        self.logger.info("Selecionando 50 linhas para exibição...")
        self.sales_order_page.select_option()
        self.sales_order_page.select_rows(50)

    def _process_orders(self, tracking_page):
        """
        Processa os pedidos na página de Sales Order.
        """
        rows = self.sales_order_page.find_elements(SalesOrderLocators.TABLE_ROWS)

        for i in range(len(rows)):
            # Rebusca as linhas da tabela para refletir alterações no DOM
            rows = self.sales_order_page.find_elements(SalesOrderLocators.TABLE_ROWS)
            row = rows[i]

            tracking_numbers, row_element = (
                self.sales_order_page.process_single_sales_order(row)
            )
            if tracking_numbers:
                order_id = row_element.find_element(
                    *SalesOrderLocators.ORDER_ID_COLUMN
                ).text
                self.logger.info(
                    f"Verificando status de entrega para o pedido {order_id}."
                )

                # Verifica se todos os itens estão entregues
                all_delivered = tracking_page.verify_all_delivered(tracking_numbers)
                if all_delivered:
                    self.logger.info(
                        f"Pedido {order_id}: Todos os itens estão 'Delivered'. Gerando Invoice."
                    )
                    self.sales_order_page.click_generate_invoice(row_element)
                else:
                    self.logger.info(
                        f"Pedido {order_id}: Nem todos os itens estão 'Delivered'. Fechando o pedido."
                    )
                    self.sales_order_page.click_close(row_element)

                # Salva os dados no banco
                self._save_tracking_data(order_id, tracking_numbers, all_delivered)

    def _save_tracking_data(self, order_id, tracking_numbers, all_delivered):
        """
        Salva os dados de rastreamento no banco.
        """
        status = "Delivered" if all_delivered else "Not Delivered"
        for tracking_number in tracking_numbers:
            self.tracking_repository.save_tracking(order_id, tracking_number, status)
            self.logger.info(
                f"Dados salvos no banco para o pedido {order_id}, número de rastreamento {tracking_number}, status: {status}."
            )

    def _cleanup_drivers(self, *drivers):
        """
        Fecha os WebDrivers fornecidos.
        """
        for driver in drivers:
            if driver:
                WebManager.quit_webdriver(driver)
                self.logger.info("WebDriver fechado com sucesso.")
