#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from os import path
import sys
import json
import glob

#goodData_exp7_4S.txt  goodData_exp8_4S.txt  goodData_exp8_Continuum.txt  goodData_exp8_Scan.txt

exps=['7','8']
types=['4S','Continuum','Scan']

full_dic={}

for exp in exps:
	typ_dic={}
	for typ in types:
		inp_dir='/group/belle2/dataprod/Data/OfficialReco/proc10/e000%s/%s/GoodRuns/'%(exp, typ)
		if path.exists(inp_dir):
			#print('%s exists'%inp_dir)
			os.chdir(inp_dir)
			runs=[]
			for run in glob.glob("*r*"):
				#print(run)
				runs.append(run)
			typ_dic[typ]=runs
	full_dic['e000%s'%exp]=typ_dic

#print(full_dic)

os.chdir('/home/belle/varghese/DESY/BASF2/Physics_Analysis/B2BII/hadronic_vertices/MakeGoodRunList')
with open('goodData_runlist.json', 'w') as fp:
	json.dump(full_dic, fp)
