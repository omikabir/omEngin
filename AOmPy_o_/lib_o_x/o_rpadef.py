import pandas as pd

def zn_dic():
    zone = {'DHK_M':'','DHK_N':'','DHK_O':'','DHK_S':'','CTG_M':'','CTG_N':'','CTG_S':'','COM':'','NOA':'',
          'BAR':'','KHL':'','KUS':'','MYM':'','RAJ':'','RANG':'','SYL':''}
    return zone

def omdbdic():
    om = {'BAR':'BHBRN','BAR':'BHCFN','BAR':'BHDLT','BAR':'BHLMN','BAR':'BHMNP','BAR':'BHSDR','BAR':'BHTMN','BAR':'BRAMT','BAR':'BRBMN','BAR':'BRBTG','BAR':'BRPTG','BAR':'BRSDR','BAR':'BSAGL','BAR':'BSBBG','BAR':'BSBKG','BAR':'BSBNP','BAR':'BSGND','BAR':'BSHZL','BAR':'BSMDG','BAR':'BSMLD','BAR':'BSSDR','BAR':'BSWZP','BAR':'JKKTL','BAR':'JKNCT','BAR':'JKRZP','BAR':'JKSDR','BAR':'MDKLK','BAR':'MDRJR','BAR':'MDSDR','BAR':'MDSHB','BAR':'PPBND','BAR':'PPKKL','BAR':'PPMTB','BAR':'PPNSB','BAR':'PPNZP','BAR':'PPSDR','BAR':'PPZNG','BAR':'PTBFL','BAR':'PTDMK','BAR':'PTDMN','BAR':'PTGCP','BAR':'PTKLP','BAR':'PTMZG','BAR':'PTSDR','BAR':'SPBDG','BAR':'SPDMD','BAR':'SPGSR','BAR':'SPNRA','BAR':'SPSDR','BAR':'SPZNR','COM':'CMBMP','COM':'CMBRC','COM':'CMBRR','COM':'CMCND','COM':'CMDBD','COM':'CMDKN','COM':'CMHMN','COM':'CMLXM','COM':'CMMDN','COM':'CMMGN','COM':'CMMHG','COM':'CMNKT','COM':'CMSDD','COM':'CMSDR','COM':'CMTTS','COM':'CPFDG','COM':'CPHGN','COM':'CPHMC','COM':'CPKCH','COM':'CPMTB','COM':'CPSDR','COM':'CPSRT','COM':'CPUMT','CTG_M':'CGBAK','CTG_M':'CGBYZ','CTG_M':'CGCDG',
 'CTG_M':'CGDMG','CTG_M':'CGHLS','CTG_M':'CGKHL','CTG_M':'CGKTL','CTG_M':'CGPCH','CTG_M':'CGPRT','CTG_M':'CGPTG','CTG_M':'CGPTL','CTG_N':'CGFTK','CTG_N':'CGHTZ','CTG_N':'CGMIR','CTG_N':'CGRNG','CTG_N':'CGRZN','CTG_N':'CGSDP','CTG_N':'CGSKD','CTG_N':'KCDGN','CTG_N':'KCLXC','CTG_N':'KCMHC','CTG_N':'KCMKC','CTG_N':'KCMTR','CTG_N':'KCPNC','CTG_N':'KCRMG','CTG_N':'KCSDR','CTG_N':'RMBGC','CTG_N':'RMBLC','CTG_N':'RMBRK','CTG_N':'RMJCR','CTG_N':'RMKKL','CTG_N':'RMKPT','CTG_N':'RMLND','CTG_N':'RMNNC','CTG_N':'RMRTL','CTG_N':'RMSDR','CTG_S':'BBAKD','CTG_S':'BBLMA',
 'CTG_S':'BBNKC','CTG_S':'BBRMA','CTG_S':'BBRNC','CTG_S':'BBSDR','CTG_S':'BBTCI','CTG_S':'CGANW','CTG_S':'CGBLK','CTG_S':'CGBSK','CTG_S':'CGCND','CTG_S':'CGLHG','CTG_S':'CGPTA','CTG_S':'CGSKN','CTG_S':'CXCKR','CTG_S':'CXKTD','CTG_S':'CXMHK','CTG_S':'CXPKA','CTG_S':'CXRMU','CTG_S':'CXSDR','CTG_S':'CXTKN','CTG_S':'CXUKH','DHK_M':'DHADB','DHK_M':'DHBDD','DHK_M':'DHDHN','DHK_M':'DHGUL','DHK_M':'DHKHL','DHK_M':'DHKLB','DHK_M':'DHMDP','DHK_M':'DHMJH','DHK_M':'DHNMK','DHK_M':'DHPTN','DHK_M':'DHRMN','DHK_M':'DHRMP','DHK_M':'DHSBB','DHK_M':'DHSBG','DHK_M':'DHSBN','DHK_M':'DHTEJ','DHK_M':'DHTIA','DHK_N':'DHAPT','DHK_N':'DHDKK','DHK_N':'DHKKT','DHK_N':'DHTRG','DHK_N':'DHUTK','DHK_N':'DHUTT','DHK_N':'GPKLG','DHK_N':'GPKLK','DHK_N':'GPKPS','DHK_N':'GPSDR','DHK_N':'GPSRP','DHK_N':'NGARH','DHK_N':'NGRPG','DHK_N':'NSBLB','DHK_N':'NSMND','DHK_N':'NSPLS','DHK_N':'NSRPR','DHK_N':'NSSBP','DHK_N':'NSSDR',
 'DHK_O':'DHCNT','DHK_O':'DHDHM','DHK_O':'DHDHR','DHK_O':'DHDRS','DHK_O':'DHKCH','DHK_O':'DHKFR','DHK_O':'DHKGN','DHK_O':'DHMRP','DHK_O':'DHNWG','DHK_O':'DHPLB','DHK_O':'DHSHA','DHK_O':'DHSVR','DHK_O':'MGDLP','DHK_O':'MGGHR','DHK_O':'MGHRM','DHK_O':'MGSBL','DHK_O':'MGSDR','DHK_O':'MGSNG','DHK_O':'MGSTR','DHK_S':'DHBNS','DHK_S':'DHCKB','DHK_S':'DHDEM','DHK_S':'DHGND','DHK_S':'DHHZR','DHK_S':'DHJTB','DHK_S':'DHKDM','DHK_S':'DHKTL','DHK_S':'DHLLB','DHK_S':'DHSHM','DHK_S':'DHSTR','DHK_S':'MNGZR','DHK_S':'MNLHG','DHK_S':'MNSDR','DHK_S':'MNSRK','DHK_S':'MNSRN','DHK_S':'MNTGB','DHK_S':'NGBND','DHK_S':'NGSDR','DHK_S':'NGSNG','KHL':'BGCTL','KHL':'BGFKR','KHL':'BGKCH','KHL':'BGMLH','KHL':'BGMNG','KHL':'BGMRL','KHL':'BGRMP','KHL':'BGSDR','KHL':'BGSRN','KHL':'GGKOT','KHL':'GGKSN','KHL':'GGMKS','KHL':'GGSDR','KHL':'GGTNG','KHL':'JSABH','KHL':'JSBGH','KHL':'JSCGH','KHL':'JSJKR','KHL':'JSKSB','KHL':'JSMNR','KHL':'JSSDR','KHL':'JSSRS','KHL':'KHBTG','KHL':'KHDCP','KHL':'KHDGH','KHL':'KHDLP','KHL':'KHDMR','KHL':'KHKJA','KHL':'KHKLS','KHL':'KHKOY','KHL':'KHPHL',
 'KHL':'KHPKG','KHL':'KHRPS','KHL':'KHSDR','KHL':'KHSND','KHL':'KHTRK','KHL':'NRKLA','KHL':'NRLHG','KHL':'NRSDR','KHL':'SKASN','KHL':'SKDEB','KHL':'SKKLG','KHL':'SKKOL','KHL':'SKSDR','KHL':'SKSYM','KHL':'SKTLA','KUS':'CDALM','KUS':'CDDMH','KUS':'CDJBN','KUS':'CDSDR','KUS':'FPALF','KUS':'FPBHN','KUS':'FPBLM','KUS':'FPCBH','KUS':'FPMDH','KUS':'FPNGR','KUS':'FPSDR','KUS':'FPSLT','KUS':'FPSPR','KUS':'JHHRK','KUS':'JHKLG','KUS':'JHKOT','KUS':'JHMHS','KUS':'JHSDR','KUS':'JHSLK','KUS':'KUBRM','KUS':'KUDLP','KUS':'KUKKS','KUS':'KUKMK','KUS':'KUMRP','KUS':'KUSDR','KUS':'MAMDP','KUS':'MASDR','KUS':'MASLK','KUS':'MASRP','KUS':'MHGNG','KUS':'MHMJB','KUS':'MHSDR','KUS':'PBATG','KUS':'PBBER','KUS':'PBBNG','KUS':'PBCTM','KUS':'PBFRD','KUS':'PBISR','KUS':'PBSDR','KUS':'PBSNG','KUS':'PBSTH','KUS':'RJBLK','KUS':'RJGLN','KUS':'RJKLK',
 'KUS':'RJPNG','KUS':'RJSDR','MYM':'JPBKG','MYM':'JPDWG','MYM':'JPISL','MYM':'JPMDG','MYM':'JPMLN','MYM':'JPSDR','MYM':'JPSSB','MYM':'KGCRJ','MYM':'KGRMR','MYM':'KSBJT','MYM':'KSBRB','MYM':'KSHSN','MYM':'KSITN','MYM':'KSKLC','MYM':'KSKRM','MYM':'KSKTD','MYM':'KSMTM','MYM':'KSNKL','MYM':'KSOST','MYM':'KSPKN','MYM':'KSSDR','MYM':'KSTRL','MYM':'MYBLK','MYM':'MYDBR','MYM':'MYFLB','MYM':'MYFLP','MYM':'MYGFG','MYM':'MYGRP','MYM':'MYHLG','MYM':'MYISG','MYM':'MYMKT','MYM':'MYNND','MYM':'MYSDR','MYM':'MYTRL','MYM':'NKATP','MYM':'NKBRH','MYM':'NKDGP','MYM':'NKKLK','MYM':'NKKLZ','MYM':'NKKND','MYM':'NKMDN','MYM':'NKMHN','MYM':'NKPBD','MYM':'NKSDR','MYM':'SNDMP','MYM':'SRJNG','MYM':'SRNKL','MYM':'SRNLT','MYM':'SRSBD','MYM':'SRSDR','MYM':'TNBPR','MYM':'TNBSL','MYM':'TNDBR','MYM':'TNDDR','MYM':'TNGPL','MYM':'TNGTL','MYM':'TNKLH','MYM':'TNMDP','MYM':'TNMZP','MYM':'TNNGP','MYM':'TNSDR','MYM':'TNSKP','NOA':'CMCDG','NOA':'FNCGL','NOA':'FNDGN','NOA':'FNFGZ','NOA':'FNPRS','NOA':'FNSDR','NOA':'FNSNG','NOA':'LXKMN','NOA':'LXRGN','NOA':'LXRGT','NOA':'LXRPR','NOA':'LXSDR',
 'NOA':'NOBGM','NOA':'NOCMP','NOA':'NOCTK','NOA':'NOHTA','NOA':'NOKBH','NOA':'NOMJD','NOA':'NOSBC','NOA':'NOSNB','NOA':'NOSNM','RAJ':'BOADM','RAJ':'BODNT','RAJ':'BODPC','RAJ':'BOGBT','RAJ':'BOKHL','RAJ':'BONND','RAJ':'BOSBG','RAJ':'BOSDR','RAJ':'BOSJP','RAJ':'BOSNT','RAJ':'BOSRK','RAJ':'BOSRP','RAJ':'JYAKL','RAJ':'JYKLI','RAJ':'JYKTL','RAJ':'JYPBB','RAJ':'JYSDR','RAJ':'NAATR','RAJ':'NABGC','RAJ':'NADMR','RAJ':'NAMDB','RAJ':'NAMND','RAJ':'NANMT','RAJ':'NAPRS','RAJ':'NAPTN','RAJ':'NARNG','RAJ':'NASDR','RAJ':'NASPR','RAJ':'NTBGT','RAJ':'NTBRG','RAJ':'NTGDS','RAJ':'NTLLP','RAJ':'NTSDR','RAJ':'NTSNG','RAJ':'NWBLH','RAJ':'NWGMS','RAJ':'NWNCL','RAJ':'NWSBG','RAJ':'NWSDR','RAJ':'RSBGH','RAJ':'RSBGM','RAJ':'RSBLA','RAJ':'RSCGT','RAJ':'RSDGP','RAJ':'RSGDG','RAJ':'RSMHN','RAJ':'RSMHR','RAJ':'RSPBA','RAJ':'RSPTH','RAJ':'RSRJP','RAJ':'RSSMD','RAJ':'RSTNR','RAJ':'SGBKC','RAJ':'SGCHL','RAJ':'SGKMK','RAJ':'SGKZP','RAJ':'SGROY','RAJ':'SGSDR','RAJ':'SGSJP','RAJ':'SGTRS','RAJ':'SGULP','RANG':'DPBCG','RANG':'DPBRG',
 'RANG':'DPBRL','RANG':'DPBRM','RANG':'DPCRB','RANG':'DPFLB','RANG':'DPGRT','RANG':'DPHKM','RANG':'DPKHN','RANG':'DPKHR','RANG':'DPNWG','RANG':'DPPBT','RANG':'DPSDR','RANG':'GBFLC','RANG':'GBGBD','RANG':'GBPLS','RANG':'GBSDL','RANG':'GBSDR','RANG':'GBSGT','RANG':'GBSND','RANG':'KGBRM','RANG':'KGCLM','RANG':'KGFLB','RANG':'KGNGS','RANG':'KGRJR','RANG':'KGSDR','RANG':'KGULP','RANG':'LMADT','RANG':'LMHTB','RANG':'LMKLG','RANG':'LMPTG','RANG':'LMSDR','RANG':'NPDML','RANG':'NPDMR','RANG':'NPJLD','RANG':'NPKSG','RANG':'NPSDP','RANG':'NPSDR','RANG':'PGATR','RANG':'PGBDA','RANG':'PGDBG','RANG':'PGSDR','RANG':'PGTTL','RANG':'RPBDG','RANG':'RPGNG','RANG':'RPKAU','RANG':'RPMTH','RANG':'RPPGC','RANG':'RPPGN','RANG':'RPSDR','RANG':'RPTRG','RANG':'TGBLD','RANG':'TGHRP','RANG':'TGPGN','RANG':'TGRSN','RANG':'TGSDR','SYL':'BMAKH','SYL':'BMASG','SYL':'BMBJN','SYL':'BMBNC','SYL':'BMKSB','SYL':'BMNBG','SYL':'BMNNG','SYL':'BMSDR','SYL':'BMSRL','SYL':'HGAZM','SYL':'HGBBL','SYL':'HGBNC','SYL':'HGCNR','SYL':'HGLKH','SYL':'HGMDB',
 'SYL':'HGNBG','SYL':'HGSDR','SYL':'MBBRL','SYL':'MBJRI','SYL':'MBKLR','SYL':'MBKML','SYL':'MBRZN','SYL':'MBSDR','SYL':'MBSML','SYL':'SNBSM','SYL':'SNCTK','SYL':'SNDKS','SYL':'SNDRB','SYL':'SNDRI','SYL':'SNJGN','SYL':'SNJML','SYL':'SNSDR','SYL':'SNSLA','SYL':'SNTHP','SYL':'SYBLG','SYL':'SYBNB','SYL':'SYBSW','SYL':'SYCMP','SYL':'SYDKS','SYL':'SYFNC','SYL':'SYGLP','SYL':'SYGWN','SYL':'SYJNT','SYL':'SYKNG','SYL':'SYSDR','SYL':'SYZKG'}
    return om

