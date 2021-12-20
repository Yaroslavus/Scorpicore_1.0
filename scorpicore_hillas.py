#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:27:01 2021

@author: yaroslav
"""

import Pmt
import scorpicore_tools as tools
import math

def find_the_hillas_parameters(event_number, corrections_x_y):
    
    print("\n\nHillas parameters for event {} are calculating...".format(event_number))
        
    sx = 0
    sy = 0
    sx_sq = 0
    sy_sq = 0
    sxy = 0
    SIZE = 0
    

    
    for pmt_item in Pmt.pmt.list_of_pmts:
        if pmt_item.amplitude != 0:
            corrected_x = pmt_item.x - corrections_x_y[0]
            corrected_y = pmt_item.y - corrections_x_y[1]
            SIZE += pmt_item.amplitude
            sx += pmt_item.amplitude*corrected_x
            sy += pmt_item.amplitude*corrected_y
            sx_sq += pmt_item.amplitude*((corrected_x)**2)
            sy_sq += pmt_item.amplitude*((corrected_y)**2)
            sxy += pmt_item.amplitude*((corrected_x)*(corrected_y))
    try:
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
        
        SIZE = round(SIZE, 3)
        DISTANCE = round(tools.square_root(x_av**2 + y_av**2), 3)
        LENGTH = round(tools.square_root((sigma_x_sq + sigma_y_sq + z)/2), 3)
        WIDTH = round(tools.square_root((sigma_x_sq + sigma_y_sq - z)/2), 3)
        AZWIDTH = round(tools.square_root((x_av**2)*x_sq_av + y_sq_av*(y_av**2) + 2*x_av*y_av*xy_av), 3)
        MISS = round(tools.square_root((u*(x_av)**2 + v*(y_av)**2)/2 - 2*sigma_xy*x_av*y_av/z), 3)
        SINUS_ALPHA = round(MISS/DISTANCE, 3)
        ALPHA = round(math.asin(SINUS_ALPHA)*180/math.pi, 3)
        
        hillas_tuple = (SIZE, DISTANCE, LENGTH, WIDTH, AZWIDTH, MISS, ALPHA)
    
    except Exception:
        hillas_tuple = (0, 0, 0, 0, 0, 0, 0)
        print("ZERO Hillas event number {}".format(event_number))
        for pmt_item in Pmt.pmt.list_of_pmts:
            print(pmt_item.string_od_values())
    
    return hillas_tuple