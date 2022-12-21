import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
time.sleep(2)
driver.get("https://www.amazon.in/")
driver.find_element(By.XPATH,'//*[@id="nav-hamburger-menu"]').click()
time.sleep(2)
Female=driver.find_element(By.XPATH,'//*[@id="hmenu-content"]/ul[1]/li[18]/a/div')
driver.execute_script("arguments[0].scrollIntoView();",Female)
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="hmenu-content"]/ul[1]/li[18]/a/i').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="hmenu-content"]/ul[11]/li[7]/a').click()
driver.get_screenshot_as_file(".\\screenshots\\"+"\\amazon.png")
time.sleep(2)
print(driver.title)
driver.close()