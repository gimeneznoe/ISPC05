class NormativaManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def open_connection(self):
        self.connection = sqlite3.connect(self.db_file)

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def select_normativas(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM Normativa
        """)
        normativas_data = cursor.fetchall()
        #algo
