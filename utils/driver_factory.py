from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory():

    @staticmethod
    def get_driver(browser):

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("start_maximized")
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

        else:
            raise Exception("Podaj inną wersję przeglądarki.")