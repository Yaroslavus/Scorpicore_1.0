#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 05:04:05 2020

@author: yaroslav
"""
import Channel as cc
import Pmt
import scorpicore_tools as tools
import random

def global_init_of_all_channels_and_pmts_and_fill_txt_file ():

    with open (cc.script_dir + "/channel_factors.txt", "r") as channel_factors_file:

        for line in channel_factors_file.readlines ():
            l1 = list(line.split('\t'))
            cc.channel(cluster = int(l1[0]), number = int(l1[1]), gain = float(l1[2]), k_adc = float(l1[3]), code_per_pe = float(l1[4]), rel_sens = float(l1[5][:-1]))


    with open (cc.script_dir + "/pmt_coords.txt", "r") as pmt_coords:

        for line in pmt_coords.readlines ():
            l2 = list(line.split('\t'))
            for item in cc.channel.list_of_channels:
                if ((item.cluster == int(l2[0]) and item.number == int(l2[5])) or (item.cluster == int(l2[0]) and item.number == int(l2[6]))):
                    item.x = round(float(l2[3])*10, 3)
                    item.y = round(float(l2[4])*10, 3)
                    item.cur_count_rate_number = l2[7][:-1]
                    item.pmt_number = int(l2[1])
                    item.global_number = item.pmt_number*28 + item.cluster


    with open (cc.script_dir + "/channels.txt", "w+") as channels_file:
        channels_file.write (
                "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n\n".format (
                        "channel","pmt","cluster", "global_number", "gain",
                        "k_adc","rel_sens", "code_per_pe", "x","y",
                        "cur_count_rate_channel", "amplitude",
                        "ignore_status", "trigger_status"
                        ))

        for item in cc.channel.list_of_channels:
            channels_file.write(item.string_of_values ())
                
    with open("neighbors_table.txt", "w+") as fout:
        for channel in cc.channel.list_of_channels:
            if channel.number%2 == 0:
                Pmt.pmt(
                        global_number = channel.global_number,
                        x = channel.x,
                        y = channel.y,
                        amplitude = channel.amplitude
                        )
        max_len_of_list = 0
        for item_1 in Pmt.pmt.list_of_pmts:
            neighbors_list = []
            for item_2 in Pmt.pmt.list_of_pmts:
                distance = tools.square_root((item_1.x - item_2.x)**2 + (item_1.y - item_2.y)**2)
                if (20 <= distance <= 31) and (item_1.global_number != item_2.global_number) and (item_2.global_number not in neighbors_list):
                    neighbors_list.append(item_2.global_number)
            if len(neighbors_list) > max_len_of_list:
                max_len_of_list = len(neighbors_list)
            fout.write("{}\t{}\n".format(item_1.global_number, "\t".join([str(i) for i in neighbors_list])))
        if max_len_of_list != 6:
            print("WARNING!!! Maximum numbr of neighbors is ", max_len_of_list, " !!!")
    
    
def init_pmts_with_zeros ():
    
    with open ("channels.txt", "r") as channels_file:
        channel_strings = channels_file.readlines()
        channel_strings = channel_strings[2:]
    with open ("neighbors_table.txt", "r") as neighbors_file:  
        neighbors_matrix = neighbors_file.readlines() 
        
    for line in channel_strings:
        l = line.split()
        cc.channel(
                number = int(l[0]),
                pmt_number = int(l[1]),
                cluster = int(l[2]),
                global_number = int(l[3]),
                gain = float(l[4]),
                k_adc = float(l[5]),
                rel_sens = float(l[6]),
                code_per_pe = float(l[7]),
                x = round(float(l[8]), 3),
                y = round(float(l[9]), 3),
                cur_count_rate_number = float(l[10]),
                amplitude = float(l[11])
                       )
    for channel_item in cc.channel.list_of_channels:
        if channel_item.number%2 == 0:
            for line in neighbors_matrix:
                line = line.split()
                neighbors_global_number = int(line[0])
                if (neighbors_global_number == channel_item.global_number) and (neighbors_global_number != 0):
                    neighbors_line = [int(number) for number in line[1:]]
                    Pmt.pmt(
                            global_number = neighbors_global_number,
                            x = channel_item.x,
                            y = channel_item.y,
                            amplitude = 0,
                            neighbors_list = neighbors_line
                            )

def init_pmts_for_event (matrix, event_clean_id):
        
    for line in matrix:
        cluster_number_from_event = int(line[0]) + 1
        ampl_string = line[2:]
            
        if event_clean_id == "c":
            for i in range(0, len(ampl_string), 2):
                pmt_number_from_event = i//2 + 1
                ampl = float(ampl_string[i])
                low_high_channel_oddity_from_event = int(ampl_string[i+1])
    
                for channel in cc.channel.list_of_channels:

                    if (channel.cluster == cluster_number_from_event and
                        channel.pmt_number == pmt_number_from_event and
                        channel.number%2 == low_high_channel_oddity_from_event):
                        output_amplitude = 0 if ampl/channel.code_per_pe < 0 else ampl/channel.code_per_pe
                        
                for pmt_item in Pmt.pmt.list_of_pmts:

                    if pmt_item.global_number == 28*pmt_number_from_event + cluster_number_from_event:
                        pmt_item.amplitude = round(output_amplitude, 3)

        elif (event_clean_id == "d" or event_clean_id == "s"):
            for i in range(0, len(ampl_string), 3):
                pmt_number_from_event = i//3 + 1
                ampl = float(ampl_string[i])
                low_high_channel_oddity_from_event = int(ampl_string[i+1])
                ignore_status = int(ampl_string[i+2])
                
                for channel in cc.channel.list_of_channels:
                    if (channel.cluster == cluster_number_from_event and
                        channel.pmt_number == pmt_number_from_event and
                        channel.number%2 == low_high_channel_oddity_from_event):
                        output_amplitude = 0 if ampl/channel.code_per_pe < 0 else ampl/channel.code_per_pe
                        
                for pmt_item in Pmt.pmt.list_of_pmts:
                    if pmt_item.global_number == 28*pmt_number_from_event + cluster_number_from_event:
                        pmt_item.amplitude = output_amplitude
                        pmt_item.ignore_status = ignore_status
#                            for line in neighbors_matrix:
#                                line = line.split()
#                                global_number = int(line[0])
#                                if global_number == pmt_item.global_number:
#                                    neighbors_line = [int(number) for number in line[1:]]
#                                    pmt_item.neighbors_list = neighbors_line
                        
                        
#    counter_1 = 0
#    counter_2 = 0
#    for pmt_item in Pmt.pmt.list_of_pmts:
#        counter_2 += 1
#        if pmt_item.amplitude != 0:
##            print(pmt_item.global_number, pmt_item.amplitude)
#            counter_1 += 1
#    print("Non zero pmts after init: ", counter_1, "from ", counter_2)
#    if counter_1 == 0:
#        print("WARNING !!!")
    

def init_random_pmts_and_their_neighbors (number_of_pmts):
    
    random_list = []
    for _ in range (number_of_pmts):
        random_list.append(random.randint(1, 28)*28 + random.randint(1,22))
    print(random_list)

    for pmt_item in Pmt.pmt.list_of_pmts:
        if pmt_item.global_number in random_list:
            pmt_item.amplitude = 10
            for pmt_item_n in Pmt.pmt.list_of_pmts:
                if pmt_item_n.global_number in pmt_item.neighbors_list:
                    pmt_item_n.amplitude = 5

        
        
        
        
        