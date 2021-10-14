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

    def __init__(self, number=0, pmt_number=0, cluster=0, gain=0, k_adc=0,
                 rel_sens=0, code_per_pe=0, x=0, y=0, cur_count_rate_number=0,
                 amplitude=0, ignore_status=0, trigger_status=0):

        self.number = number # 1
        self.pmt_number = pmt_number # 2
        self.cluster = cluster # 3
        self.gain = gain # 4
        self.k_adc = k_adc # 5
        self.rel_sens = rel_sens # 6
        self.code_per_pe = code_per_pe # 7
        self.x = x # 8
        self.y = y # 9
        self.cur_count_rate_number = cur_count_rate_number # 10
        self.amplitude = amplitude # 11
        self.ignore_status = ignore_status # 12
        self.trigger_status = trigger_status # 13
        self.list_of_channels.append (self)
        
    def show_item (item):
        print("{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}".format(
                "number:", item.number, # 1
                "pmt_number:", item.pmt_number, # 2
                "cluster_number", item.cluster, # 3
                "amplitude:", item.amplitude, # 4
                "ignore_status:", item.ignore_status, # 5
                "trigger_status", item.trigger_status, # 6
                "gain:", item.gain, # 7
                "k_adc:", item.k_adc, # 8
                "rel_sens:", item.rel_sens, # 9
                "code_per_pe:", item.code_per_pe, # 10
                "x_coord:", item.x, # 11
                "y_coord:", item.y, # 12
                "cur_count_rate_number:", item.cur_count_rate_number)) # 13

        
    def string_of_values (item):
        return ("{} {} {} {} {} {} {} {} {} {} {} {} {}\n".format(
                item.number, item.pmt_number, item.cluster, # 3
                item.amplitude, item.ignore_status, item.trigger_status, # 6
                item.gain, item.k_adc, item.rel_sens, # 9
                item.code_per_pe, item.x, item.y, # 12
                item.cur_count_rate_number)) # 13
  
    def list_of_values (item):
        return ("{} {} {} {} {} {} {} {} {} {} {} {} {}\n".format(
                item.number, item.pmt_number, item.cluster, # 3
                item.amplitude, item.ignore_status, item.trigger_status, # 6
                item.gain, item.k_adc, item.rel_sens, # 9
                item.code_per_pe, item.x, item.y, # 12
                item.cur_count_rate_number)).split() # 13
        
    def 