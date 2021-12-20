#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 21:15:08 2021

@author: yaroslav
"""

import os
import scorpicore_tools as tools
import Channel as Ch
import init_all_channels
import scorpicore_plotter
import Pmt
import scorpicore_cleaning
import scorpicore_hillas
import pandas as pd
MIN_BORDER_THRESHOLD = 0
MAX_BORDER_THRESHOLD = 1000
TRESHOLD_CLEANING = 4000
TRESHOLD_FOR_SUM_OF_NEIGHBORS_CLEANING = 20000
TRESHOLD_FOR_NUM_OF_NEIGHBORS_CLEANING_number = 5
TRESHOLD_FOR_NUM_OF_NEIGHBORS_CLEANING_amplitude = 3000
wobble_file = "/home/yaroslav/Yaroslavus_GitHub/DATA/231119.01/pointing_data_2019-11-23_15:46:05.csv"
# =============================================================================
#
# =============================================================================
day = "231119.01"
START_TIME = tools.what_time_is_now()
init_all_channels.init_pmts_with_zeros()
amplitudes_sum = [0]*1000
amplitudes_counters = [0]*1000


table = pd.read_csv(wobble_file, delimiter=",")
time_list = [round(time_mark) for time_mark in table['hh']*3600 + table['mm']*60 + table['ss']]
source_x = list(table['source_x'])
source_y = list(table['source_y'])

with open ("hillas_out.txt", "w+") as fout:
    fout.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format("EVENT_NUMBER", "SIZE", "DISTANCE", "LENGTH", "WIDTH", "AZWIDTH", "MISS", "ALPHA"))
    
    cleaning_type = "z"
    last_tail = 138
    
    for tail_number in range (1, last_tail+1):
        
        with open(tools.data_dir() + "/" + day + "/" + "0"*(3 - len(str(tail_number))) + str(tail_number) + "_clean.out", "r") as fin:
            line = fin.readline().split()
            matrix = []
            event_number = line[1]
            print(line[0], event_number)
            for _ in range(23):
                matrix.append(fin.readline().split())
            matrix = [value for value in matrix if value != []]
            for cluster in matrix:
                event_time_list = cluster[1].split('.')[0].split(':')
# =============================================================================
        event_time_line = int(event_time_list[0])*3600 + int(event_time_list[1])*60 + int(event_time_list[2])
#                print(event_time_line)
        for i in range(len(time_list)):
            if (time_list[i] <= event_time_line) and (time_list[i+1] > event_time_line):
                start_time_mark_index = i
        print(tail_number, start_time_mark_index)
# =============================================================================


        with open(tools.data_dir() + "/" + day + "/" + "0"*(3 - len(str(tail_number))) + str(tail_number) + "_clean.out", "r") as fin:
            current_time_mark_index = start_time_mark_index
            line = fin.readline().split()
            while line:
                matrix = []
                event_number = line[1]
                print(line[0], event_number)
                for _ in range(23):
                    matrix.append(fin.readline().split())
                matrix = [value for value in matrix if value != []]
                for cluster in matrix:
                    event_time_list = cluster[1].split('.')[0].split(':')
# =============================================================================
                    
                    
                    
                event_time_line = int(event_time_list[0])*3600 + int(event_time_list[1])*60 + int(event_time_list[2])
                
                if (time_list[current_time_mark_index] <= event_time_line) and (time_list[current_time_mark_index+1] > event_time_line):
                    pass
                elif event_time_line >= time_list[current_time_mark_index+1]:
                    while event_time_line >= time_list[current_time_mark_index+1]:
                        current_time_mark_index += 1
                corrections_x_y = [source_x[current_time_mark_index], source_y[current_time_mark_index]]
                
                
                
# =============================================================================
                
                init_all_channels.init_pmts_for_event(matrix, "c")

                for pmt_item in Pmt.pmt.list_of_pmts:
                    if pmt_item.amplitude != 0:
                        amplitudes_sum[pmt_item.global_number] = +pmt_item.amplitude
                        amplitudes_counters[pmt_item.global_number] += 1
#                        print(pmt_item.global_number, pmt_item.amplitude)

                        
                scorpicore_cleaning.topological_cleaning_1(event_number, MIN_BORDER_THRESHOLD, MAX_BORDER_THRESHOLD)
                event_hillas_tuple = scorpicore_hillas.find_the_hillas_parameters(event_number, corrections_x_y)
                print("Tail number: {}/{}".format(tail_number, last_tail))
                
                for pmt_item in Pmt.pmt.list_of_pmts:
                    pmt_item.amplitude = 0
                    pmt_item.spot_id = 0

                line = fin.readline().split()
                print(tools.time_check(START_TIME))
                
                fout.write("{}\t".format(event_number))
                fout.write("\t".join([str(i) for i in event_hillas_tuple]))
                fout.write("\n")
                
        print(tail_number, " / ", last_tail)
        
        amplitudes_sum_string = ""
        for i in range(1000):
            amplitudes_sum_string += "\n{}: {}".format(amplitudes_counters[i], amplitudes_sum[i])
            
with open("amplitudes_out.txt", "w+") as fout:
    for i in range(1000):
        if amplitudes_counters[i] == 0:
            fout.write("{}\t{}\n".format(amplitudes_counters[i], amplitudes_sum[i]))
            
    
    
    
    
    
    
    
    
    
    
    