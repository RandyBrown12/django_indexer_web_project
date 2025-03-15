from django.test import TestCase, Client
from django.urls import reverse
from django_indexer_web_app.models import Block, Transaction
from bs4 import BeautifulSoup

# Create your tests here.
class NavigationBarTestCase(TestCase):
    """
    Test case for the navigation bar functionality.
    Tests both the presence of navigation elements and their correct redirection.
    """

    def setUp(self):
        """Set up the test client for all test methods."""
        self.client = Client()

    def test_navigation_elements_present(self):
        """Test that all navigation elements are present in the navbar."""
        # Get the home page response
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        nav = soup.find('nav', class_='bg-zinc-600')

        # Check if nav element exists
        self.assertIsNotNone(nav, "Navigation bar not found")

        # Find all navigation links
        nav_links = nav.find_all('a', class_='text-white')

        # Check if we have exactly 3 links
        self.assertEqual(len(nav_links), 3, "Expected 3 navigation links")

        # Check text and href attributes of each link
        expected_links = [
            {'text': 'Home', 'href': '/'},
            {'text': 'Blocks', 'href': '/blocks/'},
            {'text': 'Transactions', 'href': '/transactions/'}
        ]

        for i, link in enumerate(nav_links):
            self.assertEqual(link.text.strip(), expected_links[i]['text'], 
                             f"Expected link text to be '{expected_links[i]['text']}'")
            self.assertEqual(link['href'], expected_links[i]['href'], 
                             f"Expected href to be '{expected_links[i]['href']}'")

    def test_home_link_redirection(self):
        """Test that the Home link redirects to the home page."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_blocks_link_redirection(self):
        """Test that the Blocks link redirects to the blocks page."""
        response = self.client.get('/blocks/')
        self.assertEqual(response.status_code, 200)

    def test_transactions_link_redirection(self):
        """Test that the Transactions link redirects to the transactions page."""
        response = self.client.get('/transactions/')
        self.assertEqual(response.status_code, 200)

    def test_navigation_styling(self):
        """Test that the navigation bar has the correct styling classes."""
        response = self.client.get(reverse('home'))
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Check nav element has correct classes
        nav = soup.find('nav')
        self.assertIsNotNone(nav)
        self.assertIn('bg-zinc-600', nav['class'])
        self.assertIn('p-3', nav['class'])
        
        # Check links have correct classes
        links = nav.find_all('a')
        for link in links:
            self.assertIn('text-white', link['class'])
            self.assertIn('px-4', link['class'])