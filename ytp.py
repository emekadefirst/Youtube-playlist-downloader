# COLLECT INPUT FROM USER
print("----HEY HAPPY USER OUR PRODUCT THE SCRIPT HAS BEEN UPDATED")
print("WE NO LONGER USE savefrom.net WE NOW HAVE OUR CUSTOM DOWNLOADER SO PLEASE READ THE readme file to get along")
print('or RUN THIS COMMAND IN YOUR TERMINAL "pip install pytube" ')
print("----------- PASTE THE PLAYLIST LINK BELOW AND HIT ENTER ON YOUR KEYBOARD")
link = input(">> ")

# DEPENDENCIES
import csv
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pytube import YouTube
import os

# HEADLESS MODE
options = Options()
options.headless = True

# WEB DRIVER ACTIVATION
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)
url = (link)

# FUNCTION TO FETCH LINK FROM TARGET YOUTUBE PLAYLIST VIA THE LINK COLLECTED FROM THE USER
def fetch():
    driver.get(url)
    # MAX WINDOW  FOR BETTER PERFORMANCE
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    # WAITING TO FIND ELEMENT
    wait.until(EC.presence_of_element_located((By.XPATH, '//a[@id="video-title"]')))

    # LIST
    video_links = []

    links = driver.find_elements(By.XPATH, '//a[@id="video-title"]')
    for link in links:
        video_links.append(link.get_attribute('href'))
    #CREATING CSV FILE TO SAVE SCRAPPED LINKS
    with open('video_links.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for link in video_links:
            writer.writerow([link])
    print("----SUCCESSFUL")
    print(f"-----------ALL PLAYLIST LINK HAS BEEN SAVE TO video_links.csv IN THE FOLDER")

# FUNCTION TO READ LINK AND DOWNLOAD 
def download():
    # To read csv file for saved links
    with open("video_links.csv") as f:
        reader = csv.reader(f)
        num_downloaded = 0
        for row in reader:
            link = row[0]
            if not link:
                continue
            url = (link)
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            # Update the output_path to your Downloads directory
            output_path = os.path.join(os.path.expanduser("~"), "Downloads")
            stream.download(output_path=output_path)
            num_downloaded += 1
            print(f"Download completed for link {num_downloaded}")
        print(f"Downloaded {num_downloaded} videos. Follow me on Twitter @VikChukwuemeka also support my work on github  https://github.com/emekadefirst ")

# CALLING FUNCTION
fetch()
download()
