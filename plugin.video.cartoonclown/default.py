# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Cartoon Clown
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

addonID = 'plugin.video.cartoonclown'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UC_KRFNg2LYwpcFTYSMr-cRw"
YOUTUBE_CHANNEL_ID_2 = "bygonetoons"
YOUTUBE_CHANNEL_ID_3 = "UCqcV90P6sDm-omlt7tXHVfQ"
YOUTUBE_CHANNEL_ID_4 = "UCojpmgQicFCsChoHdouuaxQw"
YOUTUBE_CHANNEL_ID_5 = "8thManDVDcom"
YOUTUBE_CHANNEL_ID_6 = "CCCartoons"
YOUTUBE_CHANNEL_ID_7 = "UCnsbuFtsoZw1iwV6_ZiXltA"
YOUTUBE_CHANNEL_ID_8 = "TootsToons"
YOUTUBE_CHANNEL_ID_9 = "UCfef_H15Io2yIhAMwAgMklw"
YOUTUBE_CHANNEL_ID_10 = "UCNzerhn_5YifzXhOosnkWlQ"
YOUTUBE_CHANNEL_ID_11 = "UCVGySV5TosyEnfMoVHXahMA"
YOUTUBE_CHANNEL_ID_12 = "UChj-Svv3CTUW41rHIyp_iiw"
YOUTUBE_CHANNEL_ID_13 = "dandydeal"
YOUTUBE_CHANNEL_ID_14 = "UCbrb4lqXgABnemLU6vZikiQ"
YOUTUBE_CHANNEL_ID_15 = "UCbGV1e1t2INuzZlvwXsY74w"
YOUTUBE_CHANNEL_ID_16 = "cartoonnetwork"
YOUTUBE_CHANNEL_ID_17 = "DisneyShorts"
YOUTUBE_CHANNEL_ID_18 = "PinkPanther"
YOUTUBE_CHANNEL_ID_19 = "UC0mxTipHMAhdlA-SeO2LrTw"
YOUTUBE_CHANNEL_ID_20 = "spookizworld"
YOUTUBE_CHANNEL_ID_21 = "rossbollinger"
YOUTUBE_CHANNEL_ID_22 = "dhxjuniortv"
YOUTUBE_CHANNEL_ID_23 = "PLlK-Lq3jfBQR-7BfY2SlYDNuFu0tWHNgz"
YOUTUBE_CHANNEL_ID_24 = "UCbIwNAgPkmgNnL3X1j1lCKw"
YOUTUBE_CHANNEL_ID_25 = "UCtcAhY-1TtQ0NRsyHkZ1cOQ"
YOUTUBE_CHANNEL_ID_26 = "UCmYaJtm2MQGinYwg2ny222A"
YOUTUBE_CHANNEL_ID_27 = "UC6whXVotuV2aEPU_bhImUGg"
YOUTUBE_CHANNEL_ID_28 = "UCUiEtPQzNqUn698Qq1fMY1w"
YOUTUBE_CHANNEL_ID_29 = "UCDBmcgs_wvESd8r50ExpTwg"
YOUTUBE_CHANNEL_ID_30 = "UCotypeTpo_ZDDr-PvadUoKw"
YOUTUBE_CHANNEL_ID_31 = "UCcFAZjRhFUAgHrN4AqhFr_g"
YOUTUBE_CHANNEL_ID_32 = "UCeoi7-KhBIIYLA0pywg8QwQ"
YOUTUBE_CHANNEL_ID_33 = "UCw2012xCL4NW_fdTEfwqfLQ"
YOUTUBE_CHANNEL_ID_34 = "UCqdPt5-jDpVrA_MbzJ3yBtw"
YOUTUBE_CHANNEL_ID_35 = "UC7y-VWw9qh6WVvaHIK7Jtng"
YOUTUBE_CHANNEL_ID_36 = "UC1sh79zmm4lIybd0K6fFovQ"
YOUTUBE_CHANNEL_ID_37 = "UCaNQ7u0r942DL3YC7uAeLCw"
YOUTUBE_CHANNEL_ID_38 = "UCotypeTpo_ZDDr-PvadUoKw"
YOUTUBE_CHANNEL_ID_39 = "UCZl6zUcj0SzZlmgbBdIMMwg"
YOUTUBE_CHANNEL_ID_40 = "UCM2YmsRUeIbRkqjgNm0eTGQ"
YOUTUBE_CHANNEL_ID_41 = "UCpavNbT5jS5DW3Nw4qYC1wg"
YOUTUBE_CHANNEL_ID_42 = "UCFKMDr36kG3J4YBKyuS9h1g"
YOUTUBE_CHANNEL_ID_43 = "UCwWjq1bh4dtLOwjycevusAA"
YOUTUBE_CHANNEL_ID_44 = "UCU9H0RTQ0TUN1JBlF2KxmFw"
YOUTUBE_CHANNEL_ID_45 = "UCfCj08E1qRQGpMeykaf9JMw"
YOUTUBE_CHANNEL_ID_46 = "PLSGiox8oS2IaXtDynCozASS3N2aVU83X8"
YOUTUBE_CHANNEL_ID_47 = "UCuAMmXJV6hT2sFX6Gvmob1Q"
YOUTUBE_CHANNEL_ID_48 = "UC9VeCw582iCreSse5fAauRg"
YOUTUBE_CHANNEL_ID_49 = "UCFtV0ilIhR9bTVbpw_LswUQ"
YOUTUBE_CHANNEL_ID_50 = "casperfriendlyghost"
YOUTUBE_CHANNEL_ID_51 = "UCAT76FMF9TGEGNtElnAtwUQ"
YOUTUBE_CHANNEL_ID_52 = "UC88kZP-2IZ1cT0_3NdnyikA"
YOUTUBE_CHANNEL_ID_53 = "UC7rrVcp3xmrbAsCAcIfUNzg"
YOUTUBE_CHANNEL_ID_54 = "UCKJ58QcoIOgPut_l_1FZ2Jg"
YOUTUBE_CHANNEL_ID_55 = "UCng021OwwJLrl4_kWXogvqQ"
YOUTUBE_CHANNEL_ID_56 = "UCqEYO5FFbQEsf18cwK43Pdg"
YOUTUBE_CHANNEL_ID_57 = "UCe6u5j2-TZ0Y56OItY3b32g"
YOUTUBE_CHANNEL_ID_58 = "UCMqIL5R4sJKa3DaRazuKucQ"
YOUTUBE_CHANNEL_ID_59 = "UC5NZx1c7KM0TZRsoDM6ZtTA"
YOUTUBE_CHANNEL_ID_60 = "UCe4BbTj0ROHAb1TOacD-JZQ"
YOUTUBE_CHANNEL_ID_61 = "UCrz0wFuPghfLQaSx9OZ_3CA"
YOUTUBE_CHANNEL_ID_62 = "UCmZvP2JY7MdUCM5y0rajFVA"
YOUTUBE_CHANNEL_ID_63 = "UC8-Z7WhKJV02A458LZYpqXg"
YOUTUBE_CHANNEL_ID_64 = "UCzxhjnHMS1Clw6TWUr92OYg"
YOUTUBE_CHANNEL_ID_65 = "UCW2B2uQ53eSInvHH82VY-Eg"
YOUTUBE_CHANNEL_ID_66 = "UCIxTRu_vCD9CDr5jRYs_Low"
YOUTUBE_CHANNEL_ID_67 = "UCF7p-dvnk6muMB4PhiCJiQA"
YOUTUBE_CHANNEL_ID_68 = "UCo2-WuB4AkJO9h1P7IE-CMA"
YOUTUBE_CHANNEL_ID_69 = "UCweF9b377cbIGzBArTbxhIg"
YOUTUBE_CHANNEL_ID_70 = "UC4yax1Zu6bCAKZSLEB-8o8Q"
YOUTUBE_CHANNEL_ID_71 = "UCoQBLk7WTaWNiToXJdXMQ-Q"
YOUTUBE_CHANNEL_ID_72 = "UCSVqxs9sN8UF_Y-qn4LMKuA"
YOUTUBE_CHANNEL_ID_73 = "CAAiM1p0tD1G9fsANbIPWnA"
YOUTUBE_CHANNEL_ID_74 = "UCijARrAiewli1Ju2oRqpF1A"
YOUTUBE_CHANNEL_ID_75 = "UCrO_HdL8T8lNHCKISZkxsIA"
YOUTUBE_CHANNEL_ID_76 = "UCqhY0XKQI_tN1YDBYFFEXmA"
YOUTUBE_CHANNEL_ID_77 = "UCXuy6fsDt3rfGMH2PNirxbw"
YOUTUBE_CHANNEL_ID_78 = "UCJdF4DmpTZJ6gEMbqY6iGVw"
YOUTUBE_CHANNEL_ID_79 = "UCoh6nZvf_r8-Lygr--C9Vgw"
YOUTUBE_CHANNEL_ID_80 = "UCbLoGdb7seoX4UfXgV2MxfA"
YOUTUBE_CHANNEL_ID_81 = "UCWPapzaARS5VOJCAskEOvIA"
YOUTUBE_CHANNEL_ID_82 = "UC7FRXsvtr2YMemojhqscmAA"
YOUTUBE_CHANNEL_ID_83 = "UCb_u-pIVg1Ygxb0AqQjpwFA"
YOUTUBE_CHANNEL_ID_84 = "UCnYbLzfAs-YVKvWWE6Gectw"
YOUTUBE_CHANNEL_ID_85 = "UCI2NK1MfYVF0uJAKcfKC5JQ"
YOUTUBE_CHANNEL_ID_86 = "UCQ1ZuvrpV4O_ihJ7qotsuZw"
YOUTUBE_CHANNEL_ID_87 = "UCCHJGv7ycz_cLkbgvRFZ6wQ"
YOUTUBE_CHANNEL_ID_88 = "PLlAWf5sbmQaXZb9-zli1F9xAtd1on_gNf"
YOUTUBE_CHANNEL_ID_89 = "UCxGpajdxHjRIiS9b3Ya6OFQ"
YOUTUBE_CHANNEL_ID_90 = "UCEOz6SiqyPReN1QAXcHh7pg"
YOUTUBE_CHANNEL_ID_91 = "PLwp8m9anCLK3jmItMyLTgfNpM-526z8Cl"
YOUTUBE_CHANNEL_ID_92 = "UCv0LiJCpKZYik388rEtzcaA"
YOUTUBE_CHANNEL_ID_93 = "UCZYGNFi-KbP4IR4B_RjvNfg"
YOUTUBE_CHANNEL_ID_94 = "UCCA3IfGJSq5JLR3akbRHC5w"
YOUTUBE_CHANNEL_ID_95 = "UCYEm2z2cxGTz9zu0D6kXY7w"
YOUTUBE_CHANNEL_ID_96 = "UCGVpdyhxF-iGYRhvsvqElXA"
YOUTUBE_CHANNEL_ID_97 = "UCjE6QVmeXTGuk_T6fkA6eEg"
YOUTUBE_CHANNEL_ID_98 = "UC7UiU2cblsMrNujtOX_Zx2A"
YOUTUBE_CHANNEL_ID_99 = "UCze1-wAN4djo1lDN75YfUnQ"
YOUTUBE_CHANNEL_ID_100 = "UCOL9lEZS41eUfgX2Tn84PsA"
YOUTUBE_CHANNEL_ID_101 = "UCGMGmvdpzrnW3YVM0bLKFBA"
YOUTUBE_CHANNEL_ID_102 = "UCigb9BYOYeoMsWf3FxnKPWw"
YOUTUBE_CHANNEL_ID_103 = "UC87DLEIh2aFbaAfbQV616GA"
YOUTUBE_CHANNEL_ID_104 = "UCGJvSaEhya7YfDpjetMM-QQ"
YOUTUBE_CHANNEL_ID_105 = "PLS6X7rllUWyX1G1ZtbN1MW6IKH7Px2v9-"
YOUTUBE_CHANNEL_ID_106 = "PLzDOayMZNPMCeoG8ugT6qQjBt67rpacKP"
YOUTUBE_CHANNEL_ID_107 = "PLtbVmfMNVRXrsVfbAQ4mr1Qfaier0X0cA"
YOUTUBE_CHANNEL_ID_108 = "PLtU-85XZpIhhGKquKTiIEQFLpq-WYfWpn"
YOUTUBE_CHANNEL_ID_109 = "UCTogQKdBJaE56b7Be9i_oMQ"
YOUTUBE_CHANNEL_ID_110 = "UCpxRT77EG-G1b3LOhLWsDTA"
YOUTUBE_CHANNEL_ID_111 = "PLdYDihWIBOKX6XfRRdBCKxY0sPf88Kvj1"
YOUTUBE_CHANNEL_ID_112 = "PL3qRa14ih-NZxbp8j0R6T-ZKPveLWG07i"
YOUTUBE_CHANNEL_ID_113 = "PLlzSTcVtcJqEKC5txIuj_luJ6vLpAvXMD"
YOUTUBE_CHANNEL_ID_114 = "PLZVMGCh7sZUh_jIqrYMKYyyPNJtpng_ZC"
YOUTUBE_CHANNEL_ID_115 = "PL2SeSnW3tiZ8MHBBrzuz1XRNEJGlqAWc0"
YOUTUBE_CHANNEL_ID_116 = "PL6FytxeqgcEga0kEGnWZhqnuXypzYtovc"
YOUTUBE_CHANNEL_ID_117 = "PLz0F8p0BAiggu0qXQgFn82l7bjEnVSCA-"
YOUTUBE_CHANNEL_ID_118 = "PLaLo3MUy2OeTit-pQnB8a9Y4kNAPT3m7s"
YOUTUBE_CHANNEL_ID_119 = "PLHo-IIm0ajO17sNaDEGSaEmPs-R9Ng_GX"
YOUTUBE_CHANNEL_ID_120 = "PLlcTlHW42LbekPhnTJxHXdh-P8SBrlhCT"
YOUTUBE_CHANNEL_ID_121 = "PL4ECBE51B024AE1E7"
YOUTUBE_CHANNEL_ID_122 = "PL06iOPB7b1v0VuqUOoOtURFBGgFta-mE9"
YOUTUBE_CHANNEL_ID_123 = "PLZs0gQed9tMRloC4-pJE9GvOSrbGYDYDE"
YOUTUBE_CHANNEL_ID_124 = "PLZs0gQed9tMQJ2UTqLPoGy53mc5d0U0XU"
YOUTUBE_CHANNEL_ID_125 = "PLZs0gQed9tMRqzYIdbEXit8dKe0AiKzKe"
YOUTUBE_CHANNEL_ID_126 = "PLZs0gQed9tMQ_1xnqZ2ALhJ1wCCOuNqYE"
YOUTUBE_CHANNEL_ID_127 = "PLZs0gQed9tMQpC2SaGc60_drB6WyNI4OA"
YOUTUBE_CHANNEL_ID_128 = "PLZs0gQed9tMQu25Ht6uuZkjQEDe9NDbwU"
YOUTUBE_CHANNEL_ID_129 = "PLZs0gQed9tMQCtXmJ3Szsur08dVTDtz62"
YOUTUBE_CHANNEL_ID_130 = "PLZs0gQed9tMRAfBGlQhHCcqaJipEknlVM"
YOUTUBE_CHANNEL_ID_131 = "PLZs0gQed9tMQxKnMoIqQp0p8_DSJFwlBc"
YOUTUBE_CHANNEL_ID_132 = "PLZs0gQed9tMQJLvfGXI5S9X1jpgKQiic5"
YOUTUBE_CHANNEL_ID_133 = "PLZs0gQed9tMSvcfcrUr5V44AmnRWAFa2H"
YOUTUBE_CHANNEL_ID_134 = "PLZs0gQed9tMSSeEiKEbi0Fm7JUp9mQAf3"
YOUTUBE_CHANNEL_ID_135 = "PLZs0gQed9tMQdK9a6D3T0yfZtsc4fpMUx"
YOUTUBE_CHANNEL_ID_136 = "PLZs0gQed9tMSJwsr7nELmSe_wHWw-gFxL"
YOUTUBE_CHANNEL_ID_137 = "PLZs0gQed9tMSXPP9r3WfKNbh8HgjOdrsC"
YOUTUBE_CHANNEL_ID_138 = "PLZs0gQed9tMR8aJs0E6Ls8yzrZfk9vcU5"
YOUTUBE_CHANNEL_ID_139 = "PLZs0gQed9tMQ6skxELLDva4wIpy8UgRIQ"
YOUTUBE_CHANNEL_ID_140 = "PLZs0gQed9tMSbH-6lTVlrJHLzsip-Vw7u"
YOUTUBE_CHANNEL_ID_141 = "PLZs0gQed9tMR_C9CvNi8pVHM7rZDhpGHL"
YOUTUBE_CHANNEL_ID_142 = "PLaE8D0PEpUTtHl3NzB3VfscnmW68cZC58"
YOUTUBE_CHANNEL_ID_143 = "PLZs0gQed9tMSxxk4TrkcpLEVj8TLCepMi"
YOUTUBE_CHANNEL_ID_144 = "PLZs0gQed9tMTVLl2xnWN926ik1puyHc-v"
YOUTUBE_CHANNEL_ID_145 = "PLZs0gQed9tMQQWwyr8zptzMEXpMtVm58w"
YOUTUBE_CHANNEL_ID_146 = "PLZs0gQed9tMQNTbpbaMFpRvnQCwBEfWyR"
YOUTUBE_CHANNEL_ID_147 = "PLbhhIrKiYXKGMp5tLq58a0E9cqSHlpTAa"
YOUTUBE_CHANNEL_ID_148 = "PLXCPQ6zcOQ411DyMFC5wGnD8BNIMVrlhb"
YOUTUBE_CHANNEL_ID_149 = "PLWIeYs8AOmKznMRlF-CJj4qWhMulDBYQI"
YOUTUBE_CHANNEL_ID_150 = "PLZs0gQed9tMTc6Ya2V7ooJD8KgVnpxG0J"
YOUTUBE_CHANNEL_ID_151 = "PLZs0gQed9tMSlk8TkP1571MdPOoO76-xz"
YOUTUBE_CHANNEL_ID_152 = "PLG8yD0KLSSx602X8o7nS4d3dUg7oYc_Sw"
YOUTUBE_CHANNEL_ID_153 = "PLBuQjTjLLLgzAxxC6lysDD-WO6x0CPFBQ"
YOUTUBE_CHANNEL_ID_154 = "PLXHVSLxGAvNlBsEYfkfE9GXWNWAy7VpCG"
YOUTUBE_CHANNEL_ID_155 = "PLL3mxRQjTWGD1i4_Mw_L3jDgHODHXC_Bd"
YOUTUBE_CHANNEL_ID_156 = "PLL3mxRQjTWGAD0yrY_XrqVL-xs3fWG51c"
YOUTUBE_CHANNEL_ID_157 = "PL756XNZsKKiOMmHezr5K3DaUca8FvuMjk"
YOUTUBE_CHANNEL_ID_158 = "PL756XNZsKKiPWEMixEpdzaBlfs104_Mj5"

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
        title="The Best Kids Cartoons",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-229S3kh3t3I/AAAAAAAAAAI/AAAAAAAAAAA/-_eZEl708IQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Byegone Toons",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-Sk2orfS3j2k/AAAAAAAAAAI/AAAAAAAAAAA/qPilOUV-bXs/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kids Cartoons",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-FqRsQuAzliE/AAAAAAAAAAI/AAAAAAAAAAA/w7qbXCe4PcY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cartoon TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-KA_kP8kdNrU/AAAAAAAAAAI/AAAAAAAAAAA/r45pM1ldKhk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="8th Man DVD Cartoon Collection",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-WOQwEChDMUg/AAAAAAAAAAI/AAAAAAAAAAA/SSvectrYZck/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Closed Captioned Cartoons",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://i.ytimg.com/i/sfKUNMk_fUy2EDm3cjygKw/mq1.jpg?v=4f137b8a",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="TV Samsung Cartoons",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-6IA2HKKn5Ro/AAAAAAAAAAI/AAAAAAAAAAA/MPdQtzKS7L0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TootsToons",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://i.ytimg.com/i/33y1tTCzjbAWAREzZz6Nng/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TV Cartoons",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-XYmdv5r8BBc/AAAAAAAAAAI/AAAAAAAAAAA/DbE36-RDMhE/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cartoon Master",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-8lj7YVWCskg/AAAAAAAAAAI/AAAAAAAAAAA/Way92Wjjxpc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AnimationStreet Network",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-GCen9oLHz7Q/AAAAAAAAAAI/AAAAAAAAAAA/Fe0aSexkaYA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classics or Bust",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-nRP7RrvD7xk/AAAAAAAAAAI/AAAAAAAAAAA/oY3nqY7tf2Q/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dandy Deal Media - Classic Cartoons",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-fh8nVxoa_Lo/AAAAAAAAAAI/AAAAAAAAAAA/KYIUIZKo5cY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Terry Toons",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://static.wixstatic.com/media/cafcb6_7db65b19921e41f38e1112d173677be1.jpg/v1/fill/w_500,h_500,al_c,q_90/file.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nicktoons",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://www.amoeba.com/sized-images/max/500/500/uploads/albums/covers/other//799923210101.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cartoon Network",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-bqghK5VAO2I/AAAAAAAAAAI/AAAAAAAAAAA/HMEsmSxzbKg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mickey Mouse",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="http://img.clipartall.com/mickey-clip-art-clipart-mickey-mouse-500_500.gif",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pink Panther",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-lwlGXn90heE/AAAAAAAAAAI/AAAAAAAAAAA/FmCv96eMMNE/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="BEE DO - Cartoons For Kids",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://www.digitopz.com/images/minion.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Spookiz - Cartoons for Children",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-ucLJwX-w0os/AAAAAAAAAAI/AAAAAAAAAAA/o2tqriXXtNw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pencilman Cartoons",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/-NPT1pHVOgxU/AAAAAAAAAAI/AAAAAAAAAAA/UJFZQTNyYS0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Wildbrain Kids Videos",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://yt3.ggpht.com/-t0NiM7lSE5o/AAAAAAAAAAI/AAAAAAAAAAA/2HtjG3pVBdM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Weird-Ohs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/49/0b/26/490b26f67bbd47a9243ded8e2f4fb738.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Batfink",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Foster's Home for Imaginary Friends",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Codename Kids Next Door",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dexter's Laboratory",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Twisted Tales of Felix The Cat",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Felix The Cat",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Courage the Cowardly Dog",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Grim Adventures of Billy and Mandy",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ed, Edd n Eddy",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tom Slick",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Milton the Monster",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Flintstones",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Jetsons",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Powerpuff Girls",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Courage the Cowardly Dog",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hulk and the Agents of S.M.A.S.H.",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Spider-Man and His Amazing Friends",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dino-Riders",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mighty Mouse: The New Adventures",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Frankenstein, Jr. and The Impossibles",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Sylvester and Tweety Mysteries",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Dick Tracy Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jayce and the Wheeled Warriors",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Rocky and Bullwinkle Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Super Hero Squad Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The New Casper Cartoon Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Casper the Friendly Ghost",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Cool McCool",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Super Chicken",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Animaniacs",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pinky and The Brain",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tiny Toon Adventures",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Looney Tunes Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Baby Looney Tunes",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bugs Bunny",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Daffy Duck",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tasmanian Devil",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Speedy Gonzales",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="He-Man and the Masters of the Universe",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_62+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The New Adventures of He-Man",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_63+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="She-Ra: Princess of Power",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_64+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Darkwing Duck",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_65+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Samurai Jack",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_66+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cow and Chicken",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_67+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Regular Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_68+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Camp Lazlo",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_69+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Crusader Rabbit",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_70+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tennessee Tuxedo and His Tales",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_71+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Commander McBragg",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_72+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Go Go Gophers",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_73+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Klondike Kat",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_74+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Top Cat",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_75+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Underdog",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_76+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fat Albert and the Cosby Kids",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_77+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="George of the Jungle",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_78+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Freakazoid",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_79+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rugrats",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_80+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Johnny Bravo",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_81+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="BraveStarr",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_82+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Teen Titans",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_83+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ThunderCats",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_84+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SilverHawks",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_85+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )           

    plugintools.add_item( 
        #action="", 
        title="The Mighty Hercules",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_86+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Archie Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_87+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Scooby-Doo, Where Are You",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_88+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Beany and Cecil",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_89+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Count Duckula",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_90+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tom and Jerry",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_91+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Colonel Bleep",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_92+"/",
        thumbnail="https://yt3.ggpht.com/-357qSj0eCeY/AAAAAAAAAAI/AAAAAAAAAAA/UunCRpL6JzI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Groovie Ghoolies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_93+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hong Kong Phooey",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_94+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Magilla Gorilla",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_95+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jabberjaw",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_96+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Secret Squirrel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_97+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Atom Ant",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_98+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Squiddly Diddly",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_99+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Snagglepuss",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_100+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Quick Draw McGraw Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_101+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Hillbilly Bears",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_102+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dynomutt, Dog Wonder",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_103+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Captain Caveman and the Teen Angels",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_104+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Spongebob Squarepants",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_105+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Tex Avery",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_106+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Beavis and Butthead",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_107+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SPUMCO Cartoons",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_108+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Simpsons - Funniest Moments",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_109+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Simpsons and Futurama (English and Spanish)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_110+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="Batman The Animated Series", 
        title="",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_111+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="South Park",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_112+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Fairly OddParents",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_113+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Teenage Mutant Ninja Turtles",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_114+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Courage the Cowardly Dog",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_115+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Duck Tales",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_116+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Phineas and Ferb",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_117+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kim Possible",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_118+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Adventure Time",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_119+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Danny Phantom",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_120+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tweety And Sylvester",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_121+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hey Arnold",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_122+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Woody Woodpecker",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_123+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tooter Turtle",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_124+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Possible Possum",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_125+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hashimoto Mouse",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_126+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="New Adventures of The Lone Ranger",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_127+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Blackstar",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_128+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Inspector",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_129+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The New 3 Stooges",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_130+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )           

    plugintools.add_item( 
        #action="", 
        title="Abbott and Costello Cartoon",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_131+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Raccoons",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_132+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Delta State",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_133+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Josie and The Pussycats",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_134+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ruff and Reddy Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_135+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Battle of The Planets",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_136+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Manta and Moray",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_137+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Harlem Globetrotters Cartoon",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_138+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Space Pirate Captain Harlock",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_139+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bailey's Comets",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_140+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Space Sentinels",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_141+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Smurfs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_142+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Freedom Force",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_143+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Heyy It's The King",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_144+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Spider-Woman",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_145+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Beary's Family",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_146+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="HB Cartoons",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_147+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Old Cartoons",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_148+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Old Cartoons Collection",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_149+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Heathcliff",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_150+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Space Angel",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_151+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Rubik, The Amazing Cube",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_152+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lucky Luke",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_153+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Asterix",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_154+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tom Terrific",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_155+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Raggy Dolls",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_156+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pingu",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_157+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Christopher Crocodile",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_158+"/",
        thumbnail="https://img1.cgtrader.com/items/23683/9cba39f7d9/large/tv-cartoon-3d-model-max-obj-fbx.jpg",
        folder=True )          
run()
