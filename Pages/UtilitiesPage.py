from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class UtilitiesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.utilities = {
            "utilities_link": (By.XPATH, "//span[text()='Utilities']"),
            "scheme_refund_tab": (By.CSS_SELECTOR, 'ul.page-breadcrumb a[href="#/Utilities/SchemeRefund"]'),
            "counter_item": (By.XPATH, "//div[@class='counter-item']"),
            "new_scheme_refund_entry_button": (By.XPATH, "//a[contains(text(),'New Scheme Refund Entry')]"),
            "save_scheme_refund_button": (By.CSS_SELECTOR, "button#savebutton"),
            "warning_popup": (By.XPATH, "//p[contains(text(),'warning')]/../p[contains(text(),'Please fill all the mandatory fields.')]"),
        }

    def verify_mandatory_fields_warning(self):
        """
        /**
        * @Test6
        * @description This method verifies that a warning popup is displayed when attempting to save a new
        *              Scheme Refund Entry without filling in mandatory fields.
        * @expected
        * A warning popup should appear with the message: "Please fill all the mandatory fields."
        */
        """
        pass
        assert False,"TODO:Implement verify_mandatory_fields_warning"
