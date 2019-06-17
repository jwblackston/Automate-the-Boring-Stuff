#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:08:45 2019

@author: walker
"""
#Automate the Boring Stuff, CHapter 11: Web Scraping 

#Create a beautiful soup object from HTML
'''import requests, bs4

res = requests.get('http://nostarch.com') #downloads the main page
res.raise_for_status() #passes text attribute of response to 
noStarchSoup = bs4.BeautifulSoup(res.text) #this variable
type(noStarchSoup)'''

#now that we have a BS4 object, we can use its methods to locate specific parts of a
# an HTML document
#This requires the select() method:
'''import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')

type(elems)

len(elems)

type(elems[0])

elems[0].getText()

str(elems[0])

elems[0].attrs'''

#Project "I'm Feeling Lucky" Google Search
import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:])) #stores the input from command line as a list
res.raise_for_status()

#NEXT: retrieve the top search result links
soup = bs4.BeautifulSoup(res.text, features = "lmxl")

# Then, open browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems)) #finds out whether there are fewer than 5 links
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href')) #will iterate to open each new tab in browser

    
                          