#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:27:01 2021

@author: yaroslav
"""

import Pmt
import scorpicore_tools as tools
import math

def find_the_hillas_parameters(event_number):
    
    print("Hillas parameters for event {} are calculating...".format(event_number))
        
    sx = 0
    sy = 0
    sx_sq = 0
    sy_sq = 0
    sxy = 0
    SIZE = 0
    for pmt_item in Pmt.pmt.list_of_pmts:
        if pmt_item.amplitude != 0:
            SIZE += pmt_item.amplitude
            sx += pmt_item.amplitude*pmt_item.x
            sy += pmt_item.amplitude*pmt_item.y
            sx_sq += pmt_item.amplitude*((pmt_item.x)**2)
            sy_sq += pmt_item.amplitude*((pmt_item.y)**2)
            sxy += pmt_item.amplitude*((pmt_item.x)*(pmt_item.y))
            
    x_av = sx/SIZE
    y_av = sy/SIZE
    x_sq_av = sx_sq/SIZE
    y_sq_av = sy_sq/SIZE
    xy_av = sxy/SIZE
    
    sigma_x_sq = x_sq_av - (x_av)**2
    sigma_y_sq = y_sq_av - (y_av)**2
    sigma_xy = xy_av - x_av*y_av
    d = sigma_y_sq - sigma_x_sq
    z = tools.square_root(d**2 + 4*(sigma_xy)**2)
    u = 1 + d/z
    v = 2 - u
    
    DISTANCE = tools.square_root(x_av**2 + y_av**2)
    LENGTH = tools.square_root((sigma_x_sq + sigma_y_sq + z)/2)
    WIDTH = tools.square_root((sigma_x_sq + sigma_y_sq - z)/2)
    AZWIDTH = tools.square_root((x_av**2)*x_sq_av + y_sq_av*(y_av**2) + 2*x_av*y_av*xy_av)
    MISS = tools.square_root((u*(x_av)**2 + v*(y_av)**2)/2 - 2*sigma_xy*x_av*y_av/z)
    SINUS_ALPHA = MISS/DISTANCE
    ALPHA = math.asin(SINUS_ALPHA)*360/math.pi
    
    hillas_titles_tuple = ("SIZE", "DISTANCE", "LENGTH", "WIDTH", "AZWIDTH", "MISS", "ALPHA")
    hillas_tuple = (SIZE, DISTANCE, LENGTH, WIDTH, AZWIDTH, MISS, ALPHA)
    
    return hillas_titles_tuple, hillas_tuple