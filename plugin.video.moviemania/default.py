# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Movie Mania by something else promotions
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

addonID = 'plugin.video.moviemania'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "TimelessClassicMovie"
YOUTUBE_CHANNEL_ID_2 = "UC4QiKNSkOJ7n7yzmawGN4uA"
YOUTUBE_CHANNEL_ID_3 = "TheVideoCellar"
YOUTUBE_CHANNEL_ID_4 = "PizzaFlix"
YOUTUBE_CHANNEL_ID_5 = "TimelessClassicFilms"
YOUTUBE_CHANNEL_ID_6 = "cinenet"
YOUTUBE_CHANNEL_ID_7 = "GreatMoviesClassics"
YOUTUBE_CHANNEL_ID_8 = "ScreenMediaPictures"
YOUTUBE_CHANNEL_ID_9 = "UCYHHgSLnAvhpGszOpZZwnbg"
YOUTUBE_CHANNEL_ID_10 = "UCg6g3bL8VA40rxxJNXGeT8A"
YOUTUBE_CHANNEL_ID_11 = "UCo_k2NnprMHfCsOQjAZUdQA"
YOUTUBE_CHANNEL_ID_12 = "PDMotionPictures"
YOUTUBE_CHANNEL_ID_13 = "PublicDomainFilms27"
YOUTUBE_CHANNEL_ID_14 = "R4185"
YOUTUBE_CHANNEL_ID_15 = "UCU4LOefXf1Q2ZXsOIdsxQtA"
YOUTUBE_CHANNEL_ID_16 = "FilmNoirTV"
YOUTUBE_CHANNEL_ID_17 = "timelesswesternmovie"
YOUTUBE_CHANNEL_ID_18 = "FullHorrorcom"
YOUTUBE_CHANNEL_ID_19 = "TheKingsofHorror"
YOUTUBE_CHANNEL_ID_20 = "FreePDCartoons"
YOUTUBE_CHANNEL_ID_21 = "UCehvTncVj1nqBV1YriXsLsQ"
YOUTUBE_CHANNEL_ID_22 = "Tromamovies"
YOUTUBE_CHANNEL_ID_23 = "troma"

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
        title="Timeless Classic Movies",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-59bxvAQY0FU/AAAAAAAAAAI/AAAAAAAAAAA/bWmE_eGapCk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Interesting Films",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-GJ8gp45aRnU/AAAAAAAAAAI/AAAAAAAAAAA/IMnMdEaEVU4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Video Cellar",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-wUUsZatv4IU/AAAAAAAAAAI/AAAAAAAAAAA/ilplpO9VKf0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="PizzaFlix",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-1XPQgwWQHkA/AAAAAAAAAAI/AAAAAAAAAAA/Dv47-1UZMrk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Timeless Classic Films",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/--2UtXIRXjMw/AAAAAAAAAAI/AAAAAAAAAAA/2rue_pLv5oc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CiNENET",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-4PaF-kMXwvc/AAAAAAAAAAI/AAAAAAAAAAA/UYnCs4kSqJc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Great Movies Classics",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-UKNJXMHjj4s/AAAAAAAAAAI/AAAAAAAAAAA/Hy_idXBRYf8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Popcornflix",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-TPRe44ON5Dk/AAAAAAAAAAI/AAAAAAAAAAA/9lughaXz_Fc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="RBM Pictures",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-2ORe1xqvAIQ/AAAAAAAAAAI/AAAAAAAAAAA/p5pmqx9wpG8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MyFlix",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-TpjU-WIi724/AAAAAAAAAAI/AAAAAAAAAAA/_6rBGQwr9kU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Prelinger Archives Popular Videos",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://pbs.twimg.com/profile_images/717127559134056448/BYGRuZmj.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Public Domain Motion Pictures",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-_jlKhtZpLQU/AAAAAAAAAAI/AAAAAAAAAAA/WFaklTnhntM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Public Domain Films",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-pL2xfVBR8Nc/AAAAAAAAAAI/AAAAAAAAAAA/hkYWWLJnMNI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Public Domain Movies",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-n8m8WcjMzb4/AAAAAAAAAAI/AAAAAAAAAAA/3lWpdn6BsjQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="Cult Medium",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-f1jLZLcuQdI/AAAAAAAAAAI/AAAAAAAAAAA/48eIn3iwsfg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Timeless Film Noir Movies",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-zyCdYh_YSRM/AAAAAAAAAAI/AAAAAAAAAAA/9g1UdR4IBxY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Timeless Western Movies",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-VAmN310PZsY/AAAAAAAAAAI/AAAAAAAAAAA/4wsYX-3YuDg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Full Horror",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-Y2CXkDfA2jo/AAAAAAAAAAI/AAAAAAAAAAA/7gl5qWST43w/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Kings of Horror",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-kQJTY1j3FwM/AAAAAAAAAAI/AAAAAAAAAAA/WYLXCrtBTGE/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cartoons Free Public Domain",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-Aj5WJ-4gbv8/AAAAAAAAAAI/AAAAAAAAAAA/RkQHvcBWdwE/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Classic TV Shows",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/-ed1fMrhGM6w/AAAAAAAAAAI/AAAAAAAAAAA/lJqL3zM1DiQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Troma Movies",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://yt3.ggpht.com/-gBONxhdfYoY/AAAAAAAAAAI/AAAAAAAAAAA/3subBtYL_os/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Troma Universe",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://yt3.ggpht.com/-YbtE7h0a_iU/AAAAAAAAAAI/AAAAAAAAAAA/x0J_F74rOEg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
run()
