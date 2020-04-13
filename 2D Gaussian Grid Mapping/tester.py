# -*- coding: utf-8 -*-
#   ___      _ _                    _     
#  / _ \    | | |                  | |    
# / /_\ \ __| | |__   ___  ___  ___| |__  
# |  _  |/ _` | '_ \ / _ \/ _ \/ __| '_ \ 
# | | | | (_| | | | |  __/  __/\__ \ | | |
# \_| |_/\__,_|_| |_|\___|\___||___/_| |_|
# Date:   2020-04-12 21:34:03
# Last Modified time: 2020-04-12 21:34:44


import numpy as np
from main import *

def main():
	print(__file__+" running...")
	
	extend_area=10
	xy_res=0.25
	std_dev=5

	for i in range(0,5):
		obs_x=(np.random.rand(10)-0.5)*10.0
		obs_y=(np.random.rand(10)-0.5)*10.0

		gmap=gaussian_gridmap(xy_res, obs_x,obs_y,extend_area,std_dev)
		gmap.plot()

if __name__=="__main__":

	main()
