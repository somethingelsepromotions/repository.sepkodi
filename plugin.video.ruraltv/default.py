# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Rural TV
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

addonID = 'plugin.video.ruraltv'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PL6Gvyfk2G4Y8wFh8W4ieqy8G0c7Q8mVUH"
YOUTUBE_CHANNEL_ID_2 = "UCFF7G0YisvN1Lk6sdtTrvjw"
YOUTUBE_CHANNEL_ID_3 = "UCA8x81jRzcXP1FEr4qd0krQ"
YOUTUBE_CHANNEL_ID_4 = "UChPuYbypqvZbIHtoLYqLZDg"
YOUTUBE_CHANNEL_ID_5 = "UCH3ozrsO09GljlFZ3b3MO5A"
YOUTUBE_CHANNEL_ID_6 = "UCfkjYLXDbS4hAZWaxT3BJRA"
YOUTUBE_CHANNEL_ID_7 = "UCrtCEY2csnxjkB6yhb_Znhw"
YOUTUBE_CHANNEL_ID_8 = "UCBkXiCj93GWOIVzUYA07pLw"
YOUTUBE_CHANNEL_ID_9 = "PLb7rqwP0rk2eTutb5kJAAOag6_vOLCsWV"
YOUTUBE_CHANNEL_ID_10 = "PL8b3GyuNm5fu-bRU4qF_PkSNiIA2JvSQq"
YOUTUBE_CHANNEL_ID_11 = "PLfpiwa2WZC8d5k-OZSm2lunk6UBdzDFDM"
YOUTUBE_CHANNEL_ID_12 = "PLUYDoOlvFtp9ntwJ0je5UMQazzgKFOuvG"
YOUTUBE_CHANNEL_ID_13 = "PL-YxBc2c95vMP2xSURWYW6LDavAcueBKs"
YOUTUBE_CHANNEL_ID_14 = "PL67492B3700EA9340"
YOUTUBE_CHANNEL_ID_15 = "PLUBOvPMkgVXuJZn5bHrB0RGEuLmhTcgxq"
YOUTUBE_CHANNEL_ID_16 = "RFDTVnetwork"
YOUTUBE_CHANNEL_ID_17 = "UCdvfE_3-SaVYkrW5tGapYug"
YOUTUBE_CHANNEL_ID_18 = "PLZSwZhmrV90E2S2zLb2xGh8TEuvCy-Mdp"
YOUTUBE_CHANNEL_ID_19 = "PLl3U7CZqXE6Q-Q6wKHmiZPfiM_uRtQ2im"
YOUTUBE_CHANNEL_ID_20 = "PLUoKkQ90Jz1aXnsgEJa7WaQTeRNr-i_C7"
YOUTUBE_CHANNEL_ID_21 = "PLmIM-zrfEzVhTyLkoK-b_57stjMnbfBf7"
YOUTUBE_CHANNEL_ID_22 = "UCK_cT_jhcxJC3x_FTsR6NHg"
YOUTUBE_CHANNEL_ID_23 = "TheOfficialNASCAR"
YOUTUBE_CHANNEL_ID_24 = "PL3mcE8pqA9V9IYFjSdXcU3ShE2Yfg7Oy-"
YOUTUBE_CHANNEL_ID_25 = "UClYMFaf6IdjQnZmsnw9N1hQ"
YOUTUBE_CHANNEL_ID_26 = "PLgRIUpznqq_wmI5QvJ3ODxHmVYZkjWE3c"
YOUTUBE_CHANNEL_ID_27 = "PLxIXtwELHFPSx1tG53rXrQD6hxGToH-Cu"
YOUTUBE_CHANNEL_ID_28 = "PLG-H7FrlXrSXgdTxXfyJk7Ktv0MKYJOU5"
YOUTUBE_CHANNEL_ID_29 = "PL-YxBc2c95vM314C63UmdoI93vjoUBYVe"
YOUTUBE_CHANNEL_ID_30 = "PLugVUuworRQWqjiuxPRwR4BkJlzRAHKpA"
YOUTUBE_CHANNEL_ID_31 = "UCCDi3eNZhIR4C2ML9kOzkgQ"
YOUTUBE_CHANNEL_ID_32 = "PL6fJmjt84zZiWk6e8mBtjFUU2PCVcO_I6"

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
        title="Hee-Haw",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/74/c5/29/74c529df1c345791c213dc4e39f5a5e9--vintage-lunch-boxes-hee-haw.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Beverly Hillbillies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://farm9.static.flickr.com/8590/16176303652_92beaa2c84_z.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Petticoat Junction",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/70/a8/38/70a83880b38b18e067340f779796a93b.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Green Acres",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/564x/01/ca/13/01ca132a1a39a78c5b4182a102f1b8a3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Andy Griffith Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/2c/89/4e/2c894e03d2a57aea5e5ac75a5661f6f2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mayberry R.F.D.",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/98/c1/e7/98c1e7a8032912003ad3cfcc400c9490.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Gomer Pyle, U.S.M.C.",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/63/43/62/634362e88b8293512fb62fdea5c1d51f.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dusty's Trail",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/2a/ac/6c/2aac6c4270c898cf1d2b7782d814e6e2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hillbilly TV",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://rlv.zcache.com/hillbilly_square_sticker-ra5ef4f3a32c54bc0a3345ca5574db731_v9wf3_8byvr_324.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Deputy Dawg cartoons",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://i.dailymail.co.uk/i/pix/2011/07/13/article-2014322-0CFEB68D00000578-231_233x344.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Grand Ole Opry and old country music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://s3.evcdn.com/images/edpborder500/I0-001/004/144/074-1.jpeg_/grand-ole-opry-house-74.jpeg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Town Hall Party",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://direct.rhapsody.com/imageserver/images/Alb.238414240/500x500.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Li'l Abner",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/61dXMZsLwXL._SS500.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Snuffy Smith cartoons",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/61iojqv-XAL.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Real McCoys",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/bc/96/e8/bc96e829bf864c1f831fa6427207b7a6.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="RFD-TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://pbs.twimg.com/profile_images/621808900317310976/7eJ5ytnD.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Classic Country TV Shows",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-ytQuPV3acpM/AAAAAAAAAAI/AAAAAAAAAAA/xLzvj_BrcMk/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Westerns",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="http://www.filmsite.org/images/westerns-genre.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Westerns - more",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="http://www.filmsite.org/images/westerns-genre.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="The Lone Ranger",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Lone_Ranger_and_Tonto_1956.jpg/220px-Lone_Ranger_and_Tonto_1956.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Mud Bogging",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="http://www.offroadstyles.com/wp-content/uploads/2015/10/mud-trucks-wet-wild-nasty-215x215.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Monster Trucks",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/e0/e3/3a/e0e33afeffafc383f8bd34caf98ff09a.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="NASCAR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="http://www.mancavegiant.com/image/cache/catalog/NASCAR%20Logo-500x500.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Southern Rock",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://img5.bestservice.de/pic_500x500/southern_rock.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Country Music",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="http://pictures.directnews.co.uk/liveimages/Listen-to-country-music-with-Toby-Keith-in-Cincinnati_16000851_801569301_0_0_14062723_500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Southern Cooking",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="http://s3.evcdn.com/images/edpborder500/I0-001/036/520/490-6.jpeg_/cooking-chef-wells-southern-classics-southern-cuis-90.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tex Ritter's Ranch Party",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="http://direct.rhapsody.com/imageserver/images/Alb.206998556/500x500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dukes of Hazzard",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="http://pisces.bbystatic.com/image2/BestBuy_US/images/products/1887/18870058_sa.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Movies and Tv misc.",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/564x/ea/a2/ae/eaa2ae317448b0c3a1d79dde35b86f53.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mater's Tall Tales",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/61ixXN7nuPL._SX258_BO1,204,203,200_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Blue Collar Comedy Tour",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="http://direct.rhapsody.com/imageserver/images/Alb.10773509/500x500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bonanza",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/5f/40/7b/5f407bd3b2ad6f8b8d33ceffffc98935.jpg",
        folder=True )          
run()
