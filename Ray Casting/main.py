# -*- coding: utf-8 -*-
#   ___      _ _                    _     
#  / _ \    | | |                  | |    
# / /_\ \ __| | |__   ___  ___  ___| |__  
# |  _  |/ _` | '_ \ / _ \/ _ \/ __| '_ \ 
# | | | | (_| | | | |  __/  __/\__ \ | | |
# \_| |_/\__,_|_| |_|\___|\___||___/_| |_|
# Date:   2020-04-12 19:03:44
# Last Modified time: 2020-04-12 21:12:24

import numpy as np
import matplotlib.pyplot as plt
import math
from aux import *

class ray_cast():
	def __init__(self,xy_res,theta_res,obs_x,obs_y,extend_area):
		self.xy_res=xy_res
		self.theta_res=theta_res
		self.obs_x=obs_x
		self.obs_y=obs_y
		self.extend_area=extend_area

	def algorithm(self):
		self.x_min,self.y_min,self.x_max,self.y_max,self.x_width,self.y_width = self.configure(self.obs_x,self.obs_y,self.xy_res)	
		self.prob_map=np.zeros((self.x_width,self.y_width))
	
		init_cast=self.initialize(self.x_min,self.y_min,self.x_width,self.y_width,self.xy_res,self.theta_res)
				
		for (x, y) in zip(self.obs_x, self.obs_y):
			d = math.sqrt(x**2 + y**2)
			angle = self.convert_angle(y, x)
			angleid = int(math.floor(angle / self.theta_res))
			gridlist = init_cast[angleid]
			ix = int(round((x - self.x_min) / self.xy_res))
			iy = int(round((y - self.y_min) / self.xy_res))
			
			for grid in gridlist:
				if grid.d > d:
					self.prob_map[grid.ix][grid.iy] = 0.5

			self.prob_map[ix][iy] = 1.0

	def configure(self,obs_x, obs_y, xy_res):
		x_min = np.round(np.amin(obs_x,axis=0) - self.extend_area / 2.0)
		y_min = np.round(np.amin(obs_y,axis=0) - self.extend_area / 2.0)
		x_max = np.round(np.amax(obs_x,axis=0) + self.extend_area / 2.0)
		y_max = np.round(np.amax(obs_y,axis=0) + self.extend_area / 2.0)
		x_width = np.round((x_max - x_min) / xy_res).astype(int)
		y_width = np.round((y_max - y_min) / xy_res).astype(int)

		return x_min, y_min, x_max, y_max, x_width, y_width


	def initialize(self,x_min,y_min,x_width,y_width,xy_res,theta_res):
		init_cast=[[] for i in range(0,int(round((math.pi*2)/theta_res))+1)]

		for i in range(0,x_width):
			for j in range(0,y_width):
				px=i*xy_res+x_min
				py=j*xy_res+y_min

				d=math.sqrt(px**2+py**2)
				theta=self.convert_angle(py,px)
				theta_id=int(math.floor(theta/theta_res))

				db = init_cast_db()

				db.px=px
				db.py=py
				db.d=d
				db.ix=i
				db.iy=j
				db.theta=theta

				init_cast[theta_id].append(db)

		return init_cast

	def convert_angle(self,y, x):
		angle = math.atan2(y, x)
		if angle < 0.0:
			angle += math.pi * 2.0

		return angle


	def draw_heatmap(self,prob_map, x_min, x_max, y_min, y_max, xy_res):
		x, y = np.mgrid[x_min - xy_res / 2.0:x_max + xy_res / 2.0:xy_res,y_min - xy_res / 2.0: y_max + xy_res / 2.0: xy_res]
		plt.pcolor(x,y,prob_map,vmax=1,cmap=plt.cm.Blues)
		plt.axis("Equal")

	def plot(self):
		self.algorithm()
		plt.cla()
		self.draw_heatmap(self.prob_map, self.x_min, self.x_max, self.y_min, self.y_max, self.xy_res)
		plt.plot(self.obs_x, self.obs_y, "xr")
		plt.plot(0.0, 0.0, "ok")
		plt.pause(1.0)