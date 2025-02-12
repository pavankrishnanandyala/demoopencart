from selenium import webdriver
from selenium.webdriver.common.by import By


class registrationpage:

    clickon_myaccount = "//*[text()='My Account']//..//*[@class='d-none d-md-inline']"
    button_registration_xpath = "//*[text()='Register']//..//*[@class='dropdown-item']"
    #fill personal deatails
    textbox_firstname_id = "input-firstname"
    textbox_lastname_id = "input-lastname"
    textbox_email_id = "input-email"


    #passwordc reation
    textbox_password_id = "input-password"

    button_subscribe_id = "input-newsletter"
    button_privacypolicy_xpath = "//*[@class='form-check-input']"

    button_continue_xpath = "//*[@class='btn btn-primary']"

    def __init__(self , driver):
        self.driver = driver

    def clickonregistraionbutton(self):
        self.driver.find_element(By.XPATH, self. button_registration_xpath).click()


    def setfirstname(self, fname):
        firstnametext = self.driver.find_element(By.ID , self.textbox_firstname_id)
        firstnametext.clear()
        firstnametext.send_keys(fname)
    def setlastname(self, lname):
        lastnametext = self.driver.find_element(By.ID , self.textbox_lastname_id)
        lastnametext.clear()
        lastnametext.send_keys(lname)

    def setemail(self, email):
        emailtext = self.driver.find_element(By.ID , self.textbox_email_id)
        emailtext.clear()
        emailtext.send_keys(email)


    def setpassword(self, password):
        passwordtext = self.driver.find_element(By.ID , self.textbox_password_id)
        passwordtext.clear()
        passwordtext.send_keys(password)

    def clicksubscribe(self):
        self.driver.find_element(By.ID , self.button_subscribe_id).click()

    def clickprivacypolicy(self):
         self.driver.find_element(By.ID , self.button_privacypolicy_xpath).click()

    def clickcontinuebutton(self):
        self.driver.find_element(By.ID , self.button_continue_xpath).click()



