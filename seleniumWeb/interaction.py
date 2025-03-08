from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://secure-retreat-92358.herokuapp.com/')

# article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')

# print(article_count.text)

# ragner = driver.find_element(By.LINK_TEXT, value='Ragnar Garrett')

# ragner.click() #This will click the anchor tag and follow the link


#Sign up to the appbrewery testing site
name = driver.find_element(By.NAME, value='fName')
lname= driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')

name.send_keys("Mag")
lname.send_keys("Les")
email.send_keys("dave@wltcode.co.za", Keys.ENTER)

