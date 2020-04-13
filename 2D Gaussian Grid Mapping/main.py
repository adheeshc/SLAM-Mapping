# -*- coding: utf-8 -*-
#   ___      _ _                    _     
#  / _ \    | | |                  | |    
# / /_\ \ __| | |__   ___  ___  ___| |__  
# |  _  |/ _` | '_ \ / _ \/ _ \/ __| '_ \ 
# | | | | (_| | | | |  __/  __/\__ \ | | |
# \_| |_/\__,_|_| |_|\___|\___||___/_| |_|
# Date:   2020-04-12 21:21:14
# Last Modified time: 2020-04-12 22:08:30

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm


class gaussian_gridmap():
	def __init__(self,xy_res,obs_x,obs_y,extend_area,std_dev):
		self.xy_res=xy_res
		self.obs_x=obs_x
		self.obs_y=obs_y
		self.extend_area=extend_area
		self.std_dev=std_dev

	def algorithm(self):
		self.x_min,self.y_min,self.x_max,self.y_max,self.x_width,self.y_width = self.configure(self.obs_x,self.obs_y,self.xy_res)	
		self.prob_map=np.zeros((self.x_width,self.y_width))

		for i in range(0,self.x_width):
			for j in range(0,self.y_width):
				x=i*self.xy_res+self.x_min
				y=j*self.xy_res+self.y_min

				min_dist=float("inf")
				for ox,oy in zip(self.obs_x,self.obs_y):
					d=math.sqrt((ox-x)**2+(oy-y)**2)
					if min_dist>=d:
						min_dist=d
				pdf=(1-norm.cdf(min_dist,0,self.std_dev))
				self.prob_map[i][j] = pdf

	def configure(self,obs_x, obs_y, xy_res):
		x_min = np.round(np.amin(obs_x,axis=0) - self.extend_area / 2.0)
		y_min = np.round(np.amin(obs_y,axis=0) - self.extend_area / 2.0)
		x_max = np.round(np.amax(obs_x,axis=0) + self.extend_area / 2.0)
		y_max = np.round(np.amax(obs_y,axis=0) + self.extend_area / 2.0)
		x_width = np.round((x_max - x_min) / xy_res).astype(int)
		y_width = np.round((y_max - y_min) / xy_res).astype(int)

		return x_min, y_min, x_max, y_max, x_width, y_width

	def draw_heatmap(self,prob_map, x_min, x_max, y_min, y_max, xy_res):
		x, y = np.mgrid[x_min - xy_res / 2.0:x_max + xy_res / 2.0:xy_res,y_min - xy_res / 2.0: y_max + xy_res / 2.0: xy_res]
		plt.pcolor(x,y,prob_map,vmax=1,cmap=plt.cm.Blues)
		plt.axis("Equal")

	def plot(self,record=False):
		if record:
			plt.pause(5)
		self.algorithm()
		plt.cla()
		self.draw_heatmap(self.prob_map, self.x_min, self.x_max, self.y_min, self.y_max, self.xy_res)
		plt.plot(self.obs_x, self.obs_y, "xr",label="Obstacle")
		plt.plot(0.0, 0.0, "ok",label="Robot")
		plt.title("2D Gaussian Grid Map")
		plt.legend(loc=1)
		plt.pause(1.0)


