from selenium import webdriver
from selenium.webdriver.chrome.service.by import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=service(r"C:\Users\supri\Downloads\chromedriver_win32")
driver = webdriver.Chrome(r"C:\Users\supri\Downloads\chromedriver_win32")


def test_webpage_loading():
    driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001")  


def test_form_fields():
    driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001")  
    name_input = driver.find_element(By.ID, "name") 
    name_input.send_keys("supriya")
    email_input = driver.find_element(By.ID, "email")  
    email_input.send_keys("sbhele14@gmail.com")
    phone_input=driver.find_element(By.XPATH,"//*[@id='contact-form']/div/div[4]/label")
    phone_input.send_keys(9022981036)

def test_form_submission():
    driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001") 
    name_input = driver.find_element(By.ID, "name")  
    name_input.send_keys("supriya")
    email_input = driver.find_element(By.ID, "email")  
    email_input.send_keys("sbhele14@gmail.com")
    phone_input=driver.find_element(By.XPATH,'//*[@id="contact-form"]/div/div[4]/input')
    phone_input.send_keys(9022981036)
    apply_button = driver.find_element(By.XPATH, "//*[@id='contact-form']/div/div[7]/div/button[1]]")
    apply_button.click()


def test_error_handling():
    driver.get("https://www.hashtag-ca.com/careers/apply?jobCode=QAE001")  
    apply_button = driver.find_element(By.XPATH, "//*[@id='contact-form']/div/div[7]/div/button[1]")  
    apply_button.click()

wait = WebDriverWait(driver, 10)

test_webpage_loading()
test_form_fields()
test_form_submission()
test_error_handling()

driver.quit()
