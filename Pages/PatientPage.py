import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PatientPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.patient = {
            "patient_link": (By.CSS_SELECTOR, 'a[href="#/Patient"]'),
            "register_patient": (By.CSS_SELECTOR, 'ul.page-breadcrumb a[href="#/Patient/RegisterPatient"]'),
            "new_photo_button": (By.XPATH, '//button[contains(text(),"New Photo")]'),
            "upload_button": (By.CSS_SELECTOR, 'label[for="fileFromLocalDisk"]'),
            "done_button": (By.XPATH, '//button[text()="Done"]'),
            "uploaded_img": (By.CSS_SELECTOR, 'div.wrapper img'),
            "profile_picture_icon": (By.CSS_SELECTOR, 'a[title="Profile Picture"]'),
        }

    def upload_profile_picture(self):
        """
        /**
        * @Test8
        * @description This method verifies the successful upload of a profile picture for a patient by navigating to the "Register Patient" tab
        *              and completing the upload process.
        * @expected
        * Verify that the uploaded image is displayed successfully in the patient's profile.
        */
        """
        pass
        assert False,"TODO:Implement upload_profile_picture"

