import allure
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import wait_xpath
from conftest import wait_frame_id
from conftest import switch_to_frame
from conftest import switch_to_parent_frame
from conftest import switch_to_default_content


@allure.feature('Loan Setup')
@allure.story('Loan setup')
def test_loan_setup(driver_loan_setup):
    switch_to_frame(0)
    switch_to_frame(0)
    wait_xpath('//*[@id="ImportLoanButton"]').click()
    switch_to_default_content()

    wait_frame_id('BusinessChannelSelection')
    wait_xpath('//*[@id="BusinessChannelDropDownList"]').click()
    wait_xpath('//*[@id="BusinessChannelDropDownList"]/option[3]').click()
    switch_to_default_content()

    wait_xpath('//*[@id="btnOkay"]').click()

    switch_to_frame(1)
    switch_to_frame(0)
    upload_file = wait_xpath('//*[@id="AjaxFileUpload_Html5InputFile"]')
    upload_file.send_keys('./docs/kensp.xml')
    wait_xpath('//*[@id="AjaxFileUpload_UploadOrCancelButton"]').click()
    switch_to_default_content()

    global loannumber
    loannumber = wait_xpath('//*[@id="Row1"]/td[2]').text

    with allure.step('Loan number'):
        allure.attach(loannumber)

    wait_xpath(xpath='//*[@id="ExitLoanli"]/a').click()

    print(loannumber)


@allure.feature('Basic Tests')
@allure.story('Import Loan')
def test_import_loan(driver_tests):
    time.sleep(5)
    try:
        loanid = wait_xpath('//*[@id="Row1"]/td[2]')
        assert loanid.text == '9006745'  # change to loannumber
    except:
        assert False
    finally:
        wait_xpath('//*[@id="ExitLoanli"]/a').click()
