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
        time.sleep(30)

        switch_to_default_content()

        time.sleep(2)
        wait_class('dialog-confirm').click()
        time.sleep(5)

        wait_frame_id('contentFrame')

        wait_id('CreditButton').click()
        time.sleep(5)

        switch_to_default_content()

        wait_frame_id('dialogframe')

        wait_xpath('//*[@id="AUSReportWidgetGridView_GridView"]/tbody/tr[2]').click()
        time.sleep(5)

        driver_tests.switch_to.window(driver_tests.window_handles[1])
        driver_tests.save_screenshot('../screenshots/credit_reissue_screenshot.png')
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
