#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:00:36 2021

@author: seanlin
"""

import pandas as pd


def getZonedata(data) :
    noneCorner3 = data[(data['y'] > 7.8) & (data['y'] ** 2 + data['x'] ** 2 > 23.75 ** 2)]
    corner3 = data[(abs(data['x']) > 22) & (data['y'] <= 7.8)]
    twoPointer = data[~data.index.isin(corner3.index) & ~data.index.isin(noneCorner3.index)]
    return noneCorner3, corner3, twoPointer


def shot_zone_efg(data, threepointer):
    fgm = data['fgmade'].sum()
    fga = len(data)
    efg = (fgm + 0.5 * threepointer) / fga
    return efg
    

def get_shot_distribution(all_data, section_data) :
    return len(section_data)/len(all_data)


def getStats(data, team) : 
    data = data[data['team'] == team]
    nc3, c3, twoPoint = getZonedata(data)
    nc3_efg = shot_zone_efg(nc3, nc3['fgmade'].sum())
    c3_efg = shot_zone_efg(c3, c3['fgmade'].sum())
    twoPoint_efg = shot_zone_efg(twoPoint, 0)
    
    nc3_shot_distribution = get_shot_distribution(data, nc3)
    c3_shot_distribution = get_shot_distribution(data, c3)
    twoPoint_shot_distribution = get_shot_distribution(data, twoPoint)
    
    print(team + " non-corner 3 Shot distribution: " + str(round(nc3_shot_distribution * 100, 1)) + '%')
    print(team + " non-corner 3 eFG%: " + str(round(nc3_efg * 100, 1)) + '%')
    print(team + " Corner 3 Shot distribution: " + str(round(c3_shot_distribution * 100, 1)) + '%')
    print(team + " Corner 3 eFG%: " + str(round(c3_efg * 100, 1)) + '%')
    print(team + " Two pointer Shot distribution: " + str(round(twoPoint_shot_distribution * 100 ,1)) + '%')
    print(team + " Two pointer eFG%: " + str(round(twoPoint_efg * 100, 1)) + '%')
    print()
    return nc3_efg, nc3_shot_distribution, c3_efg, c3_shot_distribution, twoPoint_efg, twoPoint_shot_distribution
    
    

if __name__ == '__main__' :
    data = pd.read_csv('shots_data.csv')
    A_nc3_efg, A_nc3_shot_distribution, A_c3_efg, A_c3_shot_distribution, \
        A_twoPoint_efg, A_twoPoint_shot_distribution = getStats(data, 'Team A')
    B_nc3_efg, B_nc3_shot_distribution, B_c3_efg, B_c3_shot_distribution, \
        B_twoPoint_efg, B_twoPoint_shot_distribution = getStats(data, 'Team B')









