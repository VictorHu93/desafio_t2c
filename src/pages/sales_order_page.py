from src.locators.sales_order_locators import SalesOrderLocators
from src.pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class SalesOrderPage(BasePage):
    
    def select_option(self):
        self.click(SalesOrderLocators.SALES_ORDER_CLICK)
    
    def select_rows(self, rows: int):
        dropdown = self.find_element(SalesOrderLocators.SELECT_ROWS_DROPDOWN)
        select = Select(dropdown)
        select.select_by_value(str(rows))

    def process_sales_orders(self):
        result = []
        # Use find_elements para múltiplas linhas da tabela
        rows = self.find_elements(SalesOrderLocators.TABLE_ROWS)
        for row in rows:
            # Obter o status da ordem
            status = row.find_element(*SalesOrderLocators.STATUS_COLUMN).text
            if status in ["Confirmed", "Delivery Outstanding"]:
                # Expandir sub-tabela
                expand_icon = row.find_element(*SalesOrderLocators.EXPAND_ICON)
                expand_icon.click()

                # Processar sub-tabela
                sub_rows = self.find_elements(SalesOrderLocators.SUB_TABLE_ROWS)  # find_elements para múltiplas sub-linhas
                for sub_row in sub_rows:
                    # Obter Order ID e Tracking Number
                    order_id = row.find_element(*SalesOrderLocators.ORDER_ID_COLUMN).text
                    tracking_number = sub_row.find_element(*SalesOrderLocators.TRACKING_COLUMN).text
                    result.append((order_id, tracking_number))
                close_button = self.find_element(SalesOrderLocators.CLOSE_BUTTON)
                close_button.click()
        return result