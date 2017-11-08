# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Puppies & Kittens
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

addonID = 'plugin.video.puppieskittens'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCgRK4d4iF4OoPeOpWjYbSWA"
YOUTUBE_CHANNEL_ID_2 = "PLjkv7a2uvGrOQSfeicPzaUiGxgrW3mODg"
YOUTUBE_CHANNEL_ID_3 = "UC4BNk-D2EP0vsJrhavO6u5g"
YOUTUBE_CHANNEL_ID_4 = "UCUde4BF5-YaVxIwLnK2TT7Q"
YOUTUBE_CHANNEL_ID_5 = "PL5075BB69F757047E"
YOUTUBE_CHANNEL_ID_6 = "PLo-J_W78GbMM3uHAD2DXQEzkKa4Ih91yJ"
YOUTUBE_CHANNEL_ID_7 = "PLQ98Je3UTdzO8-jpaa-7EDFo55wEou7Ew"
YOUTUBE_CHANNEL_ID_8 = "Funnycatsandnicefish"
YOUTUBE_CHANNEL_ID_9 = "PLJHfedoaM2Z1OdIjmqH8nUEhpktnT4g8Y"

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
        title="Cute Puppies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://cdn.akc.org/content/article-body-image/pwc_cute_puppies.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Puppy Bowl",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://cdn.funcheap.com/wp-content/uploads/2016/01/Puppy-Bowl-X11-550x367.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny Puppies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://dompict.com/wp-content/uploads/2016/09/Funny-Puppies-32-Pictures-27.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cute Puppies & Kittens",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://kindofpets.com/wp-content/uploads/2017/03/cute-puppies-and-kittens-sleeping-xxu9je4v.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Too Cute Puppies & Kittens",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://i.pinimg.com/736x/41/1a/b2/411ab2ed4bbe1291e63f36b8622c333d--bestfriends-bff.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Puppies & Kittens Playing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://i.pinimg.com/originals/9d/07/89/9d078990c70173586b6a20480e5179ce.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Kittens Playing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://i.pinimg.com/736x/50/84/56/50845636673ece7c955e106316ff6575--ragdoll-kittens-for-sale-ragdoll-cats.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny Cats",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://i.ytimg.com/vi/tntOCGkgt98/maxresdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Funny Cats & Kittens",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://i.pinimg.com/originals/27/5e/1e/275e1e2059688a095681750199d91146.jpg",
        folder=True )
run()
