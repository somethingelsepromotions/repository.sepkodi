# -*- coding: utf-8 -*-
#------------------------------------------------------------
# ASMR
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

addonID = 'plugin.video.asmr'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCgpmBgxeWvmAVge2TmmgMVA"
YOUTUBE_CHANNEL_ID_2 = "UCXlGUrdK6b3q7qBjsdPbdVw"
YOUTUBE_CHANNEL_ID_3 = "UC4XtEiJW3LaQeSxktn4Y1OA"
YOUTUBE_CHANNEL_ID_4 = "ardraneala"
YOUTUBE_CHANNEL_ID_5 = "UCEWy8hds1muv8wDGvUTzMUQ"
YOUTUBE_CHANNEL_ID_6 = "TheASMRAngel"
YOUTUBE_CHANNEL_ID_7 = "tarmax82"
YOUTUBE_CHANNEL_ID_8 = "UCikebqFWoT3QC9axUbXCPYw"
YOUTUBE_CHANNEL_ID_9 = "UCHrKd8ElaVdk7OBQAgx8JrQ"
YOUTUBE_CHANNEL_ID_10 = "UCkxeDWTtYsI0-urBdXfrwvw"
YOUTUBE_CHANNEL_ID_11 = "ASMRMASSAGESPA"
YOUTUBE_CHANNEL_ID_12 = "PPOMODOLI"
YOUTUBE_CHANNEL_ID_13 = "ASMRrequests"
YOUTUBE_CHANNEL_ID_14 = "UC7wwQl26xO9-6HLWyrhNXKg"
YOUTUBE_CHANNEL_ID_15 = "PLJEBk66LAZOqdxjURqMYR35dmTUzkIR7W"
YOUTUBE_CHANNEL_ID_16 = "UCbXFAWK8hIETUStFEazmsFA"
YOUTUBE_CHANNEL_ID_17 = "UCzGEGjOCbgv9z9SF71QyI7g"
YOUTUBE_CHANNEL_ID_18 = "PLpiIAILJvoYldw5rZ2IROoI7b_URoMTMB"
YOUTUBE_CHANNEL_ID_19 = "UC7wT_mqUvCHEIWm1cuw_T1Q"
YOUTUBE_CHANNEL_ID_20 = "BrittanyASMR"
YOUTUBE_CHANNEL_ID_21 = "UCUuENVpVuzqpRsXWIDlpQTg"
YOUTUBE_CHANNEL_ID_22 = "ChristenNoelASMR"
YOUTUBE_CHANNEL_ID_23 = "KaylaSuzette"
YOUTUBE_CHANNEL_ID_24 = "UC8HznQu5C61kSH3Q770nRxg"
YOUTUBE_CHANNEL_ID_25 = "PL8PPgRW-HCmIkfb-n2nGJEbsgcWj_oH_O"
YOUTUBE_CHANNEL_ID_26 = "dahampark"
YOUTUBE_CHANNEL_ID_27 = "UCHC6fhzmkO9pdwFwNaFvArw"
YOUTUBE_CHANNEL_ID_28 = "DianaDewAsmr"
YOUTUBE_CHANNEL_ID_29 = "UCXcxoGeRwy6Swu7enU53Tyg"
YOUTUBE_CHANNEL_ID_30 = "UCgLxqgVoonLD3dlgHSxSP_w"
YOUTUBE_CHANNEL_ID_31 = "EphemeralRift"
YOUTUBE_CHANNEL_ID_32 = "feirychaRstaRs"
YOUTUBE_CHANNEL_ID_33 = "fastASMR"
YOUTUBE_CHANNEL_ID_34 = "UC2iTMEsFHE1ZbT_Z67bu4kg"
YOUTUBE_CHANNEL_ID_35 = "UCke_bkljXoufHov7hg_bT8Q"
YOUTUBE_CHANNEL_ID_36 = "UCoNfsDH8sZe13u7rSxaEBkw"
YOUTUBE_CHANNEL_ID_37 = "GentleWhispering"
YOUTUBE_CHANNEL_ID_38 = "UCE6acMV3m35znLcf0JGNn7Q"
YOUTUBE_CHANNEL_ID_39 = "Hlvillaire"
YOUTUBE_CHANNEL_ID_40 = "HeatherFeatherASMR"
YOUTUBE_CHANNEL_ID_41 = "hermetickitten"
YOUTUBE_CHANNEL_ID_42 = "UCjyi6by44TTH0j_U3vXEGpA"
YOUTUBE_CHANNEL_ID_43 = "UCYtZTs-QU406yTaxksMyOug"
YOUTUBE_CHANNEL_ID_44 = "UCGfbWCJjPwcAlBNkHT3gQ6w"
YOUTUBE_CHANNEL_ID_45 = "UCCjpp4TCjnRftS_LenXuSHw"
YOUTUBE_CHANNEL_ID_46 = "UCx-fkMnqAC3qJHMtGL0s6Mw"
YOUTUBE_CHANNEL_ID_47 = "klunatik"
YOUTUBE_CHANNEL_ID_48 = "LauraLemureX"
YOUTUBE_CHANNEL_ID_49 = "UC4d18IlLmw0utmVxIjSadLQ"
YOUTUBE_CHANNEL_ID_50 = "MassageASMR"
YOUTUBE_CHANNEL_ID_51 = "miniyuasmr"
YOUTUBE_CHANNEL_ID_52 = "UCn967cbpOl-NisfPImHvaBg"
YOUTUBE_CHANNEL_ID_53 = "videomissasmr"
YOUTUBE_CHANNEL_ID_54 = "UCAcgAdoQPU2C8zkQgKJPJsg"
YOUTUBE_CHANNEL_ID_55 = "UCrUaEUx0_xn9dvSnEDiqDyQ"
YOUTUBE_CHANNEL_ID_56 = "PL8HDHtnV6sLVtPCMRFrMUzT1KK1YvKG_Y"
YOUTUBE_CHANNEL_ID_57 = "UC_L0kymqVJEuMmCxKqDnvqg"
YOUTUBE_CHANNEL_ID_58 = "OliviaKissperASMR"
YOUTUBE_CHANNEL_ID_59 = "UCnDpv9Qqg1OevPiCfcRnj8g"
YOUTUBE_CHANNEL_ID_60 = "UC0TIPxlCiCF1_lqsNtuxZgg"
YOUTUBE_CHANNEL_ID_61 = "UCNlMeUt5nOTQ-yfjXzRKVKA"
YOUTUBE_CHANNEL_ID_62 = "pigsbum53"
YOUTUBE_CHANNEL_ID_63 = "PLRS2fClNGXDPby_gV2dh0tg1tR9iNUZvW"
YOUTUBE_CHANNEL_ID_64 = "UCMWQbdU4kjCB49xkuQ8nYRw"
YOUTUBE_CHANNEL_ID_65 = "UCMgaC2_zNzv75eHK1sMstjQ"
YOUTUBE_CHANNEL_ID_66 = "UCoZzvWz0HELYkp7y7Rr5NpA"
YOUTUBE_CHANNEL_ID_67 = "UCosSE6We3kVMrYud9DonlQA"
YOUTUBE_CHANNEL_ID_68 = "UCFO35iymWGcpKtRpOA0MI-g"
YOUTUBE_CHANNEL_ID_69 = "UCuF6wXjkBfGkdXxSP1UGL-Q"
YOUTUBE_CHANNEL_ID_70 = "UCbmPOakEEq_W2niQ1FXF1Cw"
YOUTUBE_CHANNEL_ID_71 = "UC-r8XyqbggZobMiNsqgWkDg"
YOUTUBE_CHANNEL_ID_72 = "UCHFnhreBDU-QIEE4dp53nsQ"
YOUTUBE_CHANNEL_ID_73 = "UCaZeUYfNstV7ucycXJUDYOA"
YOUTUBE_CHANNEL_ID_74 = "UCN8_ZBeNIFA6fmII02lYD4w"
YOUTUBE_CHANNEL_ID_75 = "UC2n3UiYy_dQXaAjZ41YLF4w"
YOUTUBE_CHANNEL_ID_76 = "TheOneLilium"
YOUTUBE_CHANNEL_ID_77 = "UCV508_Yoyrr3v6M0omlLlgA"
YOUTUBE_CHANNEL_ID_78 = "UC63vOrQKSnHPhvqmEekGPOQ"
YOUTUBE_CHANNEL_ID_79 = "Asmrer"
YOUTUBE_CHANNEL_ID_80 = "UCcpRD7g0AS4aJn8x9IVl6Ew"
YOUTUBE_CHANNEL_ID_81 = "VisualSounds1"
YOUTUBE_CHANNEL_ID_82 = "UCSvDxzR4NeTLUemqvwwT9tQ"
YOUTUBE_CHANNEL_ID_83 = "WhispersRedASMR"
YOUTUBE_CHANNEL_ID_84 = "UC_keZ0Ay6COJo6i5ch3sdQw"
YOUTUBE_CHANNEL_ID_85 = "UCzsipLeHCLiFAB81hfDjnmg"

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
        title="AccidentallyGraceful ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="adreambeam",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Air Light ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ARDRA -asmr-",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ASindyMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ASMR Angel",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="ASMR Barber",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ASMR Darling",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ASMRMagic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ASMRmania",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ASMR Massage Psychetruth",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ASMR PPOMO",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ASMRrequests",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ASMRSoundSpace",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ASMR Unintentional",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Asmr Vids",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="asmr zeitgeist",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="BabyZelda ASMR",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bluewhisper",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Brittany ASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Caroline ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Christen Noel ASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cosmic Tingles ASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cutebunny992 ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dahlia Daintily",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dana ASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Darya Lozhkina ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DianaDew Asmr",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Divine Munchies ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ellie Alien ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ephemeral Rift",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fairy Char ASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="fastASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Feather Jo",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Free Spirit ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FrivolousFox ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Gentle Whispering ASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Gibi ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hailey Rose",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Heather Feather ASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hermetic Kitten",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="JoJo's ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hushed Tones ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Isabel imagination ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="JellybeanASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="JUICY TINGLES",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kluna Tik",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="LauraLemurex ASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Made In France ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MassageASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Miniyu ASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MinxLaura123 ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MissASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MissBunnyWhispers",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nature Flight",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NeonIndieGirl",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nuala Whisper",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Olivia's Kissper ASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="PassionFlower ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="PeacefulMindASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pelagea ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pigsbum53 ASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_62+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="PuddingWhispers",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_63+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="RaffyTaphyASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_64+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="RedRoseWhispers",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_65+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rhosgobel Rabbit ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_66+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Scottish Whisper",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_67+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ScratchingAsmr",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_68+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SensorAdi ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_69+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Soft Serenity ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_70+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Springbok ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_71+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sweetseductiveasmr",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_72+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="thatASMRchick",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_73+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The ASMR Circus",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_74+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="the Lull",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_75+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TheOneLilium ASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_76+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TheUKASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_77+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TheWaterwhispers",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_78+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tony Bomboni ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_79+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TouchingTingles",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_80+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="VisualSounds1 ASMR",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_81+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="WhisperingGamer094 ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_82+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="WhispersRed ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_83+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="WhisperSparkles ASMR",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_84+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="WhispersUnicorn",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_85+"/",
        thumbnail="http://asmrlovers.com/wp-content/uploads/2017/02/cropped-asmrlogo.png",
        folder=True )        
run()