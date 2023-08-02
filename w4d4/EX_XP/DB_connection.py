import psycopg2

# Establish the connection


class DatabaseManager:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="restaurant",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
