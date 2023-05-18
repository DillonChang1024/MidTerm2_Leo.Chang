from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

service = Service(executable_path=ChromeDriverManager().install())
excelPath = r'PHPTravels-TestCases.xlsx'
df = pd.read_excel(excelPath)

for row in df.itertuples():
    email = row.Email
    pwd = row.Password
    excel_result = row.Result

    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    try:
        driver.get('https://phptravels.net/api/admin')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"] input[name="email"]'))).send_keys(email)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="mb-2"] input[name="password"]'))).send_keys(pwd)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*//span[contains(text(),"Login")]//parent::button'))).click()
        try:
            text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="text-muted"]'))).text
            if text == 'Sales overview & summary':
                print("success")
        except:
            print("failed")
    finally:
        driver.quit()