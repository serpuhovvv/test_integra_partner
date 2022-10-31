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
from pathlib import Path


@allure.feature('Loan Setup')
@allure.story('Loan setup')
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


