

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import 

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):


        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_class_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.password)
        password.send_keys(self.password)

        tom = TwitterBot('tomzy337@gmail.com', 'tomzyb')
        tom.login()
pass