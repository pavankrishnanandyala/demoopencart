from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

from pageobjects.resgistration_page import registrationpage
import pytest


class test_userregistration:

    def test_verifylog(self, setup):
        self.driver = setup
        self.driver.get("https://demo-opencart.com/index.php?route=common/home&language=en-gb")
        self.status = self.driver.find_element(By.XPATH, "(//img[@title='Your Store'])[1]").is_displayed()

        try:
            self.status == "https://demo-opencart.com/image/catalog/opencart-logo.png"
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert True

        except:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePagefailTitle.png")
            self.driver.close()
            assert False

    def test_registration(self, setup):
        self.driver = setup
        self.driver.get("https://demo-opencart.com/index.php?route=common/home&language=en-gb")

        self.rg = registrationpage(self)
        self.rg.clickonregistraionbutton()
        self.rg.setfirstname("ram")
        self.rg.setlastname("raju")
        self.rg.setemail("ramraju@gmail.com")
        self.rg.setpassword("Raju@1234")
        self.rg.clicksubscribe()
        self.rg.clickprivacypolicy()
        self.rg.clickcontinuebutton()
        self.status1 = self.driver.find_element(By.XPATH,
                                                "(//h1[normalize-space()='Your Account Has Been Created!'])[1]"
                                                ).text()

        try:
         self.status1 == "Your Account Has Been Created!"
         self.driver.save_screenshot(".\\Screenshots\\" + "test_registerPageTitle.png")
         self.driver.close()
         assert True

        except:
           self.driver.save_screenshot(".\\Screenshots\\" + "test_registerPagefailTitle.png")
           self.driver.close()
           assert False
