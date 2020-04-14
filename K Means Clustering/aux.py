# -*- coding: utf-8 -*-
#   ___      _ _                    _     
#  / _ \    | | |                  | |    
# / /_\ \ __| | |__   ___  ___  ___| |__  
# |  _  |/ _` | '_ \ / _ \/ _ \/ __| '_ \ 
# | | | | (_| | | | |  __/  __/\__ \ | | |
# \_| |_/\__,_|_| |_|\___|\___||___/_| |_|
# Date:   2020-04-12 22:17:26
# Last Modified time: 2020-04-13 21:50:13

import numpy as np
import random

class create_objects():
	def __init__(self,x,y,n_points,rand_dist):
		self.x=x
		self.y=y
		self.x[0]+=0.4
		self.y[0]+=0.5
		self.x[1]-=0.3
		self.y[1]-=0.5
		self.n_points=n_points
		self.rand_dist=rand_dist

	def calc_raw(self):
		obj_x,obj_y=[],[]
		for i,j in zip(self.x,self.y):
			for k in range(0,self.n_points):
				obj_x.append(i+self.rand_dist*(random.random()-0.5))
				obj_y.append(j+self.rand_dist*(random.random()-0.5))

		return obj_x,obj_y

class make_clusters():
	def __init__(self,x,y,n_clusters):
		self.x=x
		self.y=y
		self.n_clusters=n_clusters
		self.n_data=len(self.x)
		#self.n_labels=np.random.randint(0,high=n_clusters,size=self.n_data)
		self.n_labels = [random.randint(0, n_clusters - 1)for _ in range(self.n_data)]
		self.cx=[0.0 for _ in range(n_clusters)]
		self.cy=[0.0 for _ in range(n_clusters)]
