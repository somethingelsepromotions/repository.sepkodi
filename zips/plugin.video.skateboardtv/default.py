# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Skateboard TV
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

addonID = 'plugin.video.skateboardtv'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCvhWO9QAgk1TRtdluCnar1g"
YOUTUBE_CHANNEL_ID_2 = "UCwhxKJw-PLlKXeferOK6spQ"
YOUTUBE_CHANNEL_ID_3 = "UCwhxKJw-PLlKXeferOK6spQ"
YOUTUBE_CHANNEL_ID_4 = "PLJsR_-Ha0Sr3_eLIhq6sIs7my7vb9o9T3"
YOUTUBE_CHANNEL_ID_5 = "veganxbones"
YOUTUBE_CHANNEL_ID_6 = "PLiEINnZsanNTUzTUrE6y7wHOKBsZUDfBX"
YOUTUBE_CHANNEL_ID_7 = "PLWY-HIjYpdV-Rk9XmQ_I3692XQAUcVcMR"
YOUTUBE_CHANNEL_ID_8 = "UC3qRxKsV1GeG0RsSP9MR6gA"
YOUTUBE_CHANNEL_ID_9 = "UCwhxKJw-PLlKXeferOK6spQ"
YOUTUBE_CHANNEL_ID_10 = "skateboardermagazine"
YOUTUBE_CHANNEL_ID_11 = "UCt16NSYjauKclK67LCXvQyA"
YOUTUBE_CHANNEL_ID_12 = "TransworldSKATEmag"
YOUTUBE_CHANNEL_ID_13 = "UCwhxKJw-PLlKXeferOK6spQ"
YOUTUBE_CHANNEL_ID_14 = "UCCtRyJj-neU-lE0pIlqhNVg"
YOUTUBE_CHANNEL_ID_15 = "adidasSkateboarding"
YOUTUBE_CHANNEL_ID_16 = "UCX9_Ks1MXuwXCmtt0fOFsxA"
YOUTUBE_CHANNEL_ID_17 = "UCwhxKJw-PLlKXeferOK6spQ"
YOUTUBE_CHANNEL_ID_18 = "antiheroskatevids"
YOUTUBE_CHANNEL_ID_19 = "UC78RckXCW4KQD0_bSVAmOkQ"
YOUTUBE_CHANNEL_ID_20 = "BoostedCommunity"
YOUTUBE_CHANNEL_ID_21 = "pedro30000"
YOUTUBE_CHANNEL_ID_22 = "UCS6whyOq-XLfeRSEXrzjfEA"
YOUTUBE_CHANNEL_ID_23 = "EMillionSkateboarts"
YOUTUBE_CHANNEL_ID_24 = "UCFugBVZgaQ5fCp-kLmyWq1A"
YOUTUBE_CHANNEL_ID_25 = "enjoicoskateboards"
YOUTUBE_CHANNEL_ID_26 = "flipskateboards091"
YOUTUBE_CHANNEL_ID_27 = "UC2Iqa4yjvqnkRAMGzXuQbDA"
YOUTUBE_CHANNEL_ID_28 = "SkateHabitat1"
YOUTUBE_CHANNEL_ID_29 = "HUFDBC"
YOUTUBE_CHANNEL_ID_30 = "krookedskatevids"
YOUTUBE_CHANNEL_ID_31 = "MagentaSkateboards"
YOUTUBE_CHANNEL_ID_32 = "ilansabar"
YOUTUBE_CHANNEL_ID_33 = "UCADVAEBl9ZZ9gFOwURmm2kA"
YOUTUBE_CHANNEL_ID_34 = "MrKLEZO"
YOUTUBE_CHANNEL_ID_35 = "quartersnacksdotcom"
YOUTUBE_CHANNEL_ID_36 = "jasonatsalad"
YOUTUBE_CHANNEL_ID_37 = "SK8MAFIATV"
YOUTUBE_CHANNEL_ID_38 = "UCA-O9C39dj7bBHwE7s3K_Bw"
YOUTUBE_CHANNEL_ID_39 = "UC6G0fSaMTWBnc-VcQKaPOlQ"
YOUTUBE_CHANNEL_ID_40 = "TheoriesOfAtlantis"
YOUTUBE_CHANNEL_ID_41 = "welcomeskateboardss"
YOUTUBE_CHANNEL_ID_42 = "blackboxdistvideo"
YOUTUBE_CHANNEL_ID_43 = "UCwhxKJw-PLlKXeferOK6spQ"
YOUTUBE_CHANNEL_ID_44 = "PLu3d4s9OqcNY_wJGkMqswfNBdu01taER_"
YOUTUBE_CHANNEL_ID_45 = "PLKXjBoMA3qOZcg68Z36v74VjFRxpCKc-W"
YOUTUBE_CHANNEL_ID_46 = "sprocker7"
YOUTUBE_CHANNEL_ID_47 = "PLFesB6LgEqr6nGn50u8gk6Xq0dfs4I0Dd"
YOUTUBE_CHANNEL_ID_48 = "PLral92ceWIL9YH3uefLymSQxKbr6_ndiI"
YOUTUBE_CHANNEL_ID_49 = "UCgDHpnoBlaid3M3fyapkl6A"
YOUTUBE_CHANNEL_ID_50 = "PLVoC5rN5Le5JoRhUHhIRguVyVQ3rboN15"
YOUTUBE_CHANNEL_ID_51 = "PLDF45YrF5UtfeO8LLX0g3C3tByRkYGuzh"
YOUTUBE_CHANNEL_ID_52 = "PL9GbwGIB7KxSekwLoBfMywO5aoAfie0Fy"
YOUTUBE_CHANNEL_ID_53 = "PLbexj5MOjqFb8HuaGQ4I2AfGvuJGo3eH8"
YOUTUBE_CHANNEL_ID_54 = "PL7SpP4KjR2bhw-kn430ZWt54uc2vSek53"
YOUTUBE_CHANNEL_ID_55 = "PLjHBisScDKdx-JZK8xHOeqYoXXBQOblU0"
YOUTUBE_CHANNEL_ID_56 = "PLfBrdQBVXWd0KRNWtZBh_HvjnM9-rv2Ih"
YOUTUBE_CHANNEL_ID_57 = "PLiBQxG7ttG6-nUMYj0S2CwhruDacMX3ZJ"
YOUTUBE_CHANNEL_ID_58 = "PLqDSJM3wVbgeWvear0bITyQvwo50EZdn9"
YOUTUBE_CHANNEL_ID_59 = "PLHVnsqI-PiNzHyLYCwjrLWDn1PxMrB1cd"
YOUTUBE_CHANNEL_ID_60 = "PL3QOKElJ2KzrNCnmT1N1pjv4gk7wEJ-rR"
YOUTUBE_CHANNEL_ID_61 = "XGames"
YOUTUBE_CHANNEL_ID_62 = "PLFwYXp-vRX38olefEdn00Rv4hw0AE-0nG"
YOUTUBE_CHANNEL_ID_63 = "PLLVf8SKCp3pq07WC3KOpLTuZEURK-zuq1"
YOUTUBE_CHANNEL_ID_64 = "UCwhxKJw-PLlKXeferOK6spQ"
YOUTUBE_CHANNEL_ID_65 = "PLgmqIJ6D3TnMLnGZUYY8_n9LbK8QvoFlV"
YOUTUBE_CHANNEL_ID_66 = "PLaAzY1LA2RoxorLKbM16fuNZZaOdi8eMQ"
YOUTUBE_CHANNEL_ID_67 = "PL7XmrlR-Vz2SYR5r2vhkNe7UwMf7xULwj"
YOUTUBE_CHANNEL_ID_68 = "PLPmwSvIVTs7HQSWK33YOAepP97n5sciR1"
YOUTUBE_CHANNEL_ID_69 = "PLRUyS_ZWCUx6SXIec8ZpkwzwoOfqp_ND1"
YOUTUBE_CHANNEL_ID_70 = "PLflWfB4F066bYkwRAsgEIqmywkof3ZmJi"
YOUTUBE_CHANNEL_ID_71 = "PLraWXNozUKkHB1lRQKXCBy3IVS14KS27o"
YOUTUBE_CHANNEL_ID_72 = "PL5Etg1byafjTEQ3OlfhruGYsEHAxc3vR3"
YOUTUBE_CHANNEL_ID_73 = "PLIijS8KCyNY1_AhleDSfXSdkf0NfNkLy0"
YOUTUBE_CHANNEL_ID_74 = "PLlphz7jMS2XhsldsL9Jsrh_MMRWW94EDD"
YOUTUBE_CHANNEL_ID_75 = "PLWBhJv4ROlVUnjvitQ3_j9mnIn92Il5xO"
YOUTUBE_CHANNEL_ID_76 = "PLI_E8GG7f-9Irin2y6_90240jTj_TkPSO"
YOUTUBE_CHANNEL_ID_77 = "PL99RMydebF1ZNvfGqhxzN0h7T_qIcd3nm"
YOUTUBE_CHANNEL_ID_78 = "PLjt54eYGmP8HfPD5-jz7bgZ3k-SDL3PxX"
YOUTUBE_CHANNEL_ID_79 = "PL2HT2VhjWHWTjgz8PqF0pWI5mDRZLYrTY"
YOUTUBE_CHANNEL_ID_80 = "PLC9tv0O3h6LYqRWpzShdBbNkhMs4FZqTU"
YOUTUBE_CHANNEL_ID_81 = "PLM3a_xcXNU3LATJDvveRS1egAK6D-thTl"
YOUTUBE_CHANNEL_ID_82 = "PLiVdViuQZRNA3r36LYKpdmtlr-LzEuVpy"
YOUTUBE_CHANNEL_ID_83 = "PL-h3x1o8Di-VmqeDX4wmkYC1LuJ0nvvQ_"
YOUTUBE_CHANNEL_ID_84 = "PLQuYGmlICElN8cgLP741E0Qf7TUsnAWgA"
YOUTUBE_CHANNEL_ID_85 = "PLfHtRRR8SkGs7piqxMIFMCd9IaX0-4KrI"
YOUTUBE_CHANNEL_ID_86 = "PLKX0ei-8zw8T683VJoDYDiYnbSdgzu9pq"
YOUTUBE_CHANNEL_ID_87 = "PLxCA864IElX-MMFNakEeJtdA3WSaP-Re8"
YOUTUBE_CHANNEL_ID_88 = "PL9xkW9nXS3M8dvGDaakiGaetstNmk0kPD"
YOUTUBE_CHANNEL_ID_89 = "PLRLiCF_Z9iSnVMy_xgD07zPkULFao-GKc"
YOUTUBE_CHANNEL_ID_90 = "PLzmVP_HObemYUYpMNirPuuoH1utLnXvzH"
YOUTUBE_CHANNEL_ID_91 = "PL_ZRWefOOMlEbMcBOCJTnPyxUZCTDrw99"
YOUTUBE_CHANNEL_ID_92 = "PLiW6EYfp33Hkb0iCywePrndPvcfEcf3_s"
YOUTUBE_CHANNEL_ID_93 = "PLUxVjYckVYyUnC9qnhMfuLMKGuJXONFe6"
YOUTUBE_CHANNEL_ID_94 = "PLwyA-9xgV4r-bYg3XBaWz3Ibelp0uM1Cz"
YOUTUBE_CHANNEL_ID_95 = "PLehV72w3tUBi8PUc14M4csKgb86V7XEcs"
YOUTUBE_CHANNEL_ID_96 = "PLywFWKgNTOQIwOkCTwKrgt52p6rfJFGTM"
YOUTUBE_CHANNEL_ID_97 = "PLSzfu6E8Etg-GTdPBTLIFhUJrTbOQKRRA"
YOUTUBE_CHANNEL_ID_98 = "PLok7PO_UEjY05qIkkwN3mGsUECc0gBheG"
YOUTUBE_CHANNEL_ID_99 = "PLIP-cb1_DPWRnwrHHWivYLsspNvajDtuZ"
YOUTUBE_CHANNEL_ID_100 = "PLByuWV_2WmHmLg-z3MEwM225X_KjhFcuO"
YOUTUBE_CHANNEL_ID_101 = "PLxvEJcjn9_5rn8klXJy8yus4weirKaa2-"
YOUTUBE_CHANNEL_ID_102 = "PLiv076ioqYEgPU4MfuK-gfhS2N_c5pxyQ"
YOUTUBE_CHANNEL_ID_103 = "PLwUdjDxcdqdKDQ8aEldUqJbbPVhrpHhI9"
YOUTUBE_CHANNEL_ID_104 = "PL045EXtx3Nw_2jxafvoxe1aXM0j2yKUBm"
YOUTUBE_CHANNEL_ID_105 = "PLC9BTt7QQmdWH0sQB_lIsx5FMCogJEuR0"
YOUTUBE_CHANNEL_ID_106 = "PLOB8OsfrXRmkIi_0ZtvsPj4NZNQ6lPiNj"
YOUTUBE_CHANNEL_ID_107 = "JulialiuJ"
YOUTUBE_CHANNEL_ID_108 = "PLrctOh_6KOoH9LxA__6a0QYq6DEWbBtQn"
YOUTUBE_CHANNEL_ID_109 = "PLXkEqD0RCPYSYks5aihF3lp20mihiWPNu"
YOUTUBE_CHANNEL_ID_110 = "PLFJLtz_MN6AoMbZcsxFvrgN1WIAvNNnx_"
YOUTUBE_CHANNEL_ID_111 = "PLsXmhrW-JJpUxAp_BLf82hruirdDUSYRg"
YOUTUBE_CHANNEL_ID_112 = "PLudrNj8EofvXVdCRDJH7v6-FYX5cf7dGJ"
YOUTUBE_CHANNEL_ID_113 = "PL84C9EEA45EE33C6D"
YOUTUBE_CHANNEL_ID_114 = "PL-cvSPdxdjlctDbA3Ur2eX9dumL_bZXke"
YOUTUBE_CHANNEL_ID_115 = "PL54RoWGjbuy7QZA6-6JNtIDCwHy1wNQdh"
YOUTUBE_CHANNEL_ID_116 = "PL1QtuBrw-FHJObUkYK5PD29nLca0w2Ck8"
YOUTUBE_CHANNEL_ID_117 = "PLGVDJB849oxFS3vOsgEWZZCC22aj97zrR"
YOUTUBE_CHANNEL_ID_118 = "PLhM8i-OgO92cqxRqJv-KJWsN1Y7MPXqXq"
YOUTUBE_CHANNEL_ID_119 = "PLv1RspwoJzySQWnEwXQt98JCC6eBuYrk8"
YOUTUBE_CHANNEL_ID_120 = "PLULTsDbzX51RqLbPjIM0UQCVhO6L5S_YX"
YOUTUBE_CHANNEL_ID_121 = "PL4DukSjubfukkl-zZrkHJA8py-PGKpPbV"
YOUTUBE_CHANNEL_ID_122 = "PL697pkl7kOlKzLuIhbKEJb5fINgPI1YRz"
YOUTUBE_CHANNEL_ID_123 = "PLbbTYNptxB9aS68X-O2SnDX6FvDVOsieV"
YOUTUBE_CHANNEL_ID_124 = "PLuL8kUqMf5aETS40D9TyNOdMF3jGsDgs1"
YOUTUBE_CHANNEL_ID_125 = "PLmXQqExXSrcvj_vx55PBldIqULvV8KJJH"
YOUTUBE_CHANNEL_ID_126 = "PLf2g1eJKmtedBwRFJlwtYAH8DWHRVPrdc"
YOUTUBE_CHANNEL_ID_127 = "PLeaLl2uorEr00pIac68H46eivIomEhxzl"
YOUTUBE_CHANNEL_ID_128 = "PLG0vWubRC6sLXK4XxMxLnqbAAth3qZh20"
YOUTUBE_CHANNEL_ID_129 = "PLv3kVe2qkjUt4rJ13zv6kwMTQxlx2k7oX"
YOUTUBE_CHANNEL_ID_130 = "pjladd"
YOUTUBE_CHANNEL_ID_131 = "PLMdal-h1A7Jg5yf3wyCSkoYGLXzetwRod"
YOUTUBE_CHANNEL_ID_132 = "PLmJZ59Dfz7A6x2vm9D3Mc8zjhKqW5T2Fo"
YOUTUBE_CHANNEL_ID_133 = "PLY1euOtdn1zi7xceON1XSVD7GwKvGrYOh"
YOUTUBE_CHANNEL_ID_134 = "PLfXBhFMtsg0QY7jFVMKy6D1iTLi1OCkne"
YOUTUBE_CHANNEL_ID_135 = "PLpycLlHjiQKhfZn1yXj90ydbLzWZj_i--"
YOUTUBE_CHANNEL_ID_136 = "PLJatNIRthblrRqr5iQcc766j5Vm7ZpSPw"
YOUTUBE_CHANNEL_ID_137 = "PLzkUnauK9OcPZm68EeqSiAENysceuh-vn"
YOUTUBE_CHANNEL_ID_138 = "PL6sGEBUblhA9Nqx1cvAtEZ1H29O8JlAJm"
YOUTUBE_CHANNEL_ID_139 = "PLgA5KSf_YgGAEEMBeXO4nvCuay2QnYC8F"
YOUTUBE_CHANNEL_ID_140 = "PLya8EYxTHvZXVvTohP2oq-A49LM4GmfYI"
YOUTUBE_CHANNEL_ID_141 = "PLM6ypi-nW2qM-mKTXaAMkfHGtNcPZNd88"
YOUTUBE_CHANNEL_ID_142 = "PLnoyUX2bSqQNmnVWZtssQpAnknxmNOh9F"
YOUTUBE_CHANNEL_ID_143 = "PLVveffmkaKFCybrGevTJffL6zT10qLkR-"
YOUTUBE_CHANNEL_ID_144 = "PLCzWUI_3BtVLHL1NsaRF8oyiY7rDv4AsW"
YOUTUBE_CHANNEL_ID_145 = "PL20uIFEYEW8cgv0UohRZH6n7BJ9YjVNcD"
YOUTUBE_CHANNEL_ID_146 = "PL0sgg-zrd_MMVFOUhAsybgeY3o3sGqe0J"
YOUTUBE_CHANNEL_ID_147 = "PLcyU3oI6GubFwRgBrRLE4J9lZOBje1ofd"
YOUTUBE_CHANNEL_ID_148 = "PLgy1IxC4OWKXAvXUCZKiBlbTHjTSqfsEO"
YOUTUBE_CHANNEL_ID_149 = "PLsor08qcFos1Oa6OmjRMLLmu39Yy2e-YB"
YOUTUBE_CHANNEL_ID_150 = "PLQf3jKxMb4MZUc7XowyiOhZyr4lhDfQbw"
YOUTUBE_CHANNEL_ID_151 = "PLnSisiHtEGJUARDk7DEYW-BbRR6IBAxsC"
YOUTUBE_CHANNEL_ID_152 = "PLyozC3yOtsJWh3ifvcMw-lDJfGeturtn1"
YOUTUBE_CHANNEL_ID_153 = "PLWW3govtcE2GvUpJmbWCCvici2u6wpL7F"
YOUTUBE_CHANNEL_ID_154 = "PLMELsjwQkeTblrYcDboblcUJBnSPTOmJh"
YOUTUBE_CHANNEL_ID_155 = "UCChZdqMk0VjQPTa74uBa9qQ"
YOUTUBE_CHANNEL_ID_156 = "NickstaSF27"
YOUTUBE_CHANNEL_ID_157 = "theskateboardmag"
YOUTUBE_CHANNEL_ID_158 = "nkalexander7"
YOUTUBE_CHANNEL_ID_159 = "metro236"
YOUTUBE_CHANNEL_ID_160 = "OCRamps97"
YOUTUBE_CHANNEL_ID_161 = "DarkstarSkate"
YOUTUBE_CHANNEL_ID_162 = "theberrics"
YOUTUBE_CHANNEL_ID_163 = "SkateHouseMedia"
YOUTUBE_CHANNEL_ID_164 = "landyachtzlongboards"
YOUTUBE_CHANNEL_ID_165 = "beartrucks"
YOUTUBE_CHANNEL_ID_166 = "UCvav1i2NQ_Qmj0mr6ahgtyQ"
YOUTUBE_CHANNEL_ID_167 = "SKATESL8"
YOUTUBE_CHANNEL_ID_168 = "np101np101"

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
        title="[B][COLOR yellow] Skateboarding Topic[/COLOR][/B]",
        url="",
        thumbnail="",
        folder=False )	

    plugintools.add_item( 
        #action="", 
        title="Skateboarding",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://preview.ibb.co/jHNv2b/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Street Skateboarding",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://preview.ibb.co/jHNv2b/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[B][COLOR yellow] Skateboarding misc.[/COLOR][/B]",
        url="",
        thumbnail="",
        folder=False )

    plugintools.add_item( 
        #action="", 
        title="adidas Skateboarding",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://cdn.shopify.com/s/files/1/1819/5799/files/Fifty_Fifty_Adidas_160x160@2x.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Braille Skateboarding",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://www.brailleskateboarding.com/wp-content/uploads/2015/11/IMG_3078-e1448035051904.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Crunchie Longboarding",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_168+"/",
        thumbnail="http://skateslate.tv/wp-content/uploads/sites/10/2016/02/Screen-Shot-2016-02-02-at-10.05.50-PM.png",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Grind For Life",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="http://skately.com/img/library/logos/large/grind-for-life.png",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Metro Skateboarding",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_159+"/",
        thumbnail="https://pbs.twimg.com/profile_images/125023810/twotonemetroheart_400x400.gif",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Nka Vids Skateboarding",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_158+"/",
        thumbnail="https://yt3.ggpht.com/-Ueh2-_u6DvE/AAAAAAAAAAI/AAAAAAAAAAA/s8jLEbAzHcQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )			

    plugintools.add_item( 
        #action="", 
        title="RIDE Channel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://jaimiemuehlhausen.files.wordpress.com/2012/04/ride_arrow.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Sk8park Atlas",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_156+"/",
        thumbnail="http://www.sk8parkatlas.com/images/AnnArbor2.jpg",
        folder=True )		
		
    plugintools.add_item( 
        #action="", 
        title="Skateboarding (assorted vids)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://preview.ibb.co/jHNv2b/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Skate House Media",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_163+"/",
        thumbnail="https://mclovinmyliferightnow.files.wordpress.com/2012/03/shmtv-2.jpg",
        folder=True )		
		
    plugintools.add_item( 
        #action="", 
        title="SK8 stuff",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://preview.ibb.co/jHNv2b/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Skate Videos channel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://preview.ibb.co/jHNv2b/icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Berrics",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_162+"/",
        thumbnail="https://yt3.ggpht.com/-Mn37yoA6oWI/AAAAAAAAAAI/AAAAAAAAAAA/H4aRufoGgv4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Vans Park Series",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_155+"/",
        thumbnail="http://69b6f8fd736ed8836881-2f84b28f704f9f5fbcd9c873e843c0af.r11.cf1.rackcdn.com/images/entries/_960xAUTO_fit_center-center_85/GreysonFletcher_2014USOpen_Saturday_46.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Woodward Camp",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://media-cdn.tripadvisor.com/media/photo-s/04/0c/4b/6c/camp-woodward-skate-park.jpg",
        folder=True )			

    plugintools.add_item( 
        #action="", 
        title="[B][COLOR yellow]Skateboard Magazines[/COLOR][/B]",
        url="",
        thumbnail="",
        folder=False )

    plugintools.add_item( 
        #action="", 
        title="Skate[Slate]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_167+"/",
        thumbnail="https://i1.wp.com/www.skateslate.com/wp-content/uploads/2015/04/sks23-cover.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Skateboarder Magazine",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://skately.com/img/library/logos/large/skateboarder-magazine.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Skateboard Mag",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_157+"/",
        thumbnail="https://yt3.ggpht.com/-GiavkiIaF4E/AAAAAAAAAAI/AAAAAAAAAAA/9zhUXCD9BQM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Thrasher Magazine",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/71P%2BT5uVSkL._SL1248_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TransWorld SKATEboarding",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-WeH3JnWOPvM/AAAAAAAAAAI/AAAAAAAAAAA/eyJa-4HwB8U/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )


    plugintools.add_item( 
        #action="", 
        title="[B][COLOR yellow]Skateboard Companies & Accessories[/COLOR][/B]",
        url="",
        thumbnail="",
        folder=False )

    plugintools.add_item( 
        #action="", 
        title="Antihero Skateboards",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="http://www.cvltnation.com/wp-content/uploads/2016/08/antihero_original.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Baker Skateboards",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="http://skately.com/img/library/logos/large/baker-skateboards.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bear Trucks",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_165+"/",
        thumbnail="https://plunderventures.files.wordpress.com/2013/11/bear-trucks-logo.gif",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Boosted",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://pbs.twimg.com/profile_images/821097344804352000/5lr2NMXp.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bronze 56K",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="http://www.jenkemmag.com/home/wp-content/uploads/2014/08/Bronze56K_Windows_Jenkem_Interview.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Darkstar Skateboards",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_161+"/",
        thumbnail="https://www.warehouseskateboards.com/logos/custom/Darkstar-skateboards.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="DIYElectricSkateboard.com",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://i.ytimg.com/vi/fUdxf_54wIg/maxresdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="EMillion",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://pbs.twimg.com/profile_images/1878979046/EMillion_Gump_Logo_400x400.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Enertion Skateboards",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="http://cdn2.bigcommerce.com/n-yp39j5/zad02/product_images/250x250-square-enertion-logo-2017-text-blue-trans_1494506386__99291.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="enjoi",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://cdn-skateboarding.transworld.net/blogs.dir/440/files/2015/12/enjoi_panda_june_2000.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Flip Skateboards",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://pbs.twimg.com/profile_images/378800000045827529/e21c45ce5358269af537e66ec6e31d04.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fucking Awesome",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://www.bonkers-shop.com/wp-content/uploads/fucking-awesome-logo-bonkers-shop.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Habitat Skateboards",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://i.vimeocdn.com/portrait/8716837_300x300",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hawgs Wheels",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_166+"/",
        thumbnail="http://www.hawgswheels.com/pics/HawgsWheels.png",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="HUF",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://pbs.twimg.com/profile_images/542453652271550464/1HFcabKb.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Krooked Skateboarding",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="http://krookedskateboarding.com/kcracers/img/kr.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Landyachtz",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_164+"/",
        thumbnail="https://cdn.daddiesboardshop.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/l/a/landyachtz-red-logo-sticker.1506795381.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Magenta Skateboards",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://yt3.ggpht.com/-3LqujcciU9Y/AAAAAAAAAAI/AAAAAAAAAAA/OjY1Z_Kz-Yk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Metroboard",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://metro-board.com/wp-content/uploads/2015/11/Metroboard-Stealth-Electric-Longboard-Iso-View-1200x600.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="OC Ramps",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_160+"/",
        thumbnail="https://yt3.ggpht.com/-RTDEiROdC9U/AAAAAAAAAAI/AAAAAAAAAAA/tAlK0hB12D8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Palace Skateboards",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://static.highsnobiety.com/wp-content/uploads/2017/05/26170937/palace-skateboards-guide-2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Polar Skate Co",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="http://www.goodtimesmag.gr/images/skate/The%20Polar%20Skate%20Co_%20Promo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Quartersnacks",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="http://www.europeskate.com/wp-content/uploads/2015/12/Quartersnacks-Best-of-2015-820x540.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Salad Skateboards",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://yt3.ggpht.com/-iTNYHVcjVto/AAAAAAAAAAI/AAAAAAAAAAA/GCGGX8WWMsg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="sk8mafia",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://cdna.artstation.com/p/assets/images/images/001/236/104/large/eric-osterberg-2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Southern Supreme Skateboards",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://yt3.ggpht.com/-C4RRYIusZaY/AAAAAAAAAAI/AAAAAAAAAAA/qfiwWj9EMfc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sure Skateboards",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://i.pinimg.com/736x/0a/ff/cb/0affcbfd0f46ed71c4ab71147321927f--bustin-boards-skateboards.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Theories of Atlantis",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://yt3.ggpht.com/-USHVHJRv9D0/AAAAAAAAAAI/AAAAAAAAAAA/3LtAh9mksds/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Welcome Skateboards",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="http://www.twelveboardstore.com.au/web_images/news_1419630991.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Zero Skateboards",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="http://zeroskateboards.com/wp-content/uploads/2015/08/zero-logo-fb.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[B][COLOR yellow]Skateboard TV shows and Movies[/COLOR][/B]",
        url="",
        thumbnail="",
        folder=False )

    plugintools.add_item( 
        #action="", 
        title="Skateboard Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://preview.ibb.co/jHNv2b/icon.png",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="80's Skateboard Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://preview.ibb.co/jHNv2b/icon.png",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Ban This",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://i1.sndcdn.com/artworks-000035989131-5cfkzw-t500x500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bones Brigade: An Autobiography",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://bonesbrigade.com/media/wysiwyg/bbaa/about/bones-brigade-poster-sm-new.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Built To Shred",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://cdn-skateboarding.transworld.net/blogs.dir/440/files/2009/07/07/picture-2.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dogtown and Z Boys",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/511HYNVN3CL.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Life of Ryan",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/e/ed/Life_of_Ryan.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Lords of Dogtown",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="http://static.tvtropes.org/pmwiki/pub/images/img_1047_4.JPG",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rob & Big",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="http://images.zap2it.com/assets/p186441_b_h3_aa/rob-and-big.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rob Dyrdek's Fantasy Factory",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51X2YTQwGmL.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Scarred",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/3/31/Scarredlogo.jpg/250px-Scarredlogo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SK8-TV",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="http://3.bp.blogspot.com/_nuVvwBoLKt0/SWEV4b4aTYI/AAAAAAAAAEs/dcftiF8EDjs/s400/IMG_2321.JPG",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Bones Brigade Video Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="http://www.chutingstar.com/media/catalog/product/cache/1/image/1200x/040ec09b1e35df139433887a97daa66f/b/o/bonesbr.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Search for Animal Chin",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="https://i.pinimg.com/originals/54/1f/24/541f24c729ca275a52a373fcf96fef30.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Thrashin'",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="https://a.ltrbxd.com/resized/film-poster/2/8/6/1/9/28619-thrashin--0-230-0-345-crop.jpg?k=5e2fd8371f",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Viva La Bam",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/61VHcI2LB3L._SY355_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Wild Grinders",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/8/8b/Wild_Grinders_logo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="X Games",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="https://pbs.twimg.com/profile_images/489671367717945344/o_-yTsXM_400x400.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Zeke and Luther",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_63+"/",
        thumbnail="http://epguides.com/ZekeandLuther/cast.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[B][COLOR yellow]Skateboarders[/COLOR][/B]",
        url="",
        thumbnail="",
        folder=False )

    plugintools.add_item( 
        #action="", 
        title="Alana Smith",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_65+"/",
        thumbnail="http://ktrskateboardschool.com/Blog/wp-content/uploads/2014/08/AlanaSmith.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Alex Perelson",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_66+"/",
        thumbnail="http://dailygrind.se/PhotoArchive/2013/20131211_DG_Alex_Perelson.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Amy Caron",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_67+"/",
        thumbnail="http://www.realskate.com/pics/amycaron.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Andrew Reynolds",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_68+"/",
        thumbnail="https://i.pinimg.com/originals/87/d7/25/87d725b0c3220b97d8de4aadca5d32b2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Andy Macdonald",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_69+"/",
        thumbnail="http://www3.pictures.zimbio.com/gi/Andy+Macdonald+X+Games+16+W12sZrrHHqwl.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Arto Saari",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_70+"/",
        thumbnail="https://i.pinimg.com/originals/8c/4b/35/8c4b350aba8746f1fb5df586a1484845.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bam Margera",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_71+"/",
        thumbnail="https://i.pinimg.com/originals/f2/9d/5b/f29d5b0f5a3f99cfa624ba6bf8befc60.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bastien Salabanzi",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_72+"/",
        thumbnail="https://cdn-skateboarding.transworld.net/blogs.dir/440/files/wednesday-wallpaper-bastien/skb0912_wallpaper_03.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bob Burnquist",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_73+"/",
        thumbnail="https://www.laureus.com/sites/default/files/styles/profile_main_new/public/bob_burnquist_p.jpg?itok=NUiHuT6y",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Brandon Biebel",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_74+"/",
        thumbnail="https://cdn.grindtv.com/uploads/2010/12/wpid-BeebsSA_CCS3002.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Brandon Novak",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_75+"/",
        thumbnail="http://i27.tinypic.com/34g8qj7.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Brian Anderson",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_76+"/",
        thumbnail="http://www.cvltnation.com/wp-content/uploads/2016/10/Brian-Anderson-Skateboard-How-To-3-700x1053.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bucky Lasek",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_77+"/",
        thumbnail="http://buckylasek81.com/wp-content/gallery/skate/bucky_lasek_3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="C. R. Stecyk III",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_78+"/",
        thumbnail="https://cdn.surfer.com/uploads/2012/02/STECYK-bars.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Casey Neistat",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_79+"/",
        thumbnail="https://i.ytimg.com/vi/Ekg1qV-3nIQ/maxresdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chad Muska",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_80+"/",
        thumbnail="http://www.chadmuska.org/wp-content/uploads/2011/05/chadmuska_11.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chima Ferguson",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_81+"/",
        thumbnail="http://a1.espncdn.com/photo/2013/0719/as_skate_ChimaTasmania_2048.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chris Cole",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_82+"/",
        thumbnail="https://cdn-skateboarding.transworld.net/blogs.dir/440/files/2014/10/Chris-Cole-fsboard-kf-shigeo2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chris Haslam",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_83+"/",
        thumbnail="https://i.pinimg.com/originals/97/11/b7/9711b7004260fb30db6a5f4cbe6193bc.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Christian Hosoi",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_84+"/",
        thumbnail="http://refreshedmag.com/wp-content/uploads/2014/01/newsphoto-1213-ChristianHosoi.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Curren Caples",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_85+"/",
        thumbnail="https://i.ytimg.com/vi/rc7B5xzuSJQ/maxresdefault.jpg",
        folder=True )           

    plugintools.add_item( 
        #action="", 
        title="Daewon Song",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_86+"/",
        thumbnail="http://www.jenkemmag.com/home/wp-content/uploads/2012/07/daewon-grab.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Danny Way",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_87+"/",
        thumbnail="http://www.skatelog.com/photos/skaters/danny-way/espn-998187579-377x350.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dustin Dollin",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_88+"/",
        thumbnail="https://cdn-skateboarding.transworld.net/blogs.dir/440/files/2010/01/twswalldollin.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ed Templeton",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_89+"/",
        thumbnail="http://www.skateboardinghalloffame.org/wp-content/uploads/2017/07/as_skate_ET_180ng_MB_630.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Elissa Steamer",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_90+"/",
        thumbnail="http://skateparkoftampa.com/spot/images/cph10dsc_2135.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Elliot Sloan",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_91+"/",
        thumbnail="http://s3.rockstarenergy.com/2012/11/elliot_sloan_action.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Eric Koston",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_92+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/d/d4/Kostonfandangle.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Geoff Rowley",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_93+"/",
        thumbnail="https://i.pinimg.com/originals/ff/91/94/ff9194ca3e33f3ad6f37d9eb0455a5f5.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Gino Iannucci",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_94+"/",
        thumbnail="http://www.nyskateboarding.com/wp/wp-content/uploads/2011/01/4265272550_b8a0d3e9481.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Greg Lutzka",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_95+"/",
        thumbnail="https://sk8er73.files.wordpress.com/2008/10/greg-lutzka.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Guy Mariano",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_96+"/",
        thumbnail="http://a3.espncdn.com/photo/2013/0625/as_skate_Gu1_2048.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ishod Wair",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_97+"/",
        thumbnail="https://cdn-skateboarding.transworld.net/blogs.dir/440/files/ishod-wair-wallpaper-2/skb0913_wallpaper_01.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jagger Eaton",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_98+"/",
        thumbnail="http://www.thrashermagazine.com/imagesV2/Features/2013/Lake_Havasu_web/jett_eaton_invert17198.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jake Brown",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_99+"/",
        thumbnail="http://www2.pictures.zimbio.com/gi/Jake+Brown+X+Games+16+T-zV1ZCcTLTl.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jason Acuna",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_100+"/",
        thumbnail="http://gorillaflicks.typepad.com//.a/6a01a3fcef02a2970b01b8d16e3ba2970c-800wi",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jay Adams",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_101+"/",
        thumbnail="https://ozzieausband.files.wordpress.com/2015/08/jayboylogcabins.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jereme Rogers",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_102+"/",
        thumbnail="http://www.caughtinthecrossfire.com/media/images/skate/news/jeremerogers.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jerry Hsu",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_103+"/",
        thumbnail="https://static.giantbomb.com/uploads/scale_small/3/32465/1086657-jerry_hsu_overcrooks.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jim Greco",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_104+"/",
        thumbnail="https://i.pinimg.com/736x/10/b0/42/10b042f0335064233f157d8bb7f909bb--supra-footwear-wooden-toys.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Joey Brezinski",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_105+"/",
        thumbnail="https://i.ytimg.com/vi/safDq9acVrk/maxresdefault.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Josh Kalis",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_106+"/",
        thumbnail="http://quartersnacks.com/wp-content/uploads/2010/11/111210.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Julia Bruckler",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_107+"/",
        thumbnail="https://coresites-cdn.factorymedia.com/cooler_new/wp-content/uploads/2013/07/Julia-Brueckler_Krooked-Grind.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Justin Bravo",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_108+"/",
        thumbnail="https://scontent-sea1-1.cdninstagram.com/t51.2885-15/s480x480/e35/c0.134.1080.1080/21294362_286590588414382_9171964967698563072_n.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kareem Campbell",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_109+"/",
        thumbnail="https://i.pinimg.com/736x/db/18/01/db180137b3e0d82bdd4443c6c985d010--kareem-campbell-board-art.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lacey Baker",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_110+"/",
        thumbnail="https://coresites-cdn.factorymedia.com/cooler_new/wp-content/uploads/2013/04/On-Baker-Street-Lacey-Baker-Interview-5.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lance Mountain",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_111+"/",
        thumbnail="http://www3.pictures.zimbio.com/gi/X+Games+16+44bOAZOxg12x.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Letícia Bufoni",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_112+"/",
        thumbnail="http://www.boardistan.com/wp-content/uploads/2015/05/leticia-bufoni-xgames-nam-chi-van-Giveaway.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lizard King",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_113+"/",
        thumbnail="https://cdn.grindtv.com/uploads/2012/11/Screen-shot-2012-11-08-at-10.46.12-AM.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lizzie Armanto",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_114+"/",
        thumbnail="http://www.caughtinthecrossfire.com/uploads/2017/04/lizzie.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Luan Oliveira",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_115+"/",
        thumbnail="https://i.ytimg.com/vi/tA9exk2XC8Y/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lucas Puig",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_116+"/",
        thumbnail="http://liveskateboardmedia.com/sites/liveskateboardmedia.com/files/field/image/Cliche-Adi-Lucas.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lyn-Z Adams Hawkins",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_117+"/",
        thumbnail="https://usatbnqt.files.wordpress.com/2008/07/0005-4ca7ffb1-4a827815-b4ab-b34b6ed4.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Marc Johnson",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_118+"/",
        thumbnail="http://images.complex.com/complex/image/upload/c_limit,w_680/fl_lossy,pg_1,q_auto/jkccgriao7iprpconjb7.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mark Gonzales",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_119+"/",
        thumbnail="http://www.skateboardinghalloffame.org/wp-content/uploads/2013/02/Mark-Gonzales.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mike Carroll",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_120+"/",
        thumbnail="http://skateparkoftampa.com/spot/images2/carroll1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mike McGill",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_121+"/",
        thumbnail="http://vignette4.wikia.nocookie.net/skateboarding/images/4/47/Mike_McGill.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mike Mo Capaldi",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_122+"/",
        thumbnail="http://2.bp.blogspot.com/-a7D1-FO6Wyw/TvOTLRdtEyI/AAAAAAAAAgQ/kSTBUN4Yoo8/s1600/mike_mo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mike Vallely",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_123+"/",
        thumbnail="https://i.ytimg.com/vi/svWE4niC9nk/maxresdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mitchie Brusco",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_124+"/",
        thumbnail="http://ww4.hdnux.com/photos/02/35/11/643659/3/920x920.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nyjah Huston",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_125+"/",
        thumbnail="https://cdn-s3.si.com/s3fs-public/sikids/pages/images/cms/imce/users/dantec/2015/08/nyjah-huston-skateboarding-header.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pamela Rosa",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_126+"/",
        thumbnail="http://a.espncdn.com/photo/2014/0608/xgaus_sk8gall05a_rosa.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Paul Rodriguez",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_127+"/",
        thumbnail="https://cdn.grindtv.com/uploads/2014/02/Paul-Rodriguez.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pedro Barros",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_128+"/",
        thumbnail="http://istia.tv/blog/wp-content/uploads/2013/03/pedro-barros-skate-park-sun-1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pierre-Luc Gagnon",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_129+"/",
        thumbnail="http://www.revoltinstyle.com/wp-content/uploads/2012/03/PLG4.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="PJ Ladd",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_130+"/",
        thumbnail="http://skateboarders.le-site-du-skateboard.com/files/PJ-Ladd-switch-tre.jpg",
        folder=True )           

    plugintools.add_item( 
        #action="", 
        title="Rick Howard",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_131+"/",
        thumbnail="https://cdn-skateboarding.transworld.net/blogs.dir/440/files/rick-howard-photographic-memory/rick-howard-lien-air-mallorca-2004lowres.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rob Dyrdek",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_132+"/",
        thumbnail="http://www1.pictures.zimbio.com/gi/Rob+Dyrdek+Rob+Dyrdek+Unveils+7+Eleven+Urban+H9w1jJjfO4_l.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rick McCrank",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_133+"/",
        thumbnail="http://2.bp.blogspot.com/--RX9IkqI-l0/UfI214w8EiI/AAAAAAAAAS0/GBwHpyRwYhM/s1600/Rick+2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Riley Hawk",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_134+"/",
        thumbnail="http://a.espncdn.com/media/motion/2014/0529/dm_140529_RILEY_HAWK/dm_140529_RILEY_HAWK.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rodney Mullen",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_135+"/",
        thumbnail="https://www.guitar-muse.com/wp-content/uploads/2011/08/rodney-mullen.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rony Gomes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_136+"/",
        thumbnail="https://triboskate.akamaized.net/wp-content/uploads/2016/09/ronygomes-frontsidenosegrind.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ryan Gallant",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_137+"/",
        thumbnail="http://www.rippedlaces.com/wp/wp-content/uploads/2013/10/Ryan-Gallant-Wallride.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rune Glifberg",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_138+"/",
        thumbnail="http://www.volcom.co.id/wp-content/uploads/2012/07/rune_lipslide.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ryan Decenzo",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_139+"/",
        thumbnail="http://assets.caughtinthecrossfire.com/skate/features/freshblood09/ryandecenzo/decenzo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ryan Sheckler",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_140+"/",
        thumbnail="https://cdn.grindtv.com/uploads/2014/04/Etnies_Dec13_Sheckler_1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sandro Dias",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_141+"/",
        thumbnail="http://2.bp.blogspot.com/-qUtWY8HQn88/Us6bWsEc1qI/AAAAAAAA7vQ/56SC_NYRYbw/s1600/sandro-dias-riosul.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sean Malto",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_142+"/",
        thumbnail="http://streetleague.wpengine.netdna-cdn.com/wp-content/uploads/2015/07/SeanMalto_propage.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Shaun White",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_143+"/",
        thumbnail="http://www.gameinformer.com/cfs-filesystemfile.ashx/__key/CommunityServer-Blogs-Components-WeblogFiles/00-00-00-00-06/4426.whitex_2D00_largejpg1.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Stacy Peralta",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_144+"/",
        thumbnail="http://www.skateboardinghalloffame.org/wp-content/uploads/2014/04/Stacy-Peralta_board_1977-Photo-by-Jim-Goodrich.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Steve Berra",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_145+"/",
        thumbnail="http://www.thecelebworth.com/wp-content/uploads/2013/08/Steve-Berra-1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Steve Caballero",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_146+"/",
        thumbnail="https://www.skateone.com/blog-wp/wp-content/uploads/2012/02/cab-440x290.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Stevie Williams",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_147+"/",
        thumbnail="http://www.pro-skaters.net/skaterpic/Stevie_Williams_11.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Terry Kennedy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_148+"/",
        thumbnail="http://4.bp.blogspot.com/-IOFjZy3_zPQ/Um_BflV4I4I/AAAAAAAAOr0/nntQ7sspvVU/s1600/terry+kennedy+5+on+flat+msa.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tom Schaar",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_149+"/",
        thumbnail="https://olliesht.files.wordpress.com/2013/07/tom-schaar1.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Tony Alva",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_150+"/",
        thumbnail="http://www.skateboardinghalloffame.org/wp-content/uploads/2014/04/Tony-Alva-Courtesy-Brian-Logan-at-Logan-Earth-Ski.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Tony Hawk",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_151+"/",
        thumbnail="http://www.ahumblesoul.com/uploads/2/1/9/6/21969602/8247670_orig.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Tony Trujillo",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_152+"/",
        thumbnail="http://www.caughtinthecrossfire.com/uploads/2011/12/tonytrujillo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Torey Pudwill",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_153+"/",
        thumbnail="https://cdn-skateboarding.transworld.net/blogs.dir/440/files/2013/08/SKB0613_PLN59-83_Morph-600x424.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Vanessa Torres",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_154+"/",
        thumbnail="https://i.pinimg.com/originals/2b/dd/b0/2bddb0161279d29eac71d6acada4ebad.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Z Boys",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_62+"/",
        thumbnail="https://theselvedgeyard.files.wordpress.com/2012/12/zephyr-skate-team-z-boys-skateboarder.jpg",
        folder=True )		
run()
