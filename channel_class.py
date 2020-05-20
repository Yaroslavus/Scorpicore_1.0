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

    def __init__(self, number=0, pmt_number=0, cluster=0, gain=0, k_adc=0, rel_sens=0, code_per_pe=0, x=0, y=0, cur_count_rate_number=0, ampl=0):

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
        self.ampl = ampl # 11
        self.list_of_channels.append (self)
        
    def show_item (item):
        print("channel_number:\t{}\tpmt_number:\t{}\tcluster_number:\t{}\tgain:\t{}\tk_adc:\t{}\trel_sens:\t{}\tcode_per_pe:\t{}\tx:\t{}\ty:\t{}\tcur_count_rate_number:\t{}\tampl:\t{}".format(
                item.number, item.pmt_number, item.cluster, item.gain, item.k_adc, item.rel_sens, item.code_per_pe, item.x, item.y, item.cur_count_rate_number, item.ampl))

    def show_values (item):
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
                item.number, item.pmt_number, item.cluster, item.gain, item.k_adc, item.rel_sens, item.code_per_pe, item.x, item.y, item.cur_count_rate_number, item.ampl))
        
    def string_of_values (item):
        return ("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                item.number, item.pmt_number, item.cluster, item.gain, item.k_adc, item.rel_sens, item.code_per_pe, item.x, item.y, item.cur_count_rate_number, item.ampl))
  
    def return_values_list (item):
        return item.number, item.pmt_number, item.cluster, item.gain, item.k_adc, item.rel_sens, item.code_per_pe, item.x, item.y, item.cur_count_rate_number, item.ampl