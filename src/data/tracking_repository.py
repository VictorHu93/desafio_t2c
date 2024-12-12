import sqlite3

class TrackingRepository:
    def __init__(self, db_path="sales_orders.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tracking_numbers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id TEXT,
                tracking_number TEXT
            )
        """)
        conn.commit()
        conn.close()

    def save_tracking(self, order_id, tracking_number):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tracking_numbers (order_id, tracking_number) VALUES (?, ?)",
            (order_id, tracking_number)
        )
        conn.commit()
        conn.close()
