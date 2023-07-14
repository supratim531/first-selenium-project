from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# XPATH = //tagName[@AttributeName="Value"]


url = 'https://goexch777.com/admin'
driver = webdriver.Chrome()
driver.get(url)

sleep(2)
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
driver.get(f'{url}/users')

sleep(2)
searchUsernameBox = driver.find_element(
    By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/form/div[1]/input')
loadButton = driver.find_element(By.XPATH, '//*[@id="submit"]')
searchUsernameBox.send_keys('sayan12345')
loadButton.click()

sleep(1)
moreButton = driver.find_element(
    By.XPATH, '//*[@id="eventsListTbl"]/tbody/tr/td[7]/div/button[3]')
moreButton.click()
try:
    changePassword = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Change Password')))
except:
    changePassword = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'C Pass')))
changePassword.click()
password = driver.find_element(
    By.XPATH, '/html/body/div[4]/div[1]/div/div/div/div/div[2]/div[2]/form/div[1]/div/input')
confirmPassword = driver.find_element(
    By.XPATH, '/html/body/div[4]/div[1]/div/div/div/div/div[2]/div[2]/form/div[2]/div/input')
transactionCode = driver.find_element(
    By.XPATH, '/html/body/div[4]/div[1]/div/div/div/div/div[2]/div[2]/form/div[3]/div/input')
submitButton = driver.find_element(
    By.XPATH, '/html/body/div[4]/div[1]/div/div/div/div/div[2]/div[2]/form/div[4]/div/button')
password.send_keys('Abcde1234')
confirmPassword.send_keys('Abcde1234')
transactionCode.send_keys('828398')
submitButton.click()


while True:
    pass
