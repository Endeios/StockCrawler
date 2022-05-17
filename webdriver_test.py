import unittest
import webdriver_provider


class WebdriverTest(unittest.TestCase):
    def test_webdriver_can_be_created(self):
        webdriver = webdriver_provider.make_base_webdriver()
        self.assertIsNotNone(webdriver)
        webdriver.close()


if __name__ == '__main__':
    unittest.main()
