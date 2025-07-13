from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USERNAME = "Your username"
PASSWORD = "Your Password"
PHONE = 1234567890

chromeOps = webdriver.ChromeOptions()
chromeOps.add_experimental_option("detach",True)

driver = webdriver.Chrome(chromeOps)
driver.maximize_window()
driver.get("https://www.linkedin.com/feed/")
time.sleep(2)

username_field = driver.find_element(By.ID, "username")
username_field.send_keys(USERNAME)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(PASSWORD)
time.sleep(1)

login_button = driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[4]/button")
login_button.click()
time.sleep(15)


jobs_button = driver.find_element(By.LINK_TEXT, "Jobs")
jobs_button.click()


time.sleep(3)
search_for_jobs = driver.find_element(By.LINK_TEXT, "Search now")
search_for_jobs.click()

time.sleep(2)
easy_apply_button = driver.find_element(By.ID, "searchFilter_applyWithLinkedin")
easy_apply_button.click()
# ID="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4265816496-9-phoneNumber-nationalNumber" 
time.sleep(2)
job_list = driver.find_elements(By.CSS_SELECTOR, "ul.jobs-search-results__list li")

for job in job_list:
    try:
        job.click()
        time.sleep(3)

        # Wait for save button to be clickable and present
        save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        if save_button.is_enabled():
            save_button.click()
            print("Job saved successfully.")
        else:
            print("Save button not clickable.")
    except Exception as e:
        print(f"Error saving job: {e}")

 