#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 05:04:05 2020

@author: yaroslav
"""
import channel_class as cc

def init_all_channels_as_class_objects_and_fill_txt_file ():

    with open (cc.script_dir + "/channel_factors.txt", "r") as channel_factors_file:

        for line in channel_factors_file.readlines ():
            l1 = list(line.split('\t'))
            cc.channel(cluster = int(l1[0]), number = int(l1[1]), gain = l1[2], k_adc = l1[3], code_per_pe = l1[4], rel_sens = l1[5][:-1])

#    cc.channel.list_of_channels[100].show_item()
#    print (str(len(cc.channel.list_of_channels)) + "   channels filled by gain, k_adc, code_per_pe, rel_sens, cluster, number")

    with open (cc.script_dir + "/pmt_coords.txt", "r") as pmt_coords:

        for line in pmt_coords.readlines ():
            l2 = list(line.split('\t'))
            for item in cc.channel.list_of_channels:
                if ((item.cluster == int(l2[0]) and item.number == int(l2[5])) or (item.cluster == int(l2[0]) and item.number == int(l2[6]))):
                    item.x = round(float(l2[3])*10, 3)
                    item.y = round(float(l2[4])*10, 3)
                    item.cur_count_rate_number = l2[7][:-1]
                    item.pmt_number = int(l2[1])


    with open (cc.script_dir + "/channels.txt", "w+") as channels_file:
        channels_file.write (
                "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n\n".format (
                        "channel","pmt","cluster", "gain","k_adc","rel_sens", "code_per_pe", "x","y", "cur_count_rate_channel", "amplitude"
                        ))

        for item in cc.channel.list_of_channels:
            channels_file.write(item.string_of_values ())
    
    
def init_channels ():
    
    with open (cc.script_dir + "/channels.txt", "r") as channels_file:
        
        for line in channels_file.readlines ():
            l = list(line.split('\t'))
            cc.channel(
                    number = int(l[0]),
                       pmt_number = int(l[1]),
                       cluster = int(l[2]),
                       gain = l[3],
                       k_adc = l[4],
                       rel_sens = l[5],
                       code_per_pe = l[6],
                       x = round(float(l[7])*10, 3),
                       y = round(float(l[8])*10, 3),
                       cur_count_rate_channel = l[9],
                       amplitude = l[10]
                       )
        
