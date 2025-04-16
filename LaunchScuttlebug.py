#LaunchScuttlebug.py
"""
If calling LaunchScuttlebug.py from another script, use:

import LaunchScuttlebug
user = 'your username'
pw = 'your password' #you need to type your password here
folder = 'folderPath' #full path of firefox webdriver
(driver, WebDriverWait, EC, By, Keys) = LaunchScuttlebug.main(user, pw)
"""

import sys, os
import time, datetime
from selenium import webdriver


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located


def main(user, pw, folder):
    #path = os.path.join(folder, 'geckodriver.exe')
    driver = webdriver.Firefox()
    #Set up drivers for player profiles and tables
    bga_link = 'https://boardgamearena.com/account'
    
    driver.get(bga_link)
    
    wait = WebDriverWait(driver, 10)
    
    # enter username
    
    xpath_input_username = '//*[@id="account-module"]/div[3]/div[3]/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[2]/div/input'
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_input_username)))
    input_username = driver.find_element(By.XPATH, xpath_input_username)
    input_username.send_keys(user)
    
    xpath_submit_username = '//*[@id="account-module"]/div[3]/div[3]/div/div[2]/div/div[2]/div[1]/div/div[2]/form/div[3]/div/a'
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_submit_username)))
    driver.find_element(By.XPATH, xpath_submit_username).click()
    
    # enter password
    
    xpath_input_pw = '//*[@id="account-module"]/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[1]/div[2]/div/input'
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_input_pw)))
    input_password = driver.find_element(By.XPATH, xpath_input_pw)
    input_password.send_keys(pw)
    
    xpath_submit_pw = '//*[@id="account-module"]/div[3]/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div/a'
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_submit_pw)))
    driver.find_element(By.XPATH, xpath_submit_pw).click()
    
    # submit
    
    xpath_submit_login = '//*[@id="account-module"]/div[3]/div[3]/div/div[2]/div/div[2]/div[3]/div[2]/div[3]/div[3]/div/div/a'
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath_submit_login)))
    driver.find_element(By.XPATH, xpath_submit_login).click()
    print("login successful")

    return(driver, WebDriverWait, EC, By, Keys)
