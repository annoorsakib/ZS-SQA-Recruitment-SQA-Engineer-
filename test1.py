from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

USERNAME = 'testdoc'
PASSWORD = 'Test123456'
PATIENT_ID = '101010101010'

NEWUSERNAME = 'annoorsakib'
FIRSTNAME = 'MUNSHI SADMAN SAKIB'
LASTNAME = 'ANNOOR'
DOB ='15-02-1996'
EMAIL = 'annoor.sakib@gmail.com'
MOBILE = '1619960215'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://nmed-c.zssbd.com/')

user_input = driver.find_element_by_id('id_username')
user_input.send_keys(USERNAME)

password_input = driver.find_element_by_id('id_password')
password_input.send_keys(PASSWORD)

login_button = driver.find_element_by_id('clinicianLogin')
login_button.click()

link = driver.find_element_by_link_text('Patients')
link.click()

add_button = driver.find_element_by_id('add-btn')
add_button.click()

patient_input = driver.find_element_by_name('clinic_patient_ref')
patient_input.send_keys(PATIENT_ID)

check_button = driver.find_element_by_css_selector('input[type="submit"]')
check_button.click()

new_button = driver.find_element_by_xpath('//*[@id="entity-update-form"]/div[3]/div/div/a')
new_button.click()

time.sleep(2)
new_username = driver.find_element_by_id('id_username')
new_username.send_keys(NEWUSERNAME)


first_name = driver.find_element_by_id('id_first_name')
first_name.send_keys(FIRSTNAME)

last_name = driver.find_element_by_id('id_surname')
last_name.send_keys(LASTNAME)

dob = driver.find_element_by_id('datepicker')
dob.send_keys(DOB)

email = driver.find_element_by_id('id_email')
email.send_keys(EMAIL)

mobile = driver.find_element_by_id('id_mobile')
mobile.send_keys(MOBILE)

confirm_button = driver.find_element_by_xpath('//*[@id="confirmPatientForm"]')
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="confirmPatientForm"]'))))

sure_button = driver.find_element_by_xpath('//*[@id="proceedCreatePatient"]')
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="proceedCreatePatient"]'))))


time.sleep(10)

ok_button = driver.find_element_by_xpath('//*[@id="ok_button"]')
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ok_button"]'))))

time.sleep(10)
driver.refresh()

acc_link = driver.find_element_by_link_text('TestDoc')
acc_link.click()

time.sleep(10)

logout = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/ul[2]/li[6]/ul/li[2]/a')
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/ul[2]/li[6]/ul/li[2]/a'))))


