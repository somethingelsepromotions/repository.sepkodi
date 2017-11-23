# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Muruga Booker Kodi Add-on
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

addonID = 'plugin.video.muruga'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLIaMblqx8_LRUUbOyrjnkHIq8sfj4K54j"
YOUTUBE_CHANNEL_ID_2 = "PL-YxBc2c95vN3yCE7b0k3ijiy8MJNHtPm"
YOUTUBE_CHANNEL_ID_3 = "PL-YxBc2c95vOP6tftdBVdN_Xr_jecPIy8"
YOUTUBE_CHANNEL_ID_4 = "UCdZ9seZpR-NXZrUsfRGT47A"
YOUTUBE_CHANNEL_ID_5 = "PL0mUtlMiVGlKhU_z6LpOjnp1EL6nQvv8B"
YOUTUBE_CHANNEL_ID_6 = "PLuZmy2Hkmza6TKKuybCPNuor4M5_Z0VVK"
YOUTUBE_CHANNEL_ID_7 = "UCFxLw4-pZUsogw6u2-G3Sfw"
YOUTUBE_CHANNEL_ID_8 = "PLzSebjYuPXFAFJIw5NmEBW4YMBy__tS77"
YOUTUBE_CHANNEL_ID_9 = "UCwINhFMS7gagnow7T6SWCSQ"
YOUTUBE_CHANNEL_ID_10 = "PLJIO7B1_meO7spfTzOxb9XqVRpiZ6MFwi"
YOUTUBE_CHANNEL_ID_11 = "PL94gOvpr5yt0MDqDicFocbDkxPJ_f-2MB"
YOUTUBE_CHANNEL_ID_12 = "PL3FCC0A6CB27D4F6A"
YOUTUBE_CHANNEL_ID_13 = "UCGZ-ePa-J8bm_TfglDQYWkg"
YOUTUBE_CHANNEL_ID_14 = "swamisatchidananda"
YOUTUBE_CHANNEL_ID_15 = "PLwAgHfohwx3M94BwD1XeE7pO9QmNGgjNb"
YOUTUBE_CHANNEL_ID_16 = "UClFqxn5XaoVWvM6_DTqLiKw"
YOUTUBE_CHANNEL_ID_17 = "UCQxOXo5wtbcwyykPPlqryRQ"
YOUTUBE_CHANNEL_ID_18 = "UCMffWWA3fYjk4-9f_kYfe9A"
YOUTUBE_CHANNEL_ID_19 = "PLCS_7kqUshalIkWNwW1Wbz8t96msiZvTz"
YOUTUBE_CHANNEL_ID_20 = "PLbQPZvjEIgtdDMwU-tXvYdZS7hJaTdJbI"
YOUTUBE_CHANNEL_ID_21 = "UCtxum8RNo3iBPhthXo96GZQ"
YOUTUBE_CHANNEL_ID_22 = "UCCHKkq9MfwAccClcx3H1cyg"
YOUTUBE_CHANNEL_ID_23 = "UCJDnNZDlS-LilZBIvtDa1yg"
YOUTUBE_CHANNEL_ID_24 = "PLaX49E2UzwMOPG60AQjDSxRwpoLevTOkX"
YOUTUBE_CHANNEL_ID_25 = "PLu_npSo2nvWQ8h_Jd2hyOTaeLAQ7dTZrE"
YOUTUBE_CHANNEL_ID_26 = "petermadcatruth"
YOUTUBE_CHANNEL_ID_27 = "PL25D78167BA8CF788"
YOUTUBE_CHANNEL_ID_28 = "PLtNYLAzl4TDAYv8m2P6djlTJzsnU53Ut5"
YOUTUBE_CHANNEL_ID_29 = "UCf6eLh8BuGAsoHmXWbUjZRw"
YOUTUBE_CHANNEL_ID_30 = "PLfzC89ikxchHkn8CeHGH-MdS-15_-AFex"
YOUTUBE_CHANNEL_ID_31 = "PLDbK85zheU8_nPwWYrCMMoWMdCZrG4kEC"
YOUTUBE_CHANNEL_ID_32 = "PL_liV6xOclMFnYIzOtGa_cHDYhdpLVvmT"
YOUTUBE_CHANNEL_ID_33 = "PL-op_9uvotoTQ9EFJQAMmSURD_Ufk8uwO"
YOUTUBE_CHANNEL_ID_34 = "PL560MDU_6sj-8--0ZN5bCf8LORf_DOEQX"
YOUTUBE_CHANNEL_ID_35 = "PLRa6LzyWvvOd9g0kMX2g9r8b0CxQvQYkq"
YOUTUBE_CHANNEL_ID_36 = "UC2KNu2UscnS4d_xRGw1Sf2w"
YOUTUBE_CHANNEL_ID_37 = "PLDD9CEC604BAAB17E"
YOUTUBE_CHANNEL_ID_38 = "PL-KqxyRbNyKA1GcZ154LwpE0bndg4h9ER"



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
        title="visit http://murugabooker.bandcamp.com",
        url="http://murugabooker.bandcamp.com",
        thumbnail="",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="",
        url="",
        thumbnail="",
        folder=True )		
		
    plugintools.add_item( 
        #action="", 
        title="Muruga Booker",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://f4.bcbits.com/img/a2720974756_16.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Muruga Booker misc.",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://f4.bcbits.com/img/a1820254432_16.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Muruga and The Cosmic Hoedown Band (Featuring Tony Strat PFunk Thomas)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://f4.bcbits.com/img/a1546511187_16.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Low Rocks",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://images.45cat.com/low-rocks-blueberry-jam-sabre-detroit.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Thunder Rocks",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://e.snmc.io/lk/f/a/99f860804b8ad1c82afb51aba695db05/2439193.jpg",
        folder=True )        

    plugintools.add_item( 
        #action="", 
        title="Merl Saunders and The Rainforest Band",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://www.panicstream.net/vault/wp-content/uploads/2012/04/merl_lorez.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Merl Saunders",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://i.scdn.co/image/4106a1a85aad6d607c87302e64c48aed5ec96553",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Woodstock",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/b/b7/Woodstock_poster.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Perry Robinson",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51gPFIelLuL._SY344_BO1,204,203,200_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="James Gurley",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://longshotsblues.files.wordpress.com/2009/12/46gurley1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Weather Report - Sweetnighter",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/3/36/WRsweetnighter.jpg/220px-WRsweetnighter.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Dave Brubeck",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/M/MV5BMTM1NTc0NTAyOF5BMl5BanBnXkFtZTcwMzMyODE4OA@@._V1_UY317_CR13,0,214,317_AL_.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Jerry Garcia",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://jerrygarcia.com/wp-content/uploads/musicians/JerryGarcia_200.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Swami Satchidananda",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://www.biographyonline.net/imported-static/spiritual/satchidananda/satchidananda3.JPG",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Prem Das",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://f4.bcbits.com/img/a0739216482_10.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="David Peel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://lastfm-img2.akamaized.net/i/u/avatar300s/3138116df1604e348c08bc5d45a78d0a.gif",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Babatunde Olatunji",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Babatunde_Olatunji.jpeg/220px-Babatunde_Olatunji.jpeg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Sikiru Adepoju",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="http://www.sikiru.com/sikiru.04.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Buzzy Linhart",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="http://www.mwe3.com/reviews/images/Buzzy3.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Badal Roy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://i2.wp.com/www.yarlungrecords.com/wp-content/uploads/2016/09/roy-1.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="George Clinton",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="http://static.tvtropes.org/pmwiki/pub/images/georgeclinton.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Parliament Funkadelic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://www-tc.pbs.org/independentlens/parliamentfunkadelic/images/music_toppic.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Garry Shider",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="http://www.guitarnewsdaily.com/wp-content/uploads/2010/06/garry_shider.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Tony Strat Thomas",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="http://georgeclinton.com/pfunk/wp-content/uploads/2012/08/Tony-Thomas-220x220.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="John Lee Hooker",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://cps-static.rovicorp.com/3/JPG_400/MI0002/749/MI0002749029.jpg?partner=allrovi.com",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Peter Madcat Ruth",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://i.pinimg.com/originals/7c/f0/1e/7cf01edfcb392c80742d6e81abb5e935.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Brenda Lee",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://e.snmc.io/lk/f/a/f7d67b0af79126a4d5fa3b4793ce3e39/3654574.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Billy Davis Rhythm Machine",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://a2-images.myspacecdn.com/images03/35/3a6fcc8e758b411fbd479a4af704caa1/300x300.jpg",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Cosmic Knot",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="http://www.grnow.com/wp-content/uploads/2017/07/3927bfdd97006089ebc0a4e5d9922a9f.jpg",	
        folder=True ) 	

    plugintools.add_item( 
        #action="", 
        title="Jim and Jean",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="http://www.ciscohouston.com/images/other/changes.jpg",
        folder=True ) 	

    plugintools.add_item( 
        #action="", 
        title="Paul Winter Consort",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://lastfm-img2.akamaized.net/i/u/174s/14e031c97b2b45cf8ac27bd686df5849.png",
        folder=True ) 	

    plugintools.add_item( 
        #action="", 
        title="Tim Hardin",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://i.pinimg.com/736x/9b/9d/e7/9b9de746debf8db30b3d7cccc2c2af9e--folk-artists-white-man.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Sly Stone",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://e.snmc.io/lk/f/a/4c10328fede6252267ac076673070d50/1122356.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Dick Wagner",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://static.independent.co.uk/s3fs-public/styles/article_small/public/thumbnails/image/2014/07/31/12/Dick-Wagner-Getty.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Don Was Detroit All-Star Revue 2015",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://i.pinimg.com/236x/84/29/e0/8429e0858ad5b7c052230c907fa55915--all-star-bullets.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mighty Michael",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://i.ytimg.com/vi/qZr5hVVQlJc/maxresdefault.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Steven Springer Tropicoljazz",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/6/69/Stevenspringer2.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="John Lee Hooker - Detroit Tube Works 1970",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://i.pinimg.com/736x/e7/09/57/e709577604b8ff543ac2621afa13bdd3.jpg",
        folder=True )			
run()
