from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def frame_switch(name):
  driver.switch_to.frame(driver.find_element_by_name(name))



driver = webdriver.Chrome(executable_path = 'C:\gecko\chromedriver.exe')
driver.get('https://geosco.mp-objects.com/geosco/authentication/login-form')

usr = "odrca"
pwd = "OgnjenDrca12."


user_input = driver.find_element_by_xpath('//*[@id="j_username"]')
user_input.send_keys(usr)

pwd_input = driver.find_element_by_xpath('//*[@id="j_password"]')
pwd_input.send_keys(pwd)


btn = driver.find_element_by_class_name("button-login").click()


frame_switch('main_frame')

elem = driver.find_element_by_xpath('//*[@id="menuTree"]/ul/li[5]/a')
elem1 = driver.find_element_by_xpath('//*[@id="menuTree"]/ul/li[5]/ul/li[5]/a')
elem2 = driver.find_element_by_xpath('//*[@id="menuTree"]/ul/li[5]/ul/li[5]/ul/li[1]/a/span')

act = ActionChains(driver)
act.move_to_element(elem).move_to_element(elem1).move_to_element(elem2).click()
act.perform()

driver.switch_to.default_content()
frame_switch('main_frame')


inp1 = driver.find_element_by_name('inputField:0:inputFieldPanel:dateField:date')
inp1.clear()
inp1.send_keys("23/03/17")

inp2 = driver.find_element_by_name('inputField:1:inputFieldPanel:dateField:date')
inp2.clear()
inp2.send_keys("01/07/17")

chkbx = driver.find_element_by_name('email').click()
btnexe = driver.find_element_by_name('executeButton').click()

