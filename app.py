from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(2)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(1)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def like_tweet(self, hashtag):
        time.sleep(3)
        bot = self.bot
        bot.get('https://twitter.com/search?q='+ hashtag +'&src=typed_query')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('css-1dbjc4n')
            #class="css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21"
            try:
                links = [elem.get_attribute('href') for elem in tweets]
                approved = ['status']
                print(links)
                links[:] = [i for i in links if i]
                print(links)
                links[:] = [url for url in links if any(item in url for item in approved)]
                print(links)
                for link in links:
                    try:
                        time.sleep(1)
                        bot.get(link)
                        time.sleep(5)
                        likeButton = bot.find_element_by_xpath("//div[@aria-label='Like']")
                        likeButton.click()
                        time.sleep(5)
                    except:
                        time.sleep(5)
                        print("error")
            except:
                time.sleep(5)
                print("error")
            
ed = TwitterBot('username', 'password')
ed.login()
ed.like_tweet('Key Word')

