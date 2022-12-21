import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ChromeDriverManager:
    def install(self):
        pass


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
time.sleep(2)
driver.get("https://demo.guru99.com/test/newtours/")

driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input").send_keys("mercury")
driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/input").send_keys("ooiuoi")
driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/div/input").click()
time.sleep(2)
if driver.title == "Login: Mercury Tours":
    driver.get_screenshot_as_file("C:\\new\\myscreenshots1.png")

    print("test passed")

else:
    driver.get_screenshot_as_file("C:\\new\\myscreenshots1.png")

    print("test Failed")
time.sleep(2)
#
driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input").send_keys("mercury")
driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/input").send_keys("mercury")
driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/div/input").click()
driver.get_screenshot_as_file("C:\\new\\myscreenshots0.png")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/input").clear()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/input").send_keys("katta")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[3]/td[2]/input").send_keys("dharma")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td[2]/input').send_keys("0987654321")
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="userName"]').send_keys("drumakchinnamech@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td[2]/input').send_keys("palwancha, telangana, 507115, bcolony")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td[2]/input').send_keys("palwancha")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[8]/td[2]/input").send_keys("palvancha")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/input').send_keys("Telangana")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[10]/td[2]/input').send_keys("507115")
time.sleep(1)
drp_down = driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[11]/td[2]/select")
Driver = Select(drp_down)
Driver.select_by_value("INDIA")
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("mercury")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[14]/td[2]/input').send_keys("mercury")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[15]/td[2]/input').send_keys("mercury")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[17]/td/input').click()
time.sleep(3)
print("test passed")
driver.get_screenshot_as_file("C:\\new\\myscreenshots22.png")
print("you r successfully registered")
driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a").click()
time.sleep(2)
print(driver.title)
print(driver.current_url)
driver.close()