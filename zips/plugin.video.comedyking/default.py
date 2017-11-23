# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Comedy King
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

addonID = 'plugin.video.comedyking'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLT9CI5gIkkFARL_9p8BKx0H0zMk8nkTiA"
YOUTUBE_CHANNEL_ID_2 = "PLtulsw_FYXf2x8oZSY0ft_c4v8aiky2L_"
YOUTUBE_CHANNEL_ID_3 = "PLfR84G96OgFGTUQ0gRcI3_y2fAb6x10an"
YOUTUBE_CHANNEL_ID_4 = "PL_b_692zEZcYu4SNzc3Hs1xz1Mqr8G7RV"
YOUTUBE_CHANNEL_ID_5 = "PLHN7G9IVyJ3Pd22JWHZCRj_S522WamwLC"
YOUTUBE_CHANNEL_ID_6 = "PLPxBSMwXmrbtDnKmm7zLY66PIsj1sFEea"
YOUTUBE_CHANNEL_ID_7 = "PLZUqNURALnDT0x0T8HiINCZOLvjWfuUbC"
YOUTUBE_CHANNEL_ID_8 = "PLUnvw3Q6Wd6ESw116Dd9EcDR9sdVuRhih"
YOUTUBE_CHANNEL_ID_9 = "PLAB26D6C14D753E59"
YOUTUBE_CHANNEL_ID_10 = "PLp5SrqMnYJpIeOCX3sGKFh0IgH0a3XMaq"
YOUTUBE_CHANNEL_ID_11 = "PLFQoMclceTTRIJJ1nU_S52boTRCsdH6nD"
YOUTUBE_CHANNEL_ID_12 = "PLuEf0pMiQDsGR-i3CLp6h_87ZZVeEETk2"
YOUTUBE_CHANNEL_ID_13 = "PLte1O09SAtoWSamVDRPleJEoB1hmwEewK"
YOUTUBE_CHANNEL_ID_14 = "PLgwwA4SSg213JAJ1IoeFDcD4QNEtWeNmC"
YOUTUBE_CHANNEL_ID_15 = "PLEgcZlHmnPAn1Fn7MCinLz2OogS5p3tSX"
YOUTUBE_CHANNEL_ID_16 = "PLB5Umr9ZEDwq0W2GzqDLgQILZV4JWwKg6"
YOUTUBE_CHANNEL_ID_17 = "PLuWUFmyeafedQxCBGlz0ZfgQhX9ChyXLq"
YOUTUBE_CHANNEL_ID_18 = "PLC1xZwSJ78L0GJY7Cpkkds1fxewR2jc3U"
YOUTUBE_CHANNEL_ID_19 = "UCJtFGmaBMlZmFWM6fku24hQ"
YOUTUBE_CHANNEL_ID_20 = "PLLXphsIcToxPZG-dS2uq6DZ10D4v_u_pB"
YOUTUBE_CHANNEL_ID_21 = "PLm_eEqqsw9zseMrzQFzB4oxbvl-jq83jj"
YOUTUBE_CHANNEL_ID_22 = "PLJ1VBdx4v0Ofs5rsaGv1WsiPEPpqu3f3p"
YOUTUBE_CHANNEL_ID_23 = "PLLXphsIcToxPZG-dS2uq6DZ10D4v_u_pB"
YOUTUBE_CHANNEL_ID_24 = "PL8E7uzvkLxaUX9pHKdZe7gUMSvwleiPHK"
YOUTUBE_CHANNEL_ID_25 = "PLJAfSO5TqtJOlOOqM2E6OkizFs-Aw7H8Y"
YOUTUBE_CHANNEL_ID_26 = "PLFUnAiQW2RaCU0AVeh12McIFdIuxLodha"
YOUTUBE_CHANNEL_ID_27 = "PLOJtL2t4BNnMjGLw3uloIPwBeSU5jliHz"
YOUTUBE_CHANNEL_ID_28 = "PLjWddXHkjgZePU2K92cq3BtSs893HBx8r"
YOUTUBE_CHANNEL_ID_29 = "PLeI6aJZFJ_1driXCJoFyF6NVhJBgW2J9B"
YOUTUBE_CHANNEL_ID_30 = "PLaewE5_YLxZUifD8TX2Om4WiQduxdoXJq"
YOUTUBE_CHANNEL_ID_31 = "PL3g4DSl-MZxhnVUOrLujd2hg1yIYQUBYK"
YOUTUBE_CHANNEL_ID_32 = "PLHX4mQd9pGZM3oHaa15_bjb93X-1ehgb1"
YOUTUBE_CHANNEL_ID_33 = "UC499oOSUxhD2lvEik6naaHw"
YOUTUBE_CHANNEL_ID_34 = "PL7Wbovlt1GP36PqTlB_7SK_Jc4Hn9nzh5"
YOUTUBE_CHANNEL_ID_35 = "PLFZBTLQXIBdizEsYxfwDRJ5w-Gm5y8ZaX"
YOUTUBE_CHANNEL_ID_36 = "UCBH1PpAu9UZ0Dkn6qGqGsmg"
YOUTUBE_CHANNEL_ID_37 = "PLrI7-XXKSTQaPw-Q919i98ORIVOaDEQgy"
YOUTUBE_CHANNEL_ID_38 = "PLZ1f3amS4y1ffYEhGZDtawaEyRQQu69Bw"
YOUTUBE_CHANNEL_ID_39 = "PLJNudqU_mEkgBA8A7a1Sx8d3ZoEIZTLBF"
YOUTUBE_CHANNEL_ID_40 = "PLCCE9F8F1D781B198"
YOUTUBE_CHANNEL_ID_41 = "PLG6HoeSC3raE-EB8r_vVDOs-59kg3Spvd"
YOUTUBE_CHANNEL_ID_42 = "PLXzp-3-H87O85N8SDGIXNHNJr70srBpcq"
YOUTUBE_CHANNEL_ID_43 = "PLitUeK_P89nnJ6RERatkorIarv1vmlNAb"
YOUTUBE_CHANNEL_ID_44 = "PL0Mm9vNtQkohqfKlr0DI_IHK3JVsRPu5G"
YOUTUBE_CHANNEL_ID_45 = "PLL495ricb791dz4jbQLvMhfdSvK0fR-nS"
YOUTUBE_CHANNEL_ID_46 = "PLe_K5jgqTYdbiRlku_lk8ZdUG_IA7q26c"
YOUTUBE_CHANNEL_ID_47 = "PLIdyfW1oW4yTuDIctv1HI1MV2PAoxArG2"
YOUTUBE_CHANNEL_ID_48 = "PLgs3zGe9KlOEaTz8FQZfUA1ygtxoO6zEf"
YOUTUBE_CHANNEL_ID_49 = "PLcMYioSNb8ODnHNw5JbXL04biQxoXCIlu"
YOUTUBE_CHANNEL_ID_50 = "PL2E8umvLN4bBZmQ8V00aXQV2FaQXuVJIf"
YOUTUBE_CHANNEL_ID_51 = "PLHRpkGRK-AbviSJ5M9aQ5BE2fpaYQ01mM"
YOUTUBE_CHANNEL_ID_52 = "PLuWkgu1LJKezcb-Sfdvq9WXw-8HhT3xCb"
YOUTUBE_CHANNEL_ID_53 = "PLiSxBUjo1VCPqXokAhDgYpShq7FUoOKR7"
YOUTUBE_CHANNEL_ID_54 = "PL7IIy_GbHHsSiVHnMNoGBZpEM2Yu4nc9r"
YOUTUBE_CHANNEL_ID_55 = "PLuBk3vjvp0AdqA4wby6ijXEKBBlsZ5E5V"
YOUTUBE_CHANNEL_ID_56 = "PLY1vwXye3z6YfG-FcEb9qzbv_LN_DN4iR"
YOUTUBE_CHANNEL_ID_57 = "PLYJnwOK_-l5WCqeJcd6luzNvSLt6matnQ"
YOUTUBE_CHANNEL_ID_58 = "PLrT7Oi-dj3IL6rpXaC45sSGgSKTKp37CJ"
YOUTUBE_CHANNEL_ID_59 = "PLxsNyGm80cIRN0s32zrXaw8jlezzJrtxr"
YOUTUBE_CHANNEL_ID_60 = "PLyegWs_ffuf0mmftSsgLASqGWcVdrkZu1"
YOUTUBE_CHANNEL_ID_61 = "PLRY-hBDmYWMH2dryxIe5FPYh24ajiRoU-"
YOUTUBE_CHANNEL_ID_62 = "PLDZYEkNE2nvN7vVnE4np_t9cgVn5IBzyB"
YOUTUBE_CHANNEL_ID_63 = "PLBnfgEHtRP_tGS_7dT28Kv0XL9Z5vTZMq"
YOUTUBE_CHANNEL_ID_64 = "PLf7lvneGmIwBKRasWxlLHEENz3LstUaj2"
YOUTUBE_CHANNEL_ID_65 = "PL2D52E-7bKJtY8yvD0DWhdxjHu22kKMY5"
YOUTUBE_CHANNEL_ID_66 = "PLFLQA9U3xQDJ9UkYAa8fSduDxt0PvWUnJ"
YOUTUBE_CHANNEL_ID_67 = "PLE456lb84WD2UIO0N7HbsGI5g5QWA-728"
YOUTUBE_CHANNEL_ID_68 = "PLS2emyQ5EQ36Ns3GwMAmwXQ-3UojUDJOF"
YOUTUBE_CHANNEL_ID_69 = "PLclGq4B3wC23Jz3OjOm2DVO7SqYwkkJSB"
YOUTUBE_CHANNEL_ID_70 = "PLgtA55-ahLaWgFmxprK1IT4ShfUZ4GnOs"
YOUTUBE_CHANNEL_ID_71 = "PLhk-J-XVZMDxcrxQz6WulyygOrOAZJwiY"
YOUTUBE_CHANNEL_ID_72 = "PLdgUyXJjeaq94qFbXDRR8RISHHDAWTO0L"
YOUTUBE_CHANNEL_ID_73 = "PLiZceXf3jUi6P2X4XZKkK-xcZKl2aFrD_"
YOUTUBE_CHANNEL_ID_74 = "PLq4KqqWr_15NWHUJa4lh9g6UsxM-HnRFK"
YOUTUBE_CHANNEL_ID_75 = "PL566760B77B1C1B94"
YOUTUBE_CHANNEL_ID_76 = "PLMZ7cFae29RcdNOCB6jtBzVvfEbwchQwH"
YOUTUBE_CHANNEL_ID_77 = "PLfWduuEU5TVVzyBI1Mn8QnpraAXSXNv7X"
YOUTUBE_CHANNEL_ID_78 = "PLeXUN3PdqzTZ10qp62R93KjEBCU79pSvA"
YOUTUBE_CHANNEL_ID_79 = "PL9O0lnOrUF0TqIHJMpzvTR9IGejcvqYZs"
YOUTUBE_CHANNEL_ID_80 = "PLjuR5ouJJf7oFy9kYTjeOdc8n6yGm_U64"
YOUTUBE_CHANNEL_ID_81 = "PLLaMoprZv-FN6q4LdufynW-FFNZXylt4r"
YOUTUBE_CHANNEL_ID_82 = "PLJHfedoaM2Z1OdIjmqH8nUEhpktnT4g8Y"
YOUTUBE_CHANNEL_ID_83 = "PLJJHlrQhy6uP3Ff_BUri8f0CkWohkVxxz"
YOUTUBE_CHANNEL_ID_84 = "PLAnwG_qyu0V8wlgucOFIPy9wOZfGtc5Bx"
YOUTUBE_CHANNEL_ID_85 = "PLEnAMwsG9QLI5zP1bYj5XoGl4VAbe21vc"
YOUTUBE_CHANNEL_ID_86 = "PLT2ek4omyo0dwIJIVn9s5evchNUuRXp_J"
YOUTUBE_CHANNEL_ID_87 = "PL0nTfdBp8VpXV6M2-Z1WhCRIeSJ97XX4a"
YOUTUBE_CHANNEL_ID_88 = "PLSnBA_uzzcwUChg7a09HiBcAQux4k45vR"
YOUTUBE_CHANNEL_ID_89 = "PLogZusiae2uyOItzjiAqWH6iHP5wZpmov"
YOUTUBE_CHANNEL_ID_90 = "UCQW6iGeRg9PJx81bpifgfcg"
YOUTUBE_CHANNEL_ID_91 = "PLiRZChRMRi3k1Rh-hE2HGUEwINQcqtsvI"
YOUTUBE_CHANNEL_ID_92 = "PLSZ-OLXEesJ3dZYnOaiu8d-628YDph7Bd"
YOUTUBE_CHANNEL_ID_93 = "PL1wUdpvOZzIiIXIa85BJ2yN4JSK1Hg5yO"
YOUTUBE_CHANNEL_ID_94 = "PLFXuK40PQwf3v8vXDC50MBqK5_7SsO1S-"
YOUTUBE_CHANNEL_ID_95 = "PLGO8f9hH4FrLuMnCU7qMFq4ZNeCEHSAor"
YOUTUBE_CHANNEL_ID_96 = "PL7Tvushuqw-EHuwz7KHgIUk2r2nm2Ijc6"
YOUTUBE_CHANNEL_ID_97 = "PLuKw1oWzC2BOclAbo6NwpzJuPeZkiHGA2"
YOUTUBE_CHANNEL_ID_98 = "PLdyXyoDsTAaLrNZGg1WAon89psq0y_WgX"
YOUTUBE_CHANNEL_ID_99 = "PLafrat4KHJMXn0w0Z94chy-Ovwl8BdpNS"
YOUTUBE_CHANNEL_ID_100 = "PLTXbmf59DOnmAMCbK9N_crqMNSJKOC9Pz"
YOUTUBE_CHANNEL_ID_101 = "PLrWBjOWuIuq1Go-mFTY8ic67jpMoPyc72"
YOUTUBE_CHANNEL_ID_102 = "PLL8svL6IQEmpulNJvZJ5kr9TLXI5yCQWs"
YOUTUBE_CHANNEL_ID_103 = "PL6Gvyfk2G4Y8wFh8W4ieqy8G0c7Q8mVUH"
YOUTUBE_CHANNEL_ID_104 = "PLZ_Rfpk5QBRmDunPQiYxoUVcfwoRUsJIQ"
YOUTUBE_CHANNEL_ID_105 = "PLVy6fZ6rl_cLYRTsHhDDDSVE2kQow1D38"
YOUTUBE_CHANNEL_ID_106 = "PLPraSnQRmo6_Afws0uSZtKy8WL0CHXjpa"
YOUTUBE_CHANNEL_ID_107 = "PLXqCoyTSJ4idkcbOgcQyU8SL9l-PDSrBh"
YOUTUBE_CHANNEL_ID_108 = "PLiOY8ArrvTR5XG9-QwE9FC4n2ZbDZWrzZ"
YOUTUBE_CHANNEL_ID_109 = "PL3tPzgS0iPtth81j97pn00KoxUIgUn8KM"
YOUTUBE_CHANNEL_ID_110 = "PLKQwwHMcGMb-H0jUkX_vYKipGgXiERGIm"
YOUTUBE_CHANNEL_ID_111 = "PL-YxBc2c95vM0fqeS6ueuVQXiUglpuJbZ"
YOUTUBE_CHANNEL_ID_112 = "PLD0o8633xlq4sVImbOddwcIMsStK4-SH6"
YOUTUBE_CHANNEL_ID_113 = "PLn_EUwiwzNh6tMBI0t7t2QcI4ixSI3pw2"
YOUTUBE_CHANNEL_ID_114 = "PLqAbjOGVTxV_BRATD2r2dSPqCjrivXJp2"
YOUTUBE_CHANNEL_ID_115 = "PLOVuukXhEB-bpeiokGTJxwyMBfnQVRRnB"
YOUTUBE_CHANNEL_ID_116 = "UCIw20H3_k3zSKV1fWBLTL8A"
YOUTUBE_CHANNEL_ID_117 = "PL6KrT6De-O2gArq4rYeMu0uZz3EdTQYgc"
YOUTUBE_CHANNEL_ID_118 = "PLKs-cHjBXszlqtigstHgg20VTDqti8WDz"
YOUTUBE_CHANNEL_ID_119 = "PLOfPZmpOltoLcW6h0TqzACpZFK5sKeI5h"
YOUTUBE_CHANNEL_ID_120 = "PLS7rCpwZUah0h-8tcgifXMiwi5HDqWNUf"
YOUTUBE_CHANNEL_ID_121 = "PL1JAyPrwR2eeNxVPUfddtONIEH8oRu2jL"
YOUTUBE_CHANNEL_ID_122 = "PLErezV0EGvQLhmN0tjEjtfhO1rZ9C0A_x"
YOUTUBE_CHANNEL_ID_123 = "PLCVWnhOBZP8b4ChaeJFc-ckYfEi9PGj2W"
YOUTUBE_CHANNEL_ID_124 = "PLkW8okg2CiKHu_E4EhzY5atSHYOkhn3yF"
YOUTUBE_CHANNEL_ID_125 = "PL-K70rinP31VYVB58Bb21hmlTBGTzj8co"
YOUTUBE_CHANNEL_ID_126 = "PL6fJmjt84zZj-2_3xxrJJM1yOICceGCG6"
YOUTUBE_CHANNEL_ID_127 = "JustForLaughsTV"
YOUTUBE_CHANNEL_ID_128 = "PLYBlTh439OfS2X45FrInKVsFB_Vq5CYP0"
YOUTUBE_CHANNEL_ID_129 = "PL34qVdY1JdpSkivHnNicTz9xwj9Sv3Q0B"
YOUTUBE_CHANNEL_ID_130 = "PL13ZzvDpzQjmW97Wmyefkl9lZGJjB4EDa"
YOUTUBE_CHANNEL_ID_131 = "PLy0sy417uZeTL-CibSS6i2k_210oxii8i"
YOUTUBE_CHANNEL_ID_132 = "PLgaHlOvosRZ7pW2j48kJDcUEQsl-q6SLD"
YOUTUBE_CHANNEL_ID_133 = "PLEU9iel12F0_Yc6WG3aQbGzyeI7lO4inm"
YOUTUBE_CHANNEL_ID_134 = "UCVFKOfmCxbIi6DssBwNrsEg"
YOUTUBE_CHANNEL_ID_135 = "PLJazJ_0rjvbrzFOB9PLGxS9sCLf_DbGCW"
YOUTUBE_CHANNEL_ID_136 = "PLa4_J3cytwKZxZsyw2AyNYVCXI7bvpv8p"
YOUTUBE_CHANNEL_ID_137 = "PLr3vXI77U2jIPnxVR8E-Ssm8rTz8y27Ik"
YOUTUBE_CHANNEL_ID_138 = "PL_2_BTJIy4vmd5_ah5kVgPkSSfOKZ2ekm"
YOUTUBE_CHANNEL_ID_139 = "PL5L4fIMmQDrvDu0Y8w1j9-m5v9jWWq1KW"
YOUTUBE_CHANNEL_ID_140 = "PLDVj7pvDirz_MiFtulNmU9B1Cr07B7f2v"
YOUTUBE_CHANNEL_ID_141 = "PLLezrAyj5aWA-cfpM2rpG2GtpO3jZhckk"
YOUTUBE_CHANNEL_ID_142 = "PLp650M6jurbfq5SRUVEeE1RmoY3KlQrGS"
YOUTUBE_CHANNEL_ID_143 = "PLETa4CYE1Nm_OK1sV3UgkXRajogd09Cpl"
YOUTUBE_CHANNEL_ID_144 = "PL_qrrHMssxdt1xbn9YZhgdpblnBuD_dr0"
YOUTUBE_CHANNEL_ID_145 = "PLZiITj23ApfeB4JbTq9zj_tTAJY0X_cTP"
YOUTUBE_CHANNEL_ID_146 = "PLaNvporHqBZtFvp_wj3JZYh2FNGAfuxZl"
YOUTUBE_CHANNEL_ID_147 = "PL_jcrQMoR_3BYvNS6GfPEf1ornygOpyOM"
YOUTUBE_CHANNEL_ID_148 = "UCmp54yNycDoE8UEV5f9bLhQ"
YOUTUBE_CHANNEL_ID_149 = "PLJ9w_R6K5AApJgeRJP7wWG6ZghWKeXTO7"
YOUTUBE_CHANNEL_ID_150 = "PL-LRcs3PmKq53hfEr0eB-L_vg7EO80zIr"
YOUTUBE_CHANNEL_ID_151 = "PLO3Saaykdy5SW3-dG99xGArUq2Gxl8WO7"
YOUTUBE_CHANNEL_ID_152 = "PLRWydu1kSgTIKPMXGGYhYwb9xNqVC41jd"
YOUTUBE_CHANNEL_ID_153 = "PLCxefNhmAKsN5SEj2VPJ6dswPGYjzGEeb"
YOUTUBE_CHANNEL_ID_154 = "PLIAGnFmlKUL7DW9SOQkcZVyQ6qkL8W_6j"
YOUTUBE_CHANNEL_ID_155 = "PLV2xo-FrFOu_aTLABKShBIjL8cOqfOEkY"
YOUTUBE_CHANNEL_ID_156 = "PLutTviYZk9KhfrBUqlwSDvPpMYMhgj7Rn"
YOUTUBE_CHANNEL_ID_157 = "PLVwG5O3xsqwNdqZZA-C6Ca38X3Yd7TPHl"
YOUTUBE_CHANNEL_ID_158 = "PLdSitq2h7vCKiT9PsFnnUlxkhuBpA8mKN"
YOUTUBE_CHANNEL_ID_159 = "PL46H0TpAdm3EARc1K4VQowyppP2gmb1va"
YOUTUBE_CHANNEL_ID_160 = "PLlKlg98NPleNT_Va5I3aUOF-6cTYotQPs"
YOUTUBE_CHANNEL_ID_161 = "PLd4ZP0qc_4J_v8FSX_1wdv8DZJk63gkxd"
YOUTUBE_CHANNEL_ID_162 = "PL7gRVXvSqr44fWetzw6Wvmh35X0fNA4to"
YOUTUBE_CHANNEL_ID_163 = "PLS5hkS-vD9CXOFeikdjErti9OhK6Tloj3"
YOUTUBE_CHANNEL_ID_164 = "PLMHM5-dwmI8FQG78IE-9cCB-HzvWjbWXh"
YOUTUBE_CHANNEL_ID_165 = "PLdeiBYnf0YBmnqBPCtO4mmjjP9vgQihwj"
YOUTUBE_CHANNEL_ID_166 = "PLG9w-7UOrMG3BE6GgtA5IpqrMXwmyiEW9"
YOUTUBE_CHANNEL_ID_167 = "PLlVXoVdq9vWnEfK7h9DgLZ1s108Gitz59"
YOUTUBE_CHANNEL_ID_168 = "PL6fJmjt84zZhJ40WIwsbrmJaSLDvG5zNq"
YOUTUBE_CHANNEL_ID_169 = "PL6l6gmCNou51-4Mvu_dDQHsoblubM1FZd"
YOUTUBE_CHANNEL_ID_170 = "PLC6dyS5uZ4TwMAcAPUhK_FIAtT7n3rVZM"
YOUTUBE_CHANNEL_ID_171 = "PLHo5m9zfQvkSJW2Qa880iAMvyN2xYlIKB"
YOUTUBE_CHANNEL_ID_172 = "PLVjkcOOKO6DMslh7UL1WYGS6Y9GE5tBTB"
YOUTUBE_CHANNEL_ID_173 = "PL2AF155372EFE8DA0"
YOUTUBE_CHANNEL_ID_174 = "UCGGe5QkDaQljTEBPB4l_ggw"
YOUTUBE_CHANNEL_ID_175 = "PL-LbyE8S6hrkiHi2KLqmR42XKtg9QeMOl"
YOUTUBE_CHANNEL_ID_176 = "PLcNh_q0ZuqfXh2qvlHTxVAngyGkVyz_yA"
YOUTUBE_CHANNEL_ID_177 = "PL9DKjFkAdKepUCYvPkrpxXI4IMRkOeHN5"
YOUTUBE_CHANNEL_ID_178 = "PLZAtRdngK4gvUagyG0RMIy4ipFbsUsNXF"
YOUTUBE_CHANNEL_ID_179 = "PLBNWQPjDpOeXjSZXbLHBPUeBgHfajdSUV"
YOUTUBE_CHANNEL_ID_180 = "PLmzhSIKdhdXzp5AkvGJuhLbtcMuctfcAR"
YOUTUBE_CHANNEL_ID_181 = "PLTJl-mozM7lsBXT2CZnDQx7vXgZFNoKj_"
YOUTUBE_CHANNEL_ID_182 = "PL_Fs_-hMcnvJ187v3E39lS7Aw8NMqzibL"
YOUTUBE_CHANNEL_ID_183 = "PLJtOuURKdwmaEqYPf_fApkir4Lca9d7uv"
YOUTUBE_CHANNEL_ID_184 = "PLM8HyfLc0NBzrKh70FRt5AKDHj8yFAA7J"
YOUTUBE_CHANNEL_ID_185 = "PLkIz0A0fICS7Udfx89082ZaJxuO2TjXUG"
YOUTUBE_CHANNEL_ID_186 = "PL_00JAaq2fMMZu89mY4q3ZewshcZQ7nEp"
YOUTUBE_CHANNEL_ID_187 = "PLfgvcoi-AEhJCqGShMlEgnSsteX58scGY"
YOUTUBE_CHANNEL_ID_188 = "PLlqh3IWJw4-Xax0lV4ZoxI04Efl8wOoXA"
YOUTUBE_CHANNEL_ID_189 = "PLqh0J7BR5v69U5sKMi7U_geScHdqAWRWv"
YOUTUBE_CHANNEL_ID_190 = "PL0hcwMVyPPyEiyyMju7AFM0NjE_TbLJw4"
YOUTUBE_CHANNEL_ID_191 = "PLGeINXAFv8QhpjGijYbPDYkiOczrgXrka"
YOUTUBE_CHANNEL_ID_192 = "PLkMQ_CJMj6QaIhGwYGhj3edC7RlvwRv7J"
YOUTUBE_CHANNEL_ID_193 = "UCwoYgzY-lranjTD0QFZtnSA"
YOUTUBE_CHANNEL_ID_194 = "PLgUw4atv1vAnOTQgUNEonC1deP44Q7D9r"
YOUTUBE_CHANNEL_ID_195 = "PLzE_YcUQmigfhLSD6a3yyPwwY7BCpk8QQ"
YOUTUBE_CHANNEL_ID_196= "PLd2lDWWAdNqWNUMEFOyhj6O9lgrw0OFVe"
YOUTUBE_CHANNEL_ID_197 = "PL54856EB4DCF67FD6"
YOUTUBE_CHANNEL_ID_198 = "PLsx_q58dL8KFA4Ulv_d1Ly9KKRQn2k6Bv"
YOUTUBE_CHANNEL_ID_199 = "PLh3E8R3TZM1vybqQBVfAUZ-LW4F9g59Om"
YOUTUBE_CHANNEL_ID_200 = "PLiq4tFPSfcg5UdrrWLNBeKup0Emxs1SpR"
YOUTUBE_CHANNEL_ID_201 = "PL4S7WPfhr-ADhzh8NPxQ0X-UZSiIvBsm5"
YOUTUBE_CHANNEL_ID_202 = "PLI2OfbXGIjuBie-MO5EhCn01N-vN3qyd9"
YOUTUBE_CHANNEL_ID_203 = "PLqal8KdJyWc8a_dWhlvqXx0DCX9ZLUt78"
YOUTUBE_CHANNEL_ID_204 = "PL6Kwd1RCONOtofKE7dKgBKlxzOY8eDyHA"
YOUTUBE_CHANNEL_ID_205 = "PL1LR4lLgv8wJpq17EqbhWl9fP_Y9TSXlm"
YOUTUBE_CHANNEL_ID_206 = "PL2RzsTTHhhwXArYD05sQhkrblr5fC0rzg"
YOUTUBE_CHANNEL_ID_207 = "PL-we1BvXNmXnem9TAX98vi3BX4eYrozTP"
YOUTUBE_CHANNEL_ID_208 = "PLkexxh-KfPFpudbP9gycDCzQonp7mW9dB"
YOUTUBE_CHANNEL_ID_209 = "PLONlV9FPbFJVtO2GsynVnFw5ogp8_Cb-2"
YOUTUBE_CHANNEL_ID_210 = "UCHF6bik7Ce58RwIZR2JR-ww"
YOUTUBE_CHANNEL_ID_211 = "PLs4ShdpKBtevtQle4DGWmBWygwhH37JrV"
YOUTUBE_CHANNEL_ID_212 = "PLhLqgh-2uKfubU_av477STefoRduTV_Q_"
YOUTUBE_CHANNEL_ID_213 = "PL7rWEelTPsWl_QmPrjFs9IING2WzQpqpd"
YOUTUBE_CHANNEL_ID_214 = "PLqxp1vgVKVwMhEVhmU0NERDdHgyphbIZ3"
YOUTUBE_CHANNEL_ID_215 = "PL6WV78vq5Cp69ueeWpyLf-ZkrGy2BFKgC"
YOUTUBE_CHANNEL_ID_216 = "PLfzcZIWaTZ2R1fDeVR7y59EPmV5TwZBHP"
YOUTUBE_CHANNEL_ID_217 = "PLnWUPRwwB9XrVKoUp9FobAGtHXQP8WaJo"
YOUTUBE_CHANNEL_ID_218 = "PL-wcLP0dedm5sT4o99Bv9ybuer8q_x670"
YOUTUBE_CHANNEL_ID_219 = "PLX60AGP3BjqfPf4MfCyHjiDPCDEgJLhbu"
YOUTUBE_CHANNEL_ID_220 = "PLingvdtU8lIUpVzYHXgUPvO9wAEQIlDSc"
YOUTUBE_CHANNEL_ID_221 = "PLxVm8vGPApNRhZBS_a1uN1qcuPtLgj5Ne"
YOUTUBE_CHANNEL_ID_222 = "PL5TDzEcg9MggrCIDSc2qCVSffvKxKn_f1"
YOUTUBE_CHANNEL_ID_223 = "southparkstudios"
YOUTUBE_CHANNEL_ID_224 = "PLoJpmGGFRuoEfyxhNo1xoqqory19ZPgkB"
YOUTUBE_CHANNEL_ID_225 = "UCNYyzLPpr_iJWMrbKeugD1w"
YOUTUBE_CHANNEL_ID_226 = "PLIdToQCe4iCDCZQLmII8zrCFeNY3SLH4k"
YOUTUBE_CHANNEL_ID_227 = "PLDQvVs2Jn5mbK29dgY0YOHjLtoVJo5s9x"
YOUTUBE_CHANNEL_ID_228 = "PLP1pVFTMxmhz1U75-02BPEAjdu7t0n1d_"
YOUTUBE_CHANNEL_ID_229 = "PLBsOFQDmwFzP3i13OYLsnIeQAqphrFqgD"
YOUTUBE_CHANNEL_ID_230 = "UCjfuCKj49GuyysgC9zzDuSQ"
YOUTUBE_CHANNEL_ID_231 = "PL2MpdH56omP66BmVe38-QRNGLhXljruYC"
YOUTUBE_CHANNEL_ID_232 = "PLHE9gVmXFiuQ8BHOc0HHxghlxeCgNaRZQ"
YOUTUBE_CHANNEL_ID_233 = "UC2teM2AXzety_ya31pZnOOA"
YOUTUBE_CHANNEL_ID_234 = "PLYnLKyP-VUz5lfJAvdneeF5pIYWNIQWsa"
YOUTUBE_CHANNEL_ID_235 = "PLFINu0qGF5n6L7cbpBiJInr0rtZhoQH0o"
YOUTUBE_CHANNEL_ID_236 = "PLtAUhMuKZ9dbtM325iOkpEESgTo4WF2Qz"
YOUTUBE_CHANNEL_ID_237 = "PLbrg2AlEj90Ub72YMY3iyPjfCmAJPnQ3H"
YOUTUBE_CHANNEL_ID_238 = "PLIqkENqCFrAyR3xW40HxJbGj5N4yqttx4"
YOUTUBE_CHANNEL_ID_239 = "PLs3QVVdErCGxIVsa8DDCLTtKwT5U_k7j3"
YOUTUBE_CHANNEL_ID_240 = "PL5FG2ORbtNy4pW6s1RxgYvvjsuxtPVE4_"
YOUTUBE_CHANNEL_ID_241 = "PLrolYE1hS9aL9uOcHA9sPa90PQJlB5hBI"
YOUTUBE_CHANNEL_ID_242 = "PLvupJ7Pqeu1qtqt9TUgGQZbDC8VsOm0ej"
YOUTUBE_CHANNEL_ID_243 = "PLFsbvbIo45keMmnvZrIAiHshRWiSfWqYK"
YOUTUBE_CHANNEL_ID_244 = "PLUtyelKnYB0BaJaB2UUzwSmrpttvLuMzy"
YOUTUBE_CHANNEL_ID_245 = "PL_pBm59CmTLvO4f3RfEoVm1TmH-wCsEy3"
YOUTUBE_CHANNEL_ID_246 = "PLZynWltRKeQaq-jTw0mAqlYP_cnhnU2tF"
YOUTUBE_CHANNEL_ID_247 = "PLEpydwKzu27jJUgYKNq1uTdzX2-5Exd8e"
YOUTUBE_CHANNEL_ID_248 = "PL0-31eWh3Qpnycjz5r1639qY2OnDKQW3v"
YOUTUBE_CHANNEL_ID_249 = "PLMZkSF_vEa7e55chCDDB-bOxq8A-xdzcy"
YOUTUBE_CHANNEL_ID_250 = "UCkfJA6w0Qt9d1H1XkkyIFVg"
YOUTUBE_CHANNEL_ID_251 = "PLvISu4ns9LJw-H3dA9hw9kbhbP1Kktb8P"
YOUTUBE_CHANNEL_ID_252 = "PLVN98XhsfSmKHTrtXohW6SHyOCoEsbCCv"
YOUTUBE_CHANNEL_ID_253 = "PLZOeEwuABeKt2_IhLzZToJrURBvcemC4I"
YOUTUBE_CHANNEL_ID_254 = "PL9AGmb_ncNyw9aYc4iq_EFvpRLQz5bO8H"
YOUTUBE_CHANNEL_ID_255 = "PLq0q5n9Nn1aLV8JXh9DCxuaV4HJbf-XZr"
YOUTUBE_CHANNEL_ID_256 = "PLtbScrt6Sxo9IkkUWcmk_hgBVvoZ5bJeB"
YOUTUBE_CHANNEL_ID_257 = "PL_QPPcZlYgRfGUYuEOTc1yk-z_NUc18Ri"
YOUTUBE_CHANNEL_ID_258 = "PLooDYdhPQZJC_NnQx727UHFH86xnNMN0N"
YOUTUBE_CHANNEL_ID_259 = "UCNUvjpUyelv565LRh70F13Q"
YOUTUBE_CHANNEL_ID_260 = "PLxk7IMmndUKuh0ruobQp88iTjr_qssv2k"
YOUTUBE_CHANNEL_ID_261 = "PLMPSJv6tKI01tEvaBfxKHpml1-Fuzz1jM"
YOUTUBE_CHANNEL_ID_262 = "PL8kSBfCxDebvq3eoZD2qnl0JjBcuRLiNP"
YOUTUBE_CHANNEL_ID_263 = "PLQXnnj9pdejcTM6OhxK0pOthm1CJNe9Hm"
YOUTUBE_CHANNEL_ID_264 = "PLVY0mK9ux2DyvdgJU3jw6GUTklpPq0LsX"
YOUTUBE_CHANNEL_ID_265 = "PLVke2_qZUHOrtVfHN2SBiuNRe1ColQkI0"
YOUTUBE_CHANNEL_ID_266 = "PLr9dn-_32mDcjffF7M-1nP5nNPYk6lBaN"
YOUTUBE_CHANNEL_ID_267 = "PLecYxHnp2I2KkmtyrXdPQ8HBanhXnPjv9"
YOUTUBE_CHANNEL_ID_268 = "PLe5HutljgbCdEvQMooxzJKJlk5roqX1mf"
YOUTUBE_CHANNEL_ID_269 = "PLFdTizVQ4p0tQvRPqSqP_b4RK4ajEfZrw"
YOUTUBE_CHANNEL_ID_270 = "PLPfexRHg55rdYyXoIKzjUtahVOkq3gK09"
YOUTUBE_CHANNEL_ID_271 = "PLdYzuIgs98bHjfViMvXHulK_rdDZeoGWw"
YOUTUBE_CHANNEL_ID_272 = "PL9HOFfqLwLftkK064zzg9xsMGaWE1aBY4"
YOUTUBE_CHANNEL_ID_273 = "PL27ZfevcNNlXv7PYgQzoNeii3ulgcvYSC"
YOUTUBE_CHANNEL_ID_274 = "UCzciDN9nGovrqPZrSLQ2Aig"
YOUTUBE_CHANNEL_ID_275 = "PLKuzFhxtS9BEtKqEjmCNzRIEYpFK7gzY6"
YOUTUBE_CHANNEL_ID_276 = "PLPpz1ABAkE6gYbTSRnQ5tJS2GTHovEfHG"
YOUTUBE_CHANNEL_ID_277 = "PLWhpoN2bHhj-ytrUDcrVMGui0CscsQ7Db"
YOUTUBE_CHANNEL_ID_278 = "PLHQ_oTd6hcIVM0Sz4pgLmGfv2-Q5RqP2M"
YOUTUBE_CHANNEL_ID_279 = "UClpnmftuE-eSFe6e3OvjGRw"
YOUTUBE_CHANNEL_ID_280 = "PLwxBsQAmNZi2TDU3IWy9rkmWCefJyY0Hi"
YOUTUBE_CHANNEL_ID_281 = "PL3G-K8eQQmysJQozGfnxWR5C6b8Vtvoqm"
YOUTUBE_CHANNEL_ID_282 = "PLozX5ELVtUH5DH1v_-Xu21FQb7Es1D3HD"
YOUTUBE_CHANNEL_ID_283 = "PLyeh6fixWRJA0PwlvL9xDs_n8Z9AMgmbO"
YOUTUBE_CHANNEL_ID_284 = "PLtBvTXy2nakjPUOfqoLI0e5mv65xpTRyN"
YOUTUBE_CHANNEL_ID_285 = "PLdgrrdU4AQThd0VRWeVP7-PAMqEd6OaKi"
YOUTUBE_CHANNEL_ID_286 = "PLDPrTXJWjYEC04NaoopGUtNml7-iRak18"
YOUTUBE_CHANNEL_ID_287 = "PLbzg2YPoHDDj00-S64SFjuUIEH-SPtz6_"
YOUTUBE_CHANNEL_ID_288 = "PLSU9W-QBp2ftiDrrxFB96zzFVzIxFT1SL"
YOUTUBE_CHANNEL_ID_289 = "PL2F217D855BEA1AD6"
YOUTUBE_CHANNEL_ID_290 = "PL6fJmjt84zZiXLrW3oSLPa4TvvYzKzkuk"
YOUTUBE_CHANNEL_ID_291 = "PLjB1oGzn24fyEDm6owCjcbkVKwSM74GdY"
YOUTUBE_CHANNEL_ID_292 = "PL1UZjRVHxvFXUf4kQwEV96_wMqFkZGpWS"
YOUTUBE_CHANNEL_ID_293 = "PLu8hkxftSUCa5ECpLuCxfC7WKuH0xEQtL"
YOUTUBE_CHANNEL_ID_294 = "PLjCHQ6f-84yIpauu4oOmSouCxvWAc9vRa"
YOUTUBE_CHANNEL_ID_295 = "PL617alMoU-4zEMpFnBIPhyQddGunIIY_v"
YOUTUBE_CHANNEL_ID_296 = "PLnvf2A0109q750YCFp_KptORZRGlTo0xS"
YOUTUBE_CHANNEL_ID_297 = "PLuofBZ5JW5fTIsSfMjb6ULPoY6udKTTbl"
YOUTUBE_CHANNEL_ID_298 = "PLYA1dURVg2KxVhXX-y0viKQi4HoiDSqCs"
YOUTUBE_CHANNEL_ID_299 = "PLl03ZzGdfVGfUrAYLDdj7vNHRGn64wO3C"
YOUTUBE_CHANNEL_ID_300 = "PLBKSOTDRapq9iKuynkxEu3yVYqeLKmANR"
YOUTUBE_CHANNEL_ID_301 = "PLXUE7jvMSzBgevVGeGg5HO6RDsunPJzpI"
YOUTUBE_CHANNEL_ID_302 = "PLt5RI41LZXIG_ksI5jJescqAoi7TV6XGg"
YOUTUBE_CHANNEL_ID_303 = "PLORGLwxEexXQbWUir9bdsKENZRxTZl8US"
YOUTUBE_CHANNEL_ID_304 = "PL4C-qQqO-WH76I4gW9EvcbJBv8yXyu2uN"
YOUTUBE_CHANNEL_ID_305 = "PLeY7w-PAPTxgVYpTYrGWr01Bbqf-FcXNn"
YOUTUBE_CHANNEL_ID_306 = "PLEgRWlWjKFGI_JA43yomUOtYc2YmJGKcx"
YOUTUBE_CHANNEL_ID_307 = "PLgQFNNi6bnudsOB7uFycgX3ZQpjcWa5em"
YOUTUBE_CHANNEL_ID_308 = "PLx_Pgqw_rNDwgwvMGwewzuXU_HwfHDNN6"
YOUTUBE_CHANNEL_ID_309 = "PLQaOoH32QUQSESBaPNzGiUHtbLo2A3Glm"
YOUTUBE_CHANNEL_ID_310 = "PLDGoDsC8VILsw1ZISDO6K-Jg4pKBppa_q"
YOUTUBE_CHANNEL_ID_311 = "PLYyxPgJYQq2mZDZvziU86prrN9Nd1M2UE"
YOUTUBE_CHANNEL_ID_312 = "PL2mWrdNMxh6_KK_APehlckxzCgVMq8yGe"
YOUTUBE_CHANNEL_ID_313 = "PLN27Dkvp_PlXFhrgEfyYBj4U__b1Q2BwH"
YOUTUBE_CHANNEL_ID_314 = "PLkcgo2RnjCXQofVX6_VXHuHhjuV7TRSJc"
YOUTUBE_CHANNEL_ID_315 = "PLwp5eKmtoaigJw_hLqMdQj1gLbzNETPe8"
YOUTUBE_CHANNEL_ID_316 = "PL9F_wRTOZaztsjj12YwtPmu1Y5TuQhfUz"
YOUTUBE_CHANNEL_ID_317 = "PLcZGj3OZ_oTlQ36RPsWzcVf-9OWJRzAgh"
YOUTUBE_CHANNEL_ID_318 = "PLACDJgRlYhhkYoR37zq4rP8kiBsjg78ue"
YOUTUBE_CHANNEL_ID_319 = "PL2D8NMWnu6vUYGpEN4WHRXSih5mbYIclV"
YOUTUBE_CHANNEL_ID_320 = "PLGDoChxXzTQzGNho5RxXLjpepvXeXlRwu"
YOUTUBE_CHANNEL_ID_321 = "PLvsBARGIoD_iSVdSKapmxCNV6UyqjcGSO"
YOUTUBE_CHANNEL_ID_322 = "PLOFsA99jxR1PTEs_9lX0ArQtiC_aWGVwt"
YOUTUBE_CHANNEL_ID_323 = "PLbTcrjtgHvyKugU5CGdlZG3Zo82pXntaO"
YOUTUBE_CHANNEL_ID_324 = "PLOnK2V9jd0x7hpc0oj4PbqVrFMmSPcB7J"
YOUTUBE_CHANNEL_ID_325 = "PLrEnWoR732-AKYdZyzAnuf-MnPiw7rT4Q"
YOUTUBE_CHANNEL_ID_326 = "PLO80YgdoKsrPjep-BjvJQN8Hqgty3bdf8"
YOUTUBE_CHANNEL_ID_327 = "PLeFDJcmrni1lsBfko-cvKHm23rBx02uCX"
YOUTUBE_CHANNEL_ID_328 = "PL-ySemJkwvEMmke4MvGSd0WlicgoFzM-r"
YOUTUBE_CHANNEL_ID_329 = "PLvdkqP5HJkATVDkHa5g0_nJJ1tVu4aonm"
YOUTUBE_CHANNEL_ID_330 = "PLGBE8rlg5QeKSNSXtCOaGXggwOFPA7AST"
YOUTUBE_CHANNEL_ID_331 = "PL1sUWjMkugMQgokvHm5wS-vMHv9-2oDNO"
YOUTUBE_CHANNEL_ID_332 = "PLqq4JnCv0a1QXAlEqHrvzJ2IbLFyJJb-8"
YOUTUBE_CHANNEL_ID_333 = "PLJ0Tuf8bkHt41tSAfpXkHyc86GSrqvcpe"
YOUTUBE_CHANNEL_ID_334 = "PLrZ3USaDUbE760Vqs1XbZwfIlrtbk0UKL"
YOUTUBE_CHANNEL_ID_335 = "PLkEW2ev4gq041dLHTjmTWqO629H3w4NG8"
YOUTUBE_CHANNEL_ID_336 = "PLl3eTUWtsO9omcKc5R1q06NZmMcjPqTc-"
YOUTUBE_CHANNEL_ID_337 = "PLSdy1579EREHOTIdpGflx6O84qi-VqYu4"
YOUTUBE_CHANNEL_ID_338 = "PLPsEburL_mH3tPfTSm4jPU0HbhxyjN2iq"
YOUTUBE_CHANNEL_ID_339 = "PL-NyMxBKWM7bxy7hIIHlvEVqHESofvcWa"
YOUTUBE_CHANNEL_ID_340 = "PLVt5TSZyWM2o_Qr0UdT03lGRaTfVQK9yO"
YOUTUBE_CHANNEL_ID_341 = "PL4gt2Trt0k7IWdpEsfCQ-WO8mIMTQ39kC"
YOUTUBE_CHANNEL_ID_342 = "PLLjk5NX4bh6YlucjLSmUF1DglZB3vmXpB"
YOUTUBE_CHANNEL_ID_343 = "PLs7j-0BppWuDhxkk7HMLwiZnWnC-l2mKO"
YOUTUBE_CHANNEL_ID_344 = "PLiysj-EKbPPrhY-dZLyGVsg5ef_WKir4F"

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
        title="227",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://cdn.smosh.com/sites/default/files/legacy.images/smosh-pit/022011/227%20on%20gmc.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Absolutely Fabulous",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/5c/8f/b5/5c8fb5bc2c1bdadbbc2bd3fd982f42e3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="According to Jim",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/90/29/f1/9029f1476a2ad937c71a9da960efbd23.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="All in the Family",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/564x/6a/a6/46/6aa64627a5bebecead45adad08628cfa.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Allo Allo",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/0d/ff/7e/0dff7e6134a0843b7533705ded9db4f3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Amen",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/f3/f3/9b/f3f39b6ea6b5c70a2e6b84560e0cb0c4.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="America's Funniest Home Videos",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/7/75/AFHV_original_logo.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Amos and Andy Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/33/0b/d9/330bd90fd8b73ad401e096f14ef67bea.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Andy Kaufman/Jerry Lawler Feud",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://www.memphisflyer.com/backissues/issue440/images/cvr440a.gif",
        folder=True )           

    plugintools.add_item( 
        #action="", 
        title="Aqua Teen Hunger Force",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/fd/d9/57/fdd957356bbe13f03609117f976a53f3.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Are You Being Served",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/0d/45/44/0d454414f2e4254034699fc154b77652.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Arrested Development",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/8a/7e/7e/8a7e7e687acdd4e9d40990f0bb76e52e.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Attack of the Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://www.millionaireplayboy.com/mpb/wp-content/uploads/2010/04/aots-april.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Auf Wiedersehen, Pet",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="http://i4.chroniclelive.co.uk/incoming/article6058299.ece/ALTERNATES/s615/aufmain.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Bachelor Father",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/1b/dc/0e/1bdc0e9e67dd77ca999c81e6a05327a3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bad Lip Reading",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/5c/3e/54/5c3e545f55364a73581915995932f1cf.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Balls of Steel",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://contentpl-a.akamaihd.net/images/playlists/image/medium/101125.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Barney Miller",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51Rkbq5%2B2tL.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Beadle's About",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://heartshapedbackpack.files.wordpress.com/2015/06/beadles-about.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Becker",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51KRe5nL%2BFL.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Being Erica",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://cmsimg-290a.kxcdn.com/bigarticles/beingerica2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Between Two Ferns with Zach Galifianakis",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="http://bigfanboy.com/wp/wp-content/uploads/2014/03/betweenferns-obama.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Bewitched",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/1f/ba/7c/1fba7cbe6b06aae25f65241ebc9c286f.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Big Train",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/M/MV5BNjI3NDk4MTk1M15BMl5BanBnXkFtZTcwNjAzNTI0MQ@@._V1_UY268_CR3,0,182,268_AL_.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Blackadder",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/52/37/8c/52378cbca44f7a505aefbef0eca4e76d.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Black Books",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/88/34/75/883475cb5f9b55da1c02000344c4cde0.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Bless This House",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/564x/fa/3d/c1/fa3dc1bd1d6ec4f8c1927fbcec86bd30.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Blondie",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51q%2BXnMIcLL.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Bo Selecta",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51DVXE208XL._AC_UL320_SR226,320_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bosom Buddies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/fe/eb/ab/feebab76c5037383450e7c478142c51b.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bottom",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="http://static.tvtropes.org/pmwiki/pub/images/bottom_281.png",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Burnistoun",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://images-eu.ssl-images-amazon.com/images/I/51Q7BNFZkVL._SY300_QL70_.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Brass Eye",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="http://sotcaa.org/history/sotcaa2000/hidden/images/brassad_dvd.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Bread",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="http://images.45cat.com/the-cast-home-theme-from-bbc-tv-series-bread-1986-3.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Brush Strokes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/51F105CPjAL.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Candid Camera",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://yt3.ggpht.com/-9Krczke7OK0/AAAAAAAAAAI/AAAAAAAAAAA/yp8T4XrELyM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Car 54, Where Are You",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/f3/04/c5/f304c5543754edf6949db1610ebd8f2b.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Carpool Karaoke",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="http://carpoolkaraoke.com/wp-content/uploads/2017/03/CarpoolKaraokeLogo_sm_whiteback.png",
        folder=True )           

    plugintools.add_item( 
        #action="", 
        title="Catastrophe",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51xQydvfhDL._SX940_.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Cavemen",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="http://www.monologuedb.com/wp-content/uploads/2011/03/ben-weber-geico-caveman.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Chappelle's Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51B5Z142P1L.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Charles in Charge",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/3b/25/66/3b2566d6e02aea499b48a4d85c5822da.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cher Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Cher_-_The_Cher_Show_opening.jpg/250px-Cher_-_The_Cher_Show_opening.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Chewin' the Fat",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/f/f8/Chewinthefatdvdcover.jpg/250px-Chewinthefatdvdcover.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Come Fly with Me",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="http://4.bp.blogspot.com/-l4YAfU55PFE/TftAJCaQn1I/AAAAAAAABXg/A25f3gzU-FM/s1600/come_fly_with_me_fan.png",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Comedy Central Presents",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="http://www.nytix.com/repository/tvshows/ComedyCentral/logo.jpg",
        folder=True )     

    plugintools.add_item( 
        #action="", 
        title="Comedy Central Roast",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/b/b0/Comedy_Central_Roast_2011.png",
        folder=True )        

    plugintools.add_item( 
        #action="", 
        title="Corner Gas",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/f4/88/2d/f4882da098fbdad5e8b6742040daa575.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Crayon Shin-Chan",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/81vjTyeT3tL._AC_UL320_SR240,320_.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Da Ali G Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://static1.squarespace.com/static/555bc76ee4b0db4a78d442be/t/5560244ce4b07a2428ec5fd3/1432364109569/ALI+G+PF.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Dad's Army",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="http://verycollectable.com/wp-content/uploads/2017/01/clive-dunn.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Dennis the Menace",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/3c/15/4f/3c154f5f977aa72993c01592a9f1c24f.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Diff’rent Strokes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/ac/7f/e1/ac7fe1f2a7f5ae3bbcbeb9919bf9753b.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Dinosaurs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/c6/bf/51/c6bf51b0fe6e8a4ad414a95e243b7820.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Doctor at Large",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/30/ea/c8/30eac862463bd3c335c27fe538215bc2.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Doctor in the House",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/7/79/Doctor_in_the_House_title_card.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Doogie Howser, M.D.",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="http://rt2qxflpae-flywheel.netdna-ssl.com/wp-content/uploads/2014/07/markus-redmond.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Double Dare",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/d/df/Double_Dare_logo.png",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Double Trouble",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/8/8e/SagalTwins_M2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Downfall Parodies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="http://vignette1.wikia.nocookie.net/hitlerparody/images/9/97/Downfall_Parodies_Logo_Square.jpg",
        folder=True )      

    plugintools.add_item( 
        #action="", 
        title="Dr. Demento",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="http://drdemento.com/images/demento1-s-t.gif",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Drawn Together",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_62+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/6e/b4/61/6eb461cbb23e85e4d96d00a8b42d8a2f.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Drop the Dead Donkey",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_63+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51oZS4qp0lL.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Drunk History",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_64+"/",
        thumbnail="https://pbs.twimg.com/profile_images/638769413894705152/2qsJxIoi.jpg",
        folder=True )        

    plugintools.add_item( 
        #action="", 
        title="Empty Nest",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_65+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/0/05/Empty_nest_cast_1993_1995.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ernie Kovacs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_66+"/",
        thumbnail="https://yt3.ggpht.com/-aCwgaR-YExA/AAAAAAAAAAI/AAAAAAAAAAA/G_9XPB53clw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Even Stevens",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_67+"/",
        thumbnail="http://mustangimdb.com/images/jmovies/img_pictures/even-stevens.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Everybody Loves Raymond",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_68+"/",
        thumbnail="http://multimedia.bbycastatic.ca/multimedia/products/500x500/m21/m2194/m2194261.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Family Feud",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_69+"/",
        thumbnail="https://yt3.ggpht.com/-lRk8jg_TRsk/AAAAAAAAAAI/AAAAAAAAAAA/gUcSv_YYju8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Family Guy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_70+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/d8/3e/3e/d83e3e2d961238d025f520565465ea80.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Family Ties",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_71+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/ce/f4/31/cef431eaf345321f80c4840843664657.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Father Knows Best",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_72+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/78/71/c2/7871c2e525e4bca423e066c3e40f01d0.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Father Ted",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_73+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/81/59/34/8159349572bbd829c02376f20751154f.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fawlty Towers",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_74+"/",
        thumbnail="http://images.eil.com/large_image/XXX-251074.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fernwood Tonight - America Tonight",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_75+"/",
        thumbnail="http://classicdvdworld.com/assets/images/fernwood_logo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ferris Bueller",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_76+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/51/3d/5f/513d5fe4305bd77b06b6a57516d1761b.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Freaks and Geeks",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_77+"/",
        thumbnail="http://akns-images.eonline.com/eol_images/Entire_Site/2014825/rs_560x415-140925114004-1024.freaks-and-geeks.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Friday Night Dinner",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_78+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/93/93/ee/9393ee9a214c01ce2eee4d4528ebc332.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Fridays",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_79+"/",
        thumbnail="http://www.tvparty.com/bgifs24/fridays.jpg",
        folder=True )     

    plugintools.add_item( 
        #action="", 
        title="Full Length Comedy Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_80+"/",
        thumbnail="http://blog.laterooms.com/wp-content/uploads/2011/09/Laughing1.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Funny Animated Short Films & Cool Animation",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_81+"/",
        thumbnail="https://www.funnypica.com/wp-content/uploads/2012/09/Funny-Animations-20.gif",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Funny Cat Videos",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_82+"/",
        thumbnail="http://s2.dmcdn.net/eINkN/x240-xjW.png",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Garth Marenghi's Darkplace",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_83+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/41pr73xYYBL.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Gary: Tank Commander",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_84+"/",
        thumbnail="https://ichef.bbci.co.uk/images/ic/640x360/p01h037r.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Gavin & Stacey",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_85+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/26/7b/8f/267b8f34e977fccfb959cdd99e2f2fc0.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="George and Mildred",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_86+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/18/2c/71/182c710af67e9b4e11df5372857cd983.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Get a Life",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_87+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/24/ae/7d/24ae7d012d915055f8f4119195ae8be0.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Gilligan’s Island",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_88+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/31/e7/e9/31e7e960351da705e7f87374a9276f83.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Gimme a Break",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_89+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/0b/73/81/0b73817d311c6542cea3eb213f6865d9.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Girlfriends",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_90+"/",
        thumbnail="http://is3.mzstatic.com/image/thumb/Video/64/db/dd/mzl.fxejcgsn.jpg/600x600bb-85.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Gomer Pyle, U.S.M.C.",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_91+"/",
        thumbnail="http://mustangimdb.com/images/jmovies/img_pictures/gomer-pyle-ep5.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Good Times",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_92+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/57/be/a8/57bea828d1dc591ab56f3f9bba6e956e.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Green Acres",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_93+"/",
        thumbnail="https://ezboxset.com/image/cache/catalog/green-acres-dvd-box-the-complete-series-70-500x500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Green Wing",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_94+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/512EQbur70L._SX342_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Grounded for Life",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_95+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/41/2c/2c/412c2c8a30f9c46e1ed191bae96b646e.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hancock’s Half-Hour",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_96+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/13/bb/b9/13bbb97f93c48a26a7be97589e3b18b2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hannah Montana",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_97+"/",
        thumbnail="http://musicyeah.net/wp-content/uploads/2015/09/Hannah-Montana-Hannah-Montana-3-Music-from-the-TV-Show.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Happy Days",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_98+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/564x/d4/69/bf/d469bfb19dd2573e54fb6f6b2b0eadbf.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Harry & Paul",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_99+"/",
        thumbnail="https://image.tmdb.org/t/p/w185/sYOibjurlgWxO2xip1TeMrA8sqG.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Have I Got News for You",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_100+"/",
        thumbnail="http://www.swindonweb.com/uploaded_files/2992/images/have_i_got_news_for_you_logo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hazel",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_101+"/",
        thumbnail="http://mustang.is/images/jmovies/img_pictures/hazel.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Head of the Class",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_102+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/9e/37/57/9e3757e1a0183880349ddde8d2d57738.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hee Haw",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_103+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/8a/c6/57/8ac6574051b4d94632acbe43e04b1515.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Here's Lucy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_104+"/",
        thumbnail="https://s3.amazonaws.com/metvnetwork/YDCBR-1490630055-8116-list_items-hereslucy_title.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Herman's Head",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_105+"/",
        thumbnail="http://iv1.lisimg.com/image/7079856/290full-herman%27s-head-poster.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hi-De-Hi",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_106+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/ce/31/0a/ce310a38bc3ca0e8e59f3f476874a01c.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Hogan's Heroes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_107+"/",
        thumbnail="http://multimedia.bbycastatic.ca/multimedia/products/500x500/m22/m2219/m2219724.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hollywood Squares",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_108+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/6/65/Hollywood_Squares_%28TV_series%29_titlecard.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Home Improvement",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_109+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/2f/eb/07/2feb079a4f39ec6c6be4037da8c7a0f9.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hot Properties",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_110+"/",
        thumbnail="http://tvseriesfinale.com/assets/hotproperties02m.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Humor misc. asstd. funny fun",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_111+"/",
        thumbnail="https://lh5.ggpht.com/ULrK7jO0smSmyCwEKJdSU7_8XWqPJPpgkBgZerKAHRIubDR5fWSc6jLLqZhrdSaCQuo=w300",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="I Dream of Jeannie",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_112+"/",
        thumbnail="http://mustangimdb.com/images/jmovies/img_pictures/i_dream_of_jeannie.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="I Love Lucy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_113+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/61PCgLNMvPL.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="I Married Joan",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_114+"/",
        thumbnail="https://www.vcientertainment.com/image/cache/data/2014/089859860324-500x500.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="I'm Alan Partridge",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_115+"/",
        thumbnail="http://thumbs4.ebaystatic.com/d/l225/m/mC4cXh5JmhnRvwLD-xSQPxA.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Impractical Jokers",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_116+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/a5/8a/91/a58a9116b83b0b3b27332456622280d5.jpg",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="In Living Color",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_117+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/d/de/InLivingColorlogo.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="It Ain't Half Hot Mum",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_118+"/",
        thumbnail="http://farm5.static.flickr.com/4050/4563373636_ccbccb0f43_o.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="It's A Living",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_119+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/7/71/Itsalivingscreen.jpg/250px-Itsalivingscreen.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="It's Always Sunny in Philadelphia",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_120+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/612o6gYBREL._SS500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="I've Got a Secret",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_121+"/",
        thumbnail="http://userdata.acd.net/ottinger/cullen/tvseries/igas5.jpg",
        folder=True )           

    plugintools.add_item( 
        #action="", 
        title="Jessie",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_122+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/01/95/4a/01954a3576d684726e895f3aaf729ae9.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Joanie Loves Chachi",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_123+"/",
        thumbnail="https://i5.walmartimages.ca/images/Large/501/112/1501112.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jonas",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_124+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/cb/4f/a4/cb4fa45bf90ac05800dc5deaf38619cd.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jonathan Winters",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_125+"/",
        thumbnail="http://www.jonathanwinters.com/images/pic_winters-border.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Just Add Water",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_126+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/65/53/f9/6553f9c6420dc8df73ea572855f1c5ee.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Just for Laughs",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_127+"/",
        thumbnail="https://yt3.ggpht.com/-yNspfCq56dQ/AAAAAAAAAAI/AAAAAAAAAAA/il9bnycTmHI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Just the Ten of Us",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_128+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/18/b9/63/18b9638317cba02f82635d45c5ce290d.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kath and Kim",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_129+"/",
        thumbnail="http://farm4.static.flickr.com/3068/2600626250_1737771807_o.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Keeping Up Appearances",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_130+"/",
        thumbnail="https://southernaristocracy.files.wordpress.com/2012/04/kua.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kenan and Kel",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_131+"/",
        thumbnail="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Last of the Summer Wine",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_132+"/",
        thumbnail="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Laurel and Hardy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_133+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/a/ad/Stanandoliie.png/220px-Stanandoliie.png",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Laverne and Shirley",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_134+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/87/40/ed/8740ed607adf12f3f197fe40b9a7812d.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Leave It To Beaver",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_135+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/20/68/67/2068679183c7877b58f4bb5db46d607f.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Legends of the Hidden Temple",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_136+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/7/77/LegendsTitlecard.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Lenny Bruce",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_137+"/",
        thumbnail="https://www.biography.com/.image/c_fill,cs_srgb,dpr_1.0,g_face,h_300,q_80,w_300/MTE5NTU2MzE2MTY3Mzc0MzQ3/lenny-bruce-9229168-1-402.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Life with Lucy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_138+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/b/b5/LifeWithLucyTitleScreen.jpg/250px-LifeWithLucyTitleScreen.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Limmy's Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_139+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/41EsUILZZNL._SY445_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Little Britain",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_140+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/b5/39/74/b539747a042b46bf5cf6f69f86658831.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Liv and Maddie",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_141+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51lGWRYL8UL._SS500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Living Single",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_142+"/",
        thumbnail="http://static.tvtropes.org/pmwiki/pub/images/111254541.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Lizzie McGuire",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_143+"/",
        thumbnail="https://images-production.global.ssl.fastly.net/uploads/posts/image/47401/lizzie-mcguire-hilary-duff.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Love, American Style",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_144+"/",
        thumbnail="https://s3.amazonaws.com/images.sheetmusicdirect.com/Product/smd_h_00377166/large.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Love Thy Neighbour",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_145+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/b9/11/e0/b911e0e8b64dfabbae6383a34827b60e.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mad TV",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_146+"/",
        thumbnail="http://orig09.deviantart.net/3596/f/2016/070/b/b/mad_tv_v1_by_vamps1-d9uqlpo.png",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Mad",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_147+"/",
        thumbnail="https://shiniscope.files.wordpress.com/2010/03/mad-tv-guide1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Married With Children",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_148+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/65/2c/48/652c4815dba9c89be8226fc77e9a8246.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Martin",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_149+"/",
        thumbnail="http://cdn.playbuzz.com/cdn/e5ecc718-6017-45fd-9fb3-6016b454b085/9a3ffcda-67e5-45bc-98bc-0a6448797c5d.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Match Game",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_150+"/",
        thumbnail="https://pbs.twimg.com/profile_images/725107279150764032/VjBl7JKc.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="McHale's Navy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_151+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/fb/f6/50/fbf65099c9335286c8f33771054c89e4.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mind Your Language",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_152+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/02/d3/75/02d3756c5a8e886a2d646bf6e235cccd.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Minder",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_153+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/19/88/96/198896ef2e2e32e72f46516c708c2a01.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Moesha",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_154+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/25/3d/4d/253d4d44ef38521f9aed47d4f91ac2b2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Monk",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_155+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/d/d3/Monk_Season_One_DVD.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Monty Python's Flying Circus",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_156+"/",
        thumbnail="http://lh3.ggpht.com/_xYY7IOt8M-8/SvNLj2M0vSI/AAAAAAAAHFU/BiChJKaRVSs/montypythonfoot.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Moonlighting",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_157+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/1d/bd/4b/1dbd4bad1c4cecca5e2f71f8b133fc9f.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mork and Mindy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_158+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/18/a0/3c/18a03ce6f0694a5dc40c18f3eb2eb0f1.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Mr. Bean",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_159+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/2d/f9/71/2df9714732510ab3c7bc2a467ddd991a.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mr. Belvedere",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_160+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/0f/9a/4d/0f9a4d7ebf7c15c42c5b045260014647.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mr. Show with Bob and David",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_161+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/M/MV5BMjAwMDg4ODEwNl5BMl5BanBnXkFtZTcwMjk1MjYyMQ@@._V1_UY268_CR7,0,182,268_AL_.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Mrs. Brown's Boys",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_162+"/",
        thumbnail="https://metrouk2.files.wordpress.com/2014/07/mrs-brown-e1418302007877.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Muppets Tonight",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_163+"/",
        thumbnail="https://muppetmindset.files.wordpress.com/2013/07/be9ea-muppets_group.jpg",
        folder=True )        

    plugintools.add_item( 
        #action="", 
        title="Murphy Brown",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_164+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/a9/ef/85/a9ef856fc38977f84ed6900dd8d4e93f.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="My Favorite Martian",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_165+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/47/ea/38/47ea38a0f5e19f58e5069390cf9efdee.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="My Little Margie",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_166+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/53/ca/ff/53caff7da315feff603388bedb48ac88.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="My Mother The Car",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_167+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/ab/12/f5/ab12f52151766b5d3937f1a915ec18ba.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="My Parents Are Aliens",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_168+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/53/5a/37/535a37247820c68ee3732e93def9e3c6.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Mystery Science Theater 3000",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_169+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/e6/08/49/e608499155e0d039b441b59b63e012a7.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mystery Science Theater 3000 (ordered)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_170+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/f/fc/MST3K-logo.png",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Naked and Funny",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_171+"/",
        thumbnail="https://yt3.ggpht.com/--ybnxL0rAKk/AAAAAAAAAAI/AAAAAAAAAAA/avGI5qsDCIU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="National Lampoon",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_172+"/",
        thumbnail="http://deltafonts.com/wp-content/uploads/National_Lampoon_LOGO.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Newhart",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_173+"/",
        thumbnail="https://ezboxset.com/image/cache/catalog/newhart-dvd-box-set-the-complete-series-92-500x500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="NewsRadio",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_174+"/",
        thumbnail="http://www.joelipe.com/wp-content/uploads/2008/11/newsradio_cast.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nickelodeon Guts",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_175+"/",
        thumbnail="http://www.gmkfreelogos.com/logos/N/img/Nickelodeon_GUTS.gif",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Nighty Night",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_176+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/97/9c/e2/979ce273a8f0c431ca9806c056acd752.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Oliver At Large",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_177+"/",
        thumbnail="http://www.sams247.com/images/Oliver%20at%20large%20vol.3_sm.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="On the Buses",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_178+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/28/42/43/28424354adc0bf9863394c03004c78b5.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="One Foot in the Grave",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_179+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/73/c9/6d/73c96db8cba74476d374a4947cb7e321.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Only Fools and Horses",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_180+"/",
        thumbnail="http://thumbs4.ebaystatic.com/d/l225/m/mX1gnCPD9pgIj7kgJLCDbbg.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Only an Excuse",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_181+"/",
        thumbnail="https://i.ytimg.com/vi/k8QGh8zaDFI/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Open All Hours",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_182+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/52/de/c0/52dec061599ef486dd3a28eca7e553b6.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Our Miss Brooks",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_183+"/",
        thumbnail="http://4.bp.blogspot.com/-BV3D-fR3GL8/U6hK9MUY_BI/AAAAAAAAcwg/QHXad0M1GbM/s1600/Our-Miss-Brooks-Eve-Arden.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Outsider Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_184+"/",
        thumbnail="http://e.snmc.io/lk/f/s/e0b611f6f0e4a9508e601d4052af1b73/3737406.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Pee-Wee's Playhouse",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_185+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/63/af/9f/63af9ffd4f1eeb8152e44f3301f4760a.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Peep Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_186+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/eb/14/20/eb14200ad913babedd2393ab65afb9f3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Penn and Teller",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_187+"/",
        thumbnail="http://s1.ticketm.net/tm/en-us/dam/a/be6/6abeb8e1-996f-4b4b-a9d0-8951aa9debe6_107991_CUSTOM.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Petticoat Junction",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_188+"/",
        thumbnail="http://cheesyflix.com/store/image/cache/data/product/main/petticoat-500x500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Phoenix Nights",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_189+"/",
        thumbnail="http://cps-static.rovicorp.com/3/JPG_500/MI0002/815/MI0002815399.jpg?partner=allrovi.com",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Please Sir",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_190+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/8d/66/54/8d6654a89c729fc0aeb3c239856a7666.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Police Squad",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_191+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/ff/03/51/ff035191f1124111788bddfa9d1e7f9e.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Porridge",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_192+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51G0minV36L._AC_UL320_SR228,320_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Punk'd",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_193+"/",
        thumbnail="https://pbs.twimg.com/profile_images/1567315365/punkdlogoorange.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Punky Brewster",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_194+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/4b/e9/5e/4be95e5a8d7b040203fb0c2dd78baba0.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rab C. Nesbitt",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_195+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/c0/81/05/c08105f8f5349370a9ae09b7be79983b.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Red Dwarf",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_196+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/6c/5d/fd/6c5dfd2b2d739209a8c9e7247ed976ce.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Reddit Best 30 Second Youtube Clips",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_197+"/",
        thumbnail="https://assets.ifttt.com/images/channels/1352860597/icons/on_color_large.png",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Reno 911",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_198+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/81jxOvGIzPL._SL1500_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rifftrax",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_199+"/",
        thumbnail="http://cf-images.emusic.com/music/images/album/151/639/15163916/600x600.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Rhoda",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_200+"/",
        thumbnail="https://jaydeanhcr.files.wordpress.com/2011/04/large_rhodafamily.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Rising Damp",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_201+"/",
        thumbnail="http://1.bp.blogspot.com/_0OvRhA2-gFg/RpcC-PuD0pI/AAAAAAAAAMU/P9IPJJr6-Q4/w1200-h630-p-k-no-nu/Rising+Damp+series+4.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Robin's Nest",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_202+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/c2/6e/14/c26e14b94ed9a265d141f5698c828ed4.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Robot Chicken",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_203+"/",
        thumbnail="http://vignette2.wikia.nocookie.net/theoryreader/images/d/d1/Robot_Chicken.jpg/revision/latest?cb=20160125101001",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Room 222",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_204+"/",
        thumbnail="http://www.annotatedmst.com/tinymce/plugins/moxiemanager/data/files/Hellcats/room%20222.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Roseanne",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_205+"/",
        thumbnail="https://pbs.twimg.com/profile_images/3166807611/21a0a617e946f9b4e041d9ca02e020ae.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rowan and Martin's Laugh-In",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_206+"/",
        thumbnail="http://45rpmvinyl.com/pic/laufinlpr.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Salute Your Shorts",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_207+"/",
        thumbnail="https://i.redd.it/e2kdttsqdwdx.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Sanford and Son",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_208+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/32/3d/61/323d61f6efa0de9e2ff9d95cb135686c.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Saturday Night Live",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_209+"/",
        thumbnail="https://pbs.twimg.com/profile_images/648938732150636544/0xudvt4i_400x400.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Second City Television",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_210+"/",
        thumbnail="https://yt3.ggpht.com/-beN1J6zgXGk/AAAAAAAAAAI/AAAAAAAAAAA/I45Yb-ozyRI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Schitt’s Creek",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_211+"/",
        thumbnail="http://www.tvdvdvideo.com/image/cache/data/Schitts-Creek/Schitts-Creek-Season-1-111-500x500.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Screwball Comedies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_212+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/His_Girl_Friday_still_2.jpg/220px-His_Girl_Friday_still_2.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Scrubs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_213+"/",
        thumbnail="http://vignette3.wikia.nocookie.net/scrubs/images/b/b4/Season_5_iTunes_Artwork.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Shasta McNasty",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_214+"/",
        thumbnail="http://www.chud.com/articles/content_images/247/shasta-mcnasty.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Silver Spoons",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_215+"/",
        thumbnail="http://www.jaehakim.com/wp-content/uploads/2007/06/Silver-Spoons.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sister, Sister",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_216+"/",
        thumbnail="https://heymikeyatl.files.wordpress.com/2015/05/sistersister03.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sit Down, Shut Up",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_217+"/",
        thumbnail="http://img.sharetv.com/shows/standard/sit_down_shut_up.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Small Wonder",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_218+"/",
        thumbnail="http://2.bp.blogspot.com/_2wnh27OhVKk/S_By4mtpTeI/AAAAAAAAAn4/lCnaKq1tMno/s1600/small-wonder.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Smart Guy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_219+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/1/1b/Smart_Guy.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Soap",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_220+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/83/f1/b3/83f1b317a635212e2f2066b0a0ac5630.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="Some Mothers Do 'Ave 'Em",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_221+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/7e/a3/fe/7ea3fe1a3ca60684ac4c248eed600462.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sonny with a Chance",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_222+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/13/35/88/133588acc7ae352707181603aa78c49e.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="South Park",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_223+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/e9/66/a6/e966a6deddaebe43e2494f16be5120d3.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Spike Jones",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_224+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51SATSXZC6L.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Spin City",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_225+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/10/0e/f8/100ef8ae557f07e9cff31455d178f64a.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sports Night",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_226+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/86/7f/5f/867f5f411c1041dda02693c4a33e7861.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Steptoe and Son",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_227+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/1a/3b/1e/1a3b1e681a6848bfc80023d43e730490.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Still Open All Hours",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_228+"/",
        thumbnail="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Still Game",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_229+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51A90PP3HPL._AC_UL320_SR240,320_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Still Standing",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_230+"/",
        thumbnail="http://images.usatoday.com/life/_photos/2006/03/08/inside-stillstanding-riha.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tattletales",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_231+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/66/c9/93/66c993b17ba7001fd544b332cf20880b.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Taxi",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_232+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/f/f4/Taxi_title_screen.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Taxicab Confessions",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_233+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/82/78/81/82788160ba54851bc3ad47a1078aac55.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="That 70's Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_234+"/",
        thumbnail="http://www.impawards.com/tv/posters/that_seventies_show.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="That Mitchell and Webb Look",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_235+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51IFKcZK24L.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="That's My Mama",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_236+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/c3/56/f6/c356f628f7f923ee2dbe031d79a915ec.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The 11 O'Clock Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_237+"/",
        thumbnail="https://i.ytimg.com/vi/QfAeWJikaIY/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Abbott and Costello Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_238+"/",
        thumbnail="http://www.abbottandcostellofanclub.com/TVshowbig.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Adventures of Ozzie and Harriet",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_239+"/",
        thumbnail="http://www.sitcomsonline.com/nelsons.gif",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="The Amanda Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_240+"/",
        thumbnail="https://images-production.global.ssl.fastly.net/uploads/photos/file/200847/amanda-bynes.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Amazing Johnathan",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_241+"/",
        thumbnail="http://www.azquotes.com/public/pictures/authors/6e/1a/6e1ab5a56b01f4a637740658ccd99e49/5536024eaa3f4_the_amazing_johnathan.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="The Andy Griffith Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_242+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/610VL3ygHVL.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Benny Hill Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_243+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/d0/3f/08/d03f08dbd9a2fff408c04aa7966e0487.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Beverly Hillbillies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_244+"/",
        thumbnail="http://tvseriesfinale.com/assets/beverlyhillbillies04a.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Bill Cosby Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_245+"/",
        thumbnail="http://www.myinterestingfacts.com/wp-content/uploads/2013/06/Bill-Cosby-Facts.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Bob Cummings Show - Love That Bob",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_246+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/0a/bf/59/0abf595e5b9f76eee0941b368cf35b01.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Boondocks",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_247+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/53/08/45/530845288434b03099c827729df5ebc9.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Brady Bunch",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_248+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/8/8a/BradyBunchtitle.png",
        folder=True )           

    plugintools.add_item( 
        #action="", 
        title="The Brady Bunch Hour",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_249+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/M/MV5BMTQzOTU5NTM0Nl5BMl5BanBnXkFtZTcwMDI5MjAyMQ@@._V1_UY268_CR3,0,182,268_AL_.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="The Carbonaro Effect",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_250+"/",
        thumbnail="https://files.greatermedia.com/uploads/sites/28/2016/03/showposter.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Carol Burnett Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_251+"/",
        thumbnail="http://www.dvdtalk.com/reviews/images/reviews/103/1428495905_2.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Chris Gethard Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_252+"/",
        thumbnail="https://yt3.ggpht.com/-omCunSxX6RM/AAAAAAAAAAI/AAAAAAAAAAA/63gTUqABoUg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="The Colgate Comedy Hour",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_253+"/",
        thumbnail="http://4.bp.blogspot.com/_08zJqTvYq1A/TQg-jlzDVII/AAAAAAAAAiI/ua3iHplOCv8/s400/colgate1.png",
        folder=True )          
        
    plugintools.add_item( 
        #action="", 
        title="The Cosby Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_254+"/",
        thumbnail="http://www.eonline.com/resize/500/500//eol_images/Entire_Site/2011224/300.cosbyshow.lc.032411.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Danny Thomas Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_255+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/c9/d4/91/c9d4916161fcb2a5d916911fced3088a.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Dean Martin Celebrity Roasts",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_256+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/81Ofn0TOG2L._AC_UL320_SR226,320_.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="The Dick Van Dyke Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_257+"/",
        thumbnail="http://theredlist.com/media/database/films/tv-series/sitcom-and-soap/1960/the-dick-van-dyke-show/001-the-dick-van-dyke-show-theredlist.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Donna Reed Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_258+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/e6/60/59/e66059aedd20cad41c0da9d02d90578b.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Donny & Marie Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_259+"/",
        thumbnail="http://tvseriesfinale.com/assets/donnyandmarie03m.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="The Facts of Life",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_260+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/88/74/fb/8874fbec8753e39c7c56f9343b33b6f6.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Fast Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_261+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/a5/61/9e/a5619e37c5272a7af9bda2dae67c8141.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Fenn Street Gang",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_262+"/",
        thumbnail="https://static.episodate.com/images/tv-show/full/8734.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The George Burns and Gracie Allen Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_263+"/",
        thumbnail="https://travsd.files.wordpress.com/2013/07/tumblr_mdej4wy5511rkizano1_cover.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Ghost & Mrs. Muir",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_264+"/",
        thumbnail="http://bygonetv.com/shows/the_ghost_and_mrs_muir/images/credits.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Golden Girls",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_265+"/",
        thumbnail="http://multimedia.bbycastatic.ca/multimedia/products/500x500/m22/m2220/m2220104.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Golden Palace",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_266+"/",
        thumbnail="http://static.tvtropes.org/pmwiki/pub/images/AkjtOqLhZGoSOk6_3094.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Gong Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_267+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/df/77/c7/df77c747713cef9f48ab142732d04624.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Great Gildersleeve",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_268+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Great_Gildersleeve_1.jpg/200px-Great_Gildersleeve_1.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="The Hollywood Palace",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_269+"/",
        thumbnail="http://www.ioffer.com/img3/item/175/648/751/hollywood-palace-sammy-davis-engelbert-humperdinck-dvd-ca078.jpg",
        folder=True )           

    plugintools.add_item( 
        #action="", 
        title="The Honeymooners",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_270+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/34/75/c4/3475c444892dc77b68349e83ad38a7c9.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Inbetweeners",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_271+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/7a/4c/d3/7a4cd3c81e5f998baf6a8416f36197ca.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Jack Benny Program",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_272+"/",
        thumbnail="https://www.oldtimeradiodownloads.com/assets/img/serie/img_jack-benny-2.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Jamie Foxx Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_273+"/",
        thumbnail="https://i1.ytimg.com/sh/T7XV6WZFymk/showposter.jpg?v=53098137",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Jamie Kennedy Experiment",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_274+"/",
        thumbnail="http://s1.evcdn.com/images/edpborder500/I0-001/017/911/168-1.jpeg_/comedian-jamie-kennedy-68.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Jeffersons",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_275+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/71/2d/f2/712df25ac3c6ae3af60c60432a3778ce.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Jim Henson Hour",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_276+"/",
        thumbnail="http://vignette4.wikia.nocookie.net/muppet/images/4/4f/Jimhour.jpg/revision/latest?cb=20060712043048",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="The Kids in the Hall",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_277+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/e6/5f/fa/e65ffa9dc03837c2b7c4ae63f5cacfb7.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The King of Queens",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_278+"/",
        thumbnail="http://cdn.mamamia.com.au/wp/wp-content/uploads/gallery/tv-shows-that-have-gone-on-for-too-long/the-king-of-queens.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Larry Sanders Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_279+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/07/f9/3c/07f93c956fccd650752b212393ebf47e.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Life of Riley",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_280+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/3d/6c/09/3d6c099f6a80c272b8e55cf342b5ea9f.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Likely Lads",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_281+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/28/8a/62/288a627493052f515814156bddbd2ea2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Little Rascals - Our Gang",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_282+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/dc/39/fb/dc39fb4a880f7283c80ea47a18f558ee.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Liver Birds",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_283+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/67/3a/89/673a890135d9ad9575db26502e43976e.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Lost Saucer",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_284+"/",
        thumbnail="http://www.retrocrush.com/archive2004/buzzi/thelostsaucer.jpg",
        folder=True )        

    plugintools.add_item( 
        #action="", 
        title="The Lucy Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_285+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/51p8v9AM8JL.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Lucy–Desi Comedy Hour",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_286+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/M/MV5BMTU5NTczNjc4NF5BMl5BanBnXkFtZTcwNTU2OTIyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Many Loves of Dobie Gillis",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_287+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51Uq1dJkSBL.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Mike Douglas Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_288+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/M/MV5BMTgyMjg4NjExMl5BMl5BanBnXkFtZTcwMDA0NTI2MQ@@._V1_UY268_CR1,0,182,268_AL_.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="The Monkees",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_289+"/",
        thumbnail="https://www.mesaartscenter.com/sysimg/media-box-image-shows-performing-live-the-monkees-media-box-9147-image.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Monkees (more)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_290+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/5f/b1/69/5fb1697672816a2395d4d5e3907c58c2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Munsters",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_291+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/09/b7/dd/09b7ddebf9d283cec0fd300ffda42fc4.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Muppet Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_292+"/",
        thumbnail="http://vignette2.wikia.nocookie.net/muppet/images/3/33/Tms_logo_small_o.jpg/revision/latest/scale-to-width-down/300?cb=20120623165703",
        folder=True )           

    plugintools.add_item( 
        #action="", 
        title="The Nanny",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_293+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/3d/6c/35/3d6c35a647ec12d1fc1646890bfafbdf.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Office(UK)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_294+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/8a/39/f1/8a39f120d422ae7a19d480dfcf452c1a.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Partridge Family",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_295+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/61SGUY6zz-L._SS500.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Phil Silvers Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_296+"/",
        thumbnail="http://pdxretro.com/wp-content/uploads/2011/04/Philsilversshow_thumb.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Real McCoys",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_297+"/",
        thumbnail="https://userscontent2.emaze.com/images/20f6cafb-1921-4472-a31a-d66d3750f818/961d6e70722ea28b36fc46dcf144f8ce.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Red Green Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_298+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/2f/c3/cd/2fc3cdcb994b396d98d537c33a18d947.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Red Skelton Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_299+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/33/c7/8e/33c78e837858de4d7e1f143ac937dc34.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="The Fall and Rise of Reginald Perrin",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_300+"/",
        thumbnail="http://nostalgiacentral.com/wp-content/uploads/2014/06/regperrin_70c.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Graham Norton Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_301+"/",
        thumbnail="http://insidesouthaustralia.com.au/wp-content/uploads/2016/08/Blog508px-graham-norton.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Richard Pryor Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_302+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/51VGZBH70JL._SL500_AA300_.jpg",
        folder=True )   

    plugintools.add_item( 
        #action="", 
        title="The Ritz Brothers",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_303+"/",
        thumbnail="http://www.latimes.com/includes/projects/hollywood/portraits/the_ritz_brothers.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="The Ropers",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_304+"/",
        thumbnail="https://bittergertrude.files.wordpress.com/2014/07/mrsroper.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Simpsons",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_305+"/",
        thumbnail="http://www.copygeneralusa.com/images/bartsimpsonpictures.squarelogic.net/bart-simpson-01.gif",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Smothers Brothers Comedy Hour",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_306+"/",
        thumbnail="http://uploads.neatorama.com/images/posts/993/79/79993/1425257039-0.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Sonny & Cher Comedy Hour",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_307+"/",
        thumbnail="http://www.ioffer.com/img/item/103/728/411/HJAsAiWoxMqNSEJ.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Soupy Sales Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_308+"/",
        thumbnail="http://www.thewho.info/wfc/images/SoupyShow-LP.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="The Steve Harvey Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_309+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/a0/9f/cd/a09fcd7335735b16d9048a273d2e0123.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Suite Life of Zack and Cody",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_310+"/",
        thumbnail="http://az616578.vo.msecnd.net/files/2016/12/27/6361847667164392131233195090_suite%20life.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Thick of It",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_311+"/",
        thumbnail="https://image.tmdb.org/t/p/w185/xeDmkXIlO4lOQD2VA6HWrZ5x2nl.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Three Stooges",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_312+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/13/84/54/138454cb8f38c280f10064a5583aa1e6.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The Tonight Show Starring Johnny Carson",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_313+"/",
        thumbnail="http://media.hollywood.com/images/225x335/7284399.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="The Two Ronnies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_314+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/c0/53/5e/c0535eb968c4187bcf472534aad33dd5.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Vicar of Dibley",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_315+"/",
        thumbnail="http://www.episodedata.com/images/series/vicarofdibley.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Young Ones",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_316+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/8e/2f/88/8e2f8870f2e02fc873fddd461ee7b026.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="This Morning with Richard Not Judy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_317+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/TMWRNJ.jpg/250px-TMWRNJ.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Three's a Crowd",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_318+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/1c/3f/e6/1c3fe65609c68c18bcf7194b3bfaf97e.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Three's Company",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_319+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/9c/d6/45/9cd6451d3fc081f66b9447e22531ef24.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tia and Tamera",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_320+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/fb/67/54/fb67547567c4a0dd906ef36d076dd1bb.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Till Death Us Do Part",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_321+"/",
        thumbnail="http://www.dvdorchard.com.au/images/coverart/148460.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Time Gentlemen Please",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_322+"/",
        thumbnail="http://img.sharetv.com/shows/standard/time_gentlemen_please_uk.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="To Tell the Truth",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_323+"/",
        thumbnail="http://www.sitcomsonline.com/photopost/data/815/15585to-tell-the-truth-logo.jpg",
        folder=True )        

    plugintools.add_item( 
        #action="", 
        title="To the Manor Born",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_324+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/17/6a/0d/176a0db391e3f0537c4e791470445d2f.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Today's Funniest Clips",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_325+"/",
        thumbnail="https://i.ytimg.com/vi/FhjOPgRBWIE/maxresdefault.jpg",
        folder=True )         

    plugintools.add_item( 
        #action="", 
        title="Tom Goes To The Mayor",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_326+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/f7/97/7e/f7977e95fc1ed6de56576b602336a104.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Too Close for Comfort",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_327+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/f6/33/bd/f633bd3a0d777614ff4d806016ac87fa.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Tosh.0",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_328+"/",
        thumbnail="http://akns-images.eonline.com/eol_images/Entire_Site/2014311/rs_560x415-140411140601-1024.tosh.o.cm.41114.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Trailer Park Boys",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_329+"/",
        thumbnail="https://yt3.ggpht.com/KrN1dmu9PB_dd1wokh13glxAsVD4jYji-1D8VEhzvuJTbV9AIcA7RXdPQ_MqaVL53jrErbr4AQ=s900-nd-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Trigger Happy TV",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_330+"/",
        thumbnail="https://www.thesun.co.uk/wp-content/uploads/2016/10/nintchdbpict000135708474.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Twenty Twelve",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_331+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/originals/8c/9b/d2/8c9bd28ac54e81b83b2ca0ee0236063c.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Two Pints of Lager and a Packet of Crisps",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_332+"/",
        thumbnail="https://www.comedy.co.uk/images/library/comedies/300/t/two_pints_2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Undeclared",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_333+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/4c/32/03/4c3203518289404740d53f97407121d5.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Upright Citizens Brigade",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_334+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxOTk3NDUxN15BMl5BanBnXkFtZTcwNzMzNDQyMQ@@._V1_UY268_CR9,0,182,268_AL_.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Venture Bros.",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_335+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/c8/97/99/c89799ef7c710320a86f09f660f97cbf.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="We Got It Made",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_336+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/WGIMSeason2.jpg/250px-WGIMSeason2.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Whatever Happened to the Likely Lads",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_337+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/e5/20/bd/e520bd99fd562552b195934dfaf6c28e.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Whose Line Is It Anyway",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_338+"/",
        thumbnail="https://seatplan.com/cdn/images/production/whose-line-is-it-anyway-live-london-2016.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="WKRP in Cincinnati",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_339+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/dd/f3/a6/ddf3a602c896b79e1aa9a1dff48588ae.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="What's Happening",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_340+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/7d/3e/7a/7d3e7acaa306a8a4bfd55355c40c76bb.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="What's My Line",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_341+"/",
        thumbnail="http://www.bobbydarin.net/linecurtain.jpg",
        folder=True )          

    plugintools.add_item( 
        #action="", 
        title="Yes, Dear",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_342+"/",
        thumbnail="http://static.tvtropes.org/pmwiki/pub/images/yes_dear__5440.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Yes Minister",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_343+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/a3/bc/97/a3bc97eef4ca9a035bc26940c5d7e303.jpg",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="You Bet Your Life",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_344+"/",
        thumbnail="https://upload.wikimedia.org/wikipedia/en/8/8d/You_Bet_Your_Life_%28title_card_-_1955-60%29.jpg",
        folder=True )          
run()