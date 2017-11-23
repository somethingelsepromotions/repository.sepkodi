# -*- coding: utf-8 -*-
#------------------------------------------------------------
# relaxation
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

addonID = 'plugin.video.relaxation'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLZjJ5RM4zE4QHYkUSfdfdNng6lvlgfoot"
YOUTUBE_CHANNEL_ID_2 = "Relax321Relaxing"
YOUTUBE_CHANNEL_ID_3 = "UCDtynufG2PYl8_t2zVvFm7g"
YOUTUBE_CHANNEL_ID_4 = "FLhgnzDd1DpRMOnMMvDH4TAw"
YOUTUBE_CHANNEL_ID_5 = "UCnj31fpPRsSJLchEKMEChrw"
YOUTUBE_CHANNEL_ID_6 = "PLb09q0R7gAwQ3ou1lUWZcJZEtgNeoJNJf"
YOUTUBE_CHANNEL_ID_7 = "UC6DwsFKHx-2H8waTHUP5N4Q"
YOUTUBE_CHANNEL_ID_8 = "UCWaZJ2Mu5zjfhZoEEMxs1MQ"
YOUTUBE_CHANNEL_ID_9 = "UCphOK9NiPE6qnj9Mp9aHWZg"
YOUTUBE_CHANNEL_ID_10 = "PLUKEyWe_h29wySYJPZPFTrSSD_ZIe2lWW"
YOUTUBE_CHANNEL_ID_11 = "PLUKEyWe_h29zspHg7a9VjWH3kzQxN4Zdb"
YOUTUBE_CHANNEL_ID_12 = "PLKVr8wLpcCezOSlJzFXhZpOJSFEk5S6W9"
YOUTUBE_CHANNEL_ID_13 = "UCll_bPd_hXXuns4_cd_GYcQ"
YOUTUBE_CHANNEL_ID_14 = "UC6WJQjnXNj_DL1BEgjzysdw"
YOUTUBE_CHANNEL_ID_15 = "UCN4vyryy6O4GlIXcXTIuZQQ"
YOUTUBE_CHANNEL_ID_16 = "UCdPhziOA6JLS_umQfh80rSg"
YOUTUBE_CHANNEL_ID_17 = "UCqPYhcdFgrlUXiGmPRAej1w"
YOUTUBE_CHANNEL_ID_18 = "PLZoDGrriQgsI7aatwbJZGTVNuZPtQyliv"
YOUTUBE_CHANNEL_ID_19 = "UCLs4IKoo9ByJ3IQS6u0pRRw"
YOUTUBE_CHANNEL_ID_20 = "UC_A2DlEYUTzmIluMvwJ3Ugg"
YOUTUBE_CHANNEL_ID_21 = "UCJa4jSLgxtsdnD8J9zdmZGA"
YOUTUBE_CHANNEL_ID_22 = "laurenlouisefenton"
YOUTUBE_CHANNEL_ID_23 = "EdensCloset"
YOUTUBE_CHANNEL_ID_24 = "ManifestoMeditations"
YOUTUBE_CHANNEL_ID_25 = "UCjf5RYy2xntkYRMITw0X0FA"
YOUTUBE_CHANNEL_ID_26 = "UCM7XCXnxtYJkkMN0zf0tsSw"
YOUTUBE_CHANNEL_ID_27 = "meditationrelaxclub"
YOUTUBE_CHANNEL_ID_28 = "organicheart"
YOUTUBE_CHANNEL_ID_29 = "UCqWB6EseWbMKnzunyewBDqg"
YOUTUBE_CHANNEL_ID_30 = "UCgg-bH_HR8QJGSxhqUhNxKQ"
YOUTUBE_CHANNEL_ID_31 = "TheMeditativeMind"
YOUTUBE_CHANNEL_ID_32 = "MichaelSealey"
YOUTUBE_CHANNEL_ID_33 = "UCKp9S0rMUS1hrKTCV68Lk2w"
YOUTUBE_CHANNEL_ID_34 = "MrKriswelshlifecoach"
YOUTUBE_CHANNEL_ID_35 = "themiracleforest"
YOUTUBE_CHANNEL_ID_36 = "NewHorizonHolistic"
YOUTUBE_CHANNEL_ID_37 = "numeditationmusic"
YOUTUBE_CHANNEL_ID_38 = "UCJrudw3JoLikY2bkom9-Rvw"
YOUTUBE_CHANNEL_ID_39 = "PLZjJ5RM4zE4S8X3H1YP1OjVA1XYF_HAui"
YOUTUBE_CHANNEL_ID_40 = "PositiveMagazine"
YOUTUBE_CHANNEL_ID_41 = "UCxBl72R4EzfzROLp1xok4Mg"
YOUTUBE_CHANNEL_ID_42 = "PowerThoughtsclub"
YOUTUBE_CHANNEL_ID_43 = "relaxmydog"
YOUTUBE_CHANNEL_ID_44 = "UCdqTXLgppLHnPNHsWGjVhNw"
YOUTUBE_CHANNEL_ID_45 = "UCter1EdDMAWLvO2a9CUrluA"
YOUTUBE_CHANNEL_ID_46 = "UCjzHeG1KWoonmf9d5KBvSiw"
YOUTUBE_CHANNEL_ID_47 = "UCLXoDkJDC7MIRXOyP2elXBA"
YOUTUBE_CHANNEL_ID_48 = "TheHonestGuys"
YOUTUBE_CHANNEL_ID_49 = "UCF40d8ZegQXzDp_nXQ2iJFw"
YOUTUBE_CHANNEL_ID_50 = "therelaxedguy"
YOUTUBE_CHANNEL_ID_51 = "UCIhF7UphByxU9oC8L0VgmTg"
YOUTUBE_CHANNEL_ID_52 = "justtanui"
YOUTUBE_CHANNEL_ID_53 = "YellowBrickCinema"
YOUTUBE_CHANNEL_ID_54 = "UCcqmIur-b51hdIByTPIfifw"

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
        title="8 Hour Deep Sleep Meditations",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="321 Relaxing",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Best Relaxing Music",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Beyond Purpose",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Binaural Beats Sounds",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Boho Beautiful",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Bryn Madoc Meditation",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Buddha's Lounge",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Calm",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Children's Meditations",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Corys ConsciousLiving",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Debra Berndt-Maldonado",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Digital Therapy Meditation Music",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Freebird Meditations",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Great Meditation",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Interdreamer",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jason Stephenson",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Joanne D'Amico",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Joe Treacy",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kalawna Biggs",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kireiki Healing",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lauren Ostrowski Fenton",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lilian Eden",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ManifestoMeditations",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Meditation - TOPIC",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Meditation and Healing",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="meditationrelaxclub",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Meditations with Rasa Lukosiute",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Meditation Vacation",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Meditation Zen",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Meditative Mind",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Michael Sealey",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Michelle's Sanctuary",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mind Set",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Miracle Forest",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="New Horizon",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NuMeditationMusic",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Paradigm Meditations",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Paul Santisi",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Positive Magazine",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Positive Suggestion",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="PowerThoughts Meditation Club",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Relax My Dog",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Relaxing Sleep Station",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sleep Ezy Relax",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Soothing Relaxation",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Susannah Is This A Dream",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TheHonestGuys",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Relaxation Project",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Relaxed Guy",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="White Lotus",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Wiara",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="YellowBrickCinema",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ZenLifeRelax",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="http://innervisionjourney.com/wp-content/uploads/2015/02/meditator-in-circle-square.jpg",
        folder=True )     
run()