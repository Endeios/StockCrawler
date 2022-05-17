import unittest

from morningstar_parse_tests import Morningstar
from load_config_from_file import LoadConfigFromFile
from webdriver_test import WebdriverTest

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LoadConfigFromFile))
    suite.addTest(unittest.makeSuite(Morningstar))
    suite.addTest(unittest.makeSuite(WebdriverTest))
    runner.run(suite)
