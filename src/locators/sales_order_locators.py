from selenium.webdriver.common.by import By

class SalesOrderLocators:
    SALES_ORDER_CLICK = (By.CSS_SELECTOR, "a[href='salesorder-applist.html']")
    SELECT_ROWS_DROPDOWN = (By.CSS_SELECTOR, "select.custom-select-sm")
    
    TABLE_ROWS = (By.CSS_SELECTOR, "#salesOrderDataTable tbody tr")
    ORDER_ID_COLUMN = (By.CSS_SELECTOR, "td:nth-child(2)")
    STATUS_COLUMN = (By.CSS_SELECTOR, "td:nth-child(5)")
    EXPAND_ICON = (By.CSS_SELECTOR, "td.dt-control i")
    SUB_TABLE_ROWS = (By.CSS_SELECTOR, "table.sales-order-items tbody tr")
    TRACKING_COLUMN = (By.CSS_SELECTOR, "td:nth-child(2)")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(text(), 'Close')]")