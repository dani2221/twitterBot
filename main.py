from selenium import webdriver
import selenium.webdriver.support.ui as ui
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class TwitterBot:
    def __init__(self,username,password):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/danil/Downloads/chromedriver_win32/chromedriver.exe',chrome_options=chrome_options)
        self.username = username
        self.password = password


    def reddit(self):
        main_window = self.driver.current_window_handle
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'N')
        self.driver.switch_to_window(main_window)
        self.driver.get('https://www.reddit.com/r/Showerthoughts/new/')
        sleep(2)
        try:
            jokee = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]/div[1]/div/div/div[2]/div[2]/div[1]/a/div/h3').text
        except:
            sleep(10)
            self.driver.get('https://www.reddit.com/r/Showerthoughts/new/')
            sleep(2)
            jokee = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]/div[1]/div/div/div[2]/div[2]/div[1]/a/div/h3').text
        sleep(2)    
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'W')
        self.driver.switch_to_window(main_window)
        return jokee


    def twitter(self,joke):

        self.driver.get('https://twitter.com/login')
        sleep(2)

        #username
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys(self.username)
        #password
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys(self.password)
        #login button
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()
        sleep(2)
        self.postJoke(joke)


    def postJoke(self,joke):
        #post button
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div').click()
        #enter joke
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div').send_keys(joke)
        #Tweet!
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div').click()
        sleep(5)
        self.driver.close()


        
#enter username and password
while True:
    bot = TwitterBot('','')
    joke = bot.reddit()
    bot.twitter(joke)
    sleep(600)
