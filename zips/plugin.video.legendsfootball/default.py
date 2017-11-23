# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Legends Football League
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

addonID = 'plugin.video.legendsfootball'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "LingerieFootball"
YOUTUBE_CHANNEL_ID_2 = "UCUgNFdnPeNHb7RG0HepT5Mw"
YOUTUBE_CHANNEL_ID_3 = "UC7DOt3r6jja2zkjk8Uq8Udg"
YOUTUBE_CHANNEL_ID_4 = "UCe9ong-Ix_9EKmM1jOmriqw"

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
        title="Legends Football League Official",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-qXu3f7fZIu0/AAAAAAAAAAI/AAAAAAAAAAA/iTgpwPe20AQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Legends Football League YouTube topic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://ll-media.tmz.com/2015/11/20/1120-alli-albert-lfl-insta-3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="LFL by Project Cypher",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Legends_Football_League_Australia_-_%28Victoria_Maidens_vs_NSW_Surge%29_%2811888877965%29.jpg/240px-Legends_Football_League_Australia_-_%28Victoria_Maidens_vs_NSW_Surge%29_%2811888877965%29.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="LFL",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://www.smithsdaily.com/wp-content/uploads/2016/10/Legends-Football-League-10-Kim-Chase.jpg",
        folder=True )
run()