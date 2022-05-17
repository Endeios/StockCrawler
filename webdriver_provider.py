from selenium import webdriver
from selenium.webdriver.firefox import options as firefox_options


def make_base_webdriver(cache_folder="."):
    options = firefox_options.Options()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", cache_folder)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/html")
    options.headless = True

    driver = webdriver.Firefox(options=options)
    return driver
