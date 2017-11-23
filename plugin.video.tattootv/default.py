# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Tattoo TV
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

addonID = 'plugin.video.tattootv'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLVnTuWQTqp6HZBSI0rDZCtm6PmnAOBl9R"
YOUTUBE_CHANNEL_ID_2 = "PLguGbiUyvCVhlhAZfTaFa-uKGTq-zlq38"
YOUTUBE_CHANNEL_ID_3 = "PL1s3NEPvwktE-C37OF3MsRH-6zGdcSNSn"
YOUTUBE_CHANNEL_ID_4 = "PLfgBz3-Ed98mz4gJAmoTwwspFGNyWUSyi"
YOUTUBE_CHANNEL_ID_5 = "PLuCH5f2eufabqW2CNcp1d_H16lwKwOWLE"
YOUTUBE_CHANNEL_ID_6 = "PLgQrm8Nlx5Tqo3_zB3I3Nld1J7F84PU4Z"
YOUTUBE_CHANNEL_ID_7 = "PLqQV7WsQBeWG6A5c_FGnE49yLjwj-EvS6"
YOUTUBE_CHANNEL_ID_8 = "PL71sZc11FwRI3TeXO1-0oR4Tut5O1pnCf"
YOUTUBE_CHANNEL_ID_9 = "PLXUBfJihF4_ANyywQqvAjrZOrcQnA9HFa"
YOUTUBE_CHANNEL_ID_10 = "PL4l2sFv5KGn-1qGgfaXVHc8Mv-f-JPI81"
YOUTUBE_CHANNEL_ID_11 = "PLRUSMfDZASkhwnKzQqjIHTl8iEwagX5-g"
YOUTUBE_CHANNEL_ID_12 = "PLVJmhNShcTWHSjJdd5-pVf_qrGdWpSZbv"
YOUTUBE_CHANNEL_ID_13 = "PLPHAb8S-VgToriyfX2RSW0DwIfPrCyywu"
YOUTUBE_CHANNEL_ID_14 = "PL_XVZxuDjuiO_bqvAqcrVRC4-48vCqfDh"
YOUTUBE_CHANNEL_ID_15 = "PLjanefNf_lUv9WWLcqJYoizOk3Ah7akzX"
YOUTUBE_CHANNEL_ID_16 = "UChW1Gcg7rg-ogYXIL32ZDYw"
YOUTUBE_CHANNEL_ID_17 = "PLySyf9o9olPlGWXgVHaTF9F_JI5DQaWZo"

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
        title="America's Worst Tattoos",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://static.tvgcdn.net/feed/1/481/thumbs/12445481_1200x1600.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bad Ink",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://images.zap2it.com/assets/p10087439_b_h3_aa/bad-ink.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Best Ink",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://is4.mzstatic.com/image/thumb/Video6/v4/a0/33/77/a0337704-ef7b-cf6f-a309-e709547ae7c9/mzl.sbjxyzxn.jpg/600x600bb-85.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Black Ink Crew: Chicago",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/51qdksIyYJL.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Black Ink Crew",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://is1.mzstatic.com/image/thumb/Features/v4/7f/ee/88/7fee88aa-898a-74a8-bda8-04c129f7343d/mza_3770173940138850056.jpg/600x600bb-85.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Epic Ink",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://i.pinimg.com/originals/2c/d8/9e/2cd89e2f6e315c324842caffd2567b97.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Inked",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://is4.mzstatic.com/image/thumb/Features/94/36/38/dj.qdmsmekr.jpg/600x600bb-85.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ink Master",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://is4.mzstatic.com/image/thumb/Video1/v4/8d/82/89/8d8289f8-f38e-550a-bf63-138bcac3d108/mzl.tfwnfhzj.lsr/600x600bb-85.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Just Tattoo of Us",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://www.mtv.com.au/sites/default/files/styles/image-w-1200-h-600-scale-crop/public/mtv_au/arc/2017/09/11/984dec53-eea3-4af2-b4fb-e2d7e0490c0c.jpg?itok=P54YIS2F",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="LA Ink",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://is1.mzstatic.com/image/thumb/Video/13/67/6b/mzl.zytfgxej.jpg/600x600bb-85.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="London Ink",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://a3-images.myspacecdn.com/images03/3/169c2c41885848b18a298872f622cff2/600x600.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Miami Ink",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://soseriadosdetv.com/wp-content/uploads/2010/04/miami-ink.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NY Ink",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://www.marvinblunte.com/wp-content/uploads/2013/09/ny-ink-82.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tattoo Fixers",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="http://www.wearebarnsley.com/assets/images/image_library/16322.jpg",
        folder=True ) 	

    plugintools.add_item( 
        #action="", 
        title="Tattoo Nightmares",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://s3-ap-southeast-2.amazonaws.com/nine-tvmg-images-prod/40/99/56/409956_457601_Tattoo%20Nightmares_TATT_ET_b_T2_t1_.jpg",
        folder=True ) 	

    plugintools.add_item( 
        #action="", 
        title="Tattoos After Dark",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://www.sonymax.co.za/sites/za.max/files/ct_series_f_primary_image/tattoos_after_dark_-_website_series_image_1600_x_900_px.jpg",
        folder=True ) 	

    plugintools.add_item( 
        #action="", 
        title="Tattoo Titans",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="http://images.zap2it.com/assets/p10103357_b_h3_ab/tattoo-titans.jpg",
        folder=True ) 			
run()