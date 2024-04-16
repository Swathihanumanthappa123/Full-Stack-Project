from db import Database
from models import Author
import psycopg2

import logging
import sys

# Create a logger
logger = logging.getLogger('stdout_logger')
logger.setLevel(logging.DEBUG)  # Set the logging level to capture all levels of messages

# Create a StreamHandler that outputs to stdout
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)  # Set the level for this handler

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(formatter)

# Add the stdout_handler to the logger
logger.addHandler(stdout_handler)


class DAO:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.db = Database(dbname, user, password, host, port)

    def get_authors_ordered_by_dob(self, limit=10) -> list[Author]:
        query = """
            SELECT *
            FROM authors
            ORDER BY date_of_birth
            LIMIT %s;
        """
        try:
            result = self.db.fetch_query(query, (limit,))
            if result:
                logging.info(f"result: {result}")
                authors = [Author(id=row[0], name=row[1], email=row[2], date_of_birth=str(row[3])) for row in result]
                return authors
            else:
                return []
        except psycopg2.Error as e:
            print(f"Error fetching authors ordered by date of birth: {e}")
            return []

    def preprocess_monetary_value(self, monetary_str: str) -> float:
        # Remove dollar sign ('$') and commas (',') from the string
        processed_str = monetary_str.replace('$', '').replace(',', '')
        # Convert the processed string to float
        return float(processed_str)

    def get_sales_total_for_author(self, author_name: str) -> float:
        query = """
            SELECT SUM(si.item_price * si.quantity) AS total_sales
            FROM sale_items si
            JOIN books b ON si.book_id = b.id
            JOIN authors a ON b.author_id = a.id
            WHERE a.name = %s;
        """
        try:
            result = self.db.fetch_query(query, (author_name,))
            if result and result[0][0]:
                return self.preprocess_monetary_value(result[0][0])
            else:
                return 0.0
        except psycopg2.Error as e:
            print(f"Error fetching sales total for author '{author_name}': {e}")
            return 0.0

    def get_top_performing_authors(self, limit=10) -> list[tuple[str, float]]:
        query = """
            SELECT a.name, SUM(si.item_price * si.quantity) AS total_revenue
            FROM authors a
            JOIN books b ON a.id = b.author_id
            JOIN sale_items si ON b.id = si.book_id
            GROUP BY a.id, a.name
            ORDER BY total_revenue DESC
            LIMIT %s;
        """
        try:
            result = self.db.fetch_query(query, (limit,))
            if result:
                top_authors = [(row[0], self.preprocess_monetary_value(row[1])) for row in result]
                return top_authors
            else:
                return []
        except psycopg2.Error as e:
            print(f"Error fetching top performing authors: {e}")
            return []

    def close_connection(self):
        self.db.close_connection()