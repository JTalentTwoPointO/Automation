import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.maximize_window()

driver.get("https://ui-dev.ecoplant.co/login")

email = driver.find_element(by=By.NAME, value="email")
password = driver.find_element(by=By.NAME, value="password")
login_btn = driver.find_element(by=By.CLASS_NAME, value="submit")
unhide_btn = driver.find_element(by=By.CLASS_NAME, value="ant-input-suffix")


# verify Placeholders exist within login page
def verify_placeholder():
    if email.get_attribute("placeholder") == "Email Address" and password.get_attribute("placeholder") == "Password":
        return True


# verify unhide button exists within login page
def verify_unhide_btn():
    if unhide_btn:
        return True


# determination if password is hidden
def pw_hidden():
    if not password.get_attribute("text"):
        return True


def login_disabled():
    email_value = email.get_attribute("value")
    pass_value = password.get_attribute("value")
    email.send_keys("alon.levi@ecoplant.co")
    if (email_value == "" or pass_value == "") and login_btn.get_attribute("disabled"):
        return True


def forgot_password_page():
    forgot_pw_link = driver.find_element(by=By.CLASS_NAME, value="forgot-password")
    forgot_pw_link.click()
    if driver.find_element(by=By.NAME, value="forgotpasswordform"):
        return True


# logging into the main page automatically
def login():
    email.send_keys("alon.levi@ecoplant.co")
    password.send_keys("Ecoayl1321@")
    login_btn.click()
    # check if page loaded is main page


driver.implicitly_wait(6)
driver.close()
