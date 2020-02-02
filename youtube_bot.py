import selenium
from selenium import webdriver
from time import sleep

class YoutubeBot:

    def __init__(self, driver_name):

        if driver_name.lower() == "firefox":
                # driver for firefox
                self.driver = webdriver.Firefox()

        sleep(0.5)
        self.driver.get("https://www.youtube.com")

    def search(self, name):

        search_box = self.driver.find_element_by_xpath("//input[@id='search']")
        search_box.send_keys(name)

        sleep(0.5)
        search_btn = self.driver.find_element_by_xpath("//button[contains(@id, 'search')]")
        search_btn.click()

    # this method is cap-sensitive and only choose the first one that matches xpath query
    # there's stil some problems with xpath queries using the the hyphen ("-") character
    def click_on_vid(self, video_name, channel_name=""):

        try:

            if channel_name == "":
                video = self.driver.find_element_by_xpath(f"//a[contains(@aria-label, '{video_name}')]")
            else:    
                video = self.driver.find_element_by_xpath(f"//a[contains(@aria-label, '{video_name} by {channel_name}')]")
            video.click()
        
        except(selenium.common.exceptions.NoSuchElementException):
            print("The video specified is not found")

    def refresh(self):
        self.driver.refresh()