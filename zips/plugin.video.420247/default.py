# -*- coding: utf-8 -*-
#------------------------------------------------------------
# 420 24/7 Kodi add-on
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: something else promotions
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.420247'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UConPop07hajKE2MemHRdFpA"
YOUTUBE_CHANNEL_ID_2 = "UCbXLN_CdaexztLvwkB4LpOg"
YOUTUBE_CHANNEL_ID_3 = "UCvHUk8tO7-KhR4e4cSA4XqA"
YOUTUBE_CHANNEL_ID_4 = "UC1Ev2zN7eBStL3TZQHN0Q6A"
YOUTUBE_CHANNEL_ID_5 = "UCAF8Fj8odT6vMhSN0rd9AKQ"
YOUTUBE_CHANNEL_ID_6 = "UCIhUprsZTPrSRiMj0pXp1fA"
YOUTUBE_CHANNEL_ID_7 = "UCp-T_iWV3SmPKZuBh7RVHYQ"
YOUTUBE_CHANNEL_ID_8 = "UC23aSgHY8WaJGw4nft7Sn7g"
YOUTUBE_CHANNEL_ID_9 = "UCV4tjsLO4Eu_UhJUCGkKnYQ"
YOUTUBE_CHANNEL_ID_10 = "UCvsRvJ0B2hqdlhb9tZokdXA"
YOUTUBE_CHANNEL_ID_11 = "UCC0gbevobKOMRA6RPzwcVNg"
YOUTUBE_CHANNEL_ID_12 = "UCw9MYDLFln8lcMiTdR-6ydQ"
YOUTUBE_CHANNEL_ID_13 = "UCUeOHcC5i_h-Rh-G_LqGoog"
YOUTUBE_CHANNEL_ID_14 = "UColTXGgXJmfYEGowvWCLQJQ"
YOUTUBE_CHANNEL_ID_15 = "UCqu_M0ARO7Sanbf_hte0Olw"
YOUTUBE_CHANNEL_ID_16 = "UC84yLdcBt2YaePTACLBrXQg"
YOUTUBE_CHANNEL_ID_17 = "UCeH4pozs0NPJn0CW5cvbt5A"
YOUTUBE_CHANNEL_ID_18 = "UCFQ7vc-dWlSUZd6OqsAepMA"
YOUTUBE_CHANNEL_ID_19 = "UCuNfQHhJVLi1aXeA6rnnETg"
YOUTUBE_CHANNEL_ID_20 = "UCC9ZMZ2ZYf27ALnODZaUmcQ"
YOUTUBE_CHANNEL_ID_21 = "UCdS7PjPJnhaxGekVfJpS4ww"

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="tokinGLX",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-IPD-DftnEbs/AAAAAAAAAAI/AAAAAAAAAAA/q0YZYbiR-Ck/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Coral Reefer",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-qUoybCzq0Us/AAAAAAAAAAI/AAAAAAAAAAA/m3ngiqKoFSc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="R3DBAND",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-hAOOu6po8r8/AAAAAAAAAAI/AAAAAAAAAAA/s2xZPfKU8Ak/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TheCCC420",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-KswhKxU8RF4/AAAAAAAAAAI/AAAAAAAAAAA/oFkIGHAfGHg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="greenhouseseeds",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-jWmZvXZh21Q/AAAAAAAAAAI/AAAAAAAAAAA/RgHhkaqtoZk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="VapeLife Will",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-aHpPFE0rTLk/AAAAAAAAAAI/AAAAAAAAAAA/Po5fDfI_0HQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="subcool420",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-aFWyEPx5kqE/AAAAAAAAAAI/AAAAAAAAAAA/sA62CbanuYA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bubbleman's World",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-8ysouZzLw7U/AAAAAAAAAAI/AAAAAAAAAAA/33Uv3eymflA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="urbangrower",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-jaJfvC853Ls/AAAAAAAAAAI/AAAAAAAAAAA/o2WtfI3aVyc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Grow Pot Cheaply",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-1AxN11RpNRs/AAAAAAAAAAI/AAAAAAAAAAA/DKzYKl7zZbM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="knottyy",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-jZ3kTwKU2Vc/AAAAAAAAAAI/AAAAAAAAAAA/7fyM0XHZCnc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="A2Pothecary",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-S2lxSQlYAOc/AAAAAAAAAAI/AAAAAAAAAAA/q_2bLiKIqdw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="medgrower1",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-nifZT4o0INQ/AAAAAAAAAAI/AAAAAAAAAAA/K_Xc7mv8L7I/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="The Home Grown Report",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-8HfxaBm0XHM/AAAAAAAAAAI/AAAAAAAAAAA/ddCbjZXVK2c/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="VaderOG",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-NixZmjH8DCk/AAAAAAAAAAI/AAAAAAAAAAA/bGHHORDiZhc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="xSTONEDxNINJAx",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-ZxtxuuBka1Y/AAAAAAAAAAI/AAAAAAAAAAA/SWKfeAvs560/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jorge Cervantes",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-o3FpeAlOW7I/AAAAAAAAAAI/AAAAAAAAAAA/hYKXMG511oU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="High Times",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-0HLaipR4bKw/AAAAAAAAAAI/AAAAAAAAAAA/rb5y-T1ncUA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="CustomGrow420",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-QonAB4_C6Ps/AAAAAAAAAAI/AAAAAAAAAAA/Pva5l89ty18/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="StrainCentral",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-eAhP59TRMkk/AAAAAAAAAAI/AAAAAAAAAAA/LxzhmbfjfrA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Haley420",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/-N7qwD1rc_k8/AAAAAAAAAAI/AAAAAAAAAAA/x_Dc_nj67bI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )   		
run()
