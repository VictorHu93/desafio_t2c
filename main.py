from src.config.environment.urls import URL_SALES_ORDER, URL_TRACK
from src.pages.login_page import LoginPage
from src.pages.sales_order_page import SalesOrderPage
from src.services.rpa_services import RPAService
from src.data.tracking_repository import TrackingRepository
from src.utils.logger import Logger


def main():
    # Configuração do logger
    logger = Logger.get_logger(name="Main", log_file="logs/main.log")

    # Instâncias principais
    login_page = LoginPage()  
    sales_order_page = SalesOrderPage()  
    tracking_repository = TrackingRepository()
    rpa_service = RPAService(login_page, sales_order_page, tracking_repository)

    try:
        logger.info("Iniciando execução do RPA...")
        rpa_service.execute(URL_SALES_ORDER, URL_TRACK)
        logger.info("Execução concluída com sucesso.")
    except Exception as e:
        logger.error(f"Erro durante a execução do RPA: {e}")
    finally:
        logger.info("Finalizando o processo.")


if __name__ == "__main__":
    main()

