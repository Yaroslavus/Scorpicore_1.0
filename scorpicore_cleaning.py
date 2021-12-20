#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:00:43 2021

@author: yaroslav
"""
import Pmt
import scorpicore_plotter
#import scorpicore_tools as tools


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
            
#def topological_cleaning(event_number, border_threshold):
#    
#        print("Topological cleaning for event {} with treshold {} is providing...".format(event_number, border_threshold))
#        cleaned_pmt_counter = 0
#        for pmt_item in Pmt.pmt.list_of_pmts:
#            if pmt_item.amplitude < 0:
#                pmt_item.amplitude = 0
#                cleaned_pmt_counter += 1
#        print(cleaned_pmt_counter, "/", len(Pmt.pmt.list_of_pmts), "pmt have been cleaned for border threshold.")
#
#        spot_counter = 0
#        for pmt_item_1 in Pmt.pmt.list_of_pmts:
#            if (pmt_item_1.amplitude != 0) and (pmt_item_1.spot_id == 0):
#                for pmt_item_2 in Pmt.pmt.list_of_pmts:
#                    if (pmt_item_2.global_number in pmt_item_1.neighbors_list) and (pmt_item_2.spot_id != 0):
#                        pmt_item_1.spot_id = pmt_item_2.spot_id
#                        break
#                if pmt_item_1.spot_id == 0:
#                    spot_counter += 1
#                    pmt_item_1.spot_id = spot_counter
#
#        for pmt_item in Pmt.pmt.list_of_pmts:
#            if pmt_item_1.spot_id != 0:
#                print("here")
#                print(pmt_item_1.spot_id)
                        
#        for pmt_item in Pmt.pmt.list_of_pmts:
#            if pmt_item.amplitude != 0:
#                print(pmt_item.string_of_values())
#####################################################################################################

#        print(spot_counter)
#        spot_size = [0]*(spot_counter+1)
#        for pmt_item in Pmt.pmt.list_of_pmts:
#                if pmt_item.spot_id != 0:
#                    spot_size[spot_counter + 1] += 1
#
#        for spot_number in range(len(spot_size)):
#            print(spot_number, spot_size[spot_number])
                
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################                
def topological_cleaning_1(event_number, min_border_threshold, max_border_threshold):
    
        print("Topological cleaning for event {} with min_treshold {} and max_threshold {} is providing...".format(
                                                                                                            event_number,
                                                                                                            min_border_threshold,
                                                                                                            max_border_threshold))        
        cleaned_pmt_counter = 0
        for pmt_item in Pmt.pmt.list_of_pmts:
            if (pmt_item.amplitude < min_border_threshold) or (pmt_item.amplitude > max_border_threshold):
                pmt_item.amplitude = 0
                cleaned_pmt_counter += 1
        print(cleaned_pmt_counter, "/", len(Pmt.pmt.list_of_pmts), "pmt have been cleaned for border threshold.")
####################################################################################################
####################################################################################################
        container_1, container_2 = [], []
        spot_counter = 0

        for pmt_item_1 in Pmt.pmt.list_of_pmts:
            if (pmt_item_1.amplitude != 0) and (pmt_item_1.spot_id == 0):
                spot_counter += 1
                pmt_item_1.spot_id = spot_counter
                container_1.append(pmt_item_1)                
                for pmt_item_2 in Pmt.pmt.list_of_pmts:
                    if (pmt_item_2.global_number in pmt_item_1.neighbors_list) and (pmt_item_2.spot_id == 0) and (pmt_item_2.amplitude != 0):
                        pmt_item_2.spot_id = spot_counter
                        container_2.append(pmt_item_2)
#                        print(pmt_item_2.global_number, pmt_item_2.spot_id)
#                if len(container_2) != 0: print([i.global_number for i in container_2])
                while len(container_2) != 0:
                    container_1 = container_2
                    container_2 = []
                    for pmt_item_3 in container_1:
                        for pmt_item_4 in Pmt.pmt.list_of_pmts:
                            if (pmt_item_4.global_number in pmt_item_3.neighbors_list) and (pmt_item_4.spot_id == 0) and (pmt_item_4.amplitude != 0):
                                pmt_item_4.spot_id = spot_counter
                                container_2.append(pmt_item_4)

        spot_size = [0]*(spot_counter+1)
        for pmt_item in Pmt.pmt.list_of_pmts:
            if pmt_item.spot_id != 0:
                spot_size[pmt_item.spot_id] += 1
                
        max_spot_id = max(enumerate(spot_size), key=lambda x: x[1])[0]
        
        for pmt_item in Pmt.pmt.list_of_pmts:
            if pmt_item.spot_id != max_spot_id:
                pmt_item.amplitude = 0
                        
                        
                    
