import unittest
from dao import DAO

class TestDAO(unittest.TestCase):
    def setUp(self):
        # Initialize DAO for testing (provide test database connection details)
        self.dao = DAO('test_db', 'test_user', 'test_password', 'localhost', 5432)

    def tearDown(self):
        # Clean up after each test (close database connection)
        self.dao.close_connection()

    def test_get_authors_ordered_by_dob(self):
        authors = self.dao.get_authors_ordered_by_dob(limit=10)
        self.assertIsInstance(authors, list)
        self.assertEqual(len(authors), 10)
        # Add more assertions based on expected behavior

    def test_get_sales_total_for_author(self):
        total_sales = self.dao.get_sales_total_for_author('Lorelai Gilmore')
        self.assertIsInstance(total_sales, float)
        # Add assertions for specific total sales value

    def test_get_top_performing_authors(self):
        top_authors = self.dao.get_top_performing_authors(limit=10)
        self.assertIsInstance(top_authors, list)
        self.assertEqual(len(top_authors), 10)
        for author in top_authors:
            self.assertIsInstance(author, tuple)
            self.assertIsInstance(author[0], str)  # Author name
            self.assertIsInstance(author[1], float)  # Total revenue
        # Add more assertions based on expected behavior

# Run the tests if executed as main script
if __name__ == '__main__':
    unittest.main()
