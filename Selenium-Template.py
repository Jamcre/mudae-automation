import os, time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()
DISCORD_EMAIL = os.getenv("DISCORD_EMAIL")
DISCORD_PASS = os.getenv("DISCORD_PASS")

options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1200,1200")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")
options.headless = True

driver = uc.Chrome(options=options)
driver.get("https://discord.com/login")

time.sleep(5)
driver.find_element(By.NAME, "email").send_keys(DISCORD_EMAIL)
driver.find_element(By.NAME, "password").send_keys(DISCORD_PASS)
driver.find_element(By.XPATH, '//button[@type="submit"]').click()

# Wait for redirect
try:
    WebDriverWait(driver, 15).until(EC.url_contains("channels"))
    login_success = True
except:
    login_success = False

# Debug results
print(f"Current URL: {driver.current_url}")
print(driver.title)
with open('./GitHub_Action_Results.txt', 'w') as f:
    f.write(f"Login successful? {login_success}\nURL: {driver.current_url}\nTitle: {driver.title}")
