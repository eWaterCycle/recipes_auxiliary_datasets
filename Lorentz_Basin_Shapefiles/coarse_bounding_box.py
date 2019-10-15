# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:46:11 2019

@author: Jerom Aerts
"""
import os
import math
import geopandas as gpd

def coarse_bounding_box(shapefile, degree_buffer=float):
    """ Extract extent from shapefile and add a buffer in degrees."""
    shape = gpd.read_file(shapefile)
    bounds = shape.bounds

    xmin = bounds['minx'].values
    ymin = bounds['miny'].values
    xmax = bounds['maxx'].values
    ymax = bounds['maxy'].values
    
    print(xmin)
    
    if xmin > 0:
        xmin_round = math.ceil(xmin) + degree_buffer
    else:
        xmin_round = math.floor(xmin)- degree_buffer
    if ymin > 0:
        ymin_round = math.ceil(ymin) + degree_buffer
    else:
        ymin_round = math.floor(ymin)- degree_buffer  
    if xmax > 0:
        xmax_round = math.ceil(xmax) + degree_buffer
    else:
        xmax_round = math.floor(xmax)- degree_buffer
    if ymax > 0:
        ymax_round = math.ceil(ymax) + degree_buffer
    else:
        ymax_round = math.floor(ymax)- degree_buffer 
    
    return xmin_round, ymin_round, xmax_round, ymax_round
    


for file in os.listdir(r"C:\Users\LocalAdmin\Desktop\GIT\recipes_auxiliary_datasets\Lorentz_Basin_Shapefiles\Doring"):
    fName, fExt = os.path.splitext(file) # break up file name and extension
    if fExt.lower() == '.shp': #only use tif files
       xmin, ymin, xmax, ymax = coarse_bounding_box(file, 1)
       