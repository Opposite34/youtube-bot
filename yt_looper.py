# just a proof-of-concept
# using this program to loop for views will result in your views being IP blocked by YouTube
# however, you can still use this to loop a song you like to listen it over and over again

import selenium
from selenium import webdriver
from time import sleep
import random
from youtube_bot import YoutubeBot

print("What video do you want to loop on?")
video_name = str(input())

print("Who made the video?")
channel_name = str(input())

print("How many times to loop for?")
num_loop = int(input())

print("What's the duration between each loop?")
duration = int(input())

bot = YoutubeBot("firefox")
bot.search(video_name)

sleep(1)

bot.click_on_vid(video_name, channel_name)

count = 0

for i in range(num_loop):
    sleep(duration) # duration until each loop
    bot.refresh()
    sleep(0.5)

    play_button = bot.driver.find_element_by_xpath("//button[contains(@class, 'ytp-play-button')]")
    play_button.click()

    count += 1
    print(f"Times looped: {count}")