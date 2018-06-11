from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Bob wants to use our to-do app. He goes to the homepage
        self.browser.get('http://localhost:8000')

        # Bob sees that the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Bob is invited to enter a to-do item straight away

        # Bob types "Buy firewood" into a textbox

        # When Bob hits enter, the page updates, and now the page lists
        # "1: Buy firewood" as an item in a to-do list

        # There is still a textbox to add more items. Bob enters
        # "Sweep the chimney"

        # The page updates again, and now shows both items on the list

        # Bob sees that the site has generated a unique URL for his list
        # -- there is some explanatory text to that effect.

        # Bob visits his URL - his to-do list is still there.

        # Bob leaves to carry on with his day

if __name__ == '__main__':
    unittest.main(warnings='ignore')