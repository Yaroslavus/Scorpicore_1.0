#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 03:12:19 2020

@author: yaroslav
"""

import os

script_dir = os.getcwd()

class channel:
    
    list_of_channels = []

    def __init__(self, number=0, pmt_number=0, cluster=0, global_number=0,
                 gain=0, k_adc=0, rel_sens=0, code_per_pe=0, x=0, y=0,
                 cur_count_rate_number=0, amplitude=0, ignore_status=0, trigger_status=0):

        self.number = number # 1
        self.pmt_number = pmt_number # 2
        self.cluster = cluster # 3
        self.global_number = global_number # 4
        self.gain = gain # 5
        self.k_adc = k_adc # 6
        self.rel_sens = rel_sens # 7
        self.code_per_pe = code_per_pe # 8
        self.x = x # 9
        self.y = y # 10
        self.cur_count_rate_number = cur_count_rate_number # 11
        self.amplitude = amplitude # 12
        self.ignore_status = ignore_status # 13
        self.trigger_status = trigger_status # 14
        self.list_of_channels.append (self)
        
    def show_item (item):
        print("{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}".format(
                "number:", item.number, # 1
                "pmt_number:", item.pmt_number, # 2
                "cluster_number", item.cluster, # 3
                "global_number", item.global_number, # 4
                "gain:", item.gain, # 5
                "k_adc:", item.k_adc, # 6
                "rel_sens:", item.rel_sens, # 7
                "code_per_pe:", item.code_per_pe, # 8
                "x_coord:", item.x, # 9
                "y_coord:", item.y, # 10
                "cur_count_rate_number:", item.cur_count_rate_number, # 11
                "amplitude:", item.amplitude, # 12
                "ignore_status:", item.ignore_status, # 13
                "trigger_status", item.trigger_status)) # 14

        
    def string_of_values (item):
        return ("{} {} {} {} {} {} {} {} {} {} {} {} {}\n".format(
                item.number, item.pmt_number, item.cluster, # 3
                item.global_number, item.gain, item.k_adc, # 6
                item.rel_sens, item.code_per_pe, item.x, item.y, # 10
                item.cur_count_rate_number, item.amplitude, # 12
                item.ignore_status, item.trigger_status)) # 14
  
    def list_of_values (item):
        return item.number, item.pmt_number, item.cluster, item.global_number, item.gain, item.k_adc, item.rel_sens, item.code_per_pe, item.x, item.y, item.cur_count_rate_number, item.amplitude, item.ignore_status, item.trigger_status # 14
    
#    def print_list_of_channels ():
#        for ch in channel.list_of_channels:
#            ch.list_of_values()
            