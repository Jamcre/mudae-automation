import os
import time
import chromedriver_autoinstaller

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
print(f'{DISCORD_EMAIL} + {DISCORD_PASS}')
wait = WebDriverWait(driver, 10)  # Explicit wait
time.sleep(2)
email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
pass_field = driver.find_element(by=By.NAME, value="password")
time.sleep(2)
email_field.send_keys(DISCORD_EMAIL)
pass_field.send_keys(DISCORD_PASS)
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-mount']/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]")))
submit_button.click()
time.sleep(3)

print(f'Current URL: {driver.current_url}')

# Navigate to Discord Channel
wait.until(EC.url_contains("discord.com/channels"))
driver.get(DISCORD_CHANNEL)
# Text Input Automation
channel_text_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Message #mudae-s3']")))
channel_text_field.send_keys('$tu')
channel_text_field.send_keys(Keys.ENTER)
time.sleep(2) # Delay for Bot to register
# Send next messages
channel_text_field.send_keys('$daily')
channel_text_field.send_keys(Keys.ENTER)
time.sleep(2) # Delay for Bot to register
channel_text_field.send_keys('$dk')
channel_text_field.send_keys(Keys.ENTER)
time.sleep(2) # Delay for Bot to register

print(f'Current URL: {driver.current_url}')


print(driver.title)
with open('./GitHub_Action_Results.txt', 'w') as f:
    f.write(f"This was written with a GitHub action {driver.title}")

