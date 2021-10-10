#!/usr/bin/env python
# coding: utf-8






from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time 
import pandas as pd
import requests
import random


# ### Begin Coding Splinter to Scrape RedPlanetScience.com




#Scrape the https://redplanetscience.com/ News Site and collect the latest News Title and Paragraph Text. 
#Assign the text to variables that you can reference later.

 

def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    title, news = mars_news(browser)
    
    
    data = {
        "title":title,
        "news":news,
        "featured_image": feature_image(browser),
        "facts":mars_fact(),
        "hemispheres": hemisphere(browser)
    }
    browser.quit()
    
    
    return data

    
    
def mars_news(browser):
    

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(1)
    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')
    try:
        for x in range(1):
            time.sleep(1)

            title = soup.find('div', class_='content_title').get_text()
            news = soup.find('div', class_='article_teaser_body').get_text()
            print(f"Title:{title} \n {news}")

        browser.quit()
        
    except:
        return None, None
    
    return title, news
   

    
def feature_image(browser):
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    time.sleep(1)

    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')

    browser.links.find_by_partial_text("FULL IMAGE").click()

    time.sleep(1)

    #<img class="fancybox-image" src="image/featured/mars2.jpg" alt="">
#     link = soup.find('img', class_='headerimage fade-in')['src']
    
    try:
        link = soup.find('img', class_='headerimage fade-in')['src']
    except:
        return None
    
    featured_image_url = (f'https://spaceimages-mars.com/{link}')
    print(featured_image_url)

    browser.quit()

    
    
    return featured_image_url



    
def mars_fact():
    url = 'https://galaxyfacts-mars.com/'

    marsfacts = pd.read_html(url)
    marsfacts_df = marsfacts[1]
    marsfacts_df.columns = ['MARS PLANET PROFILE', 'Stats']    
    
    
    
    
    return marsfacts_df.to_html(classes="table table-striped")

def hemisphere(browser):
    import random 



    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    data_on_page = []

    pageUrl=""
    for i in range(1):
        time.sleep(random.randint(1,2))
        data_on_page = []


        pageUrl = f"https://marshemispheres.com/"

        print(pageUrl)

        time.sleep(1)
        browser.visit(pageUrl)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        #https://stackoverflow.com/questions/52842778/find-partial-class-names-in-spans-with-beautiful-soup
        divs = soup.find_all('div', class_='item')

        for div in divs: 
            #Get Title
            try:
                title = div.find("h3").text
                title = title.replace("Enhanced", "")

                #Get Full Image
                end_link = div.find("a")["href"]
                image_link = "https://marshemispheres.com/" + end_link    
                browser.visit(image_link)
                html = browser.html
                soup=BeautifulSoup(html, "html.parser")
                image_url = soup.find("img", class_="wide-image")["src"]
                image_url_full = "https://marshemispheres.com/" + image_url  

                #append data
                data_on_page.append({"title": title, "img_url": image_url_full})
            
            except:
                return None

    browser.quit()  

    
    
    return data_on_page


    
    
    












