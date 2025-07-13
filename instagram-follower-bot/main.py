from selenium import webdriver
from selenium.webdriver.common.by import By
import time

my_username = "Your Username"
my_password = "Password"
target_username = "instagram"

chrome_ops = webdriver.ChromeOptions()
chrome_ops.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_ops)
driver.get(url="https://www.instagram.com/")
driver.maximize_window()
time.sleep(2)


login_username_input = driver.find_element(By.NAME, "username")
login_username_input.send_keys(my_username)

login_password_input = driver.find_element(By.NAME, "password")
login_password_input.send_keys(my_password)
time.sleep(1)

login_button = driver.find_element(By.CSS_SELECTOR, "#loginForm > div.html-div.x14z9mp.xat24cr.x1lziwak.xexx8yu.xyri2b.x18d9i69.x1c1uobl.x9f619.xjbqb8w.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.xqui205.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div:nth-child(3) > button")
login_button.click()
time.sleep(4)


not_now_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div")
not_now_btn.click()
time.sleep(3)


search_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div")
search_btn.click()
time.sleep(1)


search_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/input")
search_input.send_keys(target_username)
time.sleep(3)

found_acc = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/a[1]")
found_acc.click()
time.sleep(2)


followers_link = driver.find_element(By.XPATH, '//a[contains(@href,"/followers")]')
followers_link.click()
time.sleep(4)

scroll_box = driver.find_element(By.XPATH, "//div[@role='dialog']//div[@class='_aano']")
for _ in range(5):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
    time.sleep(2)

follow_buttons = driver.find_elements(By.XPATH, "//div[@role='dialog']//button[normalize-space()='Follow']")

followed = 0
for btn in follow_buttons:
    btn.click()
    followed += 1
    time.sleep(2) 
    