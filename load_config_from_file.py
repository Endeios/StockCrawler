import unittest
import stock_crawler_config
import os


class LoadConfigFromFile(unittest.TestCase):

    def test_config_should_not_be_none(self):
        config = stock_crawler_config.get_config()
        self.assertIsNotNone(config)

    def test_should_load_config(self):
        config = stock_crawler_config.get_config()
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        expected_position = os.path.join(curr_dir, "work_tmp")
        self.assertIsNotNone(config['morning_star_working_folder'])


if __name__ == '__main__':
    unittest.main()
