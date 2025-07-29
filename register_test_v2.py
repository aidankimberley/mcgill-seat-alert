from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_chrome_with_manager():
    logging.info("Testing Chrome setup with webdriver-manager...")
    
    try:
        # Import webdriver-manager
        from webdriver_manager.chrome import ChromeDriverManager
        
        # Basic Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1200,800')
        
        # Use webdriver-manager to get the right version
        logging.info("Getting ChromeDriver with webdriver-manager...")
        service = Service(ChromeDriverManager().install())
        
        # Try to create driver
        logging.info("Attempting to create Chrome driver...")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        logging.info("Chrome driver created successfully!")
        
        # Test a simple page load
        logging.info("Testing page load...")
        driver.get("https://www.google.com")
        logging.info(f"Page title: {driver.title}")
        
        driver.quit()
        logging.info("Test completed successfully!")
        
    except Exception as e:
        logging.error(f"Chrome test failed: {e}")
        logging.error("This might be a version compatibility issue")

if __name__ == "__main__":
    test_chrome_with_manager() 