#!/usr/bin/env python

from lxml.html import  tostring, parse

fsk_url = "http://fsk405.com/news.php"

#tables = root.cssselect('table')

def get_page_root(url):
    return parse(url).getroot()

def get_num_players_text(root):
    num_players_text = ''

    #find the td 1st and then get its par
    tr = None # the <tr> that holds all of the good stuff
    for td in root.iter('td'):
        #print td.tag + ":" + str(td.text)
        if td.get('title'):
            #print td.get('title')
            if td.get('title').strip().lower() == 'ut4_superman':
                #print 'found <td title="ut4_superman" .../>'
                tr = td.getparent().getnext()


    for span in tr.iter('span'):
        num_players_text += str(span.text.strip())

    return num_players_text

def get_players(root):
    players = []

    #find the td 1st and then get its par
    tr = None # the <tr> that holds all of the good stuff
    for td in root.iter('td'):
        #print td.tag + ":" + str(td.text)
        if td.get('title'):
            #print td.get('title')
            if td.get('title').strip().lower() == 'ut4_superman':
                #print 'found <td title="ut4_superman" .../>'
                tr = td.getparent().getnext()

    for div in tr.iter('div'):
        if div.get('title'):
            players.append(div.get('title'))

    #print players

    return players

if __name__ == "__main__":
    root = get_page_root(fsk_url)
    print get_num_players_text(root) + '\n - - - - - - -'
    for p in get_players(root):
        print p
