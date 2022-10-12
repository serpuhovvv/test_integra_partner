import allure
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import wait_xpath
from conftest import wait_id
from conftest import wait_frame_id
from conftest import switch_to_frame
from conftest import switch_to_parent_frame
from conftest import switch_to_default_content


@allure.feature('Loan Setup')
@allure.story('Loan setup')
def test_loan_setup(driver_loan_setup, loannumber_import):
    with allure.step('Loan number'):
        allure.attach(loannumber_import)

    wait_xpath(xpath='//*[@id="ExitLoanli"]/a').click()

    print(loannumber_import)


@allure.feature('Basic Tests')
@allure.story('Import Loan')
def test_import_loan(driver_tests):  # loannumber_import
    try:
        loanid = wait_xpath('//*[@id="Row1"]/td[2]')
        assert loanid.text == '9006772'  # change to loannumber
    except:
        assert False
    finally:
        wait_xpath('//*[@id="ExitLoanli"]/a').click()
