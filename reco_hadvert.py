#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import basf2 as b2
from basf2 import *
import modularAnalysis as ma
from b2biiConversion import convertBelleMdstToBelleIIMdst, setupB2BIIDatabase
import json
import glob
import vertex as vtx
import variables.collections as vc
import variables.utils as vu
from stdCharged import *


#General
reco_path = b2.create_path()


#Get job-parameters
data_kind=str(sys.argv[1])

if data_kind == 'GMC':

	file_index=int(sys.argv[2])
	typ=str(sys.argv[3])
	outputBelle2ROOTFile=str(sys.argv[4])
	#Input files
	files=[]
	for i in range((file_index*100),((file_index+1)*100)):
	#for i in range((file_index*10),((file_index+1)*10)):
		files.append('/group/belle2/dataprod/MC/release-03-01-00/DB00000547/MC12b/s00/e1003/4S/r00000/%s/%s_%s.root'%(typ,typ,i))
	globalTag = 'MC'


if data_kind == 'Data':

	input_dir = str(sys.argv[2])
	files=glob.glob('%s/*.root'%input_dir)
	outputBelle2ROOTFile=str(sys.argv[3])	
	#globalTag = 'data_reprocessing_proc9' # global tag to use with proc9 (OLD)
	globalTag = 'data_reprocessing_proc10'
	#globalTag = 'data_reprocessing_prompt' #exp-10 stuff
	use_central_database(globalTag)



#root input
ma.inputMdstList(environmentType='default', filelist=files, path=reco_path)



#Load pion list
stdPi("all", path=reco_path)

# Reconstruction

'''
#variable dictionary for 3 track vertices
var_dict = json.load(open("variables_hadvert_3track.json"))
tuple_vars = []
for key, val in var_dict['hadvert_vars'].items():
        ma.variables.addAlias('%s' % key, '%s' % val)
        tuple_vars += ['%s' % key]



# Reconstruct 3-track secondary hadronic interaction vertices

#cuts
cut_1='pi1_mom > 0.3 and pi2_mom > 0.3 and pi3_mom > 0.3 and pi1_firstSVDLayer == 3 and pi2_firstSVDLayer == 3 and pi3_firstSVDLayer == 3'
cut_2='Rho > 0.7 and Rho  < 5 and Z > -7 and Z < 7'
#reconstruct
ma.reconstructDecay("@D+:had -> pi+:all pi-:all pi+:all", cut_1, path=reco_path)
#truth match
ma.matchMCTruth('D+:had', path=reco_path)
#make duplicates
ma.copyParticles('D+:rave', 'D+:had', path=reco_path)
#vertexing
ma.vertexRave('D+:rave', conf_level=0.01, path=reco_path, silence_warning=True)
#cuts
ma.applyCuts('D+:rave', cut_2, path=reco_path)
#save trees
ma.variablesToNtuple('D+:rave', tuple_vars, filename=outputBelle2ROOTFile, treename = 'rave', path=reco_path)

'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------










#variable dictionary for 2 track vertices
var_dict_2track = json.load(open("variables_hadvert_2track.json"))
tuple_vars_2trk = []
for key, val in var_dict_2track['hadvert_vars_2trk'].items():
        ma.variables.addAlias('%s' % key, '%s' % val)
        tuple_vars_2trk += ['%s' % key]



# Reconstruct 2-track secondary hadronic interaction vertices  

#cuts
cut_1_2trk = 'pi1_mom_2trk > 0.3 and pi2_mom_2trk > 0.3 '
cut_2_2trk = 'Rho_2trk > 0.8'
#reconstruct
ma.reconstructDecay("@K_S0:had -> pi+:all pi-:all", cut_1_2trk, path=reco_path)
#truth match
ma.matchMCTruth('K_S0:had', path=reco_path)
#make duplicates
ma.copyParticles('K_S0:rave', 'K_S0:had', path=reco_path)
#vertexing
ma.vertexRave('K_S0:rave', conf_level=0.01, path=reco_path, silence_warning=True)
#cuts
ma.applyCuts('K_S0:rave', cut_2_2trk, path=reco_path)
#save trees
ma.variablesToNtuple('K_S0:rave', tuple_vars_2trk, filename=outputBelle2ROOTFile, treename = 'rave_2trk', path=reco_path)




# progress
progress = b2.register_module('Progress')
reco_path.add_module(progress)
b2.process(path=reco_path)
#b2.process(path=reco_path, max_event=5000)

# Print call statistics
print(b2.statistics)




