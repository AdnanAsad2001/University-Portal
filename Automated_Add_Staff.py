import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://127.0.0.1:8000")
driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[1]/input").clear()
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[1]/input").send_keys("adnanasad2001@gmail.com")

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[2]/input").clear()
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[2]/input").send_keys("asdf1234")

time.sleep(40)

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[4]/div[1]/div/label").click()

driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[4]/div[2]/button").click()

driver.find_element(By.XPATH, "/html/body/div/aside/div/div[4]/div/div/nav/ul/li[6]/a").click()

for i in range(1, 11):
    driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[1]/div[1]/input").clear()
    driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[1]/div[1]/input").send_keys("Staff")

    driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[1]/div[2]/input").clear()
    driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[1]/div[2]/input").send_keys(i)

    Email = "staff" + str(i) + "@gmail.com"
    driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[1]/div[3]/input").clear()
    driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[1]/div[3]/input").send_keys(Email)

    driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[1]/div[4]/select/option[1]").click()

    driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[1]/div[5]/input").clear()
    driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[1]/div[5]/input").send_keys("asdf1234")

    driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[1]/div[6]/input").send_keys("C:/Users/AdnanAsad/OneDrive/Desktop/University Portal/media/images.png")

    driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[1]/div[7]/textarea").send_keys("Karachi")

    driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[1]/div[8]/select/option[2]").click()

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    btn = driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div/div/div/form/div[2]/button")
    driver.execute_script("arguments[0].scrollIntoView();", btn)
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
