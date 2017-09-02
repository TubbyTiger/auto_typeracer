import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


link = ''
driver = webdriver.Firefox()
driver.get(link)

time.sleep(3)
ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('k').perform()
dUI = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'dUI')))

gui = dUI.find_element_by_xpath("//td[starts-with(@id,'gwt-uid')]")
spantxt = gui.find_elements_by_xpath("//table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span")
txt = ""

if len(spantxt) == 3:
    for elem in spantxt[:2]:
        txt += elem.text
    for elem in spantxt[2:3]:
        txt += " "+ elem.text
else:
    for elem in spantxt[:2]:
        txt+= elem.text + " "
time.sleep(20)
inp =WebDriverWait(driver,25).until(EC.presence_of_element_located((By.CLASS_NAME,'txtInput')))
for i in txt:
    inp.send_keys(i+' ')