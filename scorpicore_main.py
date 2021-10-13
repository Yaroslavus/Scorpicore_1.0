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
import Pmt as Pmt
import scorpicore_cleaning
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
                
        with open(tools.data_dir() + "/" + day + "/" + tail + "_clean.out", "r") as fin:
            next_event_number = int(fin.readline().split()[1])
            while next_event_number:
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
            while next_event_number:
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
            while next_event_number:
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
    
#    for value in matrix:
#        print(value)
#        print()
#    
#    for i in range(len(matrix)):
#        line = []
#        if matrix[i] != []:
#            for j in range(2, len(matrix[i]), 3):
#                line.append(float(matrix[i][j]))
#        ampl_matrix.append(line)
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

for i in range(0, len(event_numbers_list), 2):
    event_numbers_and_clean_id_list.append([event_numbers_list[i], event_numbers_list[i+1]])

event_number_list_after_zero_cleaning = []
print("START CYCLE!")
#print(event_numbers_and_clean_id_list, len(event_numbers_and_clean_id_list))

event_counter = 0
for event_box in event_numbers_and_clean_id_list:
    event_number = int(event_box[0])
    event_clean_id = event_box[1]
    print("Event number ", event_number, " with ", event_clean_id, "-mode is processing...")
    matrix_with_event_data = find_the_event_for_its_number(day, event_number, event_clean_id)

    init_all_channels.init_pmts_with_zeros()
    init_all_channels.init_pmts_for_event(matrix_with_event_data, event_clean_id)
    
#    zero_cleaning_result = scorpicore_cleaning.zero_cleaning(event_number)
#    if zero_cleaning_result == 0:
#        print("Event number ", event_number, " has been rejected by zero-cleaning!")
#    else:
#        event_number_list_after_zero_cleaning.append(event_number)
#    event_counter += 1
#    tools.syprogressbar(event_counter, int(len(event_numbers_and_clean_id_list)), '#', "zero cleaning", START_TIME)
#    
#print("{} from {} is OK. {}% of events have been deleted".format(
#        len(event_number_list_after_zero_cleaning),
#        len(event_numbers_and_clean_id_list),
#        (len(event_numbers_and_clean_id_list) - len(event_number_list_after_zero_cleaning))/len(event_numbers_and_clean_id_list)))
    
    
        

#    total_counter = 1
#    not_empty_counter = 1
#    for item in Pmt.pmt.list_of_pmts:
#        total_counter += 1
#        print(item.string_of_values())
#        if item.amplitude != 0:
#            not_empty_counter += 1
#    print(total_counter, not_empty_counter)
    
    scorpicore_plotter.draw_the_event(event_number, day)

#init_all_channels.init_pmts_with_zeros()    
#init_all_channels.init_random_pmts_and_their_neighbors(10)
#scorpicore_plotter.draw_the_event(10, "random pmts with neighbors")
