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
TRESHOLD_CLEANING = 4000
TRESHOLD_FOR_SUM_OF_NEIGHBORS_CLEANING = 20000
TRESHOLD_FOR_NUM_OF_NEIGHBORS_CLEANING_number = 5
TRESHOLD_FOR_NUM_OF_NEIGHBORS_CLEANING_amplitude = 3000
# =============================================================================
#
# =============================================================================

def find_the_event_for_its_number(day, number, event_clean_id):
    
    matrix = []
    
    if event_clean_id == "c":
        with open(tools.data_dir() + "/" + day + "/" + "clean_events_list.txt", "r") as fin:
            fin.readline()
            line = fin.readline().split()
            while line:
                if int(line[1]) == number:
                    tail = line[0]
                    break
                line = fin.readline().split()
#        print(tail, number)
#        print(tools.data_dir() + "/" + day + "/" + tail + "_clean.out")
        with open(tools.data_dir() + "/" + day + "/" + tail + "_clean.out", "r") as fin:
            next_event_number = int(fin.readline().split()[1])
            while next_event_number != '':
                if next_event_number == number:
                    for _ in range(23):
                        matrix.append(fin.readline().split())
                    break
                else:
                    for _ in range(23):
                        fin.readline()
                next_event_number = int(fin.readline().split()[1])

    elif event_clean_id == "d":
        with open(tools.data_dir() + "/" + day + "/" + "dynamic_events_list.txt", "r") as fin:
            fin.readline()
            line = fin.readline().split()
            while line:
                if int(line[1]) == number:
                    tail = line[0]
                    break
                line = fin.readline().split()
                
        with open(tools.data_dir() + "/" + day + "/" + tail + "_dynamic.out", "r") as fin:
            next_event_number = int(fin.readline().split()[1])
            while next_event_number != '':
                if next_event_number == number:
                    for _ in range(23):
                        matrix.append(fin.readline().split())
                    break
                else:
                    for _ in range(23):
                        fin.readline()
                next_event_number = int(fin.readline().split()[1])

    
    elif event_clean_id == "s":
        with open(tools.data_dir() + "/" + day + "/" + "static_events_list.txt", "r") as fin:
            fin.readline()
            line = fin.readline().split()
            while line:
                if int(line[1]) == number:
                    tail = line[0]
                    break
                line = fin.readline().split()
                
        with open(tools.data_dir() + "/" + day + "/" + tail + "_static.out", "r") as fin:
            next_event_number = int(fin.readline().split()[1])
            while next_event_number != '':
                if next_event_number == number:
                    for _ in range(23):
                        matrix.append(fin.readline().split())
                    break
                else:
                    for _ in range(23):
                        fin.readline()
                next_event_number = int(fin.readline().split()[1])
                
    else: print("CLEAN_ID wrong!!!")
    matrix = [value for value in matrix if value != []]
    return matrix 
# =============================================================================
#
# =============================================================================

START_TIME = tools.what_time_is_now()
day = "281017"
"""
event_numbers_and_clean_id_list = []

#day = "281017"

day, event_numbers_string = tools.read_input_card()

event_numbers_list = event_numbers_string.split()

for i in range(0, len(event_numbers_list), 3):
    event_numbers_and_clean_id_list.append([event_numbers_list[i], event_numbers_list[i+1], event_numbers_list[i+2]])

event_number_list_after_zero_cleaning = []

# Cycle through all events from the input card
event_counter = 0
for event_box in event_numbers_and_clean_id_list:
    event_number = int(event_box[0])
    event_clean_id = event_box[1]
    cleaning_type = event_box[2]
    print("Event number ", event_number, " with ", event_clean_id, "-mode is processing...")

# finding the matrix of events by event number
    matrix_with_event_data = find_the_event_for_its_number(day, event_number, event_clean_id)

# Initialization block
    init_all_channels.init_pmts_with_zeros()
    init_all_channels.init_pmts_for_event(matrix_with_event_data, event_clean_id)

# cleaning block    
    cleaning_sequence = cleaning_type.split()
    for cleaning in cleaning_sequence: 
    
        if cleaning_type == 'a':
            scorpicore_cleaning.sum_of_neighbors_cleaning(event_number, TRESHOLD_FOR_SUM_OF_NEIGHBORS_CLEANING)
        elif cleaning_type == 'n':
            scorpicore_cleaning.num_of_neighbors_cleaning(event_number, TRESHOLD_FOR_NUM_OF_NEIGHBORS_CLEANING_amplitude, TRESHOLD_FOR_NUM_OF_NEIGHBORS_CLEANING_number)
        elif cleaning_type == 't':
            scorpicore_cleaning.treshold_cleaning(event_number, TRESHOLD_CLEANING)
        elif cleaning_type == 'z':
            pass
        
# hillas parameters block
    event_hillas_titles_tuple, event_hillas_tuple = scorpicore_hillas.find_the_hillas_parameters(event_number)
    hillas_parameters_string = ""
    for i in range(len(event_hillas_titles_tuple)):
        hillas_parameters_string += "\n{}: {}".format(event_hillas_titles_tuple[i], event_hillas_tuple[i])
    
    print(hillas_parameters_string)
    
#    scorpicore_plotter.draw_the_event(event_number, day, hillas_parameters_string)
"""
# =============================================================================
#
# =============================================================================
# =============================================================================
#
# =============================================================================
# =============================================================================
#
# =============================================================================

