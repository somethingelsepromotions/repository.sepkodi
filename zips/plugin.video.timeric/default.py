# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Tim & Eric Kodi Add-on
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: somethingelsepromotions
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.timeric'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "TimAndEricVids"
YOUTUBE_CHANNEL_ID_2 = "TimandEricJash"
YOUTUBE_CHANNEL_ID_3 = "theidecker"
YOUTUBE_CHANNEL_ID_4 = "ericwareheim"
YOUTUBE_CHANNEL_ID_5 = "UCYB4RcgVpRpWOS9TRHkRR9w"
YOUTUBE_CHANNEL_ID_6 = "UC-uJaw9mXF1iwZGyh8pG2tQ"
YOUTUBE_CHANNEL_ID_7 = "adultswim"
YOUTUBE_CHANNEL_ID_8 = "UCgPClNr5VSYC3syrDUIlzLw"
YOUTUBE_CHANNEL_ID_9 = "UCa6X8qykISUTavVLryb_IoQ"
YOUTUBE_CHANNEL_ID_10 = "officialTIMandERIC"

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
        title="Tim & Eric Videos",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-AB3Fjg2pmgI/AAAAAAAAAAI/AAAAAAAAAAA/U-M5BTFJc6U/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tim & Eric JASH",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-n9lm4b8aafU/AAAAAAAAAAI/AAAAAAAAAAA/ddvBSgj06K0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tim Heidecker",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-s9wPE71iRiE/AAAAAAAAAAI/AAAAAAAAAAA/BdnZm_lJlUw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Eric Wareheim",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-litqGmA4mYA/AAAAAAAAAAI/AAAAAAAAAAA/ZqMBmT3uNQQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dr. Steve Brule - Topic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-JOU0zmudpK4/AAAAAAAAAAI/AAAAAAAAAAA/y9hdzXxojkU/s88-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dr. Steve Brule's Mrovies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-zXYyTnU3kjk/AAAAAAAAAAI/AAAAAAAAAAA/0p3ii2njgWM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Adult Swim",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-_78_7_OG2CY/AAAAAAAAAAI/AAAAAAAAAAA/lWy6wzoUahk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Adult Swim UK",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-_78_7_OG2CY/AAAAAAAAAAI/AAAAAAAAAAA/lWy6wzoUahk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Adult Swim Australia",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-OlISoWPPgYI/AAAAAAAAAAI/AAAAAAAAAAA/XMuyr-nxnLc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Official Tim & Eric YouTube",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-Yg2fS-ZA_HM/AAAAAAAAAAI/AAAAAAAAAAA/-krkTGKjoOM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )  		
run()
