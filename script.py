from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.linkedin.com/login')

input_email = driver.find_element(By.ID, 'username')
input_email.send_keys('seu@email.com')

input_password = driver.find_element(By.ID, 'password')
input_password.send_keys('sua_senha')

btn_login = driver.find_element(By.XPATH, "//button[@type='submit']")
btn_login.click()

busca = driver.find_element(By.XPATH, "//input[@placeholder='Pesquisar']")
busca.send_keys('python')
busca.send_keys(Keys.RETURN)


input('')