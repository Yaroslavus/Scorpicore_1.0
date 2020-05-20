#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:49:50 2020

@author: yaroslav
"""

import matplotlib.pyplot as plt
import random    
import channel_class as cc
    
def to_plot_the_chamber ():
    
    x = []
    y = []
    ampl = []
    cluster = []
    pmt_number = []
    
    for item in cc.channel.list_of_channels:
        
        values_list = item.return_values_list () 
       
        x.append(values_list[7])
        y.append(values_list[8])
#        ampl.append(values_list[10])
        cluster.append(values_list[2])
        pmt_number.append(values_list[1])

        ampl.append(random.random())
            
        
    fig, ax = plt.subplots(figsize=(15,15))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Event")
    ax.set_xlim([-500, 500])
    ax.set_ylim([-500, 500])
    
    plt.scatter(x, y, c = ampl, cmap = 'plasma', s = 250, alpha = 0.5, marker=u'$\u2B23$')
    cbar = plt.colorbar()
    cbar.set_label('Amplitudes')

    values_of_clusters = cluster [30::56]
#    print (values_of_clusters)
    x_of_clusters = x [30::56]
    y_of_clusters = y [30::56]
#    print(x_of_clusters, y_of_clusters)



    for i in range (len (pmt_number)):
        plt.annotate(pmt_number [i], xy=(x [i], y [i]), xytext=(x [i], y [i]), fontsize = 5)
    for i in range (len (values_of_clusters)):
        plt.annotate(values_of_clusters [i], xy=(x_of_clusters [i], y_of_clusters [i]), xytext=(x_of_clusters [i], y_of_clusters [i]), fontsize = 30, alpha = 0.5)
        
        
        