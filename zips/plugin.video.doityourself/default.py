# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Do It Yourself
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

addonID = 'plugin.video.doityourself'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UC295-Dw_tDNtZXFeAPAW6Aw"
YOUTUBE_CHANNEL_ID_2 = "UC8-G2_iXfYB4dYIItBIz5iQ"
YOUTUBE_CHANNEL_ID_3 = "AprilWilkersonDIY"
YOUTUBE_CHANNEL_ID_4 = "UCm0O_rdVWuBDUsiUtjjFPOg"
YOUTUBE_CHANNEL_ID_5 = "arduinoversusevil"
YOUTUBE_CHANNEL_ID_6 = "UCVoEz9zyXcGhVV0jd9ogWiQ"
YOUTUBE_CHANNEL_ID_7 = "covoniasweetpea"
YOUTUBE_CHANNEL_ID_8 = "UCYatDPXXLYABxRud2wd09vQ"
YOUTUBE_CHANNEL_ID_9 = "UCa0I64m3RkQDTu0Fc3MDn7Q"
YOUTUBE_CHANNEL_ID_10 = "UCHnYr5Y7U7J8K2sZrpqKJ-g"
YOUTUBE_CHANNEL_ID_11 = "dewalttv"
YOUTUBE_CHANNEL_ID_12 = "UCMcQNLWedovkFTOfAb6YVKw"
YOUTUBE_CHANNEL_ID_13 = "UCM3JpqUgyoMySQTSDUc0kdA"
YOUTUBE_CHANNEL_ID_14 = "UCQcMO9mBGaMHshL0dLIr4dg"
YOUTUBE_CHANNEL_ID_15 = "UCwY7JbjRe95kbfYj4lwhV4A"
YOUTUBE_CHANNEL_ID_16 = "UCb5dy9xLXC3p-phgbNResvg"
YOUTUBE_CHANNEL_ID_17 = "UCF56eZcNOYSap9Q5PflzbGg"
YOUTUBE_CHANNEL_ID_18 = "baytlma3rifa"
YOUTUBE_CHANNEL_ID_19 = "UChKlSK39lLg8eZHIX0iVzLA"
YOUTUBE_CHANNEL_ID_20 = "Lowesradio"
YOUTUBE_CHANNEL_ID_21 = "DIYHacksandHowTos"
YOUTUBE_CHANNEL_ID_22 = "UCRqtPzGcU1jef9N3iJ5spQA"
YOUTUBE_CHANNEL_ID_23 = "UCCbO23F6aI_cX0JGGfoHYsA"
YOUTUBE_CHANNEL_ID_24 = "UCY7H4ClGM-Ko4yPYZ8Zq0ug"
YOUTUBE_CHANNEL_ID_25 = "UC-PaPywUKo7dSn800KRYqDg"
YOUTUBE_CHANNEL_ID_26 = "UCPRZAan7WcHjyDgDnpWy"
YOUTUBE_CHANNEL_ID_27 = "DIYNetwork"
YOUTUBE_CHANNEL_ID_28 = "DIYPerks"
YOUTUBE_CHANNEL_ID_29 = "UCEAY1udDi0HBnu7BbxDsJUg"
YOUTUBE_CHANNEL_ID_30 = "UCvmsdOYwO29MYFHyU_yvtLA"
YOUTUBE_CHANNEL_ID_31 = "UCmniWjCdz6ym8uNyWdYTZ3w"
YOUTUBE_CHANNEL_ID_32 = "ame112292"
YOUTUBE_CHANNEL_ID_33 = "UCzr30osBdTmuFUS8IfXtXmg"
YOUTUBE_CHANNEL_ID_34 = "frugalhomediy"
YOUTUBE_CHANNEL_ID_35 = "UCETeXD_3awsQv-9rSdCYXQQ"
YOUTUBE_CHANNEL_ID_36 = "greatscottlab"
YOUTUBE_CHANNEL_ID_37 = "greatscottlab2"
YOUTUBE_CHANNEL_ID_38 = "SektorZeit"
YOUTUBE_CHANNEL_ID_39 = "hgtvhandmade"
YOUTUBE_CHANNEL_ID_40 = "UCukV8nyC6FWgM02iDeRVAMw"
YOUTUBE_CHANNEL_ID_41 = "UCVDGs-2XL6MdjVG3PaxSZ5Q"
YOUTUBE_CHANNEL_ID_42 = "UCBVP71x4_2rxUK2b0nZ9GiA"
YOUTUBE_CHANNEL_ID_43 = "idahopainters"
YOUTUBE_CHANNEL_ID_44 = "HomeMadeModern"
YOUTUBE_CHANNEL_ID_45 = "UCP2vaEZS8MvZrFklwBtW1GA"
YOUTUBE_CHANNEL_ID_46 = "MyHometalk"
YOUTUBE_CHANNEL_ID_47 = "HouseholdHacker"
YOUTUBE_CHANNEL_ID_48 = "UCpJ1vJPFqImom-NN2fkBS0A"
YOUTUBE_CHANNEL_ID_49 = "UCfIqCzQJXvYj9ssCoHq327g"
YOUTUBE_CHANNEL_ID_50 = "UCzGbp-rRVNwyFhn9gHoZr5g"
YOUTUBE_CHANNEL_ID_51 = "IBuildItHome"
YOUTUBE_CHANNEL_ID_52 = "UCaJsEh2_YxWHMcjASs4cJcA"
YOUTUBE_CHANNEL_ID_53 = "iliketomakestuffcom"
YOUTUBE_CHANNEL_ID_54 = "UCruM8e10ljDk6VEe1XrUxQA"
YOUTUBE_CHANNEL_ID_55 = "rusticman1973"
YOUTUBE_CHANNEL_ID_56 = "UC-7XY-W_C84cW2MNqujgFpg"
YOUTUBE_CHANNEL_ID_57 = "UCiEk4xHBbz0hZNIBBpowdYQ"
YOUTUBE_CHANNEL_ID_58 = "UCDQGdvrCKyfFRqjeMEr50oQ"
YOUTUBE_CHANNEL_ID_59 = "jpheisz"
YOUTUBE_CHANNEL_ID_60 = "UCzNAswnSN0rZy79clU-DRPg"
YOUTUBE_CHANNEL_ID_61 = "UCyoGyGAMVxdGOrs9TTMXeEA"
YOUTUBE_CHANNEL_ID_62 = "UCce7vvR81qpuXqFfICoKw1g"
YOUTUBE_CHANNEL_ID_63 = "Lowes"
YOUTUBE_CHANNEL_ID_64 = "LowesForProsVideo"
YOUTUBE_CHANNEL_ID_65 = "UCPKAKrjoMz7POptCloy7AIQ"
YOUTUBE_CHANNEL_ID_66 = "UChtY6O8Ahw2cz05PS2GhUbg"
YOUTUBE_CHANNEL_ID_67 = "UCbOOTKHBOXyFfACvhGJnSCg"
YOUTUBE_CHANNEL_ID_68 = "DrunkenWoodworker"
YOUTUBE_CHANNEL_ID_69 = "UC_RbkyX5b3Fh4EGI5xYPfVw"
YOUTUBE_CHANNEL_ID_70 = "MakitaPowerTools"
YOUTUBE_CHANNEL_ID_71 = "inspiretomake"
YOUTUBE_CHANNEL_ID_72 = "UCkk7f3m8WFBnrEATX4f2q7w"
YOUTUBE_CHANNEL_ID_73 = "steveinmarin"
YOUTUBE_CHANNEL_ID_74 = "UCSp_oP2S7BZ-2OG4ZFJOzbQ"
YOUTUBE_CHANNEL_ID_75 = "METToolTV"
YOUTUBE_CHANNEL_ID_76 = "UCIxAaCJ84uefATKmazDyIjw"
YOUTUBE_CHANNEL_ID_77 = "mrfixit"
YOUTUBE_CHANNEL_ID_78 = "UCg8gyknDT6PKomqpHPFYlog"
YOUTUBE_CHANNEL_ID_79 = "MrYoucandoityourself"
YOUTUBE_CHANNEL_ID_80 = "UCawT8Xv7y2Dd9cQCoJ51xpQ"
YOUTUBE_CHANNEL_ID_81 = "nathan780409"
YOUTUBE_CHANNEL_ID_82 = "UCRw39EZZfLjbt98gJhYClpQ"
YOUTUBE_CHANNEL_ID_83 = "QUIKRETEConcrete"
YOUTUBE_CHANNEL_ID_84 = "RheemMFG"
YOUTUBE_CHANNEL_ID_85 = "RIDGIDtoday"
YOUTUBE_CHANNEL_ID_86 = "ryobichannel"
YOUTUBE_CHANNEL_ID_87 = "BonsalAmerican"
YOUTUBE_CHANNEL_ID_88 = "UCuxpxCCevIlF-k-K5YU8XPA"
YOUTUBE_CHANNEL_ID_89 = "shanty2chic"
YOUTUBE_CHANNEL_ID_90 = "rnods221"
YOUTUBE_CHANNEL_ID_91 = "Searching4Savings"
YOUTUBE_CHANNEL_ID_92 = "wpm44"
YOUTUBE_CHANNEL_ID_93 = "stevinmarin"
YOUTUBE_CHANNEL_ID_94 = "techman2015"
YOUTUBE_CHANNEL_ID_95 = "homedepot"
YOUTUBE_CHANNEL_ID_96 = "TheHomeDepotPro"
YOUTUBE_CHANNEL_ID_97 = "UCDbWmfrwmzn1ZsGgrYRUxoA"
YOUTUBE_CHANNEL_ID_98 = "UC5ncuNyZTN3OGuixQXOiAYQ"
YOUTUBE_CHANNEL_ID_99 = "UCKp44bWWZIiOPShPN_ytShw"
YOUTUBE_CHANNEL_ID_100 = "UCGkDwuvbtRZZVbWYZq-cx5Q"
YOUTUBE_CHANNEL_ID_101 = "UCO39zTYpvWL5jx2q15Ma_Hw"
YOUTUBE_CHANNEL_ID_102 = "UCXbYtx6rZlbTHg8zY9AFZ-g"
YOUTUBE_CHANNEL_ID_103 = "UCogIm6A8EdsOFtJSz5EWJ3w"
YOUTUBE_CHANNEL_ID_104 = "UCqq70AnPkj4-UApS_m_6mPw"
YOUTUBE_CHANNEL_ID_105 = "UC9pxEt_fx78OG2uccntlaqQ"
YOUTUBE_CHANNEL_ID_106 = "UCdku2KLuIVRFwx1PVnjRm1w"
YOUTUBE_CHANNEL_ID_107 = "Woodentoolcompany2"
YOUTUBE_CHANNEL_ID_108 = "knecht105"
YOUTUBE_CHANNEL_ID_109 = "UC_mcFH_r7Aq6SyQ0HrGaenQ"

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
        title="5-Minute Crafts",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="99% Do It Yourself",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="April Wilkerson",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ask the builder",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AvE",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Average Joe's Joinery",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="BIGBOY'S DIY",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Craig's DIY Car",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Crazy about DIY",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DAH - DIY AT HOME",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DEWALT TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DivingHeadFirst",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY - Crafts & Life Hacks",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY - Topic",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY Auto Repair Videos",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY Car Maintenance and Repair Guide",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY Crafts & Lifehacks",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY Creators",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY Guy",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY Hacks and How To's",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY Home & Garden Projects",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY Home",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY Home and Auto",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY Home and Garden",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY Ideas for Home and Garden",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY Network",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY Perks",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY PETE",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DIY projects - step by step",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Do It Yourself - DIY HD",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Easy DIY Beauty",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Essential Craftsman",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Frugal Home DIY",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Get Hands Dirty",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="GreatScott!",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="GreatScott!2",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Heilman Hackatronics",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="HGTV Handmade",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Home & Garden for Mere Mortals",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Home Craft Chronicles",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Home DIY ideas",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Home Improvement How To's",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="HomeMadeModern",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Home Repair Tutor",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hometalk",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="HouseholdHacker",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="House Improvements",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="How To Make Everything",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="I Build It",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="I Build It Home",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="I Build It Scrap Bin",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="I Like To Make Stuff",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="I Like To Make Stuff 2",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Inspire To Make",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_71+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="izzy swan",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jay Bates ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="jimmydiresta",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Joe Basement Woodworking & DIY",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="John Heisz",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kipkay",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="KitchenAid Appliance Repair and Maintenance Self Help Videos",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Living to DIY with Rachel Metz",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_62+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lowe's Home Improvement",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_63+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="LowesForPros",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_64+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="LRN2DIY",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_65+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Make:",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_66+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Make N' Create",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_67+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Make Something",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_68+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MakeTech",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_69+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MakitaPowerTools",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_70+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Maytag Appliance Repair and Maintenance Self Help Videos",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_72+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mere Minutes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_73+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MidwestManMountain Home & Garden DIY",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_74+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Milwaukee Tool",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_75+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Modern Builds",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_76+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mr. Fix It",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_77+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mr Maker",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_78+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mr Youcandoityourself",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_79+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NAILED IT!",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_80+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nathan's DIY Garage",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_81+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Not only Wood",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_82+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="QUIKRETE",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_83+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rheem",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_84+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="RIDGID Tools",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_85+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )           

    plugintools.add_item( 
        #action="", 
        title="RYOBI",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_86+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sakrete",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_87+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Scotty Kilmer",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_88+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Shanty2Chic",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_89+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Shop built",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_90+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SomeofThisandThat",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_91+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sparky Channel",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_92+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Steve Ramsey",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_93+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Do It Yourself World",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_94+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Home Depot",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_95+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Home Depot Pro Channel",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_96+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Post Apocalyptic Inventor",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_97+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Rehab Life",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_98+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Wood Whisperer",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_99+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The WoodWorking Junkie",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_100+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Think",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_101+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Third Coast Craftsman",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_102+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Time to DIY",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_103+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="WeldingTipsAndTricks",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_104+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Whirlpool Appliance Repair Self Help Videos",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_105+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Wood.Work.LIFE.",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_106+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Wooden Tool Man",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_107+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="WoodWorkWeb",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_108+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="YouCanMakeThisToo",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_109+"/",
        thumbnail="http://www.bojanglesmuseum.com/wp-content/uploads/2017/07/Terrific-Do-It-Yourself-Logos-27-On-Online-Logo-Maker-with-Do-It-Yourself-Logos.jpg",
        folder=True )		
run()