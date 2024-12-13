from selenium.webdriver.common.by import By


class TrackingLocators:
    """
    Localizadores para elementos da página de rastreamento.
    """

    # Campo de busca do número de rastreamento
    SEARCH_FIELD = (By.ID, "inputTrackingNo")

    # Botão para verificar o status do rastreamento
    SEARCH_BUTTON = (By.ID, "btnCheckStatus")

    # Campo de entrega agendada, localizado por texto 'SCHEDULED DELIVERY'
    SCHEDULED_DELIVERY_FIELD = (
        By.XPATH,
        "//tbody[@id='shipmentStatus']//td[normalize-space()='SCHEDULED DELIVERY']/following-sibling::td",
    )

    # Campo para o número de rastreamento exibido na tabela de rastreamento
    TRACKING_NUMBER_FIELD = (
        By.CSS_SELECTOR,
        "#shipmentStatus > tr:first-child > td:nth-child(2)",
    )
