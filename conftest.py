# pip install pytest
# pip install selenium
# pip install pytest-selenium
# pip install requests
# pip install allure-pytest
# pip install pytest-xdist

# delete from git cache: git rm --cached "file_path"

# Launch: pytest --alluredir reports
# Report:  allure serve reports

import pytest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


@pytest.fixture
def driver_init():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()


@pytest.fixture
def driver_loan_setup(driver_init):
    driver.get('http://t-partner.admortgage.us/Default.aspx')

    wait_frame_id('contentFrame')

    username = wait_xpath('//*[@id="EmailAddress"]')
    password = wait_xpath('//*[@id="Password"]')
    login = wait_xpath('//*[@id="LoginButton"]')

    username.send_keys('serg.pudikov@admortgage.com')
    password.send_keys('Welcome1@')
    login.click()
    time.sleep(5)

    switch_to_frame(0)
    switch_to_frame(0)
    wait_xpath('//*[@id="ImportLoanButton"]').click()
    switch_to_parent_frame()
    switch_to_parent_frame()
    time.sleep(2)

    switch_to_frame('BusinessChannelSelection')
    wait_xpath('//*[@id="BusinessChannelDropDownList"]').click()
    wait_xpath('//*[@id="BusinessChannelDropDownList"]/option[3]').click()
    switch_to_default_content()

    wait_xpath('//*[@id="btnOkay"]').click()
    time.sleep(2)

    driver.switch_to.frame(1)
    driver.switch_to.frame(0)
    time.sleep(5)
    upload_file = driver.find_element(By.ID, "AjaxFileUpload_Html5InputFile")
    upload_file.send_keys('C:/Users/serg.pudikov/PycharmProjects/test_integra_partner/docs/kensp.xml')
    wait_xpath('//*[@id="AjaxFileUpload_UploadOrCancelButton"]').click()
    switch_to_default_content()

    global loannumber
    loannumber = wait_xpath('//*[@id="Row1"]/td[2]').text

    yield driver
    driver.close()


@pytest.fixture
def loannumber_import():
    return loannumber


@pytest.fixture
def driver_tests(driver_init):

    driver.get('http://t-partner.admortgage.us/Default.aspx')

    wait_frame_id('contentFrame')
    username = wait_xpath('//*[@id="EmailAddress"]')
    password = wait_id('Password')
    login = wait_xpath('//*[@id="LoginButton"]')

    username.send_keys('serg.pudikov@admortgage.com')
    password.send_keys('Welcome1@')
    login.click()
    time.sleep(5)

    switch_to_frame(0)
    switch_to_frame(0)
    wait_xpath('//*[@id="SearchTextBox"]').send_keys('9006772')  # Change to loannumber
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
    time.sleep(2)

    yield driver
    driver.close()


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


def wait_frame_id(id):
    WebDriverWait(driver, 30).until(EC.frame_to_be_available_and_switch_to_it((By.ID, id)))


def switch_to_frame(frame_reference):
    driver.switch_to.frame(frame_reference)


def switch_to_parent_frame():
    driver.switch_to.parent_frame()


def switch_to_default_content():
    driver.switch_to.default_content()
