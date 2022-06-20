from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class NewVisitorTest(unittest.TestCase): 	# (1)

	def setUp(self):	#(3)
		self.browser = webdriver.Firefox()

	def tearDown(self):	#(3)
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):	#(2)
				# Edith has heard about a cool new online to-do app. She goes
		# to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do',self.browser.title)	#(4)
		header_text = self.browser.find_element(By.TAG_NAME,'h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item straight away
		inputbox = self.browser.find_element(By.ID, "id_new_item")
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# She types "Buy peacock feathers" into a text box (Edith's hobby       
		# is tying fly-fishing lures)
		inputbox.send_keys('Buy peacock feathers')

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element(By.ID, 'id_list_table')
		rows = table.find_elements(By.TAG_NAME,'tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows),
			"New to-do item did not appear in table"
		)

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very methodical)
		self.fail('Finish the test!')	#(5)

		# The page updates again, and now shows both items on her list

		# Edith wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect.

		# She visits that URL - her to-do list is still there.
	

if __name__ == '__main__':	#(6)
	unittest.main()	#(7)
		# Satisfied, she goes back to sleep

		# Edith starts a new to-do list

		# She notices that her list has a unique URL

		# Now a new user, Francis, comes along to the site.

		## We use a new browser session to make sure that no information
		## of Edith's is coming through from cookies etc

		# Francis visits the home page. There is no sign of Edith's
		# list

		# Francis starts a new list by entering a new item. He
		# is less interesting than Edith...

		# Francis gets his own unique URL

		# Again, there is no trace of Edith's list

		# Satisfied, they both go back to sleep