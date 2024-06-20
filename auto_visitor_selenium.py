from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

class AutoVisitor:
    def __init__(self, url):
        self.url = url
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920x1080')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def visit_and_interact(self):
        print(f"Visiting {self.url}")
        self.driver.get(self.url)
        time.sleep(random.uniform(1, 3))  # Wait for the page to load
        print(f"Page title: {self.driver.title}")

        # Example interactions
        self.scroll_page()
        self.click_elements()

    def scroll_page(self):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        for _ in range(3):  # Scroll down 3 times
            print("Scrolling down")
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(random.uniform(1, 2))  # Wait between scrolls

    def click_elements(self):
        try:
            # Find all clickable elements (modify this selector to match actual clickable elements on your target page)
            clickable_elements = self.driver.find_elements(By.TAG_NAME, 'a')
            for elem in clickable_elements[:5]:  # Click on the first 5 elements found
                print(f"Clicking element with text: {elem.text}")
                ActionChains(self.driver).move_to_element(elem).click(elem).perform()
                time.sleep(random.uniform(1, 2))  # Wait between clicks
        except Exception as e:
            print(f"Error clicking elements: {e}")

    def run(self):
        while True:
            self.visit_and_interact()
            print("Waiting before next visit")
            time.sleep(random.uniform(10, 20))  # Wait before visiting again

if __name__ == "__main__":
    url = "https://www.highrevenuenetwork.com/iaqgtx69y1?key=14a1e46999747270c942f2634ef5306a"  # Target URL
    visitor = AutoVisitor(url)
    visitor.run()
