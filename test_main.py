from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#Mazimize browser
time.sleep(2)
driver.maximize_window()

#Open Google
driver.get("https://www.google.com")
time.sleep(1)

search = driver.find_element(By.ID, "APjFqb")
search.send_keys("UI Automation")
time.sleep(2)

search.submit()
time.sleep(5)
driver.quit()