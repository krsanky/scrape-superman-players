#!/usr/bin/env python

#from lxml import etree
from lxml.html import  tostring, parse

fsk_url = "http://fsk405.com/news.php"
root = parse(fsk_url).getroot()
#print tostring(root)

#tables = root.cssselect('table')

#find the td 1st and then get its par
tr = None # the <tr> that holds all of the good stuff
for td in root.iter('td'):
    #print td.tag + ":" + str(td.text)
    if td.get('title'):
        #print td.get('title')
        if td.get('title').strip().lower() == 'ut4_superman':
            #print 'found <td title="ut4_superman" .../>'
            tr = td.getparent().getnext()

#print tostring(tr)

print
for span in tr.iter('span'):
    print span.text.strip(),

print "\n - - - - - - -"

for div in tr.iter('div'):
    if div.get('title'):
        print div.get('title')

print
