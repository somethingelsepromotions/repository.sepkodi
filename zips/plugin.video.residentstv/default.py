# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Residents TV
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

addonID = 'plugin.video.residentstv'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLwaWPBdommvdwMG3t5C-VGHgML6ynT7P9"
YOUTUBE_CHANNEL_ID_2 = "PL4yn92zU2slGzssyV3p_0js8ms6NsKafl"
YOUTUBE_CHANNEL_ID_3 = "PL4yn92zU2slGir-wCr_020tZJMxX9orN_"
YOUTUBE_CHANNEL_ID_4 = "PLufg8LiU5XYpDVIrG_JBvn8jmpuQQG84a"
YOUTUBE_CHANNEL_ID_5 = "UCr2xdTYrY-Q02PVebrTdgiQ"
YOUTUBE_CHANNEL_ID_6 = "PLsRabwNHm4-HAK-eDExvuEn0d0vOiEJkd"
YOUTUBE_CHANNEL_ID_7 = "PLZ4TziAfqWC1idU-8lYOBq0EqrFLidskT"
YOUTUBE_CHANNEL_ID_8 = "PL7F350937793848FA"
YOUTUBE_CHANNEL_ID_9 = "PL-Casw0NnmOXqKgSHVWkOP6HK1VEUlIMl"
YOUTUBE_CHANNEL_ID_10 = "PLQyz3G-M7WQ4PXdhdTk_ttX8f9IqwuX3p"
YOUTUBE_CHANNEL_ID_11 = "PL0xsu3P3mP8TFcQSwsuicAIxltLWVqKWp"
YOUTUBE_CHANNEL_ID_12 = "PLufg8LiU5XYplSb_VEPvX98_S8hmgxDY0"

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
        title="The Residents and Ralph Records",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://www.residents.com/historical/media/image/RalphRecords.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Residents top tracks",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://www.metroactive.com/papers/cruz/10.23.02/gifs/residents-0243.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Residents popular videos",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://a1-images.myspacecdn.com/images03/35/b3e2ce0a5e92420d9a03ccdb80cb3592/300x300.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Residents (misc)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://i.pinimg.com/236x/18/b0/bc/18b0bc435102268e84055083d44cea8f--the-residents-music-videos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Residents topic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://i.pinimg.com/736x/73/33/84/7333845a305f22cbf23f9191e1f757f4--the-residents-california-usa.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Commecial DVD",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51Q03V1V6WL.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Icky Flix DVD",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Icky_Flix.jpg/220px-Icky_Flix.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Freak Show Special Edition",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://www.residents.com/historical/media/image/FreakShowMute.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Snakefinger",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/5/52/Snakefinger1.jpg/220px-Snakefinger1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="N. Senada",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://vignette.wikia.nocookie.net/the-residents/images/1/12/N._Senada_at_the_boarding_house_1971.jpg/revision/latest?cb=20140310215210",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Charles Bobuck Contraption",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://e.snmc.io/lk/l/s/524f54b2f76671e73bc814748de665f8/5944928.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Homer Flynn",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://68.media.tumblr.com/2ac60c07cc8fe4635f5c7af66b6dbcf0/tumblr_mmbw8gd7Dj1spn6xyo1_500.jpg",
        folder=True )		
run()
