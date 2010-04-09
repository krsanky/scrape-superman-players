#!/usr/bin/env python

#from lxml import etree
from lxml.html import  tostring, parse

fsk_url = "http://fsk405.com/news.php"
root = parse(fsk_url).getroot()
#print tostring(root)

tables = root.cssselect('table')

#find the td 1st and then get its par

#
#     <table cellpadding='0' cellspacing='2' style='width:160px; margin:auto; text-align:center'>
#
#           <tr>
#             <td style='text-align:center' title='GAME LINK'>
#               <div style='width:160px; white-space:nowrap; overflow:hidden; text-align:center'>
#                 <a href='qtracker://74.221.208.117:27960?game=UrbanTerror&amp;action=show' style='text-decoration:none'>
#                   74.221.208.117:27960
#                 </a>
#               </div>
#
#             </td>
#           </tr>
#
#           <tr>
#             <td style='text-align:center' title='FSK405 Official Superman [UAA]'>
#               <div style='width:160px; white-space:nowrap; overflow:hidden; text-align:center'>
#                 FSK405 Official Superman [UAA]
#               </div>
#             </td>
#           </tr>
#
#           <tr>
#             <td style='background-image:url(http://fsk405.com/e107_plugins/lgsl/lgsl_files/maps/urbanterror/q3ut4/ut4_superman.jpg); background-repeat:no-repeat; background-position:center'>
#               <a href='e107_plugins/lgsl/?s=2'>
#                 <img alt='' src='http://fsk405.com/e107_plugins/lgsl/lgsl_files/other/map_overlay.gif' style='border:none; width:160px; background:url(http://fsk405.com/e107_plugins/lgsl/lgsl_files/icons/urbanterror/urbanterror.gif); background-repeat:no-repeat; background-position:4px 4px' title='[ Type: urbanterror ] [ Game: q3ut4 ]
#  CLICK TO VIEW SERVER DETAILS' />
#               </a>
#             </td>
#           </tr>
#
#           <tr>
#
#             <td style='text-align:center' title='ut4_superman'>
#               <div style='width:160px; white-space:nowrap; overflow:hidden; text-align:center'>
#                 ut4_superman
#               </div>
#             </td>
#           </tr>
#           <tr>
#             <td style='border:1px solid'>
#               <div style='width:160px; height:76px; overflow:auto; text-align:left'>
#
#                 <span style='padding:1px; float:left'> PLAYERS: </span>
#                 <span style='padding:1px; float:right'> 2 / 26 </span>
#                 <br />
#                 <br />
#                   <div style='padding:1px; white-space:nowrap; overflow:hidden; text-align:left' title='Krusher'>Krusher</div>
#                   <div style='padding:1px; white-space:nowrap; overflow:hidden; text-align:left' title='Nervous (rus)'>Nervous (rus)</div>
#
#               </div>
#             </td>
#           </tr>
#         </table>

