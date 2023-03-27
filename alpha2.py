import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestCulturalDestination(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://culturaldestination.com")
    
    def test_homepage_loads(self):
        title = self.driver.title
        self.assertEqual(title, "Cultural Destination - Celebrate the Heritage of India")
        
    def test_virtual_tour(self):
        self.driver.find_element(By.ID, "virtual-tour-button").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "virtual-tour-video")))
        video_element = self.driver.find_element(By.ID, "virtual-tour-video")
        self.assertTrue(video_element.is_displayed())
        
    def test_artist_platform(self):
        self.driver.find_element(By.ID, "artist-platform-link").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "artist-list")))
        artist_list = self.driver.find_element(By.ID, "artist-list")
        artists = artist_list.find_elements(By.CLASS_NAME, "artist")
        self.assertGreater(len(artists), 0)
        
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
