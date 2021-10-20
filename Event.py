#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 03:12:19 2020

@author: yaroslav
"""

import os

script_dir = os.getcwd()

class Event:
    
    list_of_events = []

    def __init__(self, size=0, distance=0, length=0, width=0, azwidth=0,
                 miss=0, alpha=0, event_number=0, day=0, cleaning_id=0, cleaning_parameters=0):

        self.size = size # 1
        self.distance = distance # 2
        self.length = length # 3
        self.width = width # 4
        self.azwidth = azwidth # 5
        self.miss = miss # 6
        self.alpha = alpha # 7
        self.event_number = event_number # 8
        self.day = day # 9
        self.cleaning_id = cleaning_id # 10
        self.cleaning_parameters = cleaning_parameters # 12
        self.list_of_events.append (self)
        
    def show_item (self):
        print("{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}".format(
                "event_number:", self.event_number, # 1
                "day:", self.day, # 2
                "size:", self.size, # 3
                "distance:", self.distance, # 4
                "length", self.length, # 5
                "width:", self.width, # 6
                "azwidth:", self.azwidth, # 7
                "miss", self.miss, # 8
                "alpha:", self.alpha, # 9
                "cleaning_id:", self.cleaning_id, # 10
                "cleaning_parameters:", self.cleaning_parameters # 11
                )) # 9
                
        
    def string_of_values (self):
        return ("{} {} {} {} {} {} {} {} {} {} {} {} {}\n".format(
                self.event_number, self.day,self.size, # 3
                self.distance, self.length, self.width, # 6
                self.azwidth, self.miss, self.alpha,  # 9
                self.cleaning_id, self.cleaning_parameters # 11
                ))
  
    def list_of_values (self):
        return ("{} {} {} {} {} {} {} {} {} {} {} {} {}\n".format(
                self.event_number, self.day, self.size, # 3
                self.distance, self.length, self.width, # 6
                self.azwidth, self.miss, self.alpha, # 9
                self.cleaning_id, self.cleaning_parameters, # 11
                self.cur_count_rate_number
                ))
