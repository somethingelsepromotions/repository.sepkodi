# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Soul Cinema
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

addonID = 'plugin.video.soulcinema'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PL-KqxyRbNyKAy87-QnE06CMnW8i5gU_Ms"

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
        title="Soul Cinema",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://xenonpictures.com/wp/wp-content/uploads/2015/07/DOLEMITE-NEU.jpg",
        folder=True )
run()