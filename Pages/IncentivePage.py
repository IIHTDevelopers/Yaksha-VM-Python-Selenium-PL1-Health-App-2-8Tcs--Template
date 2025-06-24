import json
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class IncentivePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Construct the correct path for the JSON file
        base_path = os.path.dirname(os.path.abspath(__file__))  # Current script directory
        json_path = os.path.join(base_path, "..", "Data", "PatientName.json")  # Adjusted path

        # Load test data from JSON
        try:
            with open(json_path, "r") as f:
                self.test_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at {json_path}")

        self.incentive = {
            "incentive_link": (By.CSS_SELECTOR, 'a[href="#/Incentive"]'),
            "settings_tab": (By.CSS_SELECTOR, 'ul[class="page-breadcrumb"] a[href="#/Incentive/Setting"]'),
            "search_bar": (By.CSS_SELECTOR, 'input#quickFilterInput'),
            "edit_tds_button": (By.CSS_SELECTOR, 'a[danphe-grid-action="edit-tds"]'),
            "edit_tds_modal": (By.CSS_SELECTOR, 'div.modal[title="Edit TDS Percent"]'),
            "tds_input_field": (By.CSS_SELECTOR, 'input[type="number"]'),
            "update_tds_button": (By.CSS_SELECTOR, 'button#btn_GroupDistribution'),
            "tds_value_in_table": (By.XPATH, '(//div[@col-id="TDSPercent"])[2]'),
        }

    def edit_tds_for_employee(self):
        """
        /**
        * @Test9
        * @description This method updates the TDS% for a specific employee and verifies the updated value in the table.
        * @expected
        * The updated TDS% value is displayed correctly in the corresponding row of the table.
        */
        """
        pass
        assert False,"TODO:Implement edit_tds_for_employee"

