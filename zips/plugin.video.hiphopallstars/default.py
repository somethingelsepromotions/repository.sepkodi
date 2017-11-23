# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Hip Hop All Stars
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

addonID = 'plugin.video.hiphopallstars'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLH6pfBXQXHEC2uDmDy5oi3tHW6X8kZ2Jo"
YOUTUBE_CHANNEL_ID_2 = "PLem8IhDsJT-cimo3nFCzxOLbomIrAzuDv"
YOUTUBE_CHANNEL_ID_3 = "HipHopHead984"
YOUTUBE_CHANNEL_ID_4 = "PLljjkvywaiU1cYnFnVN3XIl5wmpM33LsN"
YOUTUBE_CHANNEL_ID_5 = "PL4aW3pSwgaEgGojD4-ZZIqJwIMLRjwvXt"
YOUTUBE_CHANNEL_ID_6 = "PLnoGHb5y3Ua0WBg_RGQyXFnhDzoNPPVwB"
YOUTUBE_CHANNEL_ID_7 = "PLdygkKPROAjYQmfYCtwHb_YGy5jlH93BL"
YOUTUBE_CHANNEL_ID_8 = "PLOtHap_qwlUh3nhli8DkCX06e2BXEdluQ"
YOUTUBE_CHANNEL_ID_9 = "PL2kicx1M78xVpraHDj0XUWcMjGyGMzL4c"
YOUTUBE_CHANNEL_ID_10 = "PLLQ4C_mDWRDQ6PMg5AbKelvbKZ5CTmtXm"
YOUTUBE_CHANNEL_ID_11 = "PL2YL6XQrENMBWymE4VdI6V2qfqw_aOLDb"
YOUTUBE_CHANNEL_ID_12 = "PLn3RU2qrqR1vxvgFr8xlqltqZ6m4GzaWI"
YOUTUBE_CHANNEL_ID_13 = "PLXM_bTGRgFXtbEDlyu9WUJexGI2dHQ1xG"
YOUTUBE_CHANNEL_ID_14 = "PLFO0esT_hEQQnMKuSCWniM6JP14t30wwt"
YOUTUBE_CHANNEL_ID_15 = "PLcz6fUTBbvlcyqfuNc1ilNxHQduNDfRpY"
YOUTUBE_CHANNEL_ID_16 = "PLz8k87WbRq9fPb5pCyKM9owGOHVyG5Ye3"
YOUTUBE_CHANNEL_ID_17 = "PLJdDgfq34Jz3BBKztqqnFWMopLwxmaU0p"
YOUTUBE_CHANNEL_ID_18 = "PLgXJI_F2zukK-3zspCjujumPnfTvSDtFH"
YOUTUBE_CHANNEL_ID_19 = "PLkL4SJghbvu33IhtSTjANB6gGcKuPqDnn"
YOUTUBE_CHANNEL_ID_20 = "PLFHSUPwTPcT1cU-4m9rSdUeS2sW6fDa-8"
YOUTUBE_CHANNEL_ID_21 = "PLVXEAAVgpjHH2A8IQIDvyzTQbJJ7xzHOx"
YOUTUBE_CHANNEL_ID_22 = "PLDt749rNtV4PLBg0FtqyLTo-1qmanRspG"
YOUTUBE_CHANNEL_ID_23 = "PLTEeFFaxBqw03JGafc4Ehu7sBO3NEaxSW"
YOUTUBE_CHANNEL_ID_24 = "PL3mJibUqMz6HA6lYziMXRaBd98v2UzRzl"
YOUTUBE_CHANNEL_ID_25 = "PLSEuD2vPF0ondtZjvhWvTYbw5R61C3Xps"
YOUTUBE_CHANNEL_ID_26 = "PLIgoWXhRhkH6xdfmPCrbJfj3SVYkaL7o1"
YOUTUBE_CHANNEL_ID_27 = "PLZS-o3pN86ga2lHhcM36bOTXtOo_rlALR"
YOUTUBE_CHANNEL_ID_28 = "PLI6Wzy3GVpd6N7Ob5SR87AbNJEcqJUE2P"
YOUTUBE_CHANNEL_ID_29 = "PLNHzQT4ppCxnY1An1KZhL18VLTCqC9fKl"
YOUTUBE_CHANNEL_ID_30 = "PLe8yMKfOayhoKuKX6sVv9VPbi5IKfDpxq"
YOUTUBE_CHANNEL_ID_31 = "PLvkrZwZvuNXAMdgiTCnkthw6PXfoQc9y_"
YOUTUBE_CHANNEL_ID_32 = "PLe9ajjFHyFIOnREwsnlhlBYNumBn6LHZe"
YOUTUBE_CHANNEL_ID_33 = "PLcg-xzem56OuA79eJNZ17oIOaJWDZRTOs"
YOUTUBE_CHANNEL_ID_34 = "PL-o37YO_uwcKpI9rviZ_08vUbORUDGRdb"
YOUTUBE_CHANNEL_ID_35 = "PLPOn8-id9kgBdpfyIn5Q-4CqGKaUWY9sO"
YOUTUBE_CHANNEL_ID_36 = "PLaFT49lKqsFp9WY3H34CJicukSq7MkPqT"
YOUTUBE_CHANNEL_ID_37 = "PLqusSNNVI7b4C5RV20C0qZx9Z1qnQJqpr"
YOUTUBE_CHANNEL_ID_38 = "PLZOkLRe_Ma3VTZI4UsOnhxYV-YIy4ofZf"
YOUTUBE_CHANNEL_ID_39 = "PLUYm_z71Z8pfDuOjNrm4VZ8Z23NzI_hfi"
YOUTUBE_CHANNEL_ID_40 = "PLjSqQ0qZg8T-IHG8TzL-jzULiAiZAwqN-"
YOUTUBE_CHANNEL_ID_41 = "PLQ9w3p9PtFA7Yil4mqfDYQGTBRrC99CEG"
YOUTUBE_CHANNEL_ID_42 = "PLpXROUIDg5C-MxRYzsmj3gwRmWo-3jUY5"
YOUTUBE_CHANNEL_ID_43 = "PLR_cIlfBurPXlfehrdwe1l5Q_OMOhpqG2"
YOUTUBE_CHANNEL_ID_44 = "PL76h-g8Ggldg0qFzdkXgCIwJKgA2JDhRj"
YOUTUBE_CHANNEL_ID_45 = "PLscvXDtcGr6Vz6R3tIetnScvbGlerha5w"
YOUTUBE_CHANNEL_ID_46 = "PLZpx5y1EbKuDKXL9EKw3UFYjVdKcKLqbo"
YOUTUBE_CHANNEL_ID_47 = "PLImiV1vVZGUllIdbbFH7strE6B4EWq8Ub"
YOUTUBE_CHANNEL_ID_48 = "PLsnWMwMTkllUO_6OPAM3bnoLDscRdyfMx"
YOUTUBE_CHANNEL_ID_49 = "PLURwsAewiTh0nx2ubwXuQm_JPn8BCJYbK"
YOUTUBE_CHANNEL_ID_50 = "PL4TrGu5rwzH_GuYUQQQyLmGa1Te69WA-n"
YOUTUBE_CHANNEL_ID_51 = "PLyWg_DUvxO2Wf3m4-lvKDYO1QHKWiCISN"
YOUTUBE_CHANNEL_ID_52 = "PLC0w3lEHx2SHrmVxnhuNYDs13iHHugQGD"
YOUTUBE_CHANNEL_ID_53 = "PLqwX5JyleHem89NDxucif1BkuuXmv5k2s"
YOUTUBE_CHANNEL_ID_54 = "PLorbxqHG7IW47TT4nw0ZSzp5iHkXQw1dJ"
YOUTUBE_CHANNEL_ID_55 = "PLiy6fM6jYdYHQNpzgtTE8ROPswBM4tBNr"
YOUTUBE_CHANNEL_ID_56 = "PLJ6z_vXJKxu2GVkD0xTZt7AwLCuALkWxj"
YOUTUBE_CHANNEL_ID_57 = "PLtaYARusHpmxmCH8jmKXVKTcFUqWoWXUx"
YOUTUBE_CHANNEL_ID_58 = "PL6ZJKqB5KpNdAWChZm1psN8f8R261XdEx"
YOUTUBE_CHANNEL_ID_59 = "PLlZOaLWXBglc78WjJ6_m9TuCoa89kZ-jf"
YOUTUBE_CHANNEL_ID_60 = "PLQo4-T96b_T4qPYlR7KE0PS8SLp6MoSeI"
YOUTUBE_CHANNEL_ID_61 = "PL9mRQVVv1z4MK4Ji_yeYkC5Fzzd4yaQQs"
YOUTUBE_CHANNEL_ID_62 = "PLM5UDu4_tiS_wK6zfHWGelCBTCg_WZ_rt"
YOUTUBE_CHANNEL_ID_63 = "PLOPdOVbage2p5JxyuBbWMC-oFHbc4YF2n"
YOUTUBE_CHANNEL_ID_64 = "PL4W8R09fH8WBfj0HeTFSdIoqsCEekY07M"
YOUTUBE_CHANNEL_ID_65 = "PLECta8P4s8fgi1mXHsaG7PK-uqOuoLuS1"
YOUTUBE_CHANNEL_ID_66 = "PL68938922BD14537F"
YOUTUBE_CHANNEL_ID_67 = "PLXSWNgXItHpqIB_NqbPJatLhJ7ya-PBUK"
YOUTUBE_CHANNEL_ID_68 = "PLZS72KjI4Am5mUXXEkiItBLycOCNMDSvQ"
YOUTUBE_CHANNEL_ID_69 = "PLQfEYFseEhk7j9sRUmYj3gjii8pgLMpJk"
YOUTUBE_CHANNEL_ID_70 = "PLL8N99hsW_mvV3OgErmbgLp9-x_4WvQoy"
YOUTUBE_CHANNEL_ID_71 = "PLQw3xggCuGQX9Kc6h_KvIJKOacuz-lcAT"
YOUTUBE_CHANNEL_ID_72 = "PLKItUPR--VWe3dKD_aUvYKNmbl_uqfVuw"
YOUTUBE_CHANNEL_ID_73 = "PL8LJJ1Zu1yOGnNcuSjPexDxlFMi8AQFTY"
YOUTUBE_CHANNEL_ID_74 = "PLWoovEpjozlfoMgf76ZxoynuqBOEElpEt"
YOUTUBE_CHANNEL_ID_75 = "PLq2_OrsJJtCsU_vDRfCulmPcBMYpVPV4Y"
YOUTUBE_CHANNEL_ID_76 = "PL8MfC2S-6P4c7kFobDQZgpz7_GkhhAph9"
YOUTUBE_CHANNEL_ID_77 = "PLXu_cA-xfxWuFk2B6xUUj69R7Fl3QnU9U"
YOUTUBE_CHANNEL_ID_78 = "PLIen3IPVo_U14nc1_OuU6P2Yfek9llxeL"
YOUTUBE_CHANNEL_ID_79 = "PLSHlZDOrNzDRFH6yOhSoufTkj7XvDzndw"
YOUTUBE_CHANNEL_ID_80 = "PLMOqpyVO0Oa0RdGuUQaLxl8B4-y6RANHe"
YOUTUBE_CHANNEL_ID_81 = "PLUdHxMzuw1wvnSfUP4hXZvQqMWqeGbxbS"
YOUTUBE_CHANNEL_ID_82 = "PLRbOvT-YYSdcdt4ydf9YC79X0veHkfK1M"
YOUTUBE_CHANNEL_ID_83 = "PLjY59Jtm2tT3OEgUwx1FsDYzokROUma28"
YOUTUBE_CHANNEL_ID_84 = "PLvrjXtzsj46xUjuD7OBy2shmWcIuZpVCA"
YOUTUBE_CHANNEL_ID_85 = "PLKN1i6zfpeL1wAdau8N3trNP0LilZ4Mdv"
YOUTUBE_CHANNEL_ID_86 = "PL7fnCqkcp3vaGRxnRLLWCU5cUh4LxTCSX"
YOUTUBE_CHANNEL_ID_87 = "PLasA1IRBDbhwBOJg7NLhIluQ9Aaw9RDpj"
YOUTUBE_CHANNEL_ID_88 = "PLNyy-oav0kVgNPTLYX18YuINT_YJE8Qsu"
YOUTUBE_CHANNEL_ID_89 = "PLpxwTs__tzr_k9MFajTDc8GAXR0QCA86a"
YOUTUBE_CHANNEL_ID_90 = "PLRMCvo9Td7TQQKFTcR3hu9NXjx_Ba78Ro"
YOUTUBE_CHANNEL_ID_91 = "PLf297xrOYnmRSCXgE_q1sZl8WCiLmVUQJ"
YOUTUBE_CHANNEL_ID_92 = "PLqdpZOA7TkTCvoNNeUGZJZHl54VQjeBLK"
YOUTUBE_CHANNEL_ID_93 = "PLrESV-wDzKIpkXqjrIf7WfGTsepoPSv2o"
YOUTUBE_CHANNEL_ID_94 = "PLJXSAxngU0AxYdDfigVxf900EOQBS5YTf"
YOUTUBE_CHANNEL_ID_95 = "PLgUuM4N3bcs0OH759cfiO5vU9U3K9BwGy"
YOUTUBE_CHANNEL_ID_96 = "PLU9m9dFtBL7v_Z4b88UE5sQrVy3THETL-"
YOUTUBE_CHANNEL_ID_97 = "PLFOCbUxrGkuXYWlG98-HqBbpMf9zmwEmy"
YOUTUBE_CHANNEL_ID_98 = "PLgEFVNPXJhThJs5FS8d7pLz53b1VPDGkj"
YOUTUBE_CHANNEL_ID_99 = "PLHz8__39LkNsvNEjkNUE9GT0_KYGdUV3f"
YOUTUBE_CHANNEL_ID_100 = "PLTldUy0Fnxo0WEJ6MBG6IB954Wdl7QPKx"
YOUTUBE_CHANNEL_ID_101 = "PLYagrqIg-kgQlqEuQmF7h6xzQEzi_lWYd"
YOUTUBE_CHANNEL_ID_102 = "PLfQALVM3SEjKIAhLc-O_5ppIDQBeLYTnR"
YOUTUBE_CHANNEL_ID_103 = "PLI39WpFBNkJbJ8IIIg_RC7BA1OMwDQspe"
YOUTUBE_CHANNEL_ID_104 = "PLW6T6hR4z1YTV9cK_jaaWCqCeNr9S9Gif"
YOUTUBE_CHANNEL_ID_105 = "PLcdAlXF2GZN4hKTGV05Cb4UHRNNGWdcaR"
YOUTUBE_CHANNEL_ID_106 = "PLVtAszTC0uBNG746a7Lu95DIiXdKYhxOT"
YOUTUBE_CHANNEL_ID_107 = "PLIMRwcdsgjPyh1x5ob3_tVGMQsR8XvSrH"
YOUTUBE_CHANNEL_ID_108 = "PLZqfys784zTCM9OLTFIWQ-ABz1SFSG_H_"
YOUTUBE_CHANNEL_ID_109 = "PL7BWRas7Ft4SwNnysgTF-UuERp-FcXjge"
YOUTUBE_CHANNEL_ID_110 = "PLRenhQjuCDJaPCUrC2tommsFy2MhbJCyN"
YOUTUBE_CHANNEL_ID_111 = "PLY7uDWQtM6lMqthKADz5D4G9Corcqw5KJ"
YOUTUBE_CHANNEL_ID_112 = "PLtbsu4TDgPoBq_Q9dzocloNX9oq6LIMPE"
YOUTUBE_CHANNEL_ID_113 = "PLf8nuFkWHjxIMskpkr9tKYbz6TdsD7czW"
YOUTUBE_CHANNEL_ID_114 = "PLazvjMpvktRuuoKZiYoqdjMqjqadxHJ4i"
YOUTUBE_CHANNEL_ID_115 = "PLr6xPtmPzp4oBb3Ao3Bgkj9iwWocKtrjG"
YOUTUBE_CHANNEL_ID_116 = "PLyryiSZDpmKRCfBiOQdQhxFagMqsINn49"
YOUTUBE_CHANNEL_ID_117 = "PLegvV8yC11ja5xmIvaRTj6hZ7lMeP4f6N"
YOUTUBE_CHANNEL_ID_118 = "PL8cFaF2b783IeZqu3zHc1SZ7qQGZuN-p9"
YOUTUBE_CHANNEL_ID_119 = "PLrjdEx06NlK0rE6OabK1Bm47YZaAuWRYJ"
YOUTUBE_CHANNEL_ID_120 = "PLsm5XUxQMl307n-yD12GstC8xDMNqSsPQ"
YOUTUBE_CHANNEL_ID_121 = "PLF-U_iSNJNQCUQc5EhpEni53qA_maSw_w"
YOUTUBE_CHANNEL_ID_122 = "PLKmsKsHUkedgvdxOJywibGEsK0FHG-wBH"
YOUTUBE_CHANNEL_ID_123 = "PLNF1TtPlNbF87k2HshqLCpvEFTSlrspTB"
YOUTUBE_CHANNEL_ID_124 = "PLz8qDTzkzQpp2uo86617y22-Dvr2sVwRN"
YOUTUBE_CHANNEL_ID_125 = "PLkcpByyL4FmbpQ1jaqvBRAw-LE9w9HMWE"
YOUTUBE_CHANNEL_ID_126 = "PLVCo0h-sEai2qccBdo0VKN-H00Jnqr6f8"
YOUTUBE_CHANNEL_ID_127 = "PLYqjs1ORgYMDHaNRsOLYMR9qus-VnMVL3"
YOUTUBE_CHANNEL_ID_128 = "PLkuSzeI2fUSBHs0c7ByF96C7Frqo4a278"
YOUTUBE_CHANNEL_ID_129 = "PL7X4NB3jlC3DpVqtUf_2l5zl8m_ePmvRP"
YOUTUBE_CHANNEL_ID_130 = "PLmayP0qOPHaJ54EuSTVMJIqG-im0LD8O0"
YOUTUBE_CHANNEL_ID_131 = "PL26lA2tCTUTZCNO0mKOOwA9SiE-z-EdQY"
YOUTUBE_CHANNEL_ID_132 = "PL4X8rYZufkbEcHZ_6yAHvYj7L_6X3W5dA"
YOUTUBE_CHANNEL_ID_133 = "PL9cH1TMoR4gqW5AcCWqJf7b1Pb3mKwfUM"
YOUTUBE_CHANNEL_ID_134 = "PL6cgwntb-Zirocja2vht4HiGnjicCaVPx"
YOUTUBE_CHANNEL_ID_135 = "PLPuMLy5yHHg14vw1fvCtuHmoBt3cRRnDG"
YOUTUBE_CHANNEL_ID_136 = "PL1dZRqTYNUq5tM2A8DCMAG8FH81ip5cBA"
YOUTUBE_CHANNEL_ID_137 = "PLjkZ3aAAbxk-w1FIUwMyKZEb2SxajGDnQ"
YOUTUBE_CHANNEL_ID_138 = "PLgXtP7yM0g1ZFYIo3LZTY8OlyVrVd"
YOUTUBE_CHANNEL_ID_139 = "PLcI1W-8bxk6XG_LdWlfMcaieQgokwbh0l"
YOUTUBE_CHANNEL_ID_140 = "PLqBlBO5uObwvQCXetyLxxWjemsSb8EE8T"
YOUTUBE_CHANNEL_ID_141 = "PLWbJY5eyv5CC1ZLuiCDPDREFtXH3AbRJz"
YOUTUBE_CHANNEL_ID_142 = "PLzM4WCcpOyDHNobTGOVe_ad4QLsyuRFtJ"
YOUTUBE_CHANNEL_ID_143 = "PLD9u-7LefgfO8qBLC84v1zz4JbPw7SIgQ"
YOUTUBE_CHANNEL_ID_144 = "PL_rrV0ZUBc_1Gne8y91EaiGSE0V15-zx-"
YOUTUBE_CHANNEL_ID_145 = "PLkKaok32A3scqg0J9MwVcZEVrU4JP_VO4"
YOUTUBE_CHANNEL_ID_146 = "PLyn8nyoIEv_6x1_oGeWDQLUBq83M9_2HZ"
YOUTUBE_CHANNEL_ID_147 = "PLSf4VENc-Z0_XGSepdZph-Hn4WkuAoRoW"
YOUTUBE_CHANNEL_ID_148 = "PLvRo-160Sv4RRAaibHCg6JbGb8xUNdike"
YOUTUBE_CHANNEL_ID_149 = "PLooYZnvGcpTSc-37ihLvVOK2FO-3vbBO4"
YOUTUBE_CHANNEL_ID_150 = "PLlpqT48w_qlkdtZiFTr5JugMtf1HPJiMj"
YOUTUBE_CHANNEL_ID_151 = "PLQDtEy7VBpb6eAeXg6RH2Ko1XkVZGY1GI"
YOUTUBE_CHANNEL_ID_152 = "PLeRTJl0ikTytQIqIkbdSaoM1Al3MzXQxo"
YOUTUBE_CHANNEL_ID_153 = "PLv-35pRxf3tJCBCOmOai5znYJG9-Uul8G"
YOUTUBE_CHANNEL_ID_154 = "PLT0KD4wgS6_R-5ibJ6mev150CbYmmj-3y"
YOUTUBE_CHANNEL_ID_155 = "PLySqZTaxcl5R01tZfDEf-ZUVsCvomb5o5"
YOUTUBE_CHANNEL_ID_156 = "PLJkqBXPzFZPh7y4atXTfEEh41iKADkixa"
YOUTUBE_CHANNEL_ID_157 = "PLYdgCn55M6IvNqRnyhUtCNsxuVNJ4bp-c"
YOUTUBE_CHANNEL_ID_158 = "PL_bQ3bfYo9ZV24mw1SXj70dxzqBvnpkdM"
YOUTUBE_CHANNEL_ID_159 = "UC-yXuc1__OzjwpsJPlxYUCQ"
YOUTUBE_CHANNEL_ID_160 = "PL9uczDoXQxSaxoyw9Ye08vbTH7BkQDz0e"
YOUTUBE_CHANNEL_ID_161 = "PL-95FHe5Zg6c2CJt-xGMA80K5ub9ApwFN"
YOUTUBE_CHANNEL_ID_162 = "PLVCWa6VveQWYLxI_89VHorqn2KGznjDUz"
YOUTUBE_CHANNEL_ID_163 = "PLNFI79D7MYqMWP3UdJhsWy-kih9XR_PMA"
YOUTUBE_CHANNEL_ID_164 = "PLSKRTjON-rKqFWOyWJDorV4UkY6fCsvLM"
YOUTUBE_CHANNEL_ID_165 = "PLqHU8MDc5CePEG6JtJm6aNowunV0fRmHC"
YOUTUBE_CHANNEL_ID_166 = "PLv5Fwl5i4UvQNanCPkf9dDx0kq6xuTTlX"
YOUTUBE_CHANNEL_ID_167 = "YoungThugOnline"

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
        title="Hip Hop Top Tracks",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://pbs.twimg.com/profile_images/659760227747631104/KXmQDze9.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hip Hop Popular",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://pbs.twimg.com/profile_images/659760227747631104/KXmQDze9.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hip Hop Albums",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://pbs.twimg.com/profile_images/659760227747631104/KXmQDze9.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Old School Hip Hop",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://pbs.twimg.com/profile_images/659760227747631104/KXmQDze9.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Underground Hip Hop",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://pbs.twimg.com/profile_images/659760227747631104/KXmQDze9.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="2 Chainz",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://i.huffpost.com/gen/1347832/images/o-CHAINZ-facebook.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="21 Savage",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://assets5.capitalxtra.com/2016/45/21-savage-instagram-7-1478712485-view-1.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="50 Cent",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://www.famousbirthdays.com/headshots/50-cent-6.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="A$AP Rocky",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://media.breitbart.com/media/2016/07/ASAPRocky1-640x480.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="A Boogie wit da Hoodie",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://image-ticketfly.imgix.net/00/02/62/35/76-og.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Akon",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://files.list.co.uk/images/2017/08/03/akon-LST257594-lg.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Alicia Keys",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://i.pinimg.com/736x/97/21/20/972120ed7dab64e34bd156b791911e69--famous-black-people-trending-hairstyles.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Andre 3000",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://media.pitchfork.com/photos/592992215e6ef9596931ec24/1:1/w_300/4a191ab4.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ariana Grande",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://vignette.wikia.nocookie.net/arianagrande/images/8/8f/Ariana_Billboard_2017.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="A Tribe Called Quest",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2016/12/161213-Q-Tip-Tribe-Getty-800x600.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Afrika Bambaataa",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://s3.amazonaws.com/hiphopdx-production/2015/04/Afrika-Bambaataa_04-14-2015.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Beastie Boys",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="http://richglare.com/wp-content/uploads/2014/03/beastie.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Beyonce",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://media.vanityfair.com/photos/589a59c7d1af756e234791ca/master/w_768,c_limit/beyonce-grammys-style-ss17.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Big Boi",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2012/11/1-bigboi_12-08-2012.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Big Daddy Kane",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://i.pinimg.com/736x/0a/c8/0e/0ac80edc10137ec842ad3515a9705f5a--big-daddy-kane-hip-hop-style.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Big Sean",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Big_Sean_2009.jpg/210px-Big_Sean_2009.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Birdman",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://hustlezngrindz.files.wordpress.com/2014/11/birdman1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Biz Markie",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://www.famousbirthdays.com/headshots/biz-markie-3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Blackalicious",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="http://static.canalblog.com/storagev1/jecritiquetout.canalblog.com/images/Blackalicious.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Body Count",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="http://cdn.antiquiet.com/wp-content/uploads/2016/01/bodycount-okc-1-626x417.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Boogie Down Productions",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/e/e5/Boogie_Down_Productions.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Boosie Badazz",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2016/01/Boosie-Badazz-New-Movie.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bruno Mars",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://peopledotcom.files.wordpress.com/2016/08/bruno-mars-435-16.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bryson Tiller",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2015/08/Bryson-Tiller-304.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Busta Rhymes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://www.famousbirthdays.com/headshots/busta-rhymes-7.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="C+C Music Factory",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="http://www.los40.com//images/fichas/010000017165_n_imgg.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cardi B",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://i.pinimg.com/736x/3f/c0/97/3fc0973e2e24bd00857cfc0aa7abc95c--the-harem-cardi.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chance The Rapper",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="http://www.rap-up.com/app/uploads/2017/04/chance-the-rapper-flog-gnaw.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chris Brown",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://s1.ticketm.net/tm/en-us/dam/a/93a/cb47af7d-546f-403c-848a-8edf54ff193a_296481_CUSTOM.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chuck D",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="http://www.thenervousbreakdown.com/wp-content/uploads/2012/06/9165_chuckd-profile.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ciara",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Ciara_2009.jpg/220px-Ciara_2009.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cold Crush Brothers",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://pbs.twimg.com/profile_images/574320443869503488/n8SN9lQd.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Color Me Badd",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://ewedit.files.wordpress.com/2016/04/jgkdfsldasfs.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Common",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://i.pinimg.com/564x/be/da/fb/bedafbac456f5a4591939f9c7601e855.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Coolio",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://thehomeofhiphop.com/wp-content/uploads/2013/10/Coolio.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="D-Nice",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="http://eclectikrelaxation.com/HipHop/wp-content/uploads/2013/05/dnice.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="D.R.A.M.",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="http://images.complex.com/complex/y81wsufwt9lgqrtqcyht.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="De La Soul",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://e.snmc.io/lk/f/a/31867d26a3a9444837cd4013bc8bb918/2979498.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DJ Jazzy Jeff",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://geo-static.traxsource.com/files/artists/5816.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DJ Khaled",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2016/03/DJ-Khaled_03-21-2016.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DJ Mustard",
        url="plugin://plugin.video.youtubeplaylist/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://static.spin.com/files/2015/08/dj-mustard-fancy-classic-man-940-640x429.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DJ Spinderella",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="http://www2.pictures.zimbio.com/pc/DJ+Spinderella+Carmen+Electra+guest+attend+ANo5VFk3Zqnl.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DMX",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="http://i.dailymail.co.uk/i/pix/2017/04/29/01/3FB72A1200000578-0-image-a-9_1493424881823.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dr. Dre",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/d/de/Dr._Dre_in_2011.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Drake",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/2/22/Drake-Velvet-Underground.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Eazy-E",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2015/03/Screen-Shot-2015-03-26-at-10.43.59-AM.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Eminem",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="http://www.chicagonow.com/patriotic-dissenter/files/2017/10/eminem.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Eric B. & Rakim",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="https://media.pitchfork.com/photos/592990e1ea9e61561daa2f33/1:1/w_300/2970f3f6.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Erykah Badu",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="https://www.famousbirthdays.com/faces/badu-erykah-image.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fab 5 Freddy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="http://www1.pictures.zimbio.com/gi/Fab+5+Freddy+9jDY101ufd6m.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Future",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="https://s3.amazonaws.com/hiphopdx-production/2012/06/Future-Beef-hhdx.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Gang Starr",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="http://e-cdn-images.deezer.com/images/artist/33da46164c2b42ff9fa424d3318a3dd6/500x500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ghostface Killah",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="http://s3.amazonaws.com/rapgenius/ghostface.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Grandmaster Flash",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="https://pbs.twimg.com/profile_images/550440248799281152/RrjpbG9E.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Gucci Mane",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="https://www.thea-blast.org/wp-content/uploads/2017/10/gucci-ice-cream.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="GZA",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="https://pbs.twimg.com/media/DGKOExxUQAQIIPI.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="House of Pain",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_62+"/",
        thumbnail="http://goldhiphop.net/wp-content/uploads/2015/12/House-Of-Pain-Discography-3CD-1992-1996.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ice-T",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_63+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Ice_T2.jpg/210px-Ice_T2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ice Cube",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_64+"/",
        thumbnail="https://pmcdeadline2.files.wordpress.com/2011/02/cube1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Inspectah Deck",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_65+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2015/07/Inspectah-Deck-300.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="J. Cole",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_66+"/",
        thumbnail="https://media.pitchfork.com/photos/592992b6ea9e61561daa32e5/1:1/w_300/70694344.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jam Master Jay",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_67+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Jam_Master_Jay.jpg/220px-Jam_Master_Jay.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="James DeBarge",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_68+"/",
        thumbnail="https://i.pinimg.com/originals/8d/9e/95/8d9e9525ed160fa140672f678d844821.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Janet Jackson",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_69+"/",
        thumbnail="http://www.billboard.com/files/media/janet-jackson-2015-performance-billboard-1548.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jason Derulo",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_70+"/",
        thumbnail="https://www.famousbirthdays.com/headshots/jason-derulo-1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jay Z",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_71+"/",
        thumbnail="http://www.rap-up.com/app/uploads/2014/12/jay-z.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jazzy Jay",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_72+"/",
        thumbnail="http://3.bp.blogspot.com/-9WRbAydbD4c/UV0o6YIn1xI/AAAAAAAAIFk/8h9B3JgFIuU/s1600/394467_453904361307130_1200299365_n.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jennifer Lopez",
        url="plugin://plugin.video.youtubeplaylist/"+YOUTUBE_CHANNEL_ID_73+"/",
        thumbnail="https://media.glamour.com/photos/59c9031d9e6b422a46a25e96/1:1/w_352/jennifer-lopez-tout.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="John Legend",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_74+"/",
        thumbnail="http://proudfm.com/wp-content/uploads/john-legend-may-2015-billboard-620.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Judgement Night OST",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_75+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/f/f3/Judgment_Night_%28soundtrack%29_album_coveart.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Juice Crew",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_76+"/",
        thumbnail="https://i2.wp.com/hiphopwired.com/wp-content/uploads/2013/03/juicecrew.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kanye West",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_77+"/",
        thumbnail="https://images.rapgenius.com/akiz5bo3uquc7x41u6ezdvyjs.716x1000x1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kendrick Lamar",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_78+"/",
        thumbnail="http://cache.umusic.com/_sites/kendricklamar.com/images/og.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kid 'n Play",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_79+"/",
        thumbnail="http://pragmaticobotsunite.com/wp-content/uploads/2016/10/10232483206_976b8ea6e7-3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kid Cudi",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_80+"/",
        thumbnail="http://www.thissongslaps.com/wp-content/uploads/2013/10/kid-cudi.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kodak Black",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_81+"/",
        thumbnail="https://dancehallhiphop.com/wp-content/uploads/2016/12/Kodak-Black.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kris Kross",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_82+"/",
        thumbnail="https://www.thesun.co.uk/wp-content/uploads/2016/11/nintchdbpict000284754638.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="KRS-One",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_83+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2015/11/KRS-One.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kurtis Blow",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_84+"/",
        thumbnail="http://www.lyricsmode.com/i/bpictures/7507.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lil' Kim",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_85+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/b/be/Lil_Kim_Bad_Boy_Reunion_Tour_2016.jpg",
        folder=True )           

    plugintools.add_item( 
        #action="", 
        title="Lil Uzi Vert",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_86+"/",
        thumbnail="http://www.ultimatechart.com/system/artists/Lil_Uzi_Vert.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lil Wayne",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_87+"/",
        thumbnail="https://yt3.ggpht.com/-UnYQfqfdfts/AAAAAAAAAAI/AAAAAAAAAAA/aeJj-lizNSA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lil Yachty",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_88+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Lil_Yachty_cropped.jpg/220px-Lil_Yachty_cropped.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="LL Cool J",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_89+"/",
        thumbnail="https://i.pinimg.com/originals/d8/93/1f/d8931f851e84a11a83e0e91afd953efe.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ludacris",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_90+"/",
        thumbnail="https://cdn.cinepapaya.com/stat/img/static-cp/usermovie/ludacris837-7785.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lupe Fiasco",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_91+"/",
        thumbnail="http://theboombox.com/files/2016/12/Lupe-Fiasco-Quitting-Rap.jpg?w=600&h=0&zc=1&s=0&a=t&q=89",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="M.I.A.",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_92+"/",
        thumbnail="http://supertouchart.com/wp-content/uploads/2013/03/hhhyggy667.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Marley Marl",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_93+"/",
        thumbnail="https://i.ytimg.com/vi/wiUsXm-ElOc/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Masta Killa",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_94+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2015/03/Masta-Killa_03-13-2015.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MC Hammer",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_95+"/",
        thumbnail="https://peopledotcom.files.wordpress.com/2016/05/mc-hammer-02-435.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MC Ren",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_96+"/",
        thumbnail="http://www.billboard.com/files/media/mc-ren-1992-portrait-billboard-650.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MC Shan",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_97+"/",
        thumbnail="https://e.snmc.io/lk/f/a/a19512e1cd13c37cb1adf8d62ea9f595/1148001.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Meek Mill",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_98+"/",
        thumbnail="https://pbs.twimg.com/profile_images/659760227747631104/KXmQDze9.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Melle Mel",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_99+"/",
        thumbnail="http://www4.pictures.zimbio.com/gi/Melle+Mel+GRAMMY+Nominations+Concert+Live+uqqOc_pgcOKl.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Method Man",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_100+"/",
        thumbnail="https://media.ents24network.com/image/000/155/568/5d527a297d69e96e5ed3d45dd6d07e191e31a209.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Michael Jackson",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_101+"/",
        thumbnail="http://images.genius.com/aeb5eed39667d01ea001f2eb7d09029f.440x440x1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Migos",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_102+"/",
        thumbnail="https://media.pitchfork.com/photos/592990675e6ef9596931e8d2/1:1/w_300/aae3685c.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Missy Elliott",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_103+"/",
        thumbnail="http://www.nndb.com/people/401/000026323/missy-blue.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mos Def",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_104+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/4/43/Mos_def_retouched.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="N.W.A.",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_105+"/",
        thumbnail="https://media.pitchfork.com/photos/592995335e6ef9596931f1f0/1:1/w_300/1f52685b.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Nas",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_106+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Nas-04.jpg/220px-Nas-04.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Naughty By Nature",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_107+"/",
        thumbnail="http://media.nj.com/entertainment_impact/photo/naughty-by-nature-kickstarterjpg-347f501762c3ef65.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ne-Yo",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_108+"/",
        thumbnail="https://www.famousbirthdays.com/headshots/ne-yo-3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nelly",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_109+"/",
        thumbnail="http://www.eurweb.com/wp-content/uploads/2017/10/nelly-bio.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nicki Minaj",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_110+"/",
        thumbnail="https://i.pinimg.com/736x/61/8a/93/618a935b2178577f7f198a308cdd91c5--nicki-minaj-makeup-grammy-award.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nipsey Hussle",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_111+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2010/12/2-Nipsey_Hussle-Album_Postponed.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Offset",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_112+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Offset_Veld_festival_2017.jpg/220px-Offset_Veld_festival_2017.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ol' Dirty Bastard",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_113+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/5/5c/Ol%27_Dirty_Bastard.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Outkast",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_114+"/",
        thumbnail="http://static.djbooth.net/pics-tracks/outkast.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pharrell Williams",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_115+"/",
        thumbnail="https://www.famousbirthdays.com/headshots/pharrell-williams-3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pitbull",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_116+"/",
        thumbnail="https://www.famousbirthdays.com/headshots/armando-perez-6.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Post Malone",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_117+"/",
        thumbnail="https://i.pinimg.com/736x/ab/bd/63/abbd634fb5234db66b918061ef012ad9.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Prince",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_118+"/",
        thumbnail="https://i.pinimg.com/736x/eb/62/ea/eb62ea11c33376c60119b98b05ef8542--s-music-my-baby-daddy.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Professor Griff",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_119+"/",
        thumbnail="https://aalbc.com/authors/richard-griffin.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Public Enemy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_120+"/",
        thumbnail="http://www.sosoactive.com/wp-content/uploads/2013/04/Public+Enemy+PUBLIC+EMEMY.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Quavo",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_121+"/",
        thumbnail="https://www.famousbirthdays.com/headshots/quavious-marshall-5.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Queen Latifah",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_122+"/",
        thumbnail="http://68.media.tumblr.com/69913105cfe224248854f52d664acea9/tumblr_n5oi5tLNVg1sufv62o1_500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="R. Kelly",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_123+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/6/61/Rkellytrappedinthecloset2007.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Raekwon",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_124+"/",
        thumbnail="https://image-ticketfly.imgix.net/00/02/52/99/95-og.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rakim",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_125+"/",
        thumbnail="https://s3.amazonaws.com/hiphopdx-production/2011/06/1-Rakim-Guardian_20110511.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Redman",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_126+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2015/11/151113_Redman.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rich Chigga",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_127+"/",
        thumbnail="http://wehotimes.com/wp-content/uploads/2017/04/richchigga.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rich Homie Quan",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_128+"/",
        thumbnail="https://yt3.ggpht.com/-C3f2x0CcG8Q/AAAAAAAAAAI/AAAAAAAAAAA/FCQMvbZLBZY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rick Ross",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_129+"/",
        thumbnail="https://peopledotcom.files.wordpress.com/2016/08/rick-ross-d-435.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rihanna",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_130+"/",
        thumbnail="https://www.famousbirthdays.com/headshots/rihanna-4.jpg",
        folder=True )           

    plugintools.add_item( 
        #action="", 
        title="Rock Steady Crew",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_131+"/",
        thumbnail="http://hiphop.latina.com/wp-content/uploads/2016/08/nelson-george-history-500x500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rob Base and DJ E-Z Rock",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_132+"/",
        thumbnail="https://www.ballerstatus.com/wp-content/uploads/2014/04/2014-04-26-ez.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Run-D.M.C.",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_133+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/1/1f/Rundmc_2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="RZA",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_134+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2017/08/IMG_30-800x600.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Salt-N-Pepa",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_135+"/",
        thumbnail="http://www.thewinehousemag.com/wp-content/uploads/2013/07/Salt-N-Pepa.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Scott La Rock",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_136+"/",
        thumbnail="http://thesource.com/wp-content/uploads/2015/08/scottlarock1-500x400.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sean Combs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_137+"/",
        thumbnail="https://www.famousbirthdays.com/headshots/diddy-3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Snoop Dogg",
        url="plugin://plugin.video.youtubeplaylist/"+YOUTUBE_CHANNEL_ID_138+"/",
        thumbnail="https://e.snmc.io/lk/f/a/676e53ac74df958ecef2b32e416f5ee8/1133746.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Soul Sonic Force",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_139+"/",
        thumbnail="http://img.wennermedia.com/920-width/rs-138247-20121204-3-bambaata-306x306-1354644794.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="T La Rock",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_140+"/",
        thumbnail="http://img2-azcdn.newser.com/image/1147037-11-20171012094539.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="T-Pain",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_141+"/",
        thumbnail="http://www.rapbasement.com/wp-content/uploads/2014/01/t-pain-songs.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="T.I.",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_142+"/",
        thumbnail="https://pbs.twimg.com/profile_images/893138733091897344/0qyj2JqC.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Takeoff",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_143+"/",
        thumbnail="http://www.xxlmag.com/files/2017/06/Takeoff.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Game",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_144+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/TheGameApr2011.jpg/220px-TheGameApr2011.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Notorious B.I.G.",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_145+"/",
        thumbnail="https://pbs.twimg.com/media/CvpBqFuUsAAZNVU.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tone Loc",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_146+"/",
        thumbnail="http://media.tmz.com/2012/08/15/tone-loc-5-300w.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Travis Scott",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_147+"/",
        thumbnail="https://www.famousbirthdays.com/faces/scott-travis-image.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Treacherous Three",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_148+"/",
        thumbnail="https://i.ytimg.com/vi/H7Le26FuVkc/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Trey Songz",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_149+"/",
        thumbnail="http://www.rap-up.com/app/uploads/2014/12/trey-songz.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Tupac Shakur",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_150+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/b/b5/Tupac_Amaru_Shakur2.jpg/220px-Tupac_Amaru_Shakur2.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Ty Dolla $ign",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_151+"/",
        thumbnail="https://media.pitchfork.com/photos/59299086c0084474cd0be512/1:1/w_300/1166463f.jpg",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Tyga",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_152+"/",
        thumbnail="https://www.famousbirthdays.com/headshots/tyga-3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tyrese Gibson",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_153+"/",
        thumbnail="https://peopledotcom.files.wordpress.com/2017/09/tyrese-gibson.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="U-God",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_154+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2013/07/U-God_07-01-2013.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="UGK",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_155+"/",
        thumbnail="https://s3.amazonaws.com/rapgenius/1310711069_ugk.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Usher",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_156+"/",
        thumbnail="http://z1035.com/wp-content/uploads/2017/07/usher-e1500980783644.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Whodini",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_157+"/",
        thumbnail="http://3.bp.blogspot.com/-WFvMu4saG0c/TadICbt045I/AAAAAAAAA_M/Q26v4LJHAmY/s1600/Whodini%252Bwho3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Wiz Khalifa",
        url="plugin://plugin.video.youtubeplaylist/"+YOUTUBE_CHANNEL_ID_158+"/",
        thumbnail="https://i.pinimg.com/originals/85/c5/6c/85c56ca462d8a0afb251b3141eb0e97d.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="WORLDSTARHIPHOP",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_159+"/",
        thumbnail="https://pbs.twimg.com/profile_images/488738791511703552/cxf92nyL.png",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Wu-Tang Clan",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_160+"/",
        thumbnail="http://www.wutang-corp.com/images/photos/wutangclan6.jpg",
        folder=True )  		

    plugintools.add_item( 
        #action="", 
        title="XXXTENTACION",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_161+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/3/38/Xxxtentacion.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="YG",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_162+"/",
        thumbnail="http://crowningmusic.com/storage/mOmS4f1SzuPliRQUbypu.png",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="YoungBoy Never Broke Again",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_163+"/",
        thumbnail="https://static01.nyt.com/images/2017/08/17/arts/17YOUNGBOY1/17YOUNGBOY1-blog427.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Yo Gotti",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_164+"/",
        thumbnail="http://www.yoraps.com/wp-content/uploads/2015/09/Yo-Gotti.png",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Young Jeezy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_165+"/",
        thumbnail="https://s3.amazonaws.com/hiphopdx-production/2014/10/young-jeezy-interview-304x304.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Young MC",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_166+"/",
        thumbnail="http://www1.pictures.zimbio.com/gi/Young+MC+Screening+Lionsgate+Films+Expendables+niFykW8CpvNl.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Young Thug",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_167+"/",
        thumbnail="http://s3.amazonaws.com/hiphopdx-production/2016/04/Young-Thug_04-04-2016.jpg",
        folder=True )  		
run()