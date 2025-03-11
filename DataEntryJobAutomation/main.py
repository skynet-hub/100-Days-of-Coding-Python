import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

zwalio_url = 'https://appbrewery.github.io/Zillow-Clone/'
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLScp-ev4hPDca_x2Ra9PU9GOHGRlez3mdsp64mKsaTDOR_gAQQ/viewform?usp=header'

#MAke a request to zwalio
response = requests.get(zwalio_url)

soup = BeautifulSoup(response.text, 'html.parser')

all_links = soup.select('.property-card-link')
links_clean = [link.get('href') for link in all_links]

raw_prices = soup.select('.PropertyCardWrapper__StyledPriceLine')
prices = [raw.text for raw in raw_prices]

addr = soup.find_all('address')
address = [item.text.strip() for item in addr]

#----------------Selenium to fill out google form----------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(form_url)

#Provide answers
for i in range(len(all_links)):
    time.sleep(5)

    property_addr_field = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_price_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_btn = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    #Filling in info
    property_addr_field.send_keys(address[i])
    property_price_field.send_keys(prices[i])
    link_field.send_keys(links_clean[i])
    submit_btn.click()

    time.sleep(2)
    another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()


#Testing wether code worked to fetch data or not
# print(links_clean) -Worked out well
# print(prices)
# print(address)