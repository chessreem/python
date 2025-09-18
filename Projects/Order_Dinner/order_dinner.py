# This script only works for PwC IL employees trying to order dinner via Google Forms.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Google Form Site for ordering dinner
DINNER_URL = 'www.example.com'

# Employee email for Google Authentication
AUTH_EMAIL = 'email@example.com'

# Keep chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(DINNER_URL)

# Fill in Google Workspace identity
email_field = driver.find_element(By.ID, "identifierId")
email_field.send_keys(AUTH_EMAIL, Keys.ENTER)
time.sleep(6)

# Fill in pwc login credentials
driver.find_element(By.ID, "initEmail").send_keys(AUTH_EMAIL, Keys.ENTER)
time.sleep(8)

# Click "Confirm"
driver.find_element(By.CSS_SELECTOR, "button.VfPpkd-LgbsSe").click()
time.sleep(5)

# Select email, floor 32, and click "Next"
driver.find_element(By.ID, "i5").click()
driver.find_element(By.ID, "i12").click()
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div').click()
time.sleep(2)

choice = input("toast, kit or sandwich? ")
if choice == "toast":
    # Select tuna toast
    driver.find_element(By.ID, "i11").click()
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]').click()
    time.sleep(2)
    driver.find_element(By.ID, "i8").click()
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div[1]/div[2]').click()
    time.sleep(4)

if choice == "kit":
    # Select personal kit
    driver.find_element(By.ID, "i20").click()
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]').click()
    time.sleep(2)
    driver.find_element(By.ID, "i11").click()
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]').click()

    bar = input("mars or snickers? ")
    if bar == "mars":
        # mars
        driver.find_element(By.ID, "i8").click()
    if bar == "snickers":
        # snickers
        driver.find_element(By.ID, "i11").click()
    # coke
    driver.find_element(By.ID, "i21").click()
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div[1]/div[2]').click()
    time.sleep(4)

if choice == "sandwich":
    # Select sandwich
    driver.find_element(By.ID, "i5").click()
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]').click()
    time.sleep(2)

    fish = input("tuna or salmon? ")
    bread = input("which bread, white or brown? ")
    if fish == "tuna":
        if bread == "white":
            # Select tuna and white bread
            driver.find_element(By.ID, "i20").click()
            driver.find_element(By.ID, "i27").click()
            driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div[1]/div[2]').click()
            time.sleep(4)

        if bread == "brown":
            # Select tuna and brown bread
            driver.find_element(By.ID, "i20").click()
            driver.find_element(By.ID, "i30").click()
            driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div[1]/div[2]').click()
            time.sleep(4)

    if fish == "salmon":
        if bread == "white":
            # Select salmon and white bread
            driver.find_element(By.ID, "i11").click()
            driver.find_element(By.ID, "i27").click()
            driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div[1]/div[2]').click()
            time.sleep(4)

        if bread == "brown":
            # Select salmon and brown bread
            driver.find_element(By.ID, "i11").click()
            driver.find_element(By.ID, "i30").click()
            driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div[1]/div[2]').click()
            time.sleep(4)

driver.quit()