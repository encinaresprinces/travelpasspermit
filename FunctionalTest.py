'''from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')'''

from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_browser_title(self):
        self.browser.get('http://localhost:8000/')
        self.assertIn("PureGold SignUp Form",self.browser.title)

    def check_for_rows_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('listTable')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_start_list_and_retrieve_it(self):


     headerText = self.browser.find_element_by_tag_name('h1').text
     self.assertIn("PureGold SignUp Form", headerText)
     inputbox = self.browser.find_element_by_id('fullname')
     self.assertEqual(inputbox.get_attribute('placeholder'), "Enter Full name")
     inputbox.click()
     inputbox.send_keys('Ces')
     time.sleep(1)

     inputbox2 = self.browser.find_element_by_id('gs')
     self.assertEqual(inputbox2.get_attribute('placeholder'), "Enter Age")
     inputbox2.click()
     inputbox2.send_keys('20')
     time.sleep(1)

     inputbox3 = self.browser.find_element_by_id('Gen')
     self.assertEqual(inputbox3.get_attribute('placeholder'), "Enter Gender")
     inputbox3.click()
     inputbox3.send_keys('F')
     time.sleep(1)

     inputbox4 = self.browser.find_element_by_id('adds')
     self.assertEqual(inputbox4.get_attribute('placeholder'), "Enter Address")
     inputbox4.click()
     inputbox4.send_keys('Imus')
     time.sleep(1)

     inputbox5 = self.browser.find_element_by_id('num')
     self.assertEqual(inputbox5.get_attribute('placeholder'), "Enter Phone Number")
     inputbox5.click()
     inputbox5.send_keys('123')
     time.sleep(1)

     inputbox6 = self.browser.find_element_by_id('emaladd')
     self.assertEqual(inputbox6.get_attribute('placeholder'), "Enter Email Address")
     inputbox6.click()
     inputbox6.send_keys('ces@gmail.com')
     time.sleep(1)

if __name__ == '__main__':
    unittest.main()
