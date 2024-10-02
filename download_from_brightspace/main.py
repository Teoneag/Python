from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
import sys

# ToDo find a better way then waiting 5s hardcoded
# ToDo fix white window when running in headless mode

def load_credentials(file_path):
    """Load credentials from a file."""
    credentials = {}
    with open(file_path, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            credentials[key] = value
    return credentials

def setup_driver(download_dir):
    """Setup and return a Chrome driver."""
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service("C:\src\chromedriver-win64\chromedriver.exe")
    return webdriver.Chrome(service=service, options=chrome_options)

def login(driver, username, password):
    """Log into the website."""
    driver.get("https://brightspace.tudelft.nl/d2l/le/content/595300/Home")
    time.sleep(5)  # Wait for the page to load

    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password + Keys.RETURN)
    time.sleep(5)  # Wait for login to complete

    if "logout" not in driver.page_source.lower():
        print("Login failed. Check your credentials.")
        driver.quit()
        sys.exit(1)

def get_exams(driver):
    """Retrieve exam titles and URLs."""
    exam_elements = driver.find_elements(By.CSS_SELECTOR, "li.d2l-datalist-item")
    additional_exam_elements = driver.find_elements(By.CSS_SELECTOR, "li.d2l-datalist-item.d2l-datalist-simpleitem")
    exam_elements.extend(additional_exam_elements)

    exams = []
    for exam in exam_elements:
        title_element = exam.find_element(By.CSS_SELECTOR, "a.d2l-link")
        exams.append({"title": title_element.text, "url": title_element.get_attribute("href")})
    
    return exams

def download_exam(driver, exam):
    """Download the exam content."""
    driver.get(exam["url"])
    download_button = driver.find_element(By.CSS_SELECTOR, "button.d2l-button[id^='d2l_content_']")
    download_button.click()
    print(f"Clicked download for: {exam['title']}")
    time.sleep(5)  # Wait for download to complete

def main():
    # Set up download directory
    download_dir = os.path.join(os.getcwd(), 'downloads')
    
    # Load credentials
    credentials = load_credentials(os.path.join('download_from_brightspace', 'credentials.txt'))
    
    # Initialize the driver
    driver = setup_driver(download_dir)
    
    try:
        login(driver, credentials['username'], credentials['password'])
        exams = get_exams(driver)
        print(f"Found {len(exams)} exams.")
        print("Exams:" + str(exams))

        for exam in exams:
            print(f"Exam Title: {exam['title']}, URL: {exam['url']}")
            download_exam(driver, exam)

    finally:
        driver.quit()  # Close the browser

if __name__ == "__main__":
    main()