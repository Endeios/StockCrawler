import stock_crawler_config
import webdriver_provider


class StockCrawler(object):

    def __init__(self):
        self.config = stock_crawler_config.get_config()
        self.morning_star_driver = webdriver_provider.make_base_webdriver(self.config['morning_star_working_folder'])
        self.morning_star_working_folder = self.config['morning_star_working_folder']
