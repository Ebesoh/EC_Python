# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest, time, re


class KatalonTestCas1(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_katalon_test_cas1(self):
        def test_katalon_test_cas1(self):
            driver = self.driver
            wait = WebDriverWait(driver, 30)

            driver.get("https://www.selenium.dev/selenium-ide/")

            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Docs"))).click()
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Control Flow"))).click()
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Code Export"))).click()
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Plugins"))).click()
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Requests"))).click()
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Adding Commands"))).click()



        #driver.find_element(By.LINK_TEXT, "Command-line Runner").click()
        #driver.find_element(By.LINK_TEXT, "Control Flow").click()
        #driver.find_element(By.LINK_TEXT, "Frequently Asked Questions").click()
        #driver.find_element_by_link_text("API").click()
        #driver.find_element_by_link_text("Getting Started").click()
        #driver.find_element_by_link_text("Command-line Runner").click()
        #driver.find_element_by_link_text("Control Flow").click()
        #driver.find_element_by_link_text("Frequently Asked Questions").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    @property
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()