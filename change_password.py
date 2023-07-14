from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://goexch777.com/admin'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)


def logger(text):
    time = datetime.now().strftime("%H:%M:%S")
    print(f'{time} - {text}')


def loginAsAdmin():
    logger('Waiting for login button')
    loginButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div[3]/button'))
    )
    sleep(2)
    logger('Login button found')
    loginButton.click()  # This is a button
    adminUsername = driver.find_element(By.XPATH, '//*[@id="input-1"]')
    adminPassword = driver.find_element(By.XPATH, '//*[@id="input-2"]')
    adminUsername.send_keys('777api')
    adminPassword.send_keys('Make1234')
    requestLoginButton = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div/div/div[6]/div[1]/div/div[2]/div/div[1]/form/div[3]/button')
    requestLoginButton.click()


def switchToUsersPage():
    logger('Waiting for landing page')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/header/div/div[3]/div[5]/button'))
    )
    logger('Landed at home page')
    driver.get(f'{url}/users')


def loadUser(username):
    searchUsernameBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[1]/form/div[1]/input'))
    )
    loadButton = driver.find_element(By.XPATH, '//*[@id="submit"]')
    searchUsernameBox.send_keys(username)  # This is an input field
    loadButton.click()


def hitMoreButton():
    moreButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="eventsListTbl"]/tbody/tr/td[7]/div/button[3]'))
    )
    moreButton.click()  # This is a button


def changePassword(newPassword):
    try:
        changePassword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Change Password')))
    except:
        changePassword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'C Pass')))

    changePassword.click()  # This is a link
    password = driver.find_element(
        By.XPATH, '/html/body/div[4]/div[1]/div/div/div/div/div[2]/div[2]/form/div[1]/div/input')
    confirmPassword = driver.find_element(
        By.XPATH, '/html/body/div[4]/div[1]/div/div/div/div/div[2]/div[2]/form/div[2]/div/input')
    transactionCode = driver.find_element(
        By.XPATH, '/html/body/div[4]/div[1]/div/div/div/div/div[2]/div[2]/form/div[3]/div/input')
    submitButton = driver.find_element(
        By.XPATH, '/html/body/div[4]/div[1]/div/div/div/div/div[2]/div[2]/form/div[4]/div/button')
    password.send_keys(newPassword)
    confirmPassword.send_keys(newPassword)
    transactionCode.send_keys('828398')
    submitButton.click()


if __name__ == '__main__':
    loginAsAdmin()
    switchToUsersPage()
    loadUser('sayan12345')
    hitMoreButton()
    changePassword('Abcde12345')

    while True:
        pass
