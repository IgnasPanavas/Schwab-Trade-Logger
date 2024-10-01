from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

url = os.environ["AUTH_URL"]

schwab_username = os.environ["SCHWAB_USERNAME"]
schwab_password = os.environ["SCHWAB_PASSWORD"]

def get_cookies():

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    iframe = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div[2]/div/div/iframe')
    driver.switch_to.frame(iframe)

    

    try:
        username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#loginIdInput"))
        )
        password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#passwordInput"))
        )

        button = driver.find_element(By.CSS_SELECTOR, "#btnLogin")

    
        username.send_keys(schwab_username)
        password.send_keys(schwab_password)

    except Exception as e:
        print("Element not found within the time limit:", e)
    
    button.click()
    input("Press Enter to quit the browser...")
    driver.implicitly_wait(30)

    username.send_keys()
get_cookies()