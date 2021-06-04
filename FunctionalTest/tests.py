from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
class PageTest(LiveServerTestCase):



  def wait_for_table(self, row_text):        
           start_time = time.time()
           while True:  
               try:                
                   table = self.browser.find_element_by_id('barangay_table')                  
                   rows = table.find_elements_by_tag_name('tr')                
                   self.assertIn(row_text, [row.text for row in rows])
                   return
               except (AssertionError, WebDriverException) as e:  
                   if time.time() - start_time > MAX_WAIT:  
                       raise e                  
                   time.sleep(0.5)  
                 
  def setUp(self):
   self.browser = webdriver.Firefox()

  def test_browser_title(self):
   self.browser.get('http://localhost:8000/')
   #self.browser.get(self.live_server_url)
   self.assertIn('Barangay',self.browser.title)
   header_text = self.browser.find_element_by_tag_name('h1').text
   self.assertIn('TravelPass Permit', header_text)


   inputBarangay= self.browser.find_element_by_id('TBarangay')
   self.assertEqual(inputBarangay.get_attribute('placeholder'),'TBarangay')
   inputBarangay .click()
   inputBarangay.send_keys('Malagasang 2-A')
   time.sleep(1)

   inputAmunicipal = self.browser.find_element_by_id('Amunicipal')
   self.assertEqual(inputAmunicipal.get_attribute('placeholder'),'Amunicipal')
   inputAmunicipal.click()
   inputAmunicipal.send_keys('Imus')
   time.sleep(1)
   

   inputOaddress = self.browser.find_element_by_id('Oaddress')
   self.assertEqual(inputOaddress.get_attribute('placeholder'),'Oaddress')
   inputOaddress.click()
   inputOaddress.send_keys('GGH')
   time.sleep(1)
   
   btnLogin = self.browser.find_element_by_id('btnLogin')
   btnLogin.click()
   time.sleep(2)
  
   inputlname = self.browser.find_element_by_id('lname')
   self.assertEqual(inputlname.get_attribute('placeholder'),'Enter Full name')
   inputlname.click()
   inputlname.send_keys('Ces')
   time.sleep(1)

   '''inputFage = self.browser.find_element_by_id('Fage')
   self.assertEqual(inputFage.get_attribute('placeholder'),'Enter Age')
   inputFage.click()
   inputFage.send_keys('F')
   time.sleep(1)'''

   inputFbirthday = self.browser.find_element_by_id('Fbirthday')
   self.assertEqual(inputFbirthday.get_attribute('placeholder'),'Enter Birthday')
   inputFbirthday.click()
   inputFbirthday.send_keys('feb,26,2000')
   time.sleep(1)

   inputFgender = self.browser.find_element_by_id('Fgender')
   self.assertEqual(inputFgender.get_attribute('placeholder'),'Enter Gender')
   inputFgender.click()
   inputFgender.send_keys('F')
   time.sleep(1)

   inputFaddress = self.browser.find_element_by_id('Faddress')
   self.assertEqual(inputFaddress.get_attribute('placeholder'),'Enter Address')
   inputFaddress.click()
   inputFaddress.send_keys('GGH')
   time.sleep(1)

   inputFcnumber= self.browser.find_element_by_id('Fcnumber')
   self.assertEqual(inputFcnumber.get_attribute('placeholder'),'Enter Phone Number')
   inputFcnumber.click()
   inputFcnumber.send_keys('123')
   time.sleep(1)

   inputFemail= self.browser.find_element_by_id('Femail')
   self.assertEqual(inputFemail.get_attribute('placeholder'),'Enter Email Address')
   inputFemail.click()
   inputFemail.send_keys('ces@gmail.com')
   time.sleep(1)

   btnSubmit = self.browser.find_element_by_id('btnSubmit')
   btnSubmit.click()
   time.sleep(2)
   

   if __name__=='__main__':
        unittest.main()