def scode():
    lss = ['BHBRN','BHCFN','BHDLT','BHLMN','BHMNP','BHSDR','BHTMN','BRAMT','BRBMN','BRBTG','BRPTG','BRSDR','BSAGL',
'BSBBG','BSBKG','BSBNP','BSGND','BSHZL','BSMDG','BSMLD','BSSDR','BSWZP','JKKTL','JKNCT','JKRZP','JKSDR',
'MDKLK','MDRJR','MDSDR','MDSHB','PPBND','PPKKL','PPMTB','PPNSB','PPNZP','PPSDR','PPZNG','PTBFL','PTDMK',
'PTDMN','PTGCP','PTKLP','PTMZG','PTSDR','SPBDG','SPDMD','SPGSR','SPNRA','SPSDR','SPZNR','CMBMP','CMBRC',
'CMBRR','CMCND','CMDBD','CMDKN','CMHMN','CMLXM','CMMDN','CMMGN','CMMHG','CMNKT','CMSDD','CMSDR','CMTTS',
'CPFDG','CPHGN','CPHMC','CPKCH','CPMTB','CPSDR','CPSRT','CPUMT','CGBAK','CGBYZ','CGCDG','CGDMG','CGHLS',
'CGKHL','CGKTL','CGPCH','CGPRT','CGPTG','CGPTL','CGFTK','CGHTZ','CGMIR','CGRNG','CGRZN','CGSDP','CGSKD',
'KCDGN','KCLXC','KCMHC','KCMKC','KCMTR','KCPNC','KCRMG','KCSDR','RMBGC','RMBLC','RMBRK','RMJCR','RMKKL',
'RMKPT','RMLND','RMNNC','RMRTL','RMSDR','BBAKD','BBLMA','BBNKC','BBRMA','BBRNC','BBSDR','BBTCI','CGANW',
'CGBLK','CGBSK','CGCND','CGLHG','CGPTA','CGSKN','CXCKR','CXKTD','CXMHK','CXPKA','CXRMU','CXSDR','CXTKN',
'CXUKH','DHADB','DHBDD','DHDHN','DHGUL','DHKHL','DHKLB','DHMDP','DHMJH','DHNMK','DHPTN','DHRMN','DHRMP',
'DHSBB','DHSBG','DHSBN','DHTEJ','DHTIA','DHAPT','DHDKK','DHKKT','DHTRG','DHUTK','DHUTT','GPKLG','GPKLK',
'GPKPS','GPSDR','GPSRP','NGARH','NGRPG','NSBLB','NSMND','NSPLS','NSRPR','NSSBP','NSSDR','DHCNT','DHDHM',
'DHDHR','DHDRS','DHKCH','DHKFR','DHKGN','DHMRP','DHNWG','DHPLB','DHSHA','DHSVR','MGDLP','MGGHR','MGHRM',
'MGSBL','MGSDR','MGSNG','MGSTR','DHBNS','DHCKB','DHDEM','DHGND','DHHZR','DHJTB','DHKDM','DHKTL','DHLLB',
'DHSHM','DHSTR','MNGZR','MNLHG','MNSDR','MNSRK','MNSRN','MNTGB','NGBND','NGSDR','NGSNG','BGCTL','BGFKR',
'BGKCH','BGMLH','BGMNG','BGMRL','BGRMP','BGSDR','BGSRN','GGKOT','GGKSN','GGMKS','GGSDR','GGTNG','JSABH',
'JSBGH','JSCGH','JSJKR','JSKSB','JSMNR','JSSDR','JSSRS','KHBTG','KHDCP','KHDGH','KHDLP','KHDMR','KHKJA',
'KHKLS','KHKOY','KHPHL','KHPKG','KHRPS','KHSDR','KHSND','KHTRK','NRKLA','NRLHG','NRSDR','SKASN','SKDEB','SKKLG',
'SKKOL','SKSDR','SKSYM','SKTLA','CDALM','CDDMH','CDJBN','CDSDR','FPALF','FPBHN',
'FPBLM','FPCBH','FPMDH','FPNGR','FPSDR','FPSLT','FPSPR','JHHRK','JHKLG','JHKOT','JHMHS','JHSDR','JHSLK',
'KUBRM','KUDLP','KUKKS','KUKMK','KUMRP','KUSDR','MAMDP','MASDR','MASLK','MASRP','MHGNG','MHMJB','MHSDR',
'PBATG','PBBER','PBBNG','PBCTM','PBFRD','PBISR','PBSDR','PBSNG','PBSTH','RJBLK','RJGLN','RJKLK','RJPNG',
'RJSDR','JPBKG','JPDWG','JPISL','JPMDG','JPMLN','JPSDR','JPSSB','KGCRJ','KGRMR','KSBJT','KSBRB','KSHSN',
'KSITN','KSKLC','KSKRM','KSKTD','KSMTM','KSNKL','KSOST','KSPKN','KSSDR','KSTRL','MYBLK','MYDBR','MYFLB',
'MYFLP','MYGFG','MYGRP','MYHLG','MYISG','MYMKT','MYNND','MYSDR','MYTRL','NKATP','NKBRH','NKDGP','NKKLK',
'NKKLZ','NKKND','NKMDN','NKMHN','NKPBD','NKSDR','SNDMP','SRJNG','SRNKL','SRNLT','SRSBD','SRSDR','TNBPR',
'TNBSL','TNDBR','TNDDR','TNGPL','TNGTL','TNKLH','TNMDP','TNMZP','TNNGP','TNSDR','TNSKP','CMCDG','FNCGL',
'FNDGN','FNFGZ','FNPRS','FNSDR','FNSNG','LXKMN','LXRGN','LXRGT','LXRPR','LXSDR','NOBGM','NOCMP','NOCTK',
'NOHTA','NOKBH','NOMJD','NOSBC','NOSNB','NOSNM','BOADM','BODNT','BODPC','BOGBT','BOKHL','BONND','BOSBG',
'BOSDR','BOSJP','BOSNT','BOSRK','BOSRP','JYAKL','JYKLI','JYKTL','JYPBB','JYSDR','NAATR','NABGC','NADMR',
'NAMDB','NAMND','NANMT','NAPRS','NAPTN','NARNG','NASDR','NASPR','NTBGT','NTBRG','NTGDS','NTLLP','NTSDR',
'NTSNG','NWBLH','NWGMS','NWNCL','NWSBG','NWSDR','RSBGH','RSBGM','RSBLA','RSCGT','RSDGP','RSGDG','RSMHN',
'RSMHR','RSPBA','RSPTH','RSRJP','RSSMD','RSTNR','SGBKC','SGCHL','SGKMK','SGKZP','SGROY','SGSDR','SGSJP',
'SGTRS','SGULP','DPBCG','DPBRG','DPBRL','DPBRM','DPCRB','DPFLB','DPGRT','DPHKM','DPKHN','DPKHR','DPNWG',
'DPPBT','DPSDR','GBFLC','GBGBD','GBPLS','GBSDL','GBSDR','GBSGT','GBSND','KGBRM','KGCLM','KGFLB','KGNGS',
'KGRJR','KGSDR','KGULP','LMADT','LMHTB','LMKLG','LMPTG','LMSDR','NPDML','NPDMR','NPJLD','NPKSG','NPSDP',
'NPSDR','PGATR','PGBDA','PGDBG','PGSDR','PGTTL','RPBDG','RPGNG','RPKAU','RPMTH','RPPGC','RPPGN','RPSDR',
'RPTRG','TGBLD','TGHRP','TGPGN','TGRSN','TGSDR','BMAKH','BMASG','BMBJN','BMBNC','BMKSB','BMNBG','BMNNG',
'BMSDR','BMSRL','HGAZM','HGBBL','HGBNC','HGCNR','HGLKH','HGMDB','HGNBG','HGSDR','MBBRL','MBJRI','MBKLR',
'MBKML','MBRZN','MBSDR','MBSML','SNBSM','SNCTK','SNDKS','SNDRB','SNDRI','SNJGN','SNJML','SNSDR','SNSLA',
'SNTHP','SYBLG','SYBNB','SYBSW','SYCMP','SYDKS','SYFNC','SYGLP','SYGWN','SYJNT','SYKNG','SYSDR','SYZKG']
    return lss

