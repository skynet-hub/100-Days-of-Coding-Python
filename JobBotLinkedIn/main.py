from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Let us set up browser option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Let us get open the browser
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=4161017542&f_AL=true&f_E=1%2C2&geoId=101069296&keywords=software%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R')

sign_in_button = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_button.click()

time.sleep(5)

user_name = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
password = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')

#Send keys and press enter to login
user_name.send_keys('Your email')
password.send_keys('Your password', Keys.ENTER)

time.sleep(5)

easy_apply_button = driver.find_element(By.XPATH, value='//*[@id="ember53"]')
easy_apply_button.click() #Click the easy apply to access the form

time.sleep(3)

number_field = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4161017542-15902720852-phoneNumber-nationalNumber"]')
number_field.send_keys('Your number', Keys.ENTER)

next_btn_1 = driver.find_element(By.XPATH, value='//*[@id="ember246"]')
next_btn_1.click()

time.sleep(1)

next_btn_2 = driver.find_element(By.XPATH, value='//*[@id="ember246"]')
next_btn_2.click() #Next CV will always be available

#Last phase of the form

first_field = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4161017542-15902720836-numeric"]')
second_field = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4161017542-15902720828-numeric"]')
third_field = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4161017542-15902720820-numeric"]')

#Let us now send keys to the fields and select enter
first_field.send_keys('0')
second_field.send_keys('0')
third_field.send_keys('0')

time.sleep(1)

#Let us now hit the review button and move forward
review_btn = driver.find_element(By.XPATH, value='//*[@id="ember256"]')
review_btn.click()

#Time to complete the process ie submit
time.sleep(1)

submit_btn = driver.find_element(By.XPATH, value='//*[@id="ember266"]')
submit_btn.click()

#Doing it for multiple jobs is a bit tricky, there are no one field applications anymore.
