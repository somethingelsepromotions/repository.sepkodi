# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Slave Pit TV
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

addonID = 'plugin.video.slavepit'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLcBf1NO8zlLhnOomG4h1Q_STER2p22xff"
YOUTUBE_CHANNEL_ID_2 = "UCtLpNwMBxBGGw9tC2y9Uteg"
YOUTUBE_CHANNEL_ID_3 = "PL1gtACqztO7F0SqRNipROz6T_05_H0S-D"
YOUTUBE_CHANNEL_ID_4 = "PL-YxBc2c95vOPoly-0DtAbTGYLJcuNnWJ"
YOUTUBE_CHANNEL_ID_5 = "PL-YxBc2c95vOxTyRsues5KGdjdHJbwYmf"
YOUTUBE_CHANNEL_ID_6 = "PLAB1977E05522F25D"

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
        title="GWAR",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://s1.evcdn.com/images/edpborder500/I0-001/037/855/384-8.jpeg_/gwar-84.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dave Brockie",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://s3-us-west-2.amazonaws.com/find-a-grave-prod/photos/2014/331/139272143_1417231544.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Death Piggy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://lh4.googleusercontent.com/-OvD4-pGLyRY/UJ8NHIzcgoI/AAAAAAAAD-w/A8l7T3F1pAE/s800/death%2520piggy%2520r45.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="X-Cops",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://s3.amazonaws.com/mno.products/10943/cedf9a57a6.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kepone",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://cdn.albumoftheyear.org/album/73207-ugly-dance.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="GWAR Live",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://www.40ozofhorror.com/wp-content/uploads/2014/03/40oz-of-horror-dave-brockie-oderus-urungus-gwar-500x500.png",
        folder=True )          
run()
