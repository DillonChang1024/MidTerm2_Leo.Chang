from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


#s = Service('/Users/dillon.chang/Documents/chrome_driver_file/chromedriver')
# create a new Chrome browser instance
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
#wait = WebDriverWait(driver, 10)

# maximize the browser window
driver.maximize_window()

# navigate to AppWorks School Website
driver.get("https://phptravels.net/api/admin")


#/html/body/div/div[1]/main/div/div/div/div[1]/div/form/div[4]/button

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=text]'))).send_keys(" ")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=password]'))).send_keys("demoadmin")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/main/div/div/div/div[1]/div/form/div[4]/button'))).click()
print('empty email, login fail')
driver.refresh()


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=text]'))).send_keys("admin@phptravels.com")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=password]'))).send_keys(" ")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/main/div/div/div/div[1]/div/form/div[4]/button'))).click()
print('empty password, login fail')
driver.refresh()


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=text]'))).send_keys("admin@phptravels.com")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=password]'))).send_keys("123")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/main/div/div/div/div[1]/div/form/div[4]/button'))).click()
print('wrong password, login fail')
driver.refresh()


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=text]'))).send_keys("admin@phptravels.com")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=password]'))).send_keys("123456")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/main/div/div/div/div[1]/div/form/div[4]/button'))).click()
print('wrong password, login fail')
driver.refresh()


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=text]'))).send_keys("admin@phptravels.com")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=password]'))).send_keys("demoadmin")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/main/div/div/div/div[1]/div/form/div[4]/button'))).click()
print('login success')


##layoutAuthentication_content > main > div > div > div > div.card.card-raised.shadow-10.mt-5.mt-xl-10.mb-4 > div > form > div.form-group.d-flex.align-items-center.justify-content-between.mt-4.mb-0 > button

# Load test data from the spreadsheet
workbook = openpyxl.load_workbook('PHPTravels-TestCases.xlsx')
sheet = workbook['Login']  # Assuming the test cases are in a sheet named 'Login'

# Initialize WebDriver
driver = webdriver.Chrome()  # Use appropriate WebDriver for your browser

# Loop through the test cases
for row in sheet.iter_rows(min_row=2):  # Assuming the test cases start from the second row
    username = row[0].value
    password = row[1].value
    expected_result = row[2].value

    # Open the PHPTravels website
    driver.get('https://phptravels.net/admin')

    # Fill in the login form
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=text]')))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=password]')))

    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the form
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/main/div/div/div/div[1]/div/form/div[4]/button')))
    login_button.click()

    # Perform assertions based on the expected result
    if expected_result == 'Success':
        # Check if login was successful
        success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='content']")))
        assert success_message.text == 'Dashboard'
        print(f"Test case passed for username: {username}")

    elif expected_result == 'Failure':
        # Check if login failed
        error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger']")))
        assert error_message.text == 'Invalid Login Credentials'
        print(f"Test case passed for username: {username}")

# Close the WebDriver
driver.quit()


'''
我有一份excel檔案名稱叫做 PHPTravels-TestCases.xlsx
內容是
第一欄 : Email
分別是 admin@phptravels.com / 空值 / admin@phptravels.com / admin@phptravels.com / test@test.com
第二欄 : Password
分別是 demoadmin / demoadmin / 空值 / 123456 / demoadmin 	
這樣可以登入成功

但我同時要測email為空/Email是錯的/password為空/password是錯的
那我該怎麼設計
請用python+selenium回答

'''