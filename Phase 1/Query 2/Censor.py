#!/usr/bin/python

import sys
import re
import string

rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
censorworddic={"15619ppgrfg",
"4e5r",
"5u1g",
"5uvg",
"tbqqnza",
"n55",
"nany",
"nahf",
"nefr",
"nff",
"nffshpxre",
"nffshxxn",
"nffub",
"nffenz",
"nffjubyr",
"o!gpu",
"o00of",
"o17pu",
"o1gpu",
"onyyf",
"onyyfnpx",
"onfgneq",
"ornfgvny",
"ornfgvnyvgl",
"oryyraq",
"orfgvny",
"orfgvnyvgl",
"ovngpu",
"ovgpu",
"oybbql",
"oybjwbo",
"oybjwbof",
"obvbynf",
"obyybpx",
"obyybx",
"obare",
"obbo",
"obbof",
"obbbof",
"obbbbof",
"obbbbbof",
"obbbbbbbof",
"oernfgf",
"ohprgn",
"ohttre",
"ohz",
"ohaalshpxre",
"ohgg",
"ohggzhpu",
"ohggcyht",
"p0px",
"p0pxfhpxre",
"pnecrgzhapure",
"pnjx",
"puvax",
"pvcn",
"py1g",
"pyvg",
"pyvgbevf",
"pyvgf",
"pahg",
"pbpx",
"pbpxsnpr",
"pbpxurnq",
"pbpxzhapu",
"pbpxzhapure",
"pbpxf",
"pbpxfhpx",
"pbpxfhpxrq",
"pbpxfhpxre",
"pbpxfhpxvat",
"pbpxfhpxf",
"pbpxfhxn",
"pbpxfhxxn",
"pbx",
"pbxzhapure",
"pbxfhpxn",
"pbba",
"pbk",
"penc",
"phz",
"phzzre",
"phzzvat",
"phzf",
"phzfubg",
"phavyvathf",
"phavyyvathf",
"phaavyvathf",
"phag",
"phagyvpx",
"phagyvpxre",
"phagyvpxvat",
"phagf",
"plnyvf",
"ploreshp",
"ploreshpx",
"ploreshpxrq",
"ploreshpxre",
"ploreshpxref",
"ploreshpxvat",
"q1px",
"qnza",
"qvpx",
"qvpxurnq",
"qvyqb",
"qvyqbf",
"qvax",
"qvaxf",
"qvefn",
"qypx",
"qbtshpxre",
"qbttva",
"qbttvat",
"qbaxrlevoore",
"qbbfu",
"qhpur",
"qlxr",
"rwnphyngr",
"rwnphyngrq",
"rwnphyngrf",
"rwnphyngvat",
"rwnphyngvatf",
"rwnphyngvba",
"rwnxhyngr",
"s4aal",
"snt",
"snttvat",
"snttvgg",
"snttbg",
"snttf",
"sntbg",
"sntbgf",
"sntf",
"snaalsyncf",
"snaalshpxre",
"snall",
"sphx",
"sphxre",
"sphxvat",
"srpx",
"srpxre",
"srypuvat",
"sryyngr",
"sryyngvb",
"svatreshpx",
"svatreshpxrq",
"svatreshpxre",
"svatreshpxref",
"svatreshpxvat",
"svatreshpxf",
"svfgshpx",
"svfgshpxrq",
"svfgshpxre",
"svfgshpxref",
"svfgshpxvat",
"svfgshpxvatf",
"svfgshpxf",
"synatr",
"sbbx",
"sbbxre",
"shpx",
"shpxn",
"shpxrq",
"shpxre",
"shpxref",
"shpxurnq",
"shpxurnqf",
"shpxva",
"shpxvat",
"shpxvatf",
"shpxvatfuvgzbgureshpxre",
"shpxzr",
"shpxf",
"shpxjuvg",
"shpxjvg",
"shqtrcnpxre",
"shx",
"shxre",
"shxxre",
"shxxva",
"shxf",
"shxjuvg",
"shxjvg",
"shk",
"shk0e",
"tnatonat",
"tnatonatrq",
"tnatonatf",
"tnlfrk",
"tbngfr",
"uneqpberfrk",
"uryy",
"urfur",
"ubne",
"ubner",
"ubre",
"ubzb",
"uber",
"ubeavrfg",
"ubeal",
"ubgfrk",
"wnpxbss",
"wnc",
"wrex",
"wrexbss",
"wvfz",
"wvm",
"wvmz",
"wvmm",
"xnjx",
"xabo",
"xabornq",
"xaborq",
"xaboraq",
"xabournq",
"xabowbpxl",
"xabowbxrl",
"xbpx",
"xbaqhz",
"xbaqhzf",
"xhz",
"xhzzre",
"xhzzvat",
"xhzf",
"xhavyvathf",
"y3vpu",
"y3vgpu",
"ynovn",
"yznb",
"yzsnb",
"yhfg",
"yhfgvat",
"z0s0",
"z0sb",
"z45greongr",
"zn5greo8",
"zn5greongr",
"znfbpuvfg",
"znfgreo8",
"znfgreong",
"znfgreong3",
"znfgreongr",
"znfgreongvba",
"znfgreongvbaf",
"znfgheongr",
"zbs0",
"zbsb",
"zbgunshpx",
"zbgunshpxn",
"zbgunshpxnf",
"zbgunshpxnm",
"zbgunshpxrq",
"zbgunshpxre",
"zbgunshpxref",
"zbgunshpxva",
"zbgunshpxvat",
"zbgunshpxvatf",
"zbgunshpxf",
"zbgureshpx",
"zbgureshpxrq",
"zbgureshpxre",
"zbgureshpxref",
"zbgureshpxva,"
"zbgureshpxvat",
"zbgureshpxvatf",
"zbgureshpxxn",
"zbgureshpxf",
"zhss",
"zhgun",
"zhgunsrpxre",
"zhgunshpxxre",
"zhgure",
"zhgureshpxre",
"a1ttn",
"a1ttre",
"anmv",
"avtt3e",
"avtt4u",
"avttn",
"avttnu",
"avttnf",
"avttnm",
"avttre",
"avttref",
"abournq",
"abowbpxl",
"abowbxrl",
"ahzoahgf",
"ahgfnpx",
"bzt",
"c0ea",
"cnja"
"cravf",
"cravfshpxre",
"cubarfrk",
"cuhpx",
"cuhx",
"cuhxrq",
"cuhxvat",
"cuhxxrq",
"cuhxxvat",
"cuhxf",
"cuhd",
"cvtshpxre",
"cvzcvf",
"cvff",
"cvffre",
"cvffref",
"cvffrf",
"cvffsyncf",
"cvffva",
"cvffvat",
"cvffbss",
"cbbc",
"cevpx",
"cevpxf",
"ceba",
"chor",
"chffr",
"chffv",
"chffvrf",
"chffl",
"chfflf",
"dhrre",
"erpghz",
"evzwnj",
"evzzvat",
"fpuybat",
"fpebng",
"fpebgr",
"fpebghz",
"frzra",
"frk",
"fu!g",
"fu1g",
"fuvg",
"fuvgqvpx",
"fuvgr",
"fuvgrq",
"fuvgrl",
"fuvgshpx",
"fuvgshyy",
"fuvgurnq",
"fuvgvat",
"fuvgvatf",
"fuvgf",
"fuvggrq",
"fuvggre",
"fuvggref",
"fuvggvat",
"fuvggvatf",
"fuvggl",
"fxnax",
"fyhg",
"fzrtzn",
"fzhg",
"fangpu",
"fbabsnovgpu",
"fchax",
"grrgf",
"gvg",
"gvgshpx",
"gvggvrshpxre",
"gvggvrf",
"gvgglshpx",
"gvggljnax",
"gvgjnax",
"gbffre",
"gheq",
"gj4g",
"gjng",
"gjngurnq",
"gjnggl",
"gjhag",
"gjhagre",
"i14ten",
"i1ten",
"intvan",
"ivnten",
"ihyin",
"j00fr",
"jnat",
"jnax",
"jnaxre",
"jnaxl",
"jubne",
"juber",
"juber4e5r",
"jubernany",
"juberfuvg",
"jgss"}

dirtylist=[]

for key in censorworddic:
	word= string.translate(key,rot13); 
	dirtylist.append(word)
#for key in dirtylist:
#	print key

#start words from list
#word will be the word to check
if word in dirtylist:
	censoredword=word[0] + '*'*(len(word)-2) + word[-1]
	return censoredword
else:
	return word
