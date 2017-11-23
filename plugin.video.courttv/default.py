# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Court TV
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

addonID = 'plugin.video.courttv'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLIgZR8OlTaKDq6la94sMiTO6L4lYueRti"
YOUTUBE_CHANNEL_ID_2 = "PLXolmJcowOOs5wyuKrVoYZPRbxroMKl6-"
YOUTUBE_CHANNEL_ID_3 = "PL9HpmUncZPQ8rVeupSu2AAHWpXc8xf2Zj"
YOUTUBE_CHANNEL_ID_4 = "PLrVRzqOlulRVdcyO02d35C4eLBZO20sVN"
YOUTUBE_CHANNEL_ID_5 = "PLxh-NRtHSKrOXA6HEoCmmiGL7lbW9Ikuv"
YOUTUBE_CHANNEL_ID_6 = "PLcYVWcYmaW2IQbVvamrHY8m1eqvXeSFnP"
YOUTUBE_CHANNEL_ID_7 = "PLZAqA6c9wDEw4Q1oFdxMMmlvq9prSxp0w"
YOUTUBE_CHANNEL_ID_8 = "PLKZtrYB9Q2zSaImalxe8N72ydc5nBahBi"
YOUTUBE_CHANNEL_ID_9 = "PLNAypbVleJD6dggomGLcIFIfB4OKzzDoA"
YOUTUBE_CHANNEL_ID_10 = "PLXmB4XwtoJQB09f4fKVHBDlyYyP7UvxO4"
YOUTUBE_CHANNEL_ID_11 = "PLC4D3821A41F88BD1"
YOUTUBE_CHANNEL_ID_12 = "PLSiQljCQ9-if9TpgOr6ZerQ3oSG16GKoR"
YOUTUBE_CHANNEL_ID_13 = "PL_F0eWG4q-SCekwCWZIspZHZRK7mS7IDF"
YOUTUBE_CHANNEL_ID_14 = "PLp75MS5RKYKArXQmHw2DzIDfcq8hJov_7"

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
        title="America's Court with Judge Ross",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://tvseriesfinale.com/wp-content/uploads/2012/04/americascourt03.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Divorce Court",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://pbs.twimg.com/profile_images/771115744943759361/FQX66zl5.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Judge Alex",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://images1.houstonpress.com/imager/u/original/6748493/judge_alex_wins.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Judge Faith",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://judgefaith.com/wp-content/themes/judgefaith/images/meetjfpage_bottom.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Judge Hatchett",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://static.tvgcdn.net/feed/1/815/thumbs/11849815_1300x1733.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Judge Joe Brown",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://assets.nydailynews.com/polopoly_fs/1.2692792.1467221604!/img/httpImage/image.jpg_gen/derivatives/article_750/judge-joe-brown.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Judge Judy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://pbs.twimg.com/profile_images/3724720564/0aeb2941b9d8c493b677555f04aefdbc_400x400.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Judge Karen",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://www.nytix.com/repository/tvshows/Judge%20Karen/images/Judge-karen-2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Judge Mablean",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://www.judgemablean.com/images/about_judgepic.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Judge Mathis",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://cbscwpittsburgh2.files.wordpress.com/2012/05/judge-mathis-1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Judge Pirro",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://pbs.twimg.com/profile_images/850023968484368386/jBcIv7W1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Judge Rinder",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://digitalspyuk.cdnds.net/16/18/768x512/gallery-1462377085-judge-rinder.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lauren Lake's Paternity Court",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://dtvimages.hs.llnwd.net/e1//db_photos/showcards/v5/AllPhotos/10063603/p10063603_b_v5_aa.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The People's Court",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://pbs.twimg.com/profile_images/1301014913/PROFILE-PIC_400x400.jpg",
        folder=True ) 		
run()