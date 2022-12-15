# Create requirements: pip freeze > requirements.txt
# Install requirements: pip install -r requirements.txt

# Delete from git cache: git rm --cached "file_path"

# Launch: pytest -v --alluredir reports, pytest -v tests/test_integra_partner_basic.py --alluredir reports
# Report:  allure serve reports

import pytest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from pathlib import Path

test_loan = '9007473'

sleep = 50

file_path = Path.cwd().joinpath('docs', 'kensp.xml')
# Path for Pytest: Path.cwd().joinpath('docs', 'kensp.xml')
# Path for Run: Path.cwd().parent.joinpath('docs', 'kensp.xml')

testurl = 'http://t-partner.admortgage.us/Default.aspx'

username = 'serg.pudikov@admortgage.com'
password = 'Welcome1@'


@pytest.fixture
def driver_init():
    global driver
    driver = webdriver.Chrome()  # executable_path='./driver/xxx.exe'
    driver.maximize_window()
    driver.get(testurl)

    wait_frame_id('contentFrame')
    wait_xpath('//*[@id="EmailAddress"]').send_keys(username)
    wait_xpath('//*[@id="Password"]').send_keys(password)
    wait_xpath('//*[@id="LoginButton"]').click()
    time.sleep(sleep)

    yield driver


@pytest.fixture
def driver_loan_setup(driver_init):
    switch_to_frame(0)
    switch_to_frame(0)
    wait_xpath('//*[@id="ImportLoanButton"]').click()
    switch_to_parent_frame()
    switch_to_parent_frame()
    time.sleep(2)

    switch_to_frame('BusinessChannelSelection')
    select_option('BusinessChannelDropDownList', 'Wholesale')
    switch_to_default_content()

    wait_xpath('//*[@id="btnOkay"]').click()
    time.sleep(2)

    driver.switch_to.frame(1)
    driver.switch_to.frame(0)
    time.sleep(5)
    upload_file = driver.find_element(By.ID, "AjaxFileUpload_Html5InputFile")

    upload_file.send_keys(str(file_path))
    wait_xpath('//*[@id="AjaxFileUpload_UploadOrCancelButton"]').click()
    switch_to_default_content()
    time.sleep(60)

    global loannumber
    loannumber = wait_xpath('//*[@id="Row1"]/td[2]').text

    yield driver
    driver.quit()


@pytest.fixture
def loannumber_import():
    return loannumber


@pytest.fixture
def driver_tests(driver_init):
    switch_to_frame(0)
    switch_to_frame(0)
    wait_xpath('//*[@id="SearchTextBox"]').send_keys(loannumber)  # loannumber  test_loan
    time.sleep(2)
    wait_xpath('//*[@id="SearchButton"]').click()
    switch_to_default_content()
    time.sleep(2)

    switch_to_frame(0)
    switch_to_frame(0)
    switch_to_frame(0)
    time.sleep(2)
    action = ActionChains(driver)
    a = wait_xpath('//*[@id="PipelineRow1"]/td[2]')
    action.double_click(a)
    action.perform()
    switch_to_default_content()
    time.sleep(sleep)

    yield driver
    driver.quit()


def exit_loan():
    driver.switch_to.window(driver.window_handles[0])
    switch_to_default_content()
    driver.refresh()
    switch_to_frame(0)
    switch_to_frame(0)
    wait_xpath('//*[@id="SearchTextBox"]').send_keys(loannumber)  # loannumber  test_loan
    time.sleep(2)
    wait_xpath('//*[@id="SearchButton"]').click()
    switch_to_default_content()
    time.sleep(2)

    switch_to_frame(0)
    switch_to_frame(0)
    switch_to_frame(0)
    time.sleep(2)
    action = ActionChains(driver)
    a = wait_xpath('//*[@id="PipelineRow1"]/td[2]')
    action.double_click(a)
    action.perform()
    switch_to_default_content()
    time.sleep(sleep)

    wait_id('ExitLoanli').click()
    time.sleep(10)


def wait_xpath(xpath):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, xpath)
        )
    )
    return element


def wait_id(id):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, id)
        )
    )
    return element


def wait_class(class_name):
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, class_name)
        )
    )
    return element


def long_wait_class(class_name):
    element = WebDriverWait(driver, 150).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, class_name)
        )
    )
    return element


def wait_frame_id(id):
    WebDriverWait(driver, 30).until(EC.frame_to_be_available_and_switch_to_it((By.ID, id)))


def switch_to_frame(frame_reference):
    driver.switch_to.frame(frame_reference)


def switch_to_parent_frame():
    driver.switch_to.parent_frame()


def switch_to_default_content():
    driver.switch_to.default_content()


def select_option(element_id, text):
    opt = Select(wait_id(element_id))
    opt.select_by_visible_text(text)
