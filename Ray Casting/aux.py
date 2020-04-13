# -*- coding: utf-8 -*-
#   ___      _ _                    _     
#  / _ \    | | |                  | |    
# / /_\ \ __| | |__   ___  ___  ___| |__  
# |  _  |/ _` | '_ \ / _ \/ _ \/ __| '_ \ 
# | | | | (_| | | | |  __/  __/\__ \ | | |
# \_| |_/\__,_|_| |_|\___|\___||___/_| |_|
# Date:   2020-04-12 19:04:22
# Last Modified time: 2020-04-12 21:05:41

import numpy as np

class init_cast_db:
	def __init__(self):
		self.px=0
		self.py=0
		self.d=0
		self.theta=0
		self.ix=0
		self.iy=0

	def __str__(self):
		return f'{self.px} , {self.py} , {self.d} , {self.theta}'