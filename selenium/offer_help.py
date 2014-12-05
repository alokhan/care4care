# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class OfferHelp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_offer_help(self):
        driver = self.driver
        driver.get(self.base_url + "")
        driver.find_element_by_xpath("//section[@id='main-content']/section/div[2]/div[2]/button").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Gent')])[3]").click()
        driver.find_element_by_id("id_category_2").click()
        driver.find_element_by_id("id_category_1").click()
        driver.find_element_by_id("id_category_0").click()
        driver.find_element_by_css_selector("span.glyphicon-calendar.glyphicon").click()
        driver.find_element_by_xpath("//div[@id='sizcache06690151371989828']/div/div/table/tbody/tr[6]/td").click()
        driver.find_element_by_id("id_time_3").click()
        driver.find_element_by_id("id_time_4").click()
        driver.find_element_by_id("id_time_6").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
