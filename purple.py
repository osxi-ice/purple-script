import json
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def start():
	global json_data
	print('loading json file')
	try:
		with open('purple_data.json', 'r') as file:
			json_data = json.load(file)
	except:
		print('unable to open json file')
		time.sleep(2)
		quit()
	task = raw_input('Tasks: ')
	for i in range(0, int(task)):
		create()
		time.sleep(1)


def create():
	#load chrome window
	driver = webdriver.Chrome()
	driver.get('https://purple.com/purple-boys#get-squishy')

	email_final = str(random.randint(10000, 999999999))+'@'+str(json_data['catchall_without_at'])

	#autofill
	element = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.XPATH, """//*[@id="get-squishy"]/div/div[2]/div[1]/div/div/form/input[1]""")))
	element.send_keys(email_final, Keys.TAB, Keys.ENTER)

	element = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.XPATH, """//*[@id="checkout_shipping_address_first_name"]""")))
	element.send_keys(json_data['full_name'].split(' ')[0])

	element = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.XPATH, """//*[@id="checkout_shipping_address_last_name"]""")))
	element.send_keys(json_data['full_name'].split(' ')[1])

	element = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.XPATH, """//*[@id="checkout_shipping_address_address1"]""")))
	element.send_keys(json_data['address'])

	element = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.XPATH, """//*[@id="checkout_shipping_address_city"]""")))
	element.send_keys(json_data['city'])

	element = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.XPATH, """//*[@id="checkout_shipping_address_province"]""")))
	element.send_keys(json_data['state'])

	element = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.XPATH, """//*[@id="checkout_shipping_address_zip"]""")))
	element.send_keys(json_data['zipcode'])

	element = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.XPATH, """//*[@id="checkout_shipping_address_phone"]""")))
	element.send_keys(json_data['phone'])

	time.sleep(0.15)

	element.send_keys(Keys.ENTER)

	time.sleep(1)

	element = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.XPATH, """/html/body/div/div/div[1]/div[2]/div/form/div[2]/button""")))
	element.send_keys(Keys.ENTER)

	time.sleep(1)

	element = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.XPATH, """/html/body/div/div/div[1]/div[2]/div/div/form/div[3]/div[1]/button""")))
	element.send_keys(Keys.ENTER)


	for i in range(0, 15):
		if 'thank' in str(driver.current_url):
			print('Order confirmed')
			break
		else:
			time.sleep(1)
	driver.close()



start()












