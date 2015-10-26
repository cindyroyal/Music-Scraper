#!/usr/bin/env python

import scraperwiki
import requests
import lxml.html

#initialize id
id = 0

# loops through pages ending in the element in letters
# all letters of alphabet. Also a couple with 2 on the end
letters=["","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","m2","s2"]

site = "http://governor.state.tx.us/music/musicians/talent/talent"



for letter in letters:
    newsite = site + letter

    html = requests.get(newsite).content
    dom = lxml.html.fromstring(html)


    for tr in dom.cssselect("div[style='text-align: center'] tr"):
        tds = tr.cssselect("td")
        if len(tds)==4:
          # increments id 
          id = id + 1

          data = {
            'id' : id,
            'Name': tds[0].text_content(),
            'City': tds[1].text_content(),
            'Genre': tds[2].text_content(),
            'Phone': tds[3].text_content()
    
          }
          
          print data
          scraperwiki.sql.save(['id'],data)
