import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from TestData import data
from Lib.helper import Helper
from Pages.practice_page import PracticePage
from Pages.sign_in import SignInPage

@pytest.mark.regression
def test_web(get_driver, test_logger):
    driver = get_driver
    helper = Helper(driver, test_logger)

    test_logger.info("Navigating to practice page URL")
    driver.get(data.url)

    practice_page = PracticePage(driver, test_logger)
    sign_in_page = SignInPage(driver, test_logger)
        
    alert_text = practice_page.click_alert()
    helper.write_file(f"Alert text: {alert_text}")

    practice_page.enter_text_box(data.text)
    practice_page.hide_text_box()
    hide_style_info = practice_page.get_text_box_style()
    helper.write_file(hide_style_info)
        
    practice_page.scroll_top()
        
    footer_text = practice_page.scroll_footer()
    helper.write_file(f"Footer text: {footer_text}")

    practice_page.click_sign_in()
    error_element = sign_in_page.invalid_login(data.wrong_email, data.wrong_password)
    helper.write_file(f"Login error writing: {error_element}")

    # Open a new tab and switch to it for Google
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(data.google_url)
    helper.write_file(f"Google opened on second tab with title: {driver.title}")
    test_logger.info("Test completed successfully.")
        