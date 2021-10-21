from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)

    def _open_page(self, url):
        self.driver.get(url)
        return self

    def input_value(self, locator, value):
        elem = self.driver.find_element(*locator)
        elem.send_keys(value)
        return self

    def click(self, locator):
        try:
            elem = self.wait.until(EC.visibility_of_element_located(locator)).click()
            return elem
        except TimeoutException:
            raise TimeoutException

    def get_text(self, locator):
        try:
            elem = self.wait.until(EC.presence_of_element_located(locator)).text
            return elem
        except TimeoutException:
            raise TimeoutException
