import scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


links = scraping.find_hrefs()
prices = scraping.find_prices()
addrs = scraping.find_addrs()


chrome_ops = webdriver.ChromeOptions()
chrome_ops.add_experimental_option("detach", True)


for current_property in range(len(links)):
    driver = webdriver.Chrome(chrome_ops)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdI4xOYQ8iR-F0QxkIGeHw5MvVuHYh7TVz2jgxwdEbFPyUzzA/viewform?usp=dialog")
    time.sleep(4)

    addrs_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    href_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_btn = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")

    addrs_input.send_keys(addrs[current_property])
    price_input.send_keys(prices[current_property])
    href_input.send_keys(links[current_property])
    time.sleep(1)
    submit_btn.click()
    time.sleep(2)
    driver.quit()
