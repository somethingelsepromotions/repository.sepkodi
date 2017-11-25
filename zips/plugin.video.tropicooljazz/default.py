# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Tropicooljazz
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

addonID = 'plugin.video.tropicooljazz'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLDD9CEC604BAAB17E"
YOUTUBE_CHANNEL_ID_2 = "PL290308DF3B6D1956"
YOUTUBE_CHANNEL_ID_3 = "PLFFE85F99286A5CC8"

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
        title="Steven Springer - TROPICOOLJAZZ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/6/69/Stevenspringer2.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Steven Springer - LIVE",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://i.ytimg.com/vi/rl2QxXTY_iA/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Steven Springer - Misc. Vids",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Stevenspringer.jpg/300px-Stevenspringer.jpg",
        folder=True )		
run()