from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Google
driver.get("https://www.google.com")

# Find search box (Google search input name is "q")
search_box = driver.find_element(By.NAME, "q")

# Print page title
print(driver.title)

# Close browser
driver.quit()
