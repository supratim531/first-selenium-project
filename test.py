from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# XPATH = //tagName[@AttributeName="Value"]


url = 'https://goexch777.com/admin'
driver = webdriver.Chrome()
driver.get(url)

sleep(3)
loginButton = driver.find_element(
    By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div[3]/button')
loginButton.click()
adminUsername = driver.find_element(By.XPATH, '//*[@id="input-1"]')
adminPassword = driver.find_element(By.XPATH, '//*[@id="input-2"]')
adminUsername.send_keys('777api')
adminPassword.send_keys('Make1234')
requestLoginButton = driver.find_element(
    By.XPATH, '//*[@id="app"]/div/div/div/div[6]/div[1]/div/div[2]/div/div[1]/form/div[3]/button')
requestLoginButton.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[1]/div[1]/div/div'))
)
driver.get(f'{url}/users/insertuser')

sleep(2)
username = driver.find_element(
    By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/form/div/div[1]/div/div/div[1]/input')
fullName = driver.find_element(
    By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/input')
password = driver.find_element(
    By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/input')
confirmPassword = driver.find_element(
    By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/form/div/div[1]/div/div/div[4]/input')
city = driver.find_element(
    By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/form/div/div[1]/div/div/div[5]/input')
mobile = driver.find_element(
    By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/form/div/div[1]/div/div/div[6]/input')
submitButton = driver.find_element(By.XPATH, '//*[@id="spinner-dark-8"]')
username.send_keys('supratim12345')
fullName.send_keys('Supratim Majumder')
password.send_keys('Supratim531@moon')
confirmPassword.send_keys('Supratim531@moon')
city.send_keys('Kolkata')
mobile.send_keys('9163681672')
userType = Select(driver.find_element(
    By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/form/div/div[2]/div/div/div[2]/select'))
transactionCode = driver.find_element(
    By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/form/div/div[2]/div/div/div[5]/input')
userType.select_by_visible_text('User')
transactionCode.send_keys('828398')
# submitButton.click()


while True:
    pass
