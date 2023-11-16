from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

PROMISED_DOWN = 50
PROMISED_UP = 5
CHROME_DRIVER_PATH = "/Users/charliewelch/Downloads/chromedriver_mac_arm64/chromedriver"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")

        self.driver.find_element(By.CLASS_NAME, "js-start-test").click()
        self.driver.implicitly_wait(60)
        self.driver.find_element(By.CSS_SELECTOR, ".close-btn.pure-button").click()
        download = self.driver.find_element(
            By.CSS_SELECTOR, ".result-data-large.download-speed"
        ).text
        upload = self.driver.find_element(
            By.CSS_SELECTOR, ".result-data-large.upload-speed"
        )
        self.down = download
        self.up = upload

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
        )
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'
        )

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
        )

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]'
        )
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


process = InternetSpeedTwitterBot()
process.get_internet_speed()
process.tweet_at_provider()
