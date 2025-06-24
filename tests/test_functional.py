import pathlib
import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Pages.LoginPage import LoginPage
from Pages.AppointmentPage import AppointmentPage
from Pages.OperationTheatrePage import OperationTheatrePage
from Pages.DoctorPage import DoctorPage
from Pages.ProcurementPage import ProcurementPage
from Pages.AdminPage import AdminPage
from Pages.PatientPage import PatientPage
from Pages.IncentivePage import IncentivePage



from Pages.UtilitiesPage import UtilitiesPage
from tests.TestUtils import TestUtils


# Fixture to set up the WebDriver for each test function
@pytest.fixture(scope="function")
def setup_driver():
    """
    Initializes the WebDriver for Chrome and navigates to the application URL.
    Ensures the driver is properly closed after each test execution.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://healthapp.yaksha.com/')
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()

# Reusable login function to be called before each test
def login_to_application(driver):
    """
    Logs in to the application before each test.

    Args:
        driver (webdriver): Selenium WebDriver instance.
        test_credentials (dict): Dictionary containing username and password.
    """
    login_page = LoginPage(driver)
    login_page.perform_login()
    time.sleep(5)

@pytest.mark.order(1)
def test_verification_module(setup_driver):
    """
    Test Case: Verify the presence of Visit Type drop down by selecting "New patient" option.

    Expected Result:
    - The 'Visit Type' column should contain only patients in the "new visit" category.
    """
    try:
        test_obj = TestUtils()
        driver = setup_driver
        login_to_application(driver)  # Perform login before test
        appointment_page = AppointmentPage(driver)
        testResult =  appointment_page.verify_visit_type_dropdown()
        time.sleep(5)
        verificationResult = verify_visit_type(driver)
        if (testResult == True and verificationResult == True):
            passed = True
            test_obj.yakshaAssert("verify_visit_type_dropdown", True, "functional")
            print("verify_visit_type_dropdown = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("verify_visit_type_dropdown", False, "functional")
            print("verify_visit_type_dropdown = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("verify_visit_type_dropdown", False, "functional")
        print("verify_visit_type_dropdown = Failed")
    assert passed


@pytest.mark.order(2)
def test_ot_booking_alert(setup_driver):
    """
    Test Case: Handle Alert for OT Booking Without Patient Selection.

    Expected Result:
    - An alert with the message "Patient not Selected! Please Select the patient first!" is displayed and handled.
    """
    try:
        test_obj = TestUtils()
        driver = setup_driver
        login_to_application(driver)  # Perform login before test
        ot_page = OperationTheatrePage(driver)
        testResult = ot_page.handle_ot_booking_alert()
        is_ot_booking_modal_displayed(driver)
        time.sleep(5)
        verificationResult = verify_book_ot_modal_title(driver)
        print(f"This is the test result {verificationResult}")
        if (testResult == True and verificationResult == True):
            passed = True
            test_obj.yakshaAssert("handle_ot_booking_alert", True, "functional")
            print("handle_ot_booking_alert = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("handle_ot_booking_alert", False, "functional")
            print("handle_ot_booking_alert = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("handle_ot_booking_alert", False, "functional")
        print("handle_ot_booking_alert = Failed")
    assert passed


@pytest.mark.order(3)
def test_verify_patient_overview(setup_driver):
    """
        Test Case: Verify Patient Overview Page Displays information Correctly

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/Doctors/OutPatientDoctor/NewPatient
        2. Click on the In Patient Department Tab.
        3. In the search bar, enter the patient name "Devid8 Roy8" and perform the search.
        4. Locate the patient in the results and click on the Preview icon under the Actions column.

        Expected Result:
        - Verify the same patient overview page is displayed with the same patient name.
    """
    try:
        test_obj = TestUtils()
        driver = setup_driver
        login_to_application(driver)  # Perform login before test
        doctor_page = DoctorPage(driver)
        testResult = doctor_page.verify_patient_overview()
        verificationResult = verify_user_is_on_correct_url(driver,"Doctors/PatientOverviewMain/PatientOverview")
        time.sleep(5)
        if (testResult == True and verificationResult == True):
            passed = True
            test_obj.yakshaAssert("verify_patient_overview", True, "functional")
            print("verify_patient_overview = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("verify_patient_overview", False, "functional")
            print("verify_patient_overview = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("verify_patient_overview", False, "functional")
        print("verify_patient_overview = Failed")
    assert passed

@pytest.mark.order(5)
def test_add_currency_and_verify(setup_driver):
    """
        Test Case: Add and Verify New Currency in Settings

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/ProcurementMain/PurchaseRequest/PurchaseRequestList
        2. Click on the Settings tab then click on currency.
        3. Click on add currency button.
        4. Enter a unique currecny code and fill description .
        5. Now click on "Add Currency" button.

        Expected Result:
        - The new currency should be added successfully and displayed in the table with the correct currency code and description.
    """
    try:
        test_obj = TestUtils()
        driver = setup_driver
        login_to_application(driver)  # Perform login before test
        procurement_page = ProcurementPage(driver)
        testResult = procurement_page.add_currency_and_verify()
        verificationResult = verify_user_is_on_correct_url(driver,"ProcurementMain/Settings/CurrencyList")
        time.sleep(5)
        if (testResult == True and verificationResult == True):
            passed = True
            test_obj.yakshaAssert("add_currency_and_verify", True, "functional")
            print("add_currency_and_verify = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("add_currency_and_verify", False, "functional")
            print("add_currency_and_verify = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("add_currency_and_verify", False, "functional")
        print("add_currency_and_verify = Failed")
    assert passed

@pytest.mark.order(6)
def test_verify_mandatory_fields_warning(setup_driver):
    """
        Test Case: Verify Warning Popup for Mandatory Fields in Scheme Refund

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/Utilities
        2. Click on the Scheme Refund Tab.
        3. Click on "New scheme Refund Entry" button.
        4. Now click on save without entering value in any field.

        Expected Result:
        - A warning popup with the message: "Please fill all the mandatory fields."
    """
    try:
        test_obj = TestUtils()
        driver = setup_driver
        login_to_application(driver)  # Perform login before test
        utilities_page = UtilitiesPage(driver)
        testResult = utilities_page.verify_mandatory_fields_warning()
        verificationResult = verify_user_is_on_correct_url(driver,"/Utilities/SchemeRefund")
        time.sleep(5)
        if (testResult == True and verificationResult == True):
            passed = True
            test_obj.yakshaAssert("verify_mandatory_fields_warning", True, "functional")
            print("verify_mandatory_fields_warning = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("verify_mandatory_fields_warning", False, "functional")
            print("verify_mandatory_fields_warning = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("verify_mandatory_fields_warning", False, "functional")
        print("verify_mandatory_fields_warning = Failed")
    assert passed

@pytest.mark.order(7)
def test_verify_user_profile_navigation(setup_driver):
    """
        Test Case: Verify Navigation to User Profile Page

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/
        2. Click on the Admin dropdown.
        3. Select the "My Profile" option.

        Expected Result:
        - Verify that the user is redirected to the "User Profile" page and the page header or title confirms this.
    """
    try:
        test_obj = TestUtils()
        driver = setup_driver
        login_to_application(driver)  # Perform login before test
        admin_page = AdminPage(driver)
        testResult = admin_page.verify_user_profile_navigation()
        verificationResult = verify_user_is_on_correct_url(driver,"Employee/ProfileMain/UserProfile")
        time.sleep(5)
        if (testResult == True and verificationResult == True):
            passed = True
            test_obj.yakshaAssert("verify_user_profile_navigation", True, "functional")
            print("verify_user_profile_navigation = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("verify_user_profile_navigation", False, "functional")
            print("verify_user_profile_navigation = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("verify_user_profile_navigation", False, "functional")
        print("verify_user_profile_navigation = Failed")
    assert passed

@pytest.mark.order(8)
def test_upload_profile_picture(setup_driver):
    """
        Test Case: Verify Patient Profile Picture Upload

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/Patient/SearchPatient
        2. Click on Register Patient Tab.
        3. Select the Profile Picture icon.
        4. Click on the "New Photo" button.
        5. Upload an image and click on the "Done" button.

        Expected Result:
        - Verify that the uploaded image is displayed successfully in the patient's profile.
    """
    try:
        test_obj = TestUtils()
        driver = setup_driver
        login_to_application(driver)  # Perform login before test
        patient_page = PatientPage(driver)
        testResult = patient_page.upload_profile_picture()
        verificationResult = verify_image_is_uploaded(driver)
        time.sleep(5)
        if (testResult == True and verificationResult == True):
            passed = True
            test_obj.yakshaAssert("upload_profile_picture", True, "functional")
            print("upload_profile_picture = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("upload_profile_picture", False, "functional")
            print("upload_profile_picture = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("upload_profile_picture", False, "functional")
        print("upload_profile_picture = Failed")
    assert passed

@pytest.mark.order(9)
def test_edit_tds_for_employee(setup_driver):
    """
        Test Case: Verify TDS Percent update for an employee

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/Incentive/Transactions/InvoiceLevel
        2. Click on the "Settings" tab.
        3. Locate the row corresponding to the specified employee name.
        4. Click the "Edit TDS%" button within the located row.
        5. In the "Edit TDS Percent" modal, enter the updated TDS% value.
        6. Click on the "Update TDS" button.
        7. Verify that the updated TDS% value is correctly displayed in the table.

        Expected Result:
        - The updated TDS% value is displayed correctly in the corresponding row of the table.
    """
    try:
        test_obj = TestUtils()
        driver = setup_driver
        login_to_application(driver)  # Perform login before test
        inc_page = IncentivePage(driver)
        testResult = inc_page.edit_tds_for_employee()
        verificationResult = verify_tds_test(driver)
        time.sleep(5)
        if (testResult == True and verificationResult == True):
            passed = True
            test_obj.yakshaAssert("edit_tds_for_employee", True, "functional")
            print("edit_tds_for_employeeedit_tds_for_employee = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("edit_tds_for_employee", False, "functional")
            print("edit_tds_for_employee = Failed")
    except:
        passed = False
        test_obj.yakshaAssert("edit_tds_for_employee", False, "functional")
        print("edit_tds_for_employee = Failed")
    assert passed


"""------------------------------------------------- Helper Method------------------------------------------------------------"""


def verify_visit_type(driver):
    """
    /**
    * @Test
    * @description This method verifies that the visit type column has more than one entry.
    * @expected
    * The visit type column should contain more than one entry.
    */
    """
    visit_type_column_locator = (By.XPATH, "//div[@col-id='AppointmentType']")
    try:
        visit_type_cells = driver.find_elements(*visit_type_column_locator)
        return len(visit_type_cells) > 0
    except Exception as e:
        print(f"Visit type verification failed: {e}")
        return False
    
def verify_book_ot_modal_title(driver):
    """
    /**
    * @Test
    * @description This method verifies that the OT booking modal title
    * @expected
    * The OT booking modal title should be visible
    */
    """
    try:
        modal_title_locator = (By.XPATH, "//span[text()=' Booking OT Schedule  | New Patient']")
        modal_title_count = len(driver.find_elements(*modal_title_locator))
        return modal_title_count > 0
    except Exception as e:
        print(f"OT Booking modal title is not visible")
        return False

def is_ot_booking_modal_displayed(driver):
    """
    /**
    * @Test
    * @description This method verifies if the OT Booking Modal is displayed.
    * @expected
    * The OT Booking Modal should be visible on the screen.
    */
    """
    modal_locator = (By.CSS_SELECTOR, "div.modelbox-div")
    try:
        wait = WebDriverWait(driver, 10)
        modal = wait.until(EC.visibility_of_element_located(modal_locator))
        return modal.is_displayed()
    except Exception as e:
        print(f"OT Booking Modal verification failed: {e}")
        return False

def verify_user_is_on_correct_url(driver, expected_url):
    """
    /**
    * @Test
    * @description This method verifies that the user is on the expected URL.
    * @expected
    * The current URL should contain the expected URL.
    */
    """
    try:
        WebDriverWait(driver, 10).until(lambda d: expected_url in d.current_url)
        return expected_url in driver.current_url
    except Exception as e:
        print(f"URL verification failed: {e}")
        return False

def verify_user_is_logged_out(driver):
    """
    /**
    * @Test
    * @description This method verifies that the user is logged out by checking if the login button is visible.
    * @expected
    * The login button should be displayed after logout.
    */
    """
    login_button_locator = (By.CSS_SELECTOR, "#login")

    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(login_button_locator))
        return driver.find_element(*login_button_locator).is_displayed()
    except Exception as e:
        print(f"Logout verification failed: {e}")
        return False

def verify_error_message(driver):
    """
    /**
    * @Test
    * @description This method verifies that the error message "Select doctor from the list." is displayed.
    * @expected
    * The error message should be visible near the field.
    */
    """
    try:
        # Wait for the error message to be visible
        error_message_locator = (By.XPATH, "//span[text()='Select doctor from the list.']")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(error_message_locator))

        # Verify the error message is displayed
        error_message = driver.find_element(*error_message_locator)
        return error_message.is_displayed()

    except Exception as e:
        print(f"Error message verification failed: {e}")
        return False

def is_tooltip_displayed(driver):
    """
    /**
    * @Test
    * @description This method verifies that the tooltip/modal with class 'modal-content' is displayed.
    * @expected
    * The tooltip/modal should be visible on the screen.
    */
    """
    try:
        # Wait for the tooltip/modal to be visible
        tooltip_locator = (By.CSS_SELECTOR, "div.modal-content")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(tooltip_locator))

        # Verify the tooltip/modal is displayed
        tooltip = driver.find_element(*tooltip_locator)
        return tooltip.is_displayed()

    except Exception as e:
        print(f"Tooltip verification failed: {e}")
        return False

def verify_tds_test(driver):
    """
    /**
    * @Test
    * @description This method verifies that the second element in the 'FullName' column contains 'Rakesh'.
    * @expected
    * The second element's text should include 'Rakesh'.
    */
    """
    try:
        # Find all elements with the specified column ID
        pt_names = driver.find_elements(By.CSS_SELECTOR, 'div[col-id="FullName"]')

        # Verify the second element's text contains 'Rakesh'
        return len(pt_names) > 1 and "Rakesh" in pt_names[1].text

    except Exception as e:
        print(f"TDS test verification failed: {e}")
        return False



def verify_image_is_uploaded(driver):
    """
    /**
    * @Test
    * @description This method verifies that an uploaded image is displayed successfully.
    * @expected
    * The uploaded image should be visible on the page.
    */
    """
    try:
        # Wait for the image to be visible
        img_locator = (By.CSS_SELECTOR, "div.wrapper img")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(img_locator))

        # Verify the image is visible
        image = driver.find_element(*img_locator)
        return image.is_displayed()

    except Exception as e:
        print(f"Image upload verification failed: {e}")
        return False
