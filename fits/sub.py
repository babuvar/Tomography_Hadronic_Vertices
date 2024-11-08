#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json


for i in range(72):
	os.system('bsub -q l -oo log/fit_%s.log  python3 fit.py %s'%(i,i))



