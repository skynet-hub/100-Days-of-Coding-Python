from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Include chrome optioms to keep tabs open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Create a driver and open the browser(visit Tinder)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://tinder.com/')

#Accept privacy T&Cs
accept_btn = driver.find_element(By.XPATH, value='//*[@id="q1648845715"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_btn.click()

#Hit the login in link(anchor tab)
login_link = driver.find_element(By.XPATH, value='//*[@id="q1648845715"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
login_link.click()

time.sleep(1)

#LEt us click on login with Facebook
facebook_log = driver.find_element(By.XPATH, value='//*[@id="q1870186151"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_log.click()

time.sleep(1)

#Switch window to get the window facebook pops in

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(1)

#Log in on facebook
email = driver.find_element(By.NAME, value='email')
passw = driver.find_element(By.NAME, value='pass')
email.send_keys('Your email')
passw.send_keys('your password', Keys.ENTER)

time.sleep(15)

#Switch back to tinder
driver.switch_to.window(base_window)
allow_btn = driver.find_element(By.XPATH, value='//*[@id="q1870186151"]/div/div/div/div/div[3]/button[1]')
allow_btn.click()

time.sleep(1)

#Notification, No
notify_btn = driver.find_element(By.XPATH, value='//*[@id="q1870186151"]/div/div/div/div/div[3]/button//*[@id="q1870186151"]/div/div/div/div/div[3]/button')
notify_btn.click()

#Get the like button
like_btn = driver.find_element(By.XPATH, value='//*[@id="q1648845715"]/div/div[1]/div/div/div/main/div/div/div/div/div[5]/div/div[4]/button')

while True:
    time.sleep(5)
    try:
        like_btn.click()
    except driver.NoSuchElementException:    
        time.sleep(2)



