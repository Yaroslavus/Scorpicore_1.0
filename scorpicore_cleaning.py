#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:00:43 2021

@author: yaroslav
"""
import Pmt as Pmt
import scorpicore_tools as tools


#def zero_cleaning(event_number):
#    
#    print("ZERO cleaning of event number ", event_number, " ...")
#    maximum_distance = 0
#    
#    for pmt_item_1 in Pmt.pmt.list_of_pmts:
#        for pmt_item_2 in Pmt.pmt.list_of_pmts:
#            current_distance = tools.square_root((pmt_item_1.x - pmt_item_2.x)**2 + (pmt_item_1.y - pmt_item_2.y)**2)
#            if current_distance > maximum_distance:
#                maximum_distance = current_distance
#    if maximum_distance > 2500: return 0
#    else: return 1
    
def treshold_cleaning(event_number, treshold):
    
    print("Treshold cleaning for event {} with treshold {} is providing...".format(
            event_number,
            treshold))
    for pmt_item in Pmt.pmt.list_of_pmts:
        if pmt_item.amplitude < treshold:
            pmt_item.cleaning_status = 0
            
def sum_of_neighbors_cleaning(event_number, treshold):
    
        print("Neighbors cleaning for event {} with treshold {} is providing...".format(
                event_number,
                treshold))
        for pmt_item_0 in Pmt.pmt.list_of_pmts:
            sum_amplitude = 0
            for neighbor_global_number in pmt_item_0.neighbors_list:
                for pmt_item_1 in Pmt.pmt.list_of_pmts:
                    if pmt_item_1.global_number == neighbor_global_number:
                        sum_amplitude += pmt_item_1.amplitude
            print(sum_amplitude, treshold)
            if sum_amplitude < treshold:
                pmt_item_0.cleaning_status = 0
                
def num_of_neighbors_cleaning(event_number, ampl_treshold, num_treshold):
    
    print("Neighbors number cleaning for event {} with treshold {} and required number of neighbors {} is providing...".format(
            event_number,
            ampl_treshold,
            num_treshold))
    for pmt_item_0 in Pmt.pmt.list_of_pmts:
        num = 0
        for neighbor_global_number in pmt_item_0.neighbors_list:
            for pmt_item_1 in Pmt.pmt.list_of_pmts:
                if pmt_item_1.global_number == neighbor_global_number:
                    if pmt_item_1.amplitude > ampl_treshold:
                        num += 1
        if num < num_treshold:
            pmt_item_0.cleaning_status = 0