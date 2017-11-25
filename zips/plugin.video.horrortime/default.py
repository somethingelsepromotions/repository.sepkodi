# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Horror Time
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

addonID = 'plugin.video.horrortime'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLufg8LiU5XYqta0FFuPdSqkPgJ2qzJ8Kn"
YOUTUBE_CHANNEL_ID_2 = "PLNGnyJ_9o6-XCUsz_-14-rBSJmudTvBuE"
YOUTUBE_CHANNEL_ID_3 = "PLHiBLE5Ufcp6H-lSGKlfxdm4bByOQYig9"
YOUTUBE_CHANNEL_ID_4 = "PLeagipoZmyfkNAJE3JZKuceKw4-Xm2ea1"
YOUTUBE_CHANNEL_ID_5 = "PLIt8ZEPs3tuP7ufdK02QdvElgUOfWBrBM"
YOUTUBE_CHANNEL_ID_6 = "PLOhPiFp5_wYwVb-G0fF9_cWHW2IzPetKT"
YOUTUBE_CHANNEL_ID_7 = "PLx5G4xtzQoK9WuNr8jwgxIT4JQfZNlF38"
YOUTUBE_CHANNEL_ID_8 = "PLIh8pUIWeE65co0V203iNiFDX_6PhwJck"
YOUTUBE_CHANNEL_ID_9 = "PL1319A5B702531044"
YOUTUBE_CHANNEL_ID_10 = "PLprCz0PxKdOdl8OBeNAFyweZHztTb_XAf"
YOUTUBE_CHANNEL_ID_11 = "PLKV4SMF9hziv3wy3yVB0oBdv2Tw7Ob6Tq"
YOUTUBE_CHANNEL_ID_12 = "PLeagipoZmyfkeRSN0WxLaROusTzeL5hvZ"
YOUTUBE_CHANNEL_ID_13 = "UC9dmQUSNEtQk1arVVHl6kyA"
YOUTUBE_CHANNEL_ID_14 = "PLXBd-hdeuSMXA1DaDUwaMH9N9uERLC1U0"
YOUTUBE_CHANNEL_ID_15 = "PLt00mYu4vRK9z-vqvBkoEKVDuKsgUGV7D"
YOUTUBE_CHANNEL_ID_16 = "PLkzvgsq3ySHBduUI5DSAwpJylNKkGYjqg"
YOUTUBE_CHANNEL_ID_17 = "UCGurFxX8WOIgMfGQwkmDeSg"
YOUTUBE_CHANNEL_ID_18 = "FullHorrorcoms"
YOUTUBE_CHANNEL_ID_19 = "PLC2C9BFC77856C976"
YOUTUBE_CHANNEL_ID_20 = "PLEhyTyAAL_lI_04uzEjeugLaAun8r_SHN"
YOUTUBE_CHANNEL_ID_21 = "PLDwP2TgygfCrn84Vmjnj8d22Ph4OlGCHD"
YOUTUBE_CHANNEL_ID_22 = "PL74839542356C41F1"
YOUTUBE_CHANNEL_ID_23 = "PLoBz0LpN1Ssw_RsNYBmQao64pc3bM_qjU"
YOUTUBE_CHANNEL_ID_24 = "UCFf7fTK5YaFKQpC08cXrO5Q"
YOUTUBE_CHANNEL_ID_25 = "PL9lDxmOVB4z73aA5Bycfsc6tSYgQI_wG3"
YOUTUBE_CHANNEL_ID_26 = "TheKingsofHorror"
YOUTUBE_CHANNEL_ID_27 = "PLbK8xmS4nw-TcYVM3VFArMTDlvb40r3ck"
YOUTUBE_CHANNEL_ID_28 = "PLC0U9O4O6O5LkHrr2Oqa8Wq2K7dZ1-etQ"
YOUTUBE_CHANNEL_ID_29 = "PLSoxOXrOEl91MEKHgvGbQnjXXY7Z-MOfE"
YOUTUBE_CHANNEL_ID_30 = "PLRjk56r4fQ4-LDy1EZ8GnMqNapHAlH371"
YOUTUBE_CHANNEL_ID_31 = "PL9BBBEBC8E9F18E5A"
YOUTUBE_CHANNEL_ID_32 = "PLMbPbsn-u_g2jJwgbtv_ZOVSgvFS78WUz"
YOUTUBE_CHANNEL_ID_33 = "PLv7MWTL-Arz429W0pO2C3v5WX-xr2T8KJ"
YOUTUBE_CHANNEL_ID_34 = "PLC6dyS5uZ4TwMAcAPUhK_FIAtT7n3rVZM"
YOUTUBE_CHANNEL_ID_35 = "PLIrHuYkQyAQS49FQnEy_LBWMrTPj4kkqM"
YOUTUBE_CHANNEL_ID_36 = "PLsZQnDqnebk5WAs79Qwf-TUY9ZWoHyaid"
YOUTUBE_CHANNEL_ID_37 = "PL186807FA5E805E7A"
YOUTUBE_CHANNEL_ID_38 = "PLnL6-54XkK01zTW95mT5VeWA37Yn-F9tX"
YOUTUBE_CHANNEL_ID_39 = "PLDPBIHnPrgJyKunhKnylD-3RoAtjC5t-6"
YOUTUBE_CHANNEL_ID_40 = "PLG-xfPpSq2zB9oI4iTY29zIGbFD0tuZHG"
YOUTUBE_CHANNEL_ID_41 = "PL3y5z3uh7dT8K6eyqObDEVwBHUPHAFxmH"
YOUTUBE_CHANNEL_ID_42 = "PLKrYgoh7FfKoUDJPyaC1ZcZ6n3wDGdmam"
YOUTUBE_CHANNEL_ID_43 = "PLF0CF7768CF60C1CE"
YOUTUBE_CHANNEL_ID_44 = "PLlZYCRpn-yg6Vi7ka4RDotR9YP5zB6uR8"
YOUTUBE_CHANNEL_ID_45 = "UCAGRoTT7T1oWOAhgAQcCvfQ"
YOUTUBE_CHANNEL_ID_46 = "PLufg8LiU5XYrxtffLi3HV_MAet8mCCxbw"
YOUTUBE_CHANNEL_ID_47 = "PLSeZ6qt37vqyLGXbHeS4Ko4tfZ4qsT1ZN"
YOUTUBE_CHANNEL_ID_48 = "PLmHgXUJMN1TUtIOqNXDYVesjjWKOziQq5"
YOUTUBE_CHANNEL_ID_49 = "PLGYZOMNTIJiW1dIMjpQFICryDPX62LR-Z"
YOUTUBE_CHANNEL_ID_50 = "PLA11uteL7p_x1cipbjrVXc-dcGbRFuEew"
YOUTUBE_CHANNEL_ID_51 = "PL5Bxs0I9H5VKb6OGiKgdjBYVrZDFowYb5"
YOUTUBE_CHANNEL_ID_52 = "PLHCfKqP2kHUjfU0FuP4069ueXitcXaqL0"
YOUTUBE_CHANNEL_ID_53 = "PLVyxJvG53fqC_i9Vqo8clPDFZsPFiQ5g8"
YOUTUBE_CHANNEL_ID_54 = "PLMbPbsn-u_g2zgk1iRIEDOV5GhVPfChL8"
YOUTUBE_CHANNEL_ID_55 = "PL1j14gtz6BiurbB_jVhu_psZ6WEC8zXt0"
YOUTUBE_CHANNEL_ID_56 = "PLMbPbsn-u_g2Ys8Ch2mdJ6DveiGlMzZyF"
YOUTUBE_CHANNEL_ID_57 = "PLMbPbsn-u_g25oKyIH1Z96v4BWfOgq5bw"
YOUTUBE_CHANNEL_ID_58 = "PLSeZ6qt37vqxTrOOedrgCRwWQVe2MMAqR"
YOUTUBE_CHANNEL_ID_59 = "PLw7iIIetrizxsC6QCDcQWe_fjajuvIUv0"
YOUTUBE_CHANNEL_ID_60 = "PL1j14gtz6BiuGUi3a01JzHSXqbMODWFrH"
YOUTUBE_CHANNEL_ID_61 = "PLOX1g1HkvIdsE5eWrt3YXmOdtSdRWKJgu"


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
        title="A+++ Full Length Horror Movies!",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Alfred Hitchcock Presents",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="B Horror Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bela Lugosi Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Best Horror Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="B Movie Sci-fi Classics",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Classic African-American Horror movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Horror Creature Features",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Horror movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Horror movies (more)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Creature Features",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Creature Features (more)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Crow T Robot's Video Channel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dr. Gangrene's Creature Feature",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fantom Flix (Monster Movies, Creature Features)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Free Horror Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Frightpix",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Full Horror",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Full Horror movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Full Horror movies (more)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Full Length Classic Horror Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hammer Films (classic British horror)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Horror cartoons",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Horror Movie Archive",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="HORROR MOVIES",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kings of Horror",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kolchak: The Night Stalker",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lifetime Scary Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Low Budget Horror",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Made For TV Horror Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Maverick Movies HORROR MOVIES",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Monster Creature Feature",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Monster Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MST3K - Mystery Science Theater 3000",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Old horror and monster movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Popcornflix Horror Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Public Domain Horror Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sci-Fi/Horror B movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tales from the Crypt",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tales from the Darkside",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Outer Limits",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Twilight Zone",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Toho's Godzilla movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Troma Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TVTERRORLAND",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Vincent Price Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Vintage Horror Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Zombies, Vampires, Werewolves, and More!",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Silent horror movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Silent horror movies (more)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="1930's Horror movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="1940's Horror movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="1950's Sci-Fi/Horror Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="1960's Horror Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="1960-1979 Horror/Scary Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="1970's Horror Movies (A-Z) ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="1970's Horror Movies (more)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="1980's & 1990's Horror Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="1990's Horror Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="2000's Horror Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="2000's Horror Movies (more)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="https://archive.org/download/chasbo124_aol_Icon/icon.png",
        folder=True )	
run()