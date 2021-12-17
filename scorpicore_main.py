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

def draw_the_event(channels):
    pass    
# =============================================================================
#
# =============================================================================

START_TIME = tools.what_time_is_now()
#init_all_channels.global_init_of_all_channels_and_pmts_and_fill_txt_file()

event_numbers_and_clean_id_list = []

#event_numbers_string = tools.list_of_events_pseudo_input_card(18) # 5
#day = "281017"

day, event_numbers_string = tools.read_input_card()

event_numbers_list = event_numbers_string.split()

for i in range(0, len(event_numbers_list), 3):
    event_numbers_and_clean_id_list.append([event_numbers_list[i], event_numbers_list[i+1], event_numbers_list[i+2]])

event_number_list_after_zero_cleaning = []
#print(event_numbers_and_clean_id_list, len(event_numbers_and_clean_id_list))

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

#    total_counter = 1
#    not_empty_counter = 1
#    for item in Pmt.pmt.list_of_pmts:
#        total_counter += 1
#        if item.amplitude != 0:
#            print(item.string_of_values())
#            not_empty_counter += 1
#    print(total_counter, not_empty_counter)
    
    scorpicore_plotter.draw_the_event(event_number, day, hillas_parameters_string)

#init_all_channels.init_pmts_with_zeros()    
#init_all_channels.init_random_pmts_and_their_neighbors(10)
#scorpicore_plotter.draw_the_event(10, "random pmts with neighbors")
#30389027