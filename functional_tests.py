from selenium import webdriver
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
		self.fail('Finish the test!')	#(5)

if __name__ == '__main__':	#(6)
	unittest.main()	#(7)
		# She is invited to enter a to-do item straight away

		# She types "Buy peacock feathers" into a text box (Edith's hobby       
		# is tying fly-fishing lures)

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very methodical)

		# The page updates again, and now shows both items on her list

		# Edith wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect.

		# She visits that URL - her to-do list is still there.

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