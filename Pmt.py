#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:34:48 2021

@author: yaroslav
"""

import os

script_dir = os.getcwd()

class pmt:
    
    list_of_pmts = []

    def __init__(self, global_number=0, x=0, y=0, amplitude=0, ignore_status=0, neighbors_list=[]):

        self.global_number = global_number
        self.x = x
        self.y = y
        self.amplitude = amplitude
        self.neighbors_list = neighbors_list
        self.list_of_pmts.append (self)
        
    def show_item (item):
        print("{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}".format(
                "global_number", item.global_number,
                "x_coord:", item.x,
                "y_coord:", item.y,
                "amplitude:", item.amplitude))

        
    def string_of_values (item):
        return ("Global number: {}\tX: {}\tY: {}\tAmplitude: {}\tNeighbors: {}".format(
                item.global_number, item.x, item.y, item.amplitude, item.neighbors_list))
  
    def list_of_values (item):
        return item.global_number, item.x, item.y, item.amplitude, item.neighbors_list
    
#    def print_list_of_channels ():
#        for ch in channel.list_of_channels:
#            ch.list_of_values()
            