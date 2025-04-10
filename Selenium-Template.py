import os
import time
import chromedriver_autoinstaller

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 800))  
display.start()

# Constants
load_dotenv()
DISCORD_EMAIL = os.getenv("DISCORD_EMAIL")
DISCORD_PASS = os.getenv("DISCORD_PASS")
DISCORD_CHANNEL = "https://discord.com/channels/756710284298551346/1225299689994321951"

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    

# Add your options as needed    
options = [
    # Define window size here
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
    "--headless",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    '--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

# Navigate and Log into Discord
driver.get("https://discord.com/login")


time.sleep(3)
email_field = driver.find_element(by=By.NAME, value='email')
print(email_field)
pass_field = driver.find_element(by=By.NAME, value='password')
print(pass_field)
time.sleep(2)
email_field.send_keys(DISCORD_EMAIL)
pass_field.send_keys(DISCORD_PASS)
submit_button = driver.find_element(by=By.XPATH, value='//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]')
print(submit_button)
submit_button.click()
time.sleep(3)

print(f'Current URL: {driver.current_url}')

print(driver.title)
with open('./GitHub_Action_Results.txt', 'w') as f:
    f.write(f"This was written with a GitHub action {driver.title}")

