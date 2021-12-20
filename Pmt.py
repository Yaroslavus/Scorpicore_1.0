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

    def __init__(self, global_number=0, x=0, y=0, amplitude=0, ignore_status=0, neighbors_list=[], cleaning_status=1, spot_id=0):

        self.global_number = global_number
        self.x = x
        self.y = y
        self.amplitude = amplitude
        self.neighbors_list = neighbors_list
        self.cleaning_status = cleaning_status
        self.spot_id = spot_id
        self.list_of_pmts.append (self)
        
    def show_item (self):
        print("{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}".format(
                "global_number", self.global_number,
                "x_coord:", self.x,
                "y_coord:", self.y,
                "amplitude:", self.amplitude,
                "cleaning_status", self.cleaning_status,
                "spot_id", self.spot_id))

        
    def string_of_values (self):
        return ("Global number: {}\tX: {}\tY: {}\tAmplitude: {}\tNeighbors: {}\tCleaning_status: {}\tSpot_id: {}".format(
                self.global_number, self.x, self.y, self.amplitude, self.neighbors_list, self.cleaning_status, self.spot_id))
  
    def list_of_values (self):
        return self.global_number, self.x, self.y, self.amplitude, self.neighbors_list, self.cleaning_status, self.spot_id
    
#    def print_list_of_channels ():
#        for ch in channel.list_of_channels:
#            ch.list_of_values()
            