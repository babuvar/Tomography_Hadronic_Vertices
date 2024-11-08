#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json



#---------------------------------------------------------------
#-------------------    Real Data   ----------------------------
#---------------------------------------------------------------

exp='e0010'; energy='4S'


runlist = ['r03129', 'r03130', 'r03131', 'r03132', 'r03133', 'r03134', 'r03135', 'r03137', 'r03138', 'r03142', 'r03233', 'r03234', 'r03235', 'r03236', 'r03237', 'r03238', 'r03239', 'r03396', 'r03397', 'r03398', 'r03399', 'r03400', 'r03401', 'r03402', 'r03403', 'r03405', 'r03492', 'r03493', 'r03504', 'r03505', 'r03506', 'r03507', 'r03508', 'r03509', 'r03510', 'r03511', 'r03516', 'r03517', 'r03518', 'r03549', 'r03551', 'r03553', 'r03559', 'r03560', 'r03561', 'r03562', 'r03563', 'r03564', 'r03565', 'r03570', 'r03605', 'r03606', 'r03607', 'r03609', 'r03611', 'r03612', 'r03613', 'r03614', 'r03615', 'r03617', 'r03618', 'r03619', 'r03620', 'r03621', 'r03622', 'r03623', 'r03624', 'r03625', 'r03626', 'r03627', 'r03629', 'r03649', 'r03651', 'r03654', 'r03659', 'r03660', 'r03661', 'r03662', 'r03663', 'r03705', 'r03706', 'r03707', 'r03708', 'r03709', 'r03711', 'r03728', 'r03729', 'r03734', 'r03736', 'r03737', 'r03738', 'r03739', 'r03740', 'r03741', 'r03743', 'r03744', 'r03745', 'r03746', 'r03747', 'r03748', 'r03749', 'r03750', 'r03751', 'r03754', 'r03759', 'r03760', 'r03761', 'r03766', 'r03768', 'r03770', 'r03771', 'r03774', 'r03775', 'r03776', 'r03777', 'r03787', 'r03789', 'r03790', 'r03792', 'r03793', 'r03795', 'r03796', 'r03847', 'r03850', 'r03851', 'r03852', 'r03853', 'r03855', 'r03856', 'r03857', 'r03858', 'r03859', 'r03860', 'r03864', 'r03865', 'r03867', 'r03868', 'r03869', 'r03932', 'r03933', 'r03935', 'r03936', 'r03937', 'r03938', 'r03939', 'r03940', 'r03941', 'r03942', 'r03943', 'r03944', 'r03945', 'r03946', 'r04110', 'r04111', 'r04113', 'r04114', 'r04164', 'r04165', 'r04166', 'r04167', 'r04168', 'r04169', 'r04170', 'r04176', 'r04177', 'r04178', 'r04179', 'r04180', 'r04181', 'r04182', 'r04183', 'r04184', 'r04185', 'r04186', 'r04187', 'r04188', 'r04189', 'r04190', 'r04191', 'r04192', 'r04193', 'r04194', 'r04195', 'r04196', 'r04197', 'r04200', 'r04201', 'r04203', 'r04204', 'r04247', 'r04248', 'r04249', 'r04250', 'r04251', 'r04252', 'r04253', 'r04254', 'r04257', 'r04258', 'r04259', 'r04260', 'r04261', 'r04262', 'r04263', 'r04264', 'r04265', 'r04266', 'r04268', 'r04269', 'r04270', 'r04271', 'r04272', 'r04273', 'r04274', 'r04275', 'r04276', 'r04277', 'r04278', 'r04287', 'r04290', 'r04292', 'r04295', 'r04296', 'r04297', 'r04298', 'r04299', 'r04301', 'r04302', 'r04303', 'r04304', 'r04305', 'r04307', 'r04308', 'r04309', 'r04310', 'r04311', 'r04313', 'r04314', 'r04315', 'r04316', 'r04317', 'r04318', 'r04319', 'r04320', 'r04321', 'r04322', 'r04323', 'r04324', 'r04325', 'r04326', 'r04327', 'r04328', 'r04329', 'r04330', 'r04332', 'r04333', 'r04334', 'r04335', 'r04396', 'r04397', 'r04398', 'r04399', 'r04400', 'r04406', 'r04408', 'r04409', 'r04411', 'r04412', 'r04413', 'r04414', 'r04450', 'r04451', 'r04452', 'r04453', 'r04464', 'r04465', 'r04466', 'r04467', 'r04468', 'r04554', 'r04555', 'r04556', 'r04557', 'r04607', 'r04608', 'r04610', 'r04613', 'r04614', 'r04615', 'r04616', 'r04617', 'r04618', 'r04659', 'r04660', 'r04661', 'r04662', 'r04664', 'r04669', 'r04670', 'r04671', 'r04672', 'r04673', 'r04677', 'r04678', 'r04679', 'r04680', 'r04697', 'r04698', 'r04699', 'r04700', 'r04701', 'r04702', 'r04703', 'r04704', 'r04705', 'r04706', 'r04707', 'r04708', 'r04709', 'r04710', 'r04711', 'r04712', 'r04713', 'r04714', 'r04715', 'r04716', 'r04718', 'r04719', 'r04720', 'r04721', 'r04722', 'r04724', 'r04725', 'r04726', 'r04727', 'r04731', 'r04732', 'r04734', 'r04735', 'r04736', 'r04737', 'r04738', 'r04739', 'r04740', 'r04741', 'r04742', 'r04743', 'r04748', 'r04803', 'r04804', 'r04805', 'r04808', 'r04809', 'r04810', 'r04811', 'r04812', 'r04813', 'r04854', 'r04855', 'r04856', 'r04857', 'r04858', 'r04859', 'r04860', 'r04861', 'r04863', 'r04864', 'r04865', 'r04866', 'r04867', 'r04872', 'r04874', 'r04875', 'r04876', 'r04877', 'r04878', 'r04917', 'r04918', 'r04920', 'r04922', 'r04937', 'r05094', 'r05095', 'r05096', 'r05097', 'r05098', 'r05099', 'r05100', 'r05101', 'r05102', 'r05103', 'r05104', 'r05105', 'r05106', 'r05107', 'r05108', 'r05109', 'r05110', 'r05111', 'r05140', 'r05141', 'r05142', 'r05143', 'r05144', 'r05145', 'r05146', 'r05147', 'r05148', 'r05150', 'r05151', 'r05152', 'r05153', 'r05154', 'r05155', 'r05156', 'r05157', 'r05158', 'r05159', 'r05160', 'r05168', 'r05169', 'r05170', 'r05171', 'r05172', 'r05173', 'r05178', 'r05179', 'r05181', 'r05182', 'r05183', 'r05184', 'r05185', 'r05186', 'r05187', 'r05189', 'r05190', 'r05191', 'r05192', 'r05193', 'r05194', 'r05195', 'r05198', 'r05199', 'r05201', 'r05202', 'r05203', 'r05204', 'r05206', 'r05207', 'r05208', 'r05209', 'r05210', 'r05211', 'r05212', 'r05213', 'r05214', 'r05227', 'r05228', 'r05229', 'r05232', 'r05235', 'r05236', 'r05237', 'r05238', 'r05240', 'r05241', 'r05242', 'r05243', 'r05244', 'r05245', 'r05248', 'r05249', 'r05250', 'r05251', 'r05253', 'r05256', 'r05259', 'r05260', 'r05261', 'r05325', 'r05327', 'r05328', 'r05329', 'r05330', 'r05333', 'r05335', 'r05336', 'r05337', 'r05338', 'r05339', 'r05340', 'r05343', 'r05345', 'r05346', 'r05347', 'r05387', 'r05388', 'r05389', 'r05390', 'r05391', 'r05392', 'r05393', 'r05394', 'r05395', 'r05396', 'r05398', 'r05399', 'r05400', 'r05401', 'r05449', 'r05450', 'r05451', 'r05452', 'r05453', 'r05455', 'r05456', 'r05457', 'r05458', 'r05460', 'r05461', 'r05462', 'r05463', 'r05530', 'r05531', 'r05532', 'r05533', 'r05534', 'r05535', 'r05536', 'r05538', 'r05542', 'r05606', 'r05607', 'r05608', 'r05609', 'r05610', 'r05611', 'r05612', 'r05613', 'r05614', 'r05615', 'r05616', 'r05621', 'r05622', 'r05623', 'r05624', 'r05625', 'r05627', 'r05628', 'r05629', 'r05630', 'r05631', 'r05632', 'r05640', 'r05687', 'r05688', 'r05689', 'r05690', 'r05691', 'r05693', 'r05694', 'r05695', 'r05697', 'r05702', 'r05703', 'r05704', 'r05721', 'r05722', 'r05723', 'r05724', 'r05725', 'r05726', 'r05727', 'r05728', 'r05729', 'r05730', 'r05748', 'r05749', 'r05750', 'r05751', 'r05752', 'r05753', 'r05754', 'r05755', 'r05757', 'r05758', 'r05818', 'r05819', 'r05820', 'r05821', 'r05822', 'r05823', 'r05824', 'r05825', 'r05826', 'r05827', 'r05828', 'r05830', 'r05831', 'r05832', 'r05833', 'r05834', 'r05835', 'r05890', 'r05891', 'r05892', 'r05894', 'r05895', 'r05896', 'r05897', 'r05898', 'r05899', 'r05900', 'r05901', 'r05902']

	
for run in runlist:
	
	filename='data_%s_%s_%s'%(exp,energy,run)
	input_dir='/group/belle2/dataprod/Data/PromptReco/bucket8/%s/%s/%s/all/mdst/sub00/'%(exp,energy,run)
	os.system('bsub -q l -oo log/Data_e10/%s.log  basf2 -l INFO reco_hadvert.py Data  %s  root/Data_e10/%s.root ' %(filename,input_dir,filename))
	

#---------------------------------------------------------------
#-------------------    Real Data   ----------------------------
#---------------------------------------------------------------












