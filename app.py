from selenium import webdriver 
from selenium.webdriver.common.keys import Keys    #For sending Key presses.
import time
#import org.openqa.selenium.interactions.Actions as Actions
#import org.openqa.selenium.interactions.Action as action

class Twitterbot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox() #Opens a firefox instance

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')   #finds an element tagged with class named 'email-input'
        password = bot.find_element_by_name('session[password]')    #Same as email but password here.
        email.clear()   #For clearing any previous strings
        password.clear()
        email.send_keys(self.username)  #inputs username
        password.send_keys(self.password)   #inputs password
        password.send_keys(Keys.RETURN) #sends enter/return key
        time.sleep(4)
    
    #Actions action = new Actions(bot)

    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd&lang=en')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(4)
            tweetLinks = [i.get_attribute('href')

                for i in bot.find_elements_by_xpath("//a[@dir='auto']")] # Looking for all the element where they have an attribute dir=auto - not the best way but I was in a hurry, lol
            filteredLinks = list(filter(lambda x: 'status' in x,tweetLinks))    #filters tweet links so as to get the required ones. (twitter.com/usname/status/xxxxxx)
            
            for link in filteredLinks:      #Browsing the links and liking the tweets
                bot.get(link)
                time.sleep(3)
                try:
                    #bot.find_element_by_class_name('HeartAnimation').click()   #this thing doesn't work Don't know why
                    time.sleep(1)
                    bot.find_element_by_xpath('data-original-title="Like"]').click()  #this thing is wrong 
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(10)


username = input('Enter Username : ')
password = input('Enter Password : ')
print('\n'+'Username : '+username+'\n'+'Password : '+password+'\n')

tw = Twitterbot(username,password)

tw.login()

hashtag = input('Enter the search or the hashtag : ')
print('\n'+'To be searched :'+hashtag)

tw.like_tweet(hashtag)