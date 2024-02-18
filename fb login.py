from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

usr = 'uni3469855865@gmail.com'
pwd = 'gZHU!m9$bKHuvIq'
print('Entered Email:', usr)
print('Entered Password:', pwd)


browser = webdriver.Chrome()
# Set up the ChromeDriver service
service = Service(ChromeDriverManager().install())
# Initialize the WebDriver using the service
driver = webdriver.Chrome(service=service)
driver.maximize_window() # For maximizing window
driver.get('https://www.facebook.com/')
print("Opened Facebook")
sleep(1)


username_box = driver.find_element(By.ID, 'email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)
 
password_box = driver.find_element(By.ID, 'pass')
password_box.send_keys(pwd)
print ("Password entered")
 
login_button = WebDriverWait(driver, 60).until(login_box = browser.find_element("name", "login"))
login_button.click()
 
print ("Done")