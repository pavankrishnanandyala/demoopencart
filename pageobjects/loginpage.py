from selenium import webdriver
from selenium.webdriver.common.by import By



class Loginpage():


    clickon_myaccount = "//*[text()='My Account']//..//*[@class='d-none d-md-inline']"
    clickon_loginpage = "//*[text()='Login']//..//*[@class='dropdown-item']"
    textbox_email_id = "input-email"
    textbox_password_id = "input-password"
    clickon_loginbutton_xpath = "//*[text()='Login']//..//*[@class='btn btn-primary']"


    def __init__(self , driver):
        self.driver = driver