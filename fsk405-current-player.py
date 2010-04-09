#!/usr/bin/env python

#from lxml import etree
from lxml.html import  tostring, parse

fsk_url = "http://fsk405.com/news.php"
root = parse(fsk_url).getroot()
#print tostring(root)

tables = root.cssselect('table')

#find the td 1st and then get its par
tr = None # the <tr> that holds all of the good stuff
for td in root.iter('td'):
    #print td.tag + ":" + str(td.text)
    if td.get('title'):
        #print td.get('title')
        if td.get('title').strip().lower() == 'ut4_superman':
            print 'found <td title="ut4_superman" .../>'
            tr = td.getparent().getnext()

#print tostring(tr)

for span in tr.iter('span'):
    print span.text.strip(),
print

## skip the 1st sub-div:
#for div in tr.iter('div'):
#    print div.get('title')
#
#print str(tr.getchildren()[0].tag)
sub_div_1 = tr.getchildren()[0].getchildren()[0]
#print sub_div_1.tag

for div in sub_div_1.iter('div'):
    print div.get('title')

# <tr><td style="border:1px solid">
#               <div style="width:160px; height:100px; overflow:auto; text-align:left">
#
#                 <span style="padding:1px; float:left"> PLAYERS: </span>
#                 <span style="padding:1px; float:right"> 21 / 26 </span>
#                 <br><br><div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="Altair (#PoPo#)">Altair (#PoPo#)</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="Belg">Belg</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="benji9635">benji9635</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="B.V.H.YoungstarBunny">B.V.H.YoungstarBunny</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="CDaly">CDaly</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="dragonslayer">dragonslayer</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="iLLkIlLyOu">iLLkIlLyOu</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="*IOU*Apex">*IOU*Apex</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="KingFB58">KingFB58</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="LordHadshoot">LordHadshoot</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="Master(#PoPo#)">Master(#PoPo#)</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="Moving_Target">Moving_Target</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="[NBD]yo$hi">[NBD]yo$hi</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="Ozen61">Ozen61</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="Plug[Um3]">Plug[Um3]</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="[RSG]Napoleon">[RSG]Napoleon</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="Screech Primus">Screech Primus</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="ShadowLucky">ShadowLucky</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="Smerfetto">Smerfetto</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title="Stabbity Stab">Stabbity Stab</div>
#                   <div style="padding:1px; white-space:nowrap; overflow:hidden; text-align:left" title=".!verde?ben!.">.!verde?ben!.</div>
#               </div>
#             </td>
#           </tr>
