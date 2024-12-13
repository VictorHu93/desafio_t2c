import sqlite3


class TrackingRepository:
    def __init__(self, db_path="sales_orders.db"):
        """
        Inicializa o repositório de rastreamento.

        :param db_path: Caminho para o arquivo do banco de dados SQLite.
        """
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        """
        Recria a tabela no banco de dados com a estrutura correta.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tracking_numbers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_id TEXT NOT NULL,
                    tracking_number TEXT NOT NULL,
                    status TEXT
                )
            """
            )

    def _check_table_structure(self):
        """
        Verifica se a tabela de rastreamento contém todas as colunas necessárias.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA table_info(tracking_numbers)")
            columns = [col[1] for col in cursor.fetchall()]
            return "status" in columns

    def save_tracking(self, order_id, tracking_number, status):
        """
        Salva o número de rastreamento no banco com o status associado.

        :param order_id: ID do pedido.
        :param tracking_number: Número de rastreamento.
        :param status: Status associado ('Delivered' ou 'Not Delivered').
        """
        if not order_id or not tracking_number or not status:
            raise ValueError(
                "Os campos 'order_id', 'tracking_number' e 'status' são obrigatórios."
            )

        table_has_status_column = self._check_table_structure()

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            if table_has_status_column:
                cursor.execute(
                    """
                    INSERT INTO tracking_numbers (order_id, tracking_number, status)
                    VALUES (?, ?, ?)
                    """,
                    (order_id, tracking_number, status),
                )
            else:
                cursor.execute(
                    """
                    INSERT INTO tracking_numbers (order_id, tracking_number)
                    VALUES (?, ?)
                    """,
                    (order_id, tracking_number),
                )
