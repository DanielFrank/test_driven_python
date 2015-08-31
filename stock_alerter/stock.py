import unittest

class StockTest(unittest.TestCase):
    def test_price_of_a_new_stock_class_should_be_none(self):
        stock = Stock("GOOG")
        self.assertIsNone(stock.price)

if __name__ == "__main__":
    unittest.main()


