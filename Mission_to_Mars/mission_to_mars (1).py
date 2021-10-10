#!/usr/bin/env python
# coding: utf-8

# # Install/Import tools

# In[1]:


get_ipython().system('pip install pymongo')


# In[2]:


get_ipython().system('pip install bs4')


# In[3]:


get_ipython().system('pip install splinter')


# In[4]:


get_ipython().system('pip install webdriver_manager')


# In[5]:


from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time 
import pandas as pd
import requests
import random


# ### Begin Coding Splinter to Scrape RedPlanetScience.com

# In[6]:


#Scrape the https://redplanetscience.com/ News Site and collect the latest News Title and Paragraph Text. 
#Assign the text to variables that you can reference later.

# Example:
#news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
#news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://redplanetscience.com/'
browser.visit(url)
time.sleep(1)
for x in range(1):
    time.sleep(1)
    html = browser.html
    
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('div', class_='content_title').get_text()
    news = soup.find('div', class_='article_teaser_body').get_text()
    print(f"Title:{title} \n {news}")
    
browser.quit()





# ## JPL Mars Space Images - Featured Image

# In[6]:


# Visit the url for the Featured Space Image site here.
# https://spaceimages-mars.com/
# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
# Make sure to find the image url to the full size .jpg image.
# Make sure to save a complete url string for this image.
# # Example:
# featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'


# In[7]:


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
link = soup.find('img', class_='headerimage fade-in')['src']

featured_image_url = (f'https://spaceimages-mars.com/{link}')

print(featured_image_url)
    
browser.quit()


# # Mars Facts

# In[ ]:


# Visit the Mars Facts webpage here https://galaxyfacts-mars.com/ and use Pandas to scrape the table 
#containing facts about the planet including Diameter, Mass, etc.
# Use Pandas to convert the data to a HTML table string.


# In[8]:


url = 'https://galaxyfacts-mars.com/'

marsfacts = pd.read_html(url)
marsfacts


# In[9]:


marsfacts_df = marsfacts[1]
marsfacts_df


# In[10]:


marsfacts_df.columns = ['MARS PLANET PROFILE', 'Stats']
marsfacts_df.head()


# # Mars Hemispheres

# In[ ]:


# Visit the astrogeology site here https://marshemispheres.com/ to obtain high resolution images for each of Mar's hemispheres.

# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.

# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

# # Example:
# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]


# In[11]:


import random 



executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


data_on_page = []
    
html=""
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
        time.sleep(random.randint(1,2))
        title_link = div.find('div', class_='description')
        title_link = title_link.find("h3")
        print("----------")
        print(title_link)
        data_on_page.append(title_link)
        print(data_on_page)


        
browser.quit()           
        


# In[ ]:





# In[37]:


import time 
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

hemispheres_url = "https://marshemispheres.com/"

browser.visit(hemispheres_url)
html = browser.html
time.sleep(1)
soup = BeautifulSoup(html, "html.parser")
mars_hemisphere = []

products = soup.find_all("div", class_ = "result-list" )
hemispheres = products.find("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup=BeautifulSoup(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    mars_hemisphere.append({"title": title, "img_url": image_url})
    
print(title)


# In[44]:


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
        
        
browser.quit()  


# In[45]:


data_on_page


# In[12]:


# import random 



# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)


# data_on_page = []
    
# pageUrl=""
# for i in range(1):
#     time.sleep(random.randint(1,2))
#     data_on_page = []
    
  
#     pageUrl = f"https://marshemispheres.com/"

#     print(pageUrl)
    
#     time.sleep(1)
#     browser.visit(pageUrl)
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')
#     #https://stackoverflow.com/questions/52842778/find-partial-class-names-in-spans-with-beautiful-soup
#     divs = soup.find_all('div', class_='item')
    
#     for div in divs: 
#         time.sleep(random.randint(1,2))
#         link = div.find('a')
#         href = link["href"]
#         print("----------")
#         print(href)
#         url = f'https://marshemispheres.com/{href}'
#         browser.visit(url)
#         time.sleep(random.randint(1,2))
#         res=requests.get(url)
        
#         browser.links.find_by_partial_text("Sample").click()

#         time.sleep(1)
#         res=requests.get(url)
#         soup = BeautifulSoup(res.content,'lxml')
#         data = soup.find_all('img', attrs={'class': lambda e: e.startswith('wide-image') if e else False})
#         data_on_page.append(data)
#         df = pd.DataFrame(data_on_page)[0]
#         print(data)
        
        
# browser.quit()  


# In[13]:


# df.to_csv('image_urls.csv')


# In[14]:


# pd.set_option('display.max_colwidth', None)


# In[15]:


# df_image_urls_clean=pd.read_csv('image_urls.csv')

# df_image_urls_clean_columns = df_image_urls_clean.drop(columns=['Unnamed: 0'])
# df_image_urls_clean_columns


# In[16]:


# df_image_urls_clean_columns_split = df_image_urls_clean_columns['0'].str.split("=")


# In[17]:


# df_image_urls = df_image_urls_clean_columns_split.to_list()
# column_names = ['0','image','src']
# image_urls_df = pd.DataFrame(df_image_urls,columns=column_names)


# In[18]:


# image_urls_df


# In[19]:


# image_urls_df.to_csv('image_urls.csv')


# In[20]:


# df_image_urls_clean=pd.read_csv('image_urls.csv')
# df_image_urls_clean_columns = df_image_urls_clean.drop(columns=['Unnamed: 0'])
# df_image_urls_clean_columns


# In[21]:


# html_chars = ["/>",'"'," "]
# for char in html_chars:
#     df_image_urls_clean_columns['0'] = df_image_urls_clean_columns['0'].str.replace(char, '')
#     df_image_urls_clean_columns['image'] = df_image_urls_clean_columns['image'].str.replace(char, '')
#     df_image_urls_clean_columns['src'] = df_image_urls_clean_columns['src'].str.replace(char, '')
    
   
    


# In[22]:


# df_image_urls_clean_columns


# In[23]:


# urls = df_image_urls_clean_columns["src"]
# urls


# In[24]:


# url1 = urls.iloc[0]
# url2 = urls.iloc[1]
# url3 = urls.iloc[2]
# url4 = urls.iloc[3]
# url1


# In[25]:


# url_1 = f'https://marshemispheres.com/{url1}'
# url_2 = f'https://marshemispheres.com/{url2}'
# url_3 = f'https://marshemispheres.com/{url3}'
# url_4 = f'https://marshemispheres.com/{url4}'


# In[26]:


# url_1
# url_2
# url_3
# url_4


# In[ ]:





# In[27]:


# hemisphere_image_urls = [
#     {"title": "Cerberus Hemisphere", "img_url": url_1},
#     {"title": "Schiaparelli Hemisphere", "img_url": url_2},
#     {"title": "Syrtis Major Hemisphere", "img_url": url_3},
#     {"title": "Valles Marineris Hemisphere", "img_url": url_4},
#  ]


# In[28]:


# hemisphere_image_urls


# In[29]:


# hemisphere_image_urls_df = pd.DataFrame(hemisphere_image_urls)


# In[30]:


# hemisphere_image_urls_df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




