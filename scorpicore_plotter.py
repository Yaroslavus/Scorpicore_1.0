#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:49:50 2020

@author: yaroslav
"""

import matplotlib.pyplot as plt
import Channel as Ch
import math
import Pmt
    
def draw_the_event (event_number, day):
    
#    nan = float("nan")
    x = []
    y = []
    ampl = []
    global_number = []
#    cluster_x = []
#    cluster_y = []
#    cluster_number = []
    
    for item in Pmt.pmt.list_of_pmts:
        
#        if (item.number%2 == 0) and (math.isnan(item.gain) is False):
        x.append(item.x)
        y.append(item.y)
        ampl.append(item.amplitude)
#        cluster.append(item.cluster)
        global_number.append(item.global_number)
        
    fig, ax = plt.subplots(figsize=(25,15))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Event {} in day {}".format(event_number, day))
    ax.set_xlim([-5000, 5000])
    ax.set_ylim([-5000, 5000])
    
    plt.scatter(x, y, cmap = 'hot_r', s = 60, c = ampl, alpha = 0.5, marker=u'$\u2B23$')
    cbar = plt.colorbar()
    cbar.set_label('Amplitudes')

#    values_of_clusters = global_number [3::32]
#    print (values_of_clusters, len(values_of_clusters))
#    x_of_clusters = x [3::32]
#    y_of_clusters = y [3::32]
#    print(len(values_of_clusters), len(x_of_clusters), len(y_of_clusters))



    for i in range (len (ampl)):
        if ampl[i] == 0:
            plt.annotate(ampl [i], xy=(x [i], y [i]), xytext=(x [i], y [i]), fontsize = 3)

#        plt.annotate(global_number [i], xy=(x [i], y [i]), xytext=(x [i], y [i]), fontsize = 3)
#    for i in range (len (cluster)):
#        plt.annotate(cluster [i], xy=(x_of_clusters [i], y_of_clusters [i]), xytext=(x_of_clusters [i], y_of_clusters [i]), fontsize = 30, alpha = 0.5)
        
    plt.show()
