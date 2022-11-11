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
from conftest import wait_class
from conftest import long_wait_class
from conftest import wait_frame_id
from conftest import switch_to_frame
from conftest import switch_to_parent_frame
from conftest import switch_to_default_content
from conftest import exit_loan
from conftest import select_option


@allure.feature('Workflow Tests')
@allure.story('1003 Page 1')
def test_1003_page_1(driver_tests):
    try:
        time.sleep(2)
        page_1 = driver_tests.find_element(By.PARTIAL_LINK_TEXT, '1003 Page 1')
        page_1.click()
        time.sleep(5)

        switch_to_default_content()
        wait_frame_id('contentFrame')
        time.sleep(2)

        content = wait_xpath('//*[@id="wrapper"]/div[2]')
        title = wait_xpath('//*[@id="TitleDiv"]/h1')
        assert title.text == 'URLA PAGE 1'
    except Exception as ex:
        print(ex)
        assert False
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('1003 Page 2')
def test_1003_page_2(driver_tests):
    try:
        time.sleep(2)
        page_2 = driver_tests.find_element(By.PARTIAL_LINK_TEXT, '1003 Page 2')
        page_2.click()
        time.sleep(5)

        switch_to_default_content()
        wait_frame_id('contentFrame')
        time.sleep(2)

        content = wait_xpath('//*[@id="wrapper"]/div[2]')
        title = wait_xpath('//*[@id="TitleDiv"]/h1')
        assert title.text == 'URLA PAGE 2'
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('1003 Page 3')
def test_1003_page_3(driver_tests):
    try:
        time.sleep(2)
        page_3 = driver_tests.find_element(By.PARTIAL_LINK_TEXT, '1003 Page 3')
        page_3.click()
        time.sleep(5)

        switch_to_default_content()
        wait_frame_id('contentFrame')
        time.sleep(2)

        content = wait_xpath('//*[@id="wrapper"]/div[2]')
        title = wait_xpath('//*[@id="TitleDiv"]/h1')
        assert title.text == 'URLA PAGE 3'
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('1003 Page 4')
def test_1003_page_4(driver_tests):
    try:
        time.sleep(2)
        page_4 = driver_tests.find_element(By.PARTIAL_LINK_TEXT, '1003 Page 4')
        page_4.click()
        time.sleep(5)

        switch_to_default_content()
        wait_frame_id('contentFrame')
        time.sleep(2)

        content = wait_xpath('//*[@id="wrapper"]/div[2]')
        title = wait_xpath('//*[@id="TitleDiv"]/h1')
        assert title.text == 'URLA PAGE 4'
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('Corr Funding')
def test_corr_funding(driver_tests):
    try:
        time.sleep(2)
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Corr Funding').click()
        time.sleep(5)

        switch_to_default_content()
        wait_frame_id('contentFrame')
        time.sleep(2)

        content = wait_xpath('//*[@id="CorrespondentFundingAccordion"]/div[2]')
        title = wait_xpath('//*[@id="TitleDiv"]/h1')
        assert title.text == 'CORRESPONDENT FUNDING'
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('Credit Reissue')
def test_credit_reissue_wf(driver_tests):
    try:
        time.sleep(2)
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Credit Reissue').click()
        time.sleep(5)

        switch_to_default_content()
        wait_frame_id('contentFrame')
        time.sleep(2)

        content = wait_id('AccessDiv')
        title = wait_xpath('//*[@id="wrapper"]/div[1]/h1')
        assert title.text == 'CREDIT REISSUE'
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('Doc Manager')
def test_doc_manager(driver_tests):
    try:
        time.sleep(2)
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Doc Manager').click()
        time.sleep(5)
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('Fees')
def test_fees(driver_tests):
    try:
        time.sleep(2)
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Fees').click()
        time.sleep(5)
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('High Cost')
def test_high_cost(driver_tests):
    try:
        time.sleep(2)
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'High Cost').click()
        time.sleep(5)
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('Line of Credit')
def test_line_of_credit(driver_tests):
    try:
        time.sleep(2)
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Line of Credit').click()
        time.sleep(5)
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('Loan Comments')
def test_loan_comments(driver_tests):
    try:
        time.sleep(2)
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Loan Comments').click()
        time.sleep(5)
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('Loan Contacts')
def test_loan_contacts(driver_tests):
    try:
        time.sleep(2)
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Loan Contacts').click()
        time.sleep(5)
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('Loan Summary')
def test_loan_summary(driver_tests):
    try:
        time.sleep(2)
        loan_sum = driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Loan Summary')
        loan_sum.click()
        time.sleep(5)

        switch_to_default_content()
        wait_frame_id('contentFrame')
        time.sleep(2)

        content = wait_id('LoanSummaryDiv')
        title = wait_xpath('//*[@id="LoanSummaryTitleDiv"]/h1')
        assert title.text == 'LOAN SUMMARY'
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('Mortgage Insurance')
def test_mortgage_insurance(driver_tests):
    try:
        time.sleep(2)
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Mortgage Insurance').click()
        time.sleep(5)
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('Points and Fees Test')
def test_points_and_fees_test(driver_tests):
    try:
        time.sleep(2)
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Points and Fees Test').click()
        time.sleep(5)
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('Price / Lock')
def test_price_lock_wf(driver_tests):
    try:
        time.sleep(2)
        pi = driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Price / Lock')
        pi.click()
        time.sleep(5)

        switch_to_default_content()
        wait_frame_id('contentFrame')
        time.sleep(2)

        content = wait_xpath('//*[@id="wrapper"]/div[1]')
        title = wait_xpath('//*[@id="wrapper"]/div[1]/h1')
        assert title.text == 'EXTENDED PRICER'
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('PriceSubmit')
def test_price_submit(driver_tests):
    try:
        time.sleep(2)
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'PriceSubmit').click()
        time.sleep(5)

        switch_to_default_content()
        wait_frame_id('contentFrame')
        time.sleep(2)

        content = wait_xpath('//*[@id="wrapper"]/div[2]')
        title = wait_xpath('//*[@id="TitleDiv"]/h1')
        assert title.text == 'PRICE AND SUBMIT'
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('Quality Control')
def test_quality_control(driver_tests):
    try:
        time.sleep(2)
        qc = driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Quality Control')
        qc.click()
        time.sleep(5)

        switch_to_default_content()
        wait_frame_id('contentFrame')
        time.sleep(2)

        content = wait_xpath('//*[@id="QCFilter"]')
        title = wait_xpath('//*[@id="TitleDiv"]/h1')
        assert title.text == 'QUALITY CONTROL'
    finally:
        exit_loan()


@allure.feature('Workflow Tests')
@allure.story('Run AUS')
def test_run_aus(driver_tests):
    try:
        time.sleep(2)
        driver_tests.find_element(By.PARTIAL_LINK_TEXT, 'Run AUS').click()
        time.sleep(5)
    finally:
        exit_loan()
