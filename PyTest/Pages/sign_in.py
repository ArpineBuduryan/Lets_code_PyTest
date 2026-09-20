from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Lib.helper import Helper


class SignInPage(Helper):
    email = (By.ID, "email")
    password = (By.ID, "login-password")
    login_button = (By.ID, "login")
    incorrect = (By.ID, "incorrectdetails")

    def invalid_login(self, email, password):
        try:
            self.send_keys(self.email, email)
            self.send_keys(self.password, password)
            self.click(self.login_button)

            error_element = self.wait.until(EC.visibility_of_element_located(self.incorrect))
            error_text = error_element.text
            self.test_logger.info("Invalid login executed and validation message captured.")
            return error_text
        except Exception as e:
            self.test_logger.error(f"Error in invalid_login: {e}")
            #return f"Error: {e}"
            raise