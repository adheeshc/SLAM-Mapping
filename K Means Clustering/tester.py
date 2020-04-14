# -*- coding: utf-8 -*-
#   ___      _ _                    _     
#  / _ \    | | |                  | |    
# / /_\ \ __| | |__   ___  ___  ___| |__  
# |  _  |/ _` | '_ \ / _ \/ _ \/ __| '_ \ 
# | | | | (_| | | | |  __/  __/\__ \ | | |
# \_| |_/\__,_|_| |_|\___|\___||___/_| |_|
# Date:   2020-04-12 22:17:08
# Last Modified time: 2020-04-13 22:19:41

from main import *
from aux import *

def main():
	print(__file__+" running...")

	x=[0,8]
	y=[10,10]
	n_points=10
	rand_dist=3
	n_clusters=2
	sim_time=20
	time=0

	while time<=sim_time:
		#print(f'time: {time}')
		time+=1

		#Create objects
		obj=create_objects(x,y,n_points,rand_dist)

		#Clustering
		clusters=K_Means_Clustering(obj,n_clusters)
		clusters.plot()

if __name__=="__main__"	:
	main()
