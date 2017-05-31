#Developed by Earnest Flowers
#version 1.0

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkinter
from tkinter import messagebox
import time

chromedriver = webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver.exe")
chromedriver.implicitly_wait(10)

def login_IG(myemail,mypassword):

    url = "https://www.instagram.com/"

    chromedriver.maximize_window()
    chromedriver.get(url)

    #login
    setloginintoaccount = chromedriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
    setloginintoaccount.click()

    #email
    email = chromedriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[1]/input')
    email.send_keys(myemail)

    #password
    password = chromedriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/input')
    password.send_keys(mypassword)

    #submit
    sign_in = chromedriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button')
    sign_in.click()

def endofIGmessagebox(mytitle, mymessage):
    root = tkinter.Tk()
    root.withdraw()
    root.lift()
    root.attributes("-topmost", True)
    messagebox.showinfo(mytitle, mymessage)

#function pass - email, pw
login_IG("you IG Email", "your IG Password")

hitlike = chromedriver.find_elements_by_css_selector('span[class ^="_soakw coreSpriteHeartOpen"]')

i = 0
while i < len(hitlike):

    for elements in hitlike:
        moveit = chromedriver.find_elements_by_css_selector('span[class ^="_soakw coreSpriteHeartOpen"]')
        elements.location_once_scrolled_into_view
        elements.click()
        time.sleep(1)
        i+=1
        if i == len(hitlike):
            body = chromedriver.find_element_by_css_selector('body')
            body.send_keys(Keys.PAGE_DOWN*3)
            time.sleep(2)
            i = 0
    
    #find new unliked posts
    hitlike = chromedriver.find_elements_by_css_selector('span[class ^="_soakw coreSpriteHeartOpen"]')

endofIGmessagebox("IG Liker","No new IG posts")

time.sleep(1)
chromedriver.quit()