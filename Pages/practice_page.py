from selenium.webdriver.common.by import By
from Lib.helper import Helper


class PracticePage(Helper):
    alert_button = (By.ID, "alertbtn")
    text_box = (By.ID, "displayed-text")
    hide_button = (By.XPATH, "//input[@id='hide-textbox']")
    mouse_hover = (By.ID, "mousehover")
    top = (By.XPATH, '//a[text()="Top"]')
    footer = (By.XPATH, "//footer")
    footer_text = (By.XPATH, "//div[contains(@class")
    sign_in_button = (By.XPATH, "//a[contains(text(),'Sign In')]")

    def click_alert(self):
        try:
            self.click(self.alert_button)
            popup = self.driver.switch_to.alert
            text = popup.text
            popup.accept()
            self.test_logger.info("Alert handled successfully.")
            return text
        except Exception as e:
            self.test_logger.error(f"Error in click_alert: {e}")
            return f"Error handling alert: {e}"

    def enter_text_box(self, text):
        try:
            self.send_keys(self.text_box, text)
            self.test_logger.info("Text entered into text box successfully.")
        except Exception as e:
            self.test_logger.error(f"Error in enter_text_box: {e}")
            raise

    def hide_text_box(self):
        try:
            self.click(self.hide_button)
            self.test_logger.info("Hide button clicked successfully.")
        except Exception as e:
            self.test_logger.error(f"Error in hide_text_box: {e}")
            raise

    def get_text_box_style(self):
        try:
            text_b = self.driver.find_element(*self.text_box)
            if not text_b.is_displayed():
                attribute = "style"
                value = text_b.get_attribute(attribute)
                self.test_logger.info("Captured hidden text box style attribute.")
                return f"Hide Info = Attribute: {attribute}, Value: {value}"
            return "Hide info is still displayed,"
        except Exception as e:
            self.test_logger.error(f"Error in get_text_box_style: {e}")
            return f"Error: {e}"

    def scroll_top(self):
        try:
            self.hover(self.mouse_hover)
            self.click(self.top)
            self.test_logger.info("Scrolled to top via mouse hover successfully.")
        except Exception as e:
            self.test_logger.error(f"Error in scroll_top: {e}")
            raise

    def scroll_footer(self):
        try:
            footer_element = self.scroller(self.footer)
            footer_text = footer_element.text
            self.test_logger.info("Scrolled to footer and retrieved text successfully.")
            return footer_text
        except Exception as e:
            self.test_logger.error(f"Error in scroll_footer: {e}")
            return f"Error: {e}"

    def click_sign_in(self):
        try:
            self.click(self.sign_in_button)
            self.test_logger.info("Clicked sign in button successfully.")
        except Exception as e:
            self.test_logger.error(f"Error in click_sign_in: {e}")
            raise