import stock_crawler_config
import webdriver_provider


class StockCrawler(object):

    def __init__(self):
        self.config = stock_crawler_config.get_config()
        self.morning_star_working_folder = self.config['morning_star_working_folder']

    def __enter__(self):
        self.morning_star_driver = webdriver_provider.make_base_webdriver(self.morning_star_working_folder)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.morning_star_driver.close()
