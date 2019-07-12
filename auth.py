from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from imgurpython import ImgurClient
import configparser

import os

def authenticate():
    config = configparser.ConfigParser()

    my_ini = find_file_path('auth.ini')
    config.read(my_ini)

    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')

    imgur_username = config.get('credentials', 'imgur_username')
    imgur_password = config.get('credentials', 'imgur_password')

    client = ImgurClient(client_id, client_secret)

    authorization_url = client.get_auth_url('pin')
    my_drive = find_file_path("chromedriver.exe")
    driver = webdriver.Chrome(executable_path=my_drive)
    driver.get(authorization_url)

    username = driver.find_element_by_xpath('//*[@id="username"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')
    username.clear()
    username.send_keys(imgur_username)
    password.send_keys(imgur_password)

    driver.find_element_by_name("allow").click()

    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.ID, 'pin'))
        WebDriverWait(driver, timeout).until(element_present)
        pin_element = driver.find_element_by_id('pin')
        pin = pin_element.get_attribute("value")
    except TimeoutException:
	       print("Timed out waiting for page to load")
    driver.close()

    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
    print("Authentication successful!")


    return client


def find_file_path(my_str):

    cwd = os.getcwd()

    # r=root, d=directories, f = files
    my_file = ""
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith(my_str):
                my_file = os.path.join(root, file)

    return my_file
