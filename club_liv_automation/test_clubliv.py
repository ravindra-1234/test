import base64
import os.path
from appium import webdriver
from selenium.webdriver.common.by import By
import unittest
from time import *

class ExampleTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'RZCT811MHFX'
        # desired_caps['IP address'] = '192.168.0.107'
        desired_caps['appPackage'] = 'com.vhslogitech.club_liv'
        desired_caps['appActivity'] = 'com.vhslogitech.club_liv.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        sleep(3)

    def test_login(self):
        self.driver.find_element(By.XPATH,"//android.widget.Button[@content-desc='Open navigation menu']").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//android.view.View[@content-desc='LogIn']").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Marker']").click()
        sleep(2)
        username = self.driver.find_element(By.XPATH, "//android.widget.EditText[@index='7']")
        username.click()
        username.send_keys("marker1@gmail.com")
        sleep(2)
        password=self.driver.find_element(By.XPATH, "//android.widget.EditText[@index='8']")
        password.click()
        password.send_keys("pass")
        sleep(2)
        self.driver.find_element(By.XPATH,"//android.view.View[@content-desc='Sign in']").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"	//android.view.View[@content-desc='Add | Edit | Delete | Start Game | Stop Game']").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"(//android.widget.Button[@content-desc='Add Match'])[2]").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//android.view.View[@index='4']").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='OK']").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='OK']").click()
        sleep(2)
        xyz=self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]")
        xyz.click()
        sleep(2)
        self.driver.find_element(By.XPATH,"//android.view.View[@accessibility id='Table-03(Snooker) Bowring Institue || Bangalore || 2 MP'").click()
        sleep(3)
        self.driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Submit']").click()
        sleep(2)




