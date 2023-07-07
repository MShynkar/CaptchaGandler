from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set the path to your chromedriver executable
chromedriver_path = '/path/to/chromedriver'

# Set the URL of the webpage containing hCaptcha
url = 'https://example.com'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set up Chrome service
service = Service(chromedriver_path)

# Start the webdriver with the configured settings
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the webpage
driver.get(url)

# Wait for hCaptcha iframe to load
iframe = driver.find_element(By.CSS_SELECTOR, 'iframe[src^="https://hcaptcha.com/"]')
driver.switch_to.frame(iframe)

# Find and retrieve the hCaptcha ID
hCaptcha_id = driver.execute_script('return document.getElementById("challenge-form").getAttribute("data-hcaptcha-widget-id")')

# Print the hCaptcha ID
print("hCaptcha ID:", hCaptcha_id)

# Close the webdriver
driver.quit()
