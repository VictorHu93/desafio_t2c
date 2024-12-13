from selenium.webdriver.common.by import By


class SalesOrderLocators:
    """
    Localizadores para elementos da página de pedidos (Sales Order).
    """

    # Botão para acessar a página de Sales Order
    SALES_ORDER_CLICK = (By.CSS_SELECTOR, "a[href='salesorder-applist.html']")

    # Dropdown para selecionar o número de linhas exibidas na tabela
    SELECT_ROWS_DROPDOWN = (By.CSS_SELECTOR, "select.custom-select-sm")

    # Linhas da tabela principal de pedidos
    TABLE_ROWS = (By.CSS_SELECTOR, "#salesOrderDataTable tbody tr")

    # Coluna com os IDs dos pedidos
    ORDER_ID_COLUMN = (By.CSS_SELECTOR, "td:nth-child(2)")

    # Coluna com o status dos pedidos
    STATUS_COLUMN = (By.CSS_SELECTOR, "td:nth-child(5)")

    # Ícone para expandir sub-tabelas dentro de um pedido
    EXPAND_ICON = (By.CSS_SELECTOR, "td.dt-control i")

    # Linhas da sub-tabela de itens do pedido
    SUB_TABLE_ROWS = (By.CSS_SELECTOR, "table.sales-order-items tbody tr")

    # Coluna com os números de rastreamento na sub-tabela
    TRACKING_COLUMN = (By.CSS_SELECTOR, "td:nth-child(2)")

    # Botão para fechar a janela do pedido
    CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'btn-secondary') and text()='Close']",
    )

    # Botão para gerar a fatura de um pedido
    GENERATE_INVOICE_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Generate Invoice') and contains(@onclick, 'markInvoiceSent')]",
    )
