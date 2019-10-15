# -*- coding: utf-8 -*-
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