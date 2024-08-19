#LaunchScuttlebug.py
"""
If calling this from another script, use:

import LaunchScuttlebug
user = 'your username'
pw = 'your password' #you need to type your password here
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
    path = os.path.join(folder, 'geckodriver.exe')
    driver = webdriver.Firefox()
    #Set up drivers for player profiles and tables
    bga_link = 'https://boardgamearena.com/'
    
    driver.get(bga_link)
    #print(user)
    #print(pw)
    
    login_link = 'https://en.boardgamearena.com/account'
    driver.get(login_link)
    
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.visibility_of_element_located((By.ID, "username_input")))
    username = driver.find_element(By.ID, "username_input")
    username.send_keys(user)
    
    wait.until(EC.visibility_of_element_located((By.ID, "password_input")))
    
    password = driver.find_element(By.ID, "password_input")
    password.send_keys(pw)
    
    wait.until(EC.visibility_of_element_located((By.ID, "submit_login_button")))
    driver.find_element(By.ID, "submit_login_button").click()
    return(driver, WebDriverWait, EC, By, Keys)
    


to_execute = """
import LaunchScuttlebug
user = 'your username'
pw = 'your password' #you need to type your password here

user = ''
pw = '' #

(driver, WebDriverWait, EC, By, Keys) = LaunchScuttlebug.main(user, pw)
"""