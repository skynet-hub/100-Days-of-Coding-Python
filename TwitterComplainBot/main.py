from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TWITTER_EMAIL = 'Your email'
TWITTER_PASSWORD = 'Your password'
UP_TIME = None
DOWN_TIME = None

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = DOWN_TIME
        self.up = UP_TIME

    def get_internet_speed(self) -> None:
        self.driver.get('https://www.speedtest.net/')

        time.sleep(10)

        accept_btn = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        accept_btn.click()

        time.sleep(10)

        go_btn = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a')  
        go_btn.click()  

        time.sleep(60)
        down_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        up_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(f'Down speed: {down_speed.text}')
        print(f'Up speed: {up_speed.text}')

    def tweet_at_provider(self) -> None:
        self.driver.get('https://x.com')

        time.sleep(5)

        sing_in_btn = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/a')
        sing_in_btn.click()

        time.sleep(2)

        email_field = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        email_field.send_keys('davidlesaomako@gmail.com', Keys.ENTER)

        time.sleep(2)
        passw_field = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        passw_field.send_keys('P@ssword123', Keys.ENTER)

        time.sleep(3)

        tweet = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f'down speed {self.down}, up speed: {self.up}', Keys.ENTER)

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()    