import os
import time
import undetected_chromedriver as uc
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

# Load credentials
load_dotenv()
DISCORD_EMAIL = os.getenv("DISCORD_EMAIL")
DISCORD_PASS = os.getenv("DISCORD_PASS")

# Setup Chrome options
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1200,1200")
options.headless = True  # Important for GitHub Actions

# Launch browser
driver = uc.Chrome(options=options)

# Login flow
driver.get("https://discord.com/login")
time.sleep(5)

email_field = driver.find_element(By.NAME, 'email')
pass_field = driver.find_element(By.NAME, 'password')

email_field.send_keys(DISCORD_EMAIL)
pass_field.send_keys(DISCORD_PASS)

submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
submit_button.click()

time.sleep(5)

# Output result
print(f"Current URL: {driver.current_url}")
print(driver.title)

with open('./GitHub_Action_Results.txt', 'w') as f:
    f.write(f"Logged in to Discord? {driver.current_url != 'https://discord.com/login'} | Page Title: {driver.title}")
