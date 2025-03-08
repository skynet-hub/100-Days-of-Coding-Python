from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https:www.python.org")

# dollar_price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# cents_price = driver.find_element(By.CLASS_NAME, "a-price-fraction")

# print(f"The price is: {dollar_price.text}.{cents_price.text}")

items_time = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
items = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

events = {}
for i in range(len(items)):
    events[i + 1] = {'time': items_time[i].text,
                     'name': items[i].text 
                     }

print(events)

driver.quit()