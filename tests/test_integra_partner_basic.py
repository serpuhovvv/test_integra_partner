import os
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
from pathlib import Path


@allure.feature('Basic Tests')
@allure.story('Import Loan')
def test_loan_setup(driver_loan_setup, loannumber_import):

    try:
        loanid = wait_xpath('//*[@id="Row1"]/td[2]')
        with allure.step('Loan Number'):
            allure.attach(loannumber_import, name='loannumber', attachment_type=AttachmentType.TEXT)
        print(loannumber_import)
        assert loanid.text == loannumber_import

    except Exception as ex:
        with allure.step('Error screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print(ex)
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

    except Exception as ex:
        with allure.step('Error screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print(ex)
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

    except Exception as ex:
        with allure.step('Error screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print(ex)
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

    except Exception as ex:
        with allure.step('Error screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print(ex)
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

    except Exception as ex:
        with allure.step('Error screenshot'):
            allure.attach(driver_tests.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print(ex)
        assert False

    finally:
        exit_loan()


@allure.feature('Basic Tests')
@allure.story('EDOC')
def test_edoc(driver_edoc):

    try:
        searchbar = WebDriverWait(driver_edoc, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":r4t:"]')))
        searchbar.click()
        searchbar.send_keys('9007239')
        result = WebDriverWait(driver_edoc, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popover"]/div[3]/div/a/div')))
        ActionChains(driver_edoc)\
            .click_and_hold(result)\
            .release(result)\
            .perform()

    except Exception as ex:
        with allure.step('Error screenshot'):
            allure.attach(driver_edoc.get_screenshot_as_png(), name='error_screenshot',
                          attachment_type=AttachmentType.PNG)
        print(ex)
        assert False
