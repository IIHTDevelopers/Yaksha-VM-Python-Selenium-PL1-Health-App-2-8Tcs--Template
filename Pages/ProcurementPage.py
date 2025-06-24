from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

class ProcurementPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.procurement = {
            "procurement_link": (By.CSS_SELECTOR, 'a[href="#/ProcurementMain"]'),
            "settings": (By.XPATH, '//a[contains(text(),"Settings")]'),
            "currency_sub_tab": (By.CSS_SELECTOR, 'a[routerlink="CurrencyList"]'),
            "add_currency_button1": (By.CSS_SELECTOR, 'input[value="Add Currency"]'),
            "add_currency_button2": (By.CSS_SELECTOR, 'input#AddCurrency'),
            "currency_code": (By.CSS_SELECTOR, 'input#CurrencyCode'),
            "currency_description_field": (By.CSS_SELECTOR, 'input#Description'),
            "search_bar": (By.CSS_SELECTOR, 'input#quickFilterInput'),
            "currency_code_column": (By.CSS_SELECTOR, 'div[col-id="CurrencyCode"]'),
        }

    def add_currency_and_verify(self):
        """
        /**
        * @Test5
        * @description This method navigates to the Purchase Request page, accesses the Currency Settings,
        *              adds a new currency with a unique code and description, and verifies that the new
        *              currency is successfully added to the table.
        *
        * @expected
        * The new currency should be added successfully and displayed in the table with the correct currency
        * code and description.
        */
        """
        pass
        assert False,"TODO:Implement add_currency_and_verify"

