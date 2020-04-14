# -*- coding: utf-8 -*-
#   ___      _ _                    _     
#  / _ \    | | |                  | |    
# / /_\ \ __| | |__   ___  ___  ___| |__  
# |  _  |/ _` | '_ \ / _ \/ _ \/ __| '_ \ 
# | | | | (_| | | | |  __/  __/\__ \ | | |
# \_| |_/\__,_|_| |_|\___|\___||___/_| |_|
# Date:   2020-04-12 22:17:00
# Last Modified time: 2020-04-13 22:20:13

import numpy as np
import matplotlib.pyplot as plt
import random
from aux import *

class K_Means_Clustering():
	def __init__(self,obj,n_clusters):
		self.obj=obj
		self.obj_x,self.obj_y=self.obj.calc_raw()
		self.n_clusters=n_clusters

	def algorithm(self):
		clusters=make_clusters(self.obj_x,self.obj_y,self.n_clusters)
		clusters=self.find_centroid(clusters)

		MAX_ITER=10
		COST_THRESH=0.1
		p_cost=100
		for i in range(MAX_ITER):
			# print(f'loop: {i}')
			self.clusters,cost=self.update_clusters(clusters)
			self.clusters=self.find_centroid(clusters)

			d_cost=abs(cost-p_cost)
			if d_cost < COST_THRESH:
				break
			p_cost=cost

		return self.clusters

	def find_centroid(self,clusters):
		for i in range(clusters.n_clusters):
			x,y=self.find_points(i,clusters)
			n_data=len(x)
			clusters.cx[i]=sum(x)/n_data
			clusters.cy[i]=sum(y)/n_data

		return clusters

	def find_points(self,ind,clusters):
		inds=np.array([i for i in range(clusters.n_data) if clusters.n_labels[i] == ind])
		temp_x=np.array(clusters.x)
		temp_y=np.array(clusters.y)

		x=temp_x[inds]
		y=temp_y[inds]

		return x,y

	def update_clusters(self,clusters):
		cost=0
		for i in range(clusters.n_data):
			px=clusters.x[i]
			py=clusters.y[i]
			dx=[ix-px for ix in clusters.cx]
			dy=[iy-py for iy in clusters.cy]
			dist_list=[np.sqrt(idx**2+idy**2) for idx,idy in zip(dx,dy)]
			min_dist=min(dist_list)
			min_ind=dist_list.index(min_dist)
			clusters.n_labels[i]=min_ind
			cost+=min_ind

		return clusters,cost

	def calc_association(self,cx,cy,clusters):
		inds=[]
		for i,_ in enumerate(cx):
			temp_x=cx[i]
			temp_y=cy[i]
			dx=[ix-temp_x for ix in clusters.cx]
			dy=[iy-temp_y for iy in clusters.cy]
			dist_list=[np.sqrt(idx**2+idy**2) for idx,idy in zip(dx,dy)]
			min_dist=min(dist_list)
			min_ind=dist_list.index(min_dist)
			
			inds.append(min_ind)

		return inds
	
	def plot(self,record=False):
		self.algorithm()
		plt.clf()
		inds=self.calc_association(self.obj.x,self.obj.y,self.clusters)
		for i in inds:
			x,y = self.find_points(i,self.clusters)
			plt.plot(x,y,'x', label="point",zorder=3)

		plt.plot(self.obj.x,self.obj.y,'o',label='centre',zorder=2)

		circle1=plt.Circle((self.obj.x[0],self.obj.y[0]),2,color='#80ccff',alpha=0.2,zorder=1,label='Cluster')
		circle2=plt.Circle((self.obj.x[1],self.obj.y[1]),2,color='#ffabbd',alpha=0.2,zorder=1,label='Cluster')
		plt.gcf().gca().add_artist(circle1)
		plt.gcf().gca().add_artist(circle2)

		# circle=[]
		# for i in range(0,len(inds)):
		# 	for j,k in zip(self.obj.x,self.obj.y):
		# 		circle.append(plt.Circle((j,k),2,alpha=0.2,zorder=1,label='Cluster'))
		# for i in circle:
		# 	plt.gcf().gca().add_artist(i)
		
		plt.axis("equal")
		plt.title("K Means Clustering")
		plt.legend(loc=1)
		plt.pause(1)