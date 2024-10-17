import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://127.0.0.1:8000/")

driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[1]/input").clear()
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[1]/input").send_keys("adnanasad2001@gmail.com")

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[2]/input").clear()
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[2]/input").send_keys("asdf1234")

time.sleep(40)

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[4]/div[1]/div/label").click()

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[4]/div[2]/button").click()
time.sleep(8)

driver.find_element(By.XPATH, "/html/body/div/aside/div/div[4]/div/div/nav/ul/li[3]/a/i").click()
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[1]/a/i").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[1]/div/input").send_keys("SOFTWARE QUALITY ENGINEERING")
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[2]/button").click()
time.sleep(4)

driver.find_element(By.XPATH, "/html/body/div/aside/div/div[4]/div/div/nav/ul/li[3]/a/i").click()
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[2]/a/i").click()
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/aside/div/div[4]/div/div/nav/ul/li[4]/a/i").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/i").click()
time.sleep(4)


