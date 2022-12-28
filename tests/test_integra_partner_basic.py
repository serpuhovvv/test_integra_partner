import sys
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from conftest import wait_xpath
from conftest import wait_id
from conftest import wait_class
from conftest import long_wait_class
from conftest import wait_frame_id
from conftest import switch_to_frame
from conftest import switch_to_parent_frame
from conftest import switch_to_default_content
from conftest import exit_loan
from conftest import select_option
from conftest import log_init
from conftest import log_write
from conftest import log_passed
from conftest import log_failed
import datetime

log_init(dt=datetime.datetime.now())


@allure.feature('Basic Tests')
@allure.story('Create Loan')
def test_create_loan(driver_init):
    try:
        switch_to_frame(0)
        switch_to_frame(0)
        wait_id('CreateLoanButton').click()
        switch_to_parent_frame()
        switch_to_parent_frame()
        time.sleep(2)

        wait_xpath('/html/body/div[2]/table/tbody/tr/td/div/div[4]/span[1]').click()
        time.sleep(2)

        wait_frame_id('dialogframe')

        wait_id('BusinessChannelDropDownList')

        log_passed('Create Loan', 'New Loan was successfully created')

    except Exception:
        with allure.step('Error screenshot'):
            allure.attach(driver_init.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print(str(sys.exc_info()))
        log_failed('Create Loan', (str(sys.exc_info())))
        assert False

    finally:
        driver_init.quit()


@allure.feature('Basic Tests')
@allure.story('Import Loan')
def test_import_loan(driver_loan_setup, loannumber_import):
    try:
        loanid = wait_xpath('//*[@id="Row1"]/td[2]')
        with allure.step('Loan Number'):
            allure.attach(loannumber_import, name='loannumber', attachment_type=AttachmentType.TEXT)
        print(loannumber_import)
        assert loanid.text == loannumber_import

        log_passed('Import Loan', 'The loan was successfully imported and the loan number is ' + loannumber_import)

    except Exception:
        with allure.step('Error screenshot'):
            allure.attach(driver_loan_setup.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print((str(sys.exc_info())))
        log_failed('Import Loan', (str(sys.exc_info())))
        assert False

    finally:
        exit_loan()


@allure.feature('Basic Tests')
@allure.story('Price/Lock')
def test_price_lock(driver_tests):
    try:
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Price / Lock').click()
        time.sleep(2)

        switch_to_frame(0)
        switch_to_frame(0)

        select_option('LoanTypeDropDownList', 'Conventional')
        time.sleep(1)

        select_option('DocTypeDropDownList', 'CONV/GOV/JUMBO: 1-2Y Full Doc')
        time.sleep(1)

        wait_id('InvalidProductsCheckBox').click()
        time.sleep(1)

        wait_id('FICONumberBox').send_keys('639')
        time.sleep(1)

        switch_to_default_content()

        wait_frame_id('contentFrame')

        wait_id('ProductsPane_header').click()
        time.sleep(5)

        switch_to_default_content()

        switch_to_frame(0)
        switch_to_frame(1)

        wait_xpath('/html/body/form/div[3]/div[1]/div/div[4]/div/div[2]/div[14]/table/tbody/tr[2]/td[2]/a/i').click()
        time.sleep(10)

        switch_to_default_content()

        product_status = wait_xpath('//*[@id="Row22"]/td[2]')
        assert product_status.text == 'Valid'

        log_passed('Price/Lock', 'Price/Lock set up and product status is valid')

    except Exception:
        with allure.step('Error screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print((str(sys.exc_info())))
        log_failed('Price/Lock', (str(sys.exc_info())))
        assert False

    finally:
        exit_loan()


@allure.feature('Basic Tests')
@allure.story('Credit Reissue')
def test_credit_reissue(driver_tests):
    try:
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Credit Reissue').click()
        time.sleep(2)

        wait_frame_id('contentFrame')

        select_option('CreditProviderDropDown', 'UNIVERSAL CREDIT SERVICES [ML]')
        time.sleep(2)

        wait_id('customCrLogin').send_keys('SergPu')
        wait_id('customCrPassword').send_keys('Loan321@')
        time.sleep(2)

        wait_id('ReferenceNumberOverrideCheckBox').click()
        wait_id('CreditReferenceWebText').send_keys('26722153')

        wait_id('AccessButton').click()

        switch_to_default_content()

        long_wait_class('dialog-confirm').click()
        time.sleep(5)

        wait_frame_id('contentFrame')

        wait_id('CreditButton').click()
        time.sleep(5)

        switch_to_default_content()

        wait_frame_id('dialogframe')

        wait_xpath('//*[@id="AUSReportWidgetGridView_GridView"]/tbody/tr[2]').click()
        time.sleep(5)

        driver_tests.switch_to.window(driver_tests.window_handles[1])
        driver_tests.save_screenshot('../screenshots/credit reissue/credit_reissue_screenshot.png')
        with allure.step('Credit Reissue Screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='credit_reissue_screenshot',
                          attachment_type=AttachmentType.PNG)
        driver_tests.close()

        log_passed('Credit Reissue', 'Credit Reissue successfully done')

    except Exception:
        with allure.step('Error screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print((str(sys.exc_info())))
        log_failed('Credit Reissue', (str(sys.exc_info())))
        assert False

    finally:
        exit_loan()


@allure.feature('Basic Tests')
@allure.story('AUS')
def test_aus(driver_tests):
    try:
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Run AUS').click()
        time.sleep(2)

        wait_frame_id('contentFrame')

        select_option('AusSelectionDropDown', 'Both DU and LPA')
        time.sleep(2)

        select_option('CreditProviderDropDown', 'UNIVERSAL CREDIT SERVICES [ML]')
        time.sleep(2)

        wait_id('customCrLogin').send_keys('SergPu')
        wait_id('customCrPassword').send_keys('Loan321@')
        time.sleep(2)

        wait_id('AccessButton').click()

        switch_to_default_content()

        long_wait_class('dialog-confirm').click()
        time.sleep(5)

        # DU 1

        wait_frame_id('contentFrame')

        wait_id('FindingsButton').click()

        switch_to_default_content()

        wait_frame_id('dialogframe')

        wait_xpath('//*[@id="AUSReportWidgetGridView_GridView"]/tbody/tr[2]').click()
        time.sleep(2)

        driver_tests.switch_to.window(driver_tests.window_handles[1])
        driver_tests.save_screenshot('../screenshots/aus/du_1_screenshot.png')
        with allure.step('DU 1 Screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='du_1_screenshot',
                          attachment_type=AttachmentType.PNG)
        driver_tests.close()
        time.sleep(2)

        driver_tests.switch_to.window(driver_tests.window_handles[0])

        switch_to_default_content()

        # LPA 1

        wait_frame_id('contentFrame')

        wait_id('FindingsButton').click()

        switch_to_default_content()

        wait_frame_id('dialogframe')

        wait_xpath('//*[@id="AUSReportWidgetGridView_GridView"]/tbody/tr[3]').click()
        time.sleep(2)

        driver_tests.switch_to.window(driver_tests.window_handles[1])
        driver_tests.save_screenshot('../screenshots/aus/lpa_1_screenshot.png')
        with allure.step('LPA 1 Screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='lpa_1_screenshot',
                          attachment_type=AttachmentType.PNG)
        driver_tests.close()

        driver_tests.switch_to.window(driver_tests.window_handles[0])

        switch_to_default_content()

        # DU 2

        wait_frame_id('contentFrame')

        wait_id('CreditButton').click()

        switch_to_default_content()

        wait_frame_id('dialogframe')

        wait_xpath('//*[@id="AUSReportWidgetGridView_GridView"]/tbody/tr[2]').click()
        time.sleep(2)

        driver_tests.switch_to.window(driver_tests.window_handles[1])
        driver_tests.save_screenshot('../screenshots/aus/du_2_screenshot.png')
        with allure.step('DU 2 Screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='du_2_screenshot',
                          attachment_type=AttachmentType.PNG)
        driver_tests.close()

        driver_tests.switch_to.window(driver_tests.window_handles[0])

        switch_to_default_content()

        # LPA 2

        wait_frame_id('contentFrame')

        wait_id('CreditButton').click()

        switch_to_default_content()

        wait_frame_id('dialogframe')

        wait_xpath('//*[@id="AUSReportWidgetGridView_GridView"]/tbody/tr[3]').click()
        time.sleep(2)

        driver_tests.switch_to.window(driver_tests.window_handles[1])
        driver_tests.save_screenshot('../screenshots/aus/lpa_2_screenshot.png')
        with allure.step('LPA 2 Screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='lpa_2_screenshot',
                          attachment_type=AttachmentType.PNG)
        driver_tests.close()

        driver_tests.switch_to.window(driver_tests.window_handles[0])

        switch_to_default_content()

        log_passed('AUS', 'AUS Request completed')

    except Exception:
        with allure.step('Error screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print((str(sys.exc_info())))
        log_failed('AUS', (str(sys.exc_info())))
        assert False

    finally:
        exit_loan()


@allure.feature('Basic Tests')
@allure.story('Mortgage Insurance')
def test_mortgage_insurance(driver_tests):
    try:
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Mortgage Insurance').click()
        time.sleep(2)

        wait_frame_id('contentFrame')

        select_option('MIReferenceDropDown', 'MIBestEx - MI Best Execution')
        time.sleep(2)

        wait_id('RequestMultiQuoteButton').click()
        time.sleep(2)

        switch_to_default_content()

        wait_frame_id('dialogframe')

        wait_id('InsurerGridView_InsurerGridView_GridView_ctl02_ctl00').click()
        wait_id('InsurerGridView_InsurerGridView_GridView_ctl03_ctl00').click()
        wait_id('InsurerGridView_InsurerGridView_GridView_ctl04_ctl00').click()
        wait_id('InsurerGridView_InsurerGridView_GridView_ctl05_ctl00').click()
        wait_id('InsurerGridView_InsurerGridView_GridView_ctl06_ctl00').click()
        time.sleep(2)

        wait_id('RequestQuoteButton').click()
        time.sleep(2)

        switch_to_default_content()

        wait_id('btnCancel').click()

        wait_frame_id('dialogframe')

        long_wait_class('grid_Item')

        switch_to_default_content()

        wait_id('btnCancel').click()

        driver_tests.save_screenshot('../screenshots/mi/mi_screenshot.png')
        with allure.step('MI Screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='mi_screenshot',
                          attachment_type=AttachmentType.PNG)

        log_passed('Mortgage Insurance', 'MI completed')

    except Exception:
        with allure.step('Error screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print((str(sys.exc_info())))
        log_failed('Mortgage Insurance', (str(sys.exc_info())))
        assert False

    finally:
        exit_loan()


@allure.feature('Basic Tests')
@allure.story('Appraisal')
def test_appraisal(driver_tests):
    try:
        wait_id('Appraisal').click()
        time.sleep(5)

        driver_tests.switch_to.window(driver_tests.window_handles[1])

        assert driver_tests.current_url == 'https://admortgage.spurams.com/login.aspx?ReturnUrl=%2f'

        log_passed('Appraisal', 'Appraisal request completed')

    except Exception:
        with allure.step('Error screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print((str(sys.exc_info())))
        log_failed('Appraisal', (str(sys.exc_info())))
        assert False

    finally:
        exit_loan()


@allure.feature('Basic Tests')
@allure.story('Appraisal Center')
def test_appraisal_center(driver_tests):
    try:
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Appraisal Center').click()
        time.sleep(2)

        wait_frame_id('contentFrame')

        wait_id('ServiceLoginClientIdTextEdit').send_keys('juliya.suleymanova@admortgage.com')
        wait_id('ServiceLoginPasswordTextEdit').send_keys('Welcome1@')
        wait_id('ServiceLoginButton').click()
        time.sleep(10)

        a = wait_xpath('//*[@id="ExistingAppraisalOrdersGridView_GridView"]/tbody/tr[2]/td[2]').text
        url1 = driver_tests.current_url

        wait_id('CreateNewOrderAccordionPane_header').click()
        time.sleep(5)
        wait_id('OrderNewApprisalButton').click()

        switch_to_default_content()

        wait_xpath('/html/body/div[2]/table/tbody/tr/td/div/div[4]/span[1]').click()
        time.sleep(2)
        wait_class('dialog-confirm').click()

        wait_frame_id('contentFrame')

        wait_id('ExistingOrdersAccordionPane_header').click()

        b = wait_xpath('//*[@id="ExistingAppraisalOrdersGridView_GridView"]/tbody/tr[2]/td[2]').text

        wait_xpath('//*[@id="ExistingAppraisalOrdersGridView_GridView"]/tbody/tr[2]').click()

        wait_xpath('//*[@id="ExistingAppraisalOrdersGridView_GridView"]/tbody/tr[2]').click()

        ActionChains(driver_tests).double_click(
            wait_xpath('//*[@id="ExistingAppraisalOrdersGridView_GridView"]/tbody/tr[2]')).perform()
        time.sleep(5)

        driver_tests.switch_to.window(driver_tests.window_handles[1])

        url2 = driver_tests.current_url

        assert a != b \
               and url1 != url2

        log_passed('Appraisal Center', 'Appraisal Center request works and leads to the correct web page')

    except Exception:
        with allure.step('Error screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print((str(sys.exc_info())))
        log_failed('Appraisal Center', (str(sys.exc_info())))
        assert False

    finally:
        exit_loan()


@allure.feature('Basic Tests')
@allure.story('Fees')
def test_fees(driver_tests):
    try:
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Fees').click()
        time.sleep(2)

        wait_frame_id('contentFrame')

        wait_id('PreviewFees').click()
        time.sleep(10)

        driver_tests.switch_to.window(driver_tests.window_handles[1])

        driver_tests.save_screenshot('../screenshots/fees/fees_screenshot.png')
        with allure.step('Fees Screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='fees_screenshot',
                          attachment_type=AttachmentType.PNG)

        log_passed('Fees', 'Fees submitted')

    except Exception:
        with allure.step('Error screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print((str(sys.exc_info())))
        log_failed('Fees', (str(sys.exc_info())))
        assert False

    finally:
        exit_loan()


@allure.feature('Basic Tests')
@allure.story('Submit to A&D')
def test_submit_to_ad(driver_tests):
    try:
        wait_frame_id('contentFrame')

        select_option('BorrowerInfoBor1_VeteranStatusSelection', 'No')
        time.sleep(2)

        switch_to_default_content()

        driver_tests.find_element(By.PARTIAL_LINK_TEXT, '1003 Page 2').click()
        time.sleep(10)

        wait_id('Submit Loan').click()
        time.sleep(2)

        wait_id('btnOkay').click()

        log_passed('Submit to A&D', ' ')

    except Exception:
        with allure.step('Error screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print((str(sys.exc_info())))
        log_failed('Submit to A&D', (str(sys.exc_info())))
        assert False

    finally:
        exit_loan()
