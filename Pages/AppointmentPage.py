from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.appointment = {
            "appointment_link": (By.CSS_SELECTOR, 'a[href="#/Appointment"]'),
            "counter_item": (By.XPATH, "//div[@class='counter-item']"),
            "appointment_booking_list": (By.CSS_SELECTOR, "ul.page-breadcrumb li a[href='#/Appointment/ListAppointment']"),
            "visit_type_dropdown": (By.NAME, "VistType"),
            "from_date": (By.XPATH, "(//input[@id='date'])[1]"),
            "show_patient": (By.XPATH, "//button[contains(text(),'Show Patient')]"),
            "visit_type_column": (By.XPATH, "//div[@col-id='AppointmentType']"),
        }

    def verify_visit_type_dropdown(self):
        """
        /**
        * @Test1
        * @description This method verifies the 'Visit Type' dropdown functionality and validates 'New Visit' patients.
        */
        """
        pass
        assert False,"TODO:Implement verify_visit_type_dropdown"
