import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestData import data


class Helper:

    def __init__(self, driver, test_logger):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.test_logger = test_logger

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.test_logger.info(f"Successfully clicked element: {locator}")
        except Exception as e:
            self.test_logger.error(f"Error clicking element {locator}: {e}")
            raise

    def send_keys(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            self.test_logger.info(f"Successfully sent keys to element: {locator}")
        except Exception as e:
            self.test_logger.error(f"Error sending keys to element {locator}: {e}")
            raise

    def hover(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            ActionChains(self.driver).move_to_element(element).perform()
            self.test_logger.info(f"Successfully hovered over element: {locator}")
        except Exception as e:
            self.test_logger.error(f"Error hovering over element {locator}: {e}")
            raise

    def scroller(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            ActionChains(self.driver).scroll_to_element(element).perform()
            self.test_logger.info(f"Successfully scrolled to element: {locator}")
            return element
        except Exception as e:
            self.test_logger.error(f"Error scrolling to element {locator}: {e}")
            raise

    def write_file(self, text, mode="a+"):
        try:
            with open(data.file_name, mode, encoding="utf-8") as file:
                file.write(f"{text}\n")
            self.test_logger.info(f"Successfully wrote data to file: {data.file_name}")
        except Exception as e:
            self.test_logger.error(f"Error writing to file: {e}")
            raise