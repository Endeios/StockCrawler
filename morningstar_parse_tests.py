import unittest

from StockCrawler import StockCrawler
from data_parser.morning_star.common import get_10yrs_data_from_csv, FINANCIALS


class Morningstar(unittest.TestCase):

    def test_download_csv_by_name(self):
        with StockCrawler() as stock_crawler:
            ticker = "NVDA"
            results = get_10yrs_data_from_csv(ticker, stock_crawler)
            eps_usd = results[FINANCIALS].loc["Earnings Per Share USD"]
            print(eps_usd)
            self.assertIsNotNone(eps_usd)


if __name__ == '__main__':
    unittest.main()