def chrstream():
    sx = """91,42,42,42,42,42,42,95,95,95,95,42,42,95,95,42,42,95,95,42,42,32,95,42,42,32,42,42,42,42,42,42,42,33
42,42,42,42,42,32,47,32,95,95,32,92,124,32,32,92,47,32,32,124,42,124,32,124,42,42,42,42,42,42,42,42,42,33
42,42,42,42,42,124,32,124,32,32,124,32,124,32,92,32,32,47,32,124,42,124,32,124,42,42,42,42,42,42,42,42,42,33
42,42,42,42,42,124,32,124,32,32,124,32,124,32,124,92,47,124,32,124,42,124,32,124,42,42,42,42,42,42,42,42,42,33
42,42,42,42,42,124,32,124,95,95,124,32,124,32,124,32,32,124,32,124,42,124,32,124,42,42,42,42,42,42,42,42,42,33
42,42,42,42,42,42,92,95,95,95,95,47,92,95,124,42,42,124,95,124,42,124,95,124,42,42,42,42,42,42,42,42,93,33"""
    return sx

def omdb():
    dc = {'BHBRN':'BAR','BHCFN':'BAR','BHDLT':'BAR','BHLMN':'BAR','BHMNP':'BAR','BHSDR':'BAR','BHTMN':'BAR','BRAMT':'BAR','BRBMN':'BAR','BRBTG':'BAR','BRPTG':'BAR',
'BRSDR':'BAR','BSAGL':'BAR','BSBBG':'BAR','BSBKG':'BAR','BSBNP':'BAR','BSGND':'BAR','BSHZL':'BAR','BSMDG':'BAR','BSMLD':'BAR','BSSDR':'BAR','BSWZP':'BAR',
'JKKTL':'BAR','JKNCT':'BAR','JKRZP':'BAR','JKSDR':'BAR','MDKLK':'BAR','MDRJR':'BAR','MDSDR':'BAR','MDSHB':'BAR','PPBND':'BAR','PPKKL':'BAR','PPMTB':'BAR',
'PPNSB':'BAR','PPNZP':'BAR','PPSDR':'BAR','PPZNG':'BAR','PTBFL':'BAR','PTDMK':'BAR','PTDMN':'BAR','PTGCP':'BAR','PTKLP':'BAR','PTMZG':'BAR','PTSDR':'BAR',
'SPBDG':'BAR','SPDMD':'BAR','SPGSR':'BAR','SPNRA':'BAR','SPSDR':'BAR','SPZNR':'BAR','CMBMP':'COM','CMBRC':'COM','CMBRR':'COM','CMCND':'COM','CMDBD':'COM',
'CMDKN':'COM','CMHMN':'COM','CMLXM':'COM','CMMDN':'COM','CMMGN':'COM','CMMHG':'COM','CMNKT':'COM','CMSDD':'COM','CMSDR':'COM','CMTTS':'COM','CPFDG':'COM',
'CPHGN':'COM','CPHMC':'COM','CPKCH':'COM','CPMTB':'COM','CPSDR':'COM','CPSRT':'COM','CPUMT':'COM','CGBAK':'CTG_M','CGBYZ':'CTG_M','CGCDG':'CTG_M',
'CGDMG':'CTG_M','CGHLS':'CTG_M','CGKHL':'CTG_M','CGKTL':'CTG_M','CGPCH':'CTG_M','CGPRT':'CTG_M','CGPTG':'CTG_M','CGPTL':'CTG_M','CGFTK':'CTG_N',
'CGHTZ':'CTG_N','CGMIR':'CTG_N','CGRNG':'CTG_N','CGRZN':'CTG_N','CGSDP':'CTG_N','CGSKD':'CTG_N','KCDGN':'CTG_N','KCLXC':'CTG_N','KCMHC':'CTG_N',
'KCMKC':'CTG_N','KCMTR':'CTG_N','KCPNC':'CTG_N','KCRMG':'CTG_N','KCSDR':'CTG_N','RMBGC':'CTG_N','RMBLC':'CTG_N','RMBRK':'CTG_N','RMJCR':'CTG_N',
'RMKKL':'CTG_N','RMKPT':'CTG_N','RMLND':'CTG_N','RMNNC':'CTG_N','RMRTL':'CTG_N','RMSDR':'CTG_N','BBAKD':'CTG_S','BBLMA':'CTG_S','BBNKC':'CTG_S',
'BBRMA':'CTG_S','BBRNC':'CTG_S','BBSDR':'CTG_S','BBTCI':'CTG_S','CGANW':'CTG_S','CGBLK':'CTG_S','CGBSK':'CTG_S','CGCND':'CTG_S','CGLHG':'CTG_S',
'CGPTA':'CTG_S','CGSKN':'CTG_S','CXCKR':'CTG_S','CXKTD':'CTG_S','CXMHK':'CTG_S','CXPKA':'CTG_S','CXRMU':'CTG_S','CXSDR':'CTG_S','CXTKN':'CTG_S',
'CXUKH':'CTG_S','DHADB':'DHK_M','DHBDD':'DHK_M','DHDHN':'DHK_M','DHGUL':'DHK_M','DHKHL':'DHK_M','DHKLB':'DHK_M','DHMDP':'DHK_M','DHMJH':'DHK_M',
'DHNMK':'DHK_M','DHPTN':'DHK_M','DHRMN':'DHK_M','DHRMP':'DHK_M','DHSBB':'DHK_M','DHSBG':'DHK_M','DHSBN':'DHK_M','DHTEJ':'DHK_M','DHTIA':'DHK_M',
'DHAPT':'DHK_N','DHDKK':'DHK_N','DHKKT':'DHK_N','DHTRG':'DHK_N','DHUTK':'DHK_N','DHUTT':'DHK_N','GPKLG':'DHK_N','GPKLK':'DHK_N','GPKPS':'DHK_N',
'GPSDR':'DHK_N','GPSRP':'DHK_N','NGARH':'DHK_N','NGRPG':'DHK_N','NSBLB':'DHK_N','NSMND':'DHK_N','NSPLS':'DHK_N','NSRPR':'DHK_N','NSSBP':'DHK_N',
'NSSDR':'DHK_N','DHCNT':'DHK_O','DHDHM':'DHK_O','DHDHR':'DHK_O','DHDRS':'DHK_O','DHKCH':'DHK_O','DHKFR':'DHK_O','DHKGN':'DHK_O','DHMRP':'DHK_O',
'DHNWG':'DHK_O','DHPLB':'DHK_O','DHSHA':'DHK_O','DHSVR':'DHK_O','MGDLP':'DHK_O','MGGHR':'DHK_O','MGHRM':'DHK_O','MGSBL':'DHK_O','MGSDR':'DHK_O',
'MGSNG':'DHK_O','MGSTR':'DHK_O','DHBNS':'DHK_S','DHCKB':'DHK_S','DHDEM':'DHK_S','DHGND':'DHK_S','DHHZR':'DHK_S','DHJTB':'DHK_S','DHKDM':'DHK_S',
'DHKTL':'DHK_S','DHLLB':'DHK_S','DHSHM':'DHK_S','DHSTR':'DHK_S','MNGZR':'DHK_S','MNLHG':'DHK_S','MNSDR':'DHK_S','MNSRK':'DHK_S','MNSRN':'DHK_S',
'MNTGB':'DHK_S','NGBND':'DHK_S','NGSDR':'DHK_S','NGSNG':'DHK_S','BGCTL':'KHL','BGFKR':'KHL','BGKCH':'KHL','BGMLH':'KHL','BGMNG':'KHL','BGMRL':'KHL',
'BGRMP':'KHL','BGSDR':'KHL','BGSRN':'KHL','GGKOT':'KHL','GGKSN':'KHL','GGMKS':'KHL','GGSDR':'KHL','GGTNG':'KHL','JSABH':'KHL','JSBGH':'KHL',
'JSCGH':'KHL','JSJKR':'KHL','JSKSB':'KHL','JSMNR':'KHL','JSSDR':'KHL','JSSRS':'KHL','KHBTG':'KHL','KHDCP':'KHL','KHDGH':'KHL','KHDLP':'KHL',
'KHDMR':'KHL','KHKJA':'KHL','KHKLS':'KHL','KHKOY':'KHL','KHPHL':'KHL','KHPKG':'KHL','KHRPS':'KHL','KHSDR':'KHL','KHSND':'KHL','KHTRK':'KHL',
'NRKLA':'KHL','NRLHG':'KHL','NRSDR':'KHL','SKASN':'KHL','SKDEB':'KHL','SKKLG':'KHL','SKKOL':'KHL','SKSDR':'KHL','SKSYM':'KHL','SKTLA':'KHL',
'CDALM':'KUS','CDDMH':'KUS','CDJBN':'KUS','CDSDR':'KUS','FPALF':'KUS','FPBHN':'KUS','FPBLM':'KUS','FPCBH':'KUS','FPMDH':'KUS','FPNGR':'KUS',
'FPSDR':'KUS','FPSLT':'KUS','FPSPR':'KUS','JHHRK':'KUS','JHKLG':'KUS','JHKOT':'KUS','JHMHS':'KUS','JHSDR':'KUS','JHSLK':'KUS','KUBRM':'KUS',
'KUDLP':'KUS','KUKKS':'KUS','KUKMK':'KUS','KUMRP':'KUS','KUSDR':'KUS','MAMDP':'KUS','MASDR':'KUS','MASLK':'KUS','MASRP':'KUS','MHGNG':'KUS',
'MHMJB':'KUS','MHSDR':'KUS','PBATG':'KUS','PBBER':'KUS','PBBNG':'KUS','PBCTM':'KUS','PBFRD':'KUS','PBISR':'KUS','PBSDR':'KUS','PBSNG':'KUS',
'PBSTH':'KUS','RJBLK':'KUS','RJGLN':'KUS','RJKLK':'KUS','RJPNG':'KUS','RJSDR':'KUS','JPBKG':'MYM','JPDWG':'MYM','JPISL':'MYM','JPMDG':'MYM',
'JPMLN':'MYM','JPSDR':'MYM','JPSSB':'MYM','KGCRJ':'MYM','KGRMR':'MYM','KSBJT':'MYM','KSBRB':'MYM','KSHSN':'MYM','KSITN':'MYM','KSKLC':'MYM',
'KSKRM':'MYM','KSKTD':'MYM','KSMTM':'MYM','KSNKL':'MYM','KSOST':'MYM','KSPKN':'MYM','KSSDR':'MYM','KSTRL':'MYM','MYBLK':'MYM','MYDBR':'MYM',
'MYFLB':'MYM','MYFLP':'MYM','MYGFG':'MYM','MYGRP':'MYM','MYHLG':'MYM','MYISG':'MYM','MYMKT':'MYM','MYNND':'MYM','MYSDR':'MYM','MYTRL':'MYM',
'NKATP':'MYM','NKBRH':'MYM','NKDGP':'MYM','NKKLK':'MYM','NKKLZ':'MYM','NKKND':'MYM','NKMDN':'MYM','NKMHN':'MYM','NKPBD':'MYM','NKSDR':'MYM',
'SNDMP':'MYM','SRJNG':'MYM','SRNKL':'MYM','SRNLT':'MYM','SRSBD':'MYM','SRSDR':'MYM','TNBPR':'MYM','TNBSL':'MYM','TNDBR':'MYM','TNDDR':'MYM',
'TNGPL':'MYM','TNGTL':'MYM','TNKLH':'MYM','TNMDP':'MYM','TNMZP':'MYM','TNNGP':'MYM','TNSDR':'MYM','TNSKP':'MYM','CMCDG':'NOA','FNCGL':'NOA',
'FNDGN':'NOA','FNFGZ':'NOA','FNPRS':'NOA','FNSDR':'NOA','FNSNG':'NOA','LXKMN':'NOA','LXRGN':'NOA','LXRGT':'NOA','LXRPR':'NOA','LXSDR':'NOA',
'NOBGM':'NOA','NOCMP':'NOA','NOCTK':'NOA','NOHTA':'NOA','NOKBH':'NOA','NOMJD':'NOA','NOSBC':'NOA','NOSNB':'NOA','NOSNM':'NOA','BOADM':'RAJ',
'BODNT':'RAJ','BODPC':'RAJ','BOGBT':'RAJ','BOKHL':'RAJ','BONND':'RAJ','BOSBG':'RAJ','BOSDR':'RAJ','BOSJP':'RAJ','BOSNT':'RAJ','BOSRK':'RAJ',
'BOSRP':'RAJ','JYAKL':'RAJ','JYKLI':'RAJ','JYKTL':'RAJ','JYPBB':'RAJ','JYSDR':'RAJ','NAATR':'RAJ','NABGC':'RAJ','NADMR':'RAJ','NAMDB':'RAJ',
'NAMND':'RAJ','NANMT':'RAJ','NAPRS':'RAJ','NAPTN':'RAJ','NARNG':'RAJ','NASDR':'RAJ','NASPR':'RAJ','NTBGT':'RAJ','NTBRG':'RAJ','NTGDS':'RAJ',
'NTLLP':'RAJ','NTSDR':'RAJ','NTSNG':'RAJ','NWBLH':'RAJ','NWGMS':'RAJ','NWNCL':'RAJ','NWSBG':'RAJ','NWSDR':'RAJ','RSBGH':'RAJ','RSBGM':'RAJ',
'RSBLA':'RAJ','RSCGT':'RAJ','RSDGP':'RAJ','RSGDG':'RAJ','RSMHN':'RAJ','RSMHR':'RAJ','RSPBA':'RAJ','RSPTH':'RAJ','RSRJP':'RAJ','RSSMD':'RAJ',
'RSTNR':'RAJ','SGBKC':'RAJ','SGCHL':'RAJ','SGKMK':'RAJ','SGKZP':'RAJ','SGROY':'RAJ','SGSDR':'RAJ','SGSJP':'RAJ','SGTRS':'RAJ','SGULP':'RAJ',
'DPBCG':'RANG','DPBRG':'RANG','DPBRL':'RANG','DPBRM':'RANG','DPCRB':'RANG','DPFLB':'RANG','DPGRT':'RANG','DPHKM':'RANG','DPKHN':'RANG',
'DPKHR':'RANG','DPNWG':'RANG','DPPBT':'RANG','DPSDR':'RANG','GBFLC':'RANG','GBGBD':'RANG','GBPLS':'RANG','GBSDL':'RANG','GBSDR':'RANG',
'GBSGT':'RANG','GBSND':'RANG','KGBRM':'RANG','KGCLM':'RANG','KGFLB':'RANG','KGNGS':'RANG','KGRJR':'RANG','KGSDR':'RANG','KGULP':'RANG',
'LMADT':'RANG','LMHTB':'RANG','LMKLG':'RANG','LMPTG':'RANG','LMSDR':'RANG','NPDML':'RANG','NPDMR':'RANG','NPJLD':'RANG','NPKSG':'RANG',
'NPSDP':'RANG','NPSDR':'RANG','PGATR':'RANG','PGBDA':'RANG','PGDBG':'RANG','PGSDR':'RANG','PGTTL':'RANG','RPBDG':'RANG','RPGNG':'RANG',
'RPKAU':'RANG','RPMTH':'RANG','RPPGC':'RANG','RPPGN':'RANG','RPSDR':'RANG','RPTRG':'RANG','TGBLD':'RANG','TGHRP':'RANG','TGPGN':'RANG',
'TGRSN':'RANG','TGSDR':'RANG','BMAKH':'SYL','BMASG':'SYL','BMBJN':'SYL','BMBNC':'SYL','BMKSB':'SYL','BMNBG':'SYL','BMNNG':'SYL','BMSDR':'SYL',
'BMSRL':'SYL','HGAZM':'SYL','HGBBL':'SYL','HGBNC':'SYL','HGCNR':'SYL','HGLKH':'SYL','HGMDB':'SYL','HGNBG':'SYL','HGSDR':'SYL','MBBRL':'SYL',
'MBJRI':'SYL','MBKLR':'SYL','MBKML':'SYL','MBRZN':'SYL','MBSDR':'SYL','MBSML':'SYL','SNBSM':'SYL','SNCTK':'SYL','SNDKS':'SYL','SNDRB':'SYL',
'SNDRI':'SYL','SNJGN':'SYL','SNJML':'SYL','SNSDR':'SYL','SNSLA':'SYL','SNTHP':'SYL','SYBLG':'SYL','SYBNB':'SYL','SYBSW':'SYL','SYCMP':'SYL',
'SYDKS':'SYL','SYFNC':'SYL','SYGLP':'SYL','SYGWN':'SYL','SYJNT':'SYL','SYKNG':'SYL','SYSDR':'SYL','SYZKG':'SYL'}
    df = pd.DataFrame(list(dc.items()),columns = ['sCode','sZone'])
    return df


TS = lambda x : '2G' if ('2G SITE DOWN' in x) \
                else ('3G' if ('3G SITE DOWN' in x) \
                else ('4G' if ('4G SITE DOWN' in x) \
                else ('MF' if ('MAIN' in x) \
                else ('DL' if ('VOLTAGE' in x) \
                else ('TM' if ('TEMPERATURE' in x) \
                else ('SM' if ('SMOKE' in x) \
                else ('GN' if ('GEN' in x) \
                else ('GN' if ('GENSET' in x) \
                else ('TH' if ('THEFT' in x) \
                else ('C2G' if ('2G CELL DOWN' in x) \
                else ('C3G' if ('3G CELL DOWN' in x) \
                else ('C4G' if ('4G CELL DOWN' in x) \
                else ('DOOR' if ('DOOR' in x) \
                else "NA")))))))))))))
