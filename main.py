from src.config.environment.urls import URL_SALES_ORDER, URL_TRACK
from src.pages.login_page import LoginPage
from src.pages.sales_order_page import SalesOrderPage
from src.services.rpa_services import RPAService
from src.utils.web_manager import WebManager
from src.data.tracking_repository import TrackingRepository

def main():
    login_page = LoginPage()
    sales_order_page = SalesOrderPage()
    trackingrepository = TrackingRepository()
    rpa_service = RPAService(login_page, sales_order_page, trackingrepository)
    
    try:
        print("Iniciando execução do RPA...")
        rpa_service.execute(URL_SALES_ORDER, URL_TRACK)
        print("Execução concluída com sucesso.")
    except Exception as e:
        print(f"Erro durante a execução do RPA: {e}")
    finally:
        print("Encerrando o WebDriver...")
        WebManager.quit_webdriver()

if __name__ == "__main__":
    main()
