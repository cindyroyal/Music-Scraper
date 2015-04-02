#!/usr/bin/env python

import scraperwiki
import requests
import lxml.html

#initialize id
id = 0

# loops through pages ending in the element in letters
# all letters of alphabet. Also a couple with 2 on the end
letters = ["", "m2", "s2"]
def letter_list(start, stop):
  
  for c in range(ord(start),ord(stop)+1):
    letters.append(chr(c))
    

letter_list('b', 'z')
site = "http://governor.state.tx.us/music/musicians/talent/talent"
for letter in letters:
     newsite = site + letter

     html = requests.get(newsite).content
     dom = lxml.html.fromstring(html)
     

     for tr in dom.cssselect("div[style='text-align: center'] tr"):
             tds = tr.cssselect("td")
             
             try:
                 band = tds[0].text_content()
                 city = tds[1].text_content()
                 genre = tds[2].text_content()
                 phone = tds[3].text_content()
             
                 
             
             # this checks to see if there is a ~ in the band name and removes rest of string
                 if '~' in band:
                      i = band.index('~') 
                      band = band[:+i]
                 else:
                      band
                  
             
                 # increments id 
                 id = id + 1
             
                 # section to handle links
                 url_cells = tds[0].cssselect('a')
                 url_list = []

                 if url_cells:
                    for cell in url_cells:
                        url_list.append(cell.get('href'))
                    
             
                 # writes the content into an object; joins and separates url_list
                 data = {
                    'id' : id,
                    'name' : band,
                    'city' : city,
                    'genre': genre,
                    'phone': phone,
                    'url': ', '.join(url_list)
                
                 }
                 print data
                 scraperwiki.sql.save(['id'],data)
             
             except IndexError:
                 print "{error}"
             