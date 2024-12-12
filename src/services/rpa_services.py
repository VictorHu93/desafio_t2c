class RPAService:
    def __init__(self, login_page, sales_order_page, tracking_repository):
        """
        Inicializa o serviço RPA com as páginas necessárias.
        """
        self.login_page = login_page
        self.sales_order_page = sales_order_page
        self.tracking_repository = tracking_repository

    def execute(self, url_sales_order, url_track):
        """
        Executa o fluxo principal do RPA.
        
        :param url_sales_order: URL da página de pedidos.
        :param url_track: URL para rastreamento.
        """
        try:
            # Abrir URL de Sales Order e realizar login
            print(f"Abrindo a página: {url_sales_order}")
            self.login_page.open(url_sales_order)
            print("Realizando o pré-login...")
            self.login_page.pre_login()
            print("Realizando o login...")
            self.login_page.login()

            # Operações na página de Sales Order
            print("Selecionando opção na página de Sales Order...")
            self.sales_order_page.select_option()
            print("Selecionando 50 linhas para exibição...")
            self.sales_order_page.select_rows(50)
            
            orders = self.sales_order_page.process_sales_orders()
            for order_id, tracking_number in orders:
                self.tracking_repository.save_tracking(order_id, tracking_number)

            print("Execução do RPA concluída com sucesso.")
        except Exception as e:
            print(f"Erro durante a execução do RPA: {e}")
            raise  # Relevante em casos onde o erro precisa ser tratado fora do RPAService