init_all_channels.init_pmts_with_zeros()

amplitudes_sum = [0]*1000
amplitudes_counters = [0]*1000

with open ("hillas_out.txt", "w+") as fout:
#    fout.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format("EVENT_NUMBER", "SIZE", "DISTANCE", "LENGTH", "WIDTH", "AZWIDTH", "MISS", "ALPHA"))
    
    cleaning_type = "z"
    last_tail = 138
    

    for tail_number in range (1, last_tail+1):
                
        with open(tools.data_dir() + "/" + day + "/" + "0"*(3 - len(str(tail_number))) + str(tail_number) + "_clean.out", "r") as fin:
#            line = fin.readline()
            line = fin.readline().split()
            while line:
                matrix = []
                event_number = line[1]
                print(line[0], event_number)
                for _ in range(23):
                    matrix.append(fin.readline().split())
                matrix = [value for value in matrix if value != []]
                init_all_channels.init_pmts_for_event(matrix, "c")
#                for line_1 in matrix:
#                    print(line_1)

#                if len(Pmt.pmt.list_of_pmts) != 560:
#                    print("WARNING !!! Length of the PMT list is not 560 !!!")
#                counter_1 = 0
#                counter_2 = 0
#                for pmt_item in Pmt.pmt.list_of_pmts:
#                    counter_2 += 1
#                    if pmt_item.amplitude != 0:
##                        print(pmt_item.global_number, pmt_item.amplitude)
#                        counter_1 += 1
#                print("Non zero pmts before hillas: ", counter_1, "from ", counter_2)
#                if counter_1 == 0:
#                    print("WARNING !!!")
                for pmt_item in Pmt.pmt.list_of_pmts:
                    if pmt_item.amplitude != 0:
                        amplitudes_sum[pmt_item.global_number] = +pmt_item.amplitude
                        amplitudes_counters[pmt_item.global_number] += 1
#                        pmt_item.amplitude = 0
                        
                        
                event_hillas_tuple = scorpicore_hillas.find_the_hillas_parameters(event_number)
                print("Tail number: {}/{}".format(tail_number, last_tail))
#                hillas_parameters_string = ""
#                for i in range(len(event_hillas_titles_tuple)):
#                    hillas_parameters_string += "\n{}: {}".format(event_hillas_titles_tuple[i], event_hillas_tuple[i])
#                print(hillas_parameters_string)

                
                for pmt_item in Pmt.pmt.list_of_pmts:
                    pmt_item.amplitude = 0

                line = fin.readline().split()
                print(tools.time_check(START_TIME))
                
#                fout.write("{}\t".format(event_number))
#                fout.write("\t".join([str(i) for i in event_hillas_tuple]))
#                fout.write("\n")
                
#        print(tail_number, " / ", last_tail)
        
        amplitudes_sum_string = ""
        for i in range(1000):
            amplitudes_sum_string += "\n{}: {}".format(amplitudes_counters[i], amplitudes_sum[i])
            
with open("amplitudes_out.txt", "w+") as fout:
    for i in range(1000):
        if amplitudes_counters[i] == 0:
            fout.write("{}\t{}\n".format(amplitudes_counters[i], amplitudes_sum[i]))
            
    
    
    
    
    
    
    
    
    
    
    