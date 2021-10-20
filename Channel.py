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
        
    def show_item (self):
        print("{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}".format(
                "number:", self.number, # 1
                "pmt_number:", self.pmt_number, # 2
                "cluster_number", self.cluster, # 3
                "global_number", self.global_number, # 4
                "gain:", self.gain, # 5
                "k_adc:", self.k_adc, # 6
                "rel_sens:", self.rel_sens, # 7
                "code_per_pe:", self.code_per_pe, # 8
                "x_coord:", self.x, # 9
                "y_coord:", self.y, # 10
                "cur_count_rate_number:", self.cur_count_rate_number, # 11
                "amplitude:", self.amplitude, # 12
                "ignore_status:", self.ignore_status, # 13
                "trigger_status", self.trigger_status)) # 14

        
    def string_of_values (self):
        return ("{} {} {} {} {} {} {} {} {} {} {} {} {}\n".format(
                self.number, self.pmt_number, self.cluster, # 3
                self.global_number, self.gain, self.k_adc, # 6
                self.rel_sens, self.code_per_pe, self.x, self.y, # 10
                self.cur_count_rate_number, self.amplitude, # 12
                self.ignore_status, self.trigger_status)) # 14
  
    def list_of_values (self):
        return self.number, self.pmt_number, self.cluster, self.global_number, self.gain, self.k_adc, self.rel_sens, self.code_per_pe, self.x, self.y, self.cur_count_rate_number, self.amplitude, self.ignore_status, self.trigger_status # 14
    
#    def print_list_of_channels ():
#        for ch in channel.list_of_channels:
#            ch.list_of_values()
            