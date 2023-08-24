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


'''driver.find_element(By.XPATH, "//*[@id='userEmail']").clear()
driver.find_element(By.XPATH, "//*[@id='userEmail']").send_keys("msaad@ssuet.edu.pk")

driver.find_element(By.XPATH,"//*[@id='genterWrapper']/div[2]/div[1]/label").click()

driver.find_element(By.ID,"userNumber").clear()
driver.find_element(By.ID,"userNumber").send_keys("03000263245")

driver.find_element(By.ID,"dateOfBirthInput").click()
driver.find_element(By.XPATH,"//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[11]").click()
driver.find_element(By.XPATH,"//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[85]").click()
driver.find_element(By.XPATH,"//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[3]").click()

driver.find_element(By.ID,"subjectsInput").send_keys("ENGLISH")
driver.find_element(By.ID,"subjectsInput").send_keys(Keys.ENTER)

hobbies = driver.find_element(By.XPATH,"//*[@id='hobbiesWrapper']/div[2]/div[2]/label")
driver.execute_script("arguments[0].click()",hobbies)

driver.find_element(By.ID,"uploadPicture").send_keys('C:\\Users\\Administrator\\Desktop\\download.jpg')
driver.find_element(By.ID,"currentAddress").send_keys("House no.2/5 PIB colony no.3")
time.sleep(5)


submitbtn = driver.find_element(By.ID,"submit")
driver.execute_script("arguments[0].click()",submitbtn)
time.sleep(15)'''