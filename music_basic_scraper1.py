#!/usr/bin/env python

import scraperwiki
import requests
import lxml.html

    
html = requests.get("http://governor.state.tx.us/music/musicians/talent/talent").content
dom = lxml.html.fromstring(html)

for tr in dom.cssselect("div[style='text-align: center'] tr"):
    tds = tr.cssselect("td")
    if len(tds)==4:
      band = tds[0].text_content()

      data = {
       
        'Name': tds[0].text_content(),
        'City': tds[1].text_content(),
        'Genre': tds[2].text_content(),
        'Phone': tds[3].text_content()

      }
      print data
      scraperwiki.sql.save(['Name'], data)