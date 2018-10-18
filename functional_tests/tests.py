from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        #Check home_page
        self.browser.get(self.live_server_url)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_test):
        table =  self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_test, [row.text for row in rows])

    def test_bunchOfTests(self):

        #Check title and header
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #Check inputbox and placeholder
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #Typing 'Buy peacock feathers' in text box
        inputbox.send_keys('Buy peacock feathers')

        #Hit enter in the text box
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #Typing 'Use peacock feathers to make a fly' in text box
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')

        #Hit enter in the text box
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        #Finish the test
        self.fail('Finish the test!')
