from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_chrome_with_existing_driver():
    logging.info("Testing Chrome setup with existing ChromeDriver...")
    
    try:
        # Basic Chrome options - minimal options
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-plugins')
        chrome_options.add_argument('--disable-images')
        chrome_options.add_argument('--disable-javascript')
        chrome_options.add_argument('--window-size=1200,800')
        
        # Try to create driver with existing ChromeDriver
        logging.info("Attempting to create Chrome driver...")
        driver = webdriver.Chrome(options=chrome_options)
        
        logging.info("Chrome driver created successfully!")
        
        # Test a simple page load
        logging.info("Testing page load...")
        driver.get("https://www.google.com")
        logging.info(f"Page title: {driver.title}")
        
        driver.quit()
        logging.info("Test completed successfully!")
        
    except Exception as e:
        logging.error(f"Chrome test failed: {e}")
        logging.error("The ChromeDriver version doesn't match your Chrome version")
        logging.error("Please download the correct ChromeDriver version manually")

if __name__ == "__main__":
    test_chrome_with_existing_driver() 