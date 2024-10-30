#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:21:25 2024

@author: williamrawlings
"""

import math as m


class Roof():
    def __init__(self, width, height, angle):
        self.width = width
        self.height = height
        self.angle = angle


class PV_Panel():
    def __init__(self, length, height, power):
        self.length = length
        self.height = height
        self.power = power
        

roof = Roof(0,0,0)
roof.width = float(input("Building Width: "))
roof.height = float(input("Building Length: "))
roof.angle = float(input("Roof Angle: "))

pv = PV_Panel(0,0,0)
pv.length = float(input("Panel Length: "))
pv.height = float(input("Panel Height: "))
pv.power = float(input("Panel Power: "))

rads = m.radians(roof.angle)
cos = m.cos(rads)
print(rads,cos)

roof_length = roof.width/cos
print(roof_length)

total_panels_width = m.trunc((2*((roof_length/2)/pv.length)))
print(total_panels_width)
total_panels_height = roof.height//(pv.height)
print(total_panels_height)
panels = total_panels_height*total_panels_width
print(panels)
capacity =pv.power*panels
print(capacity)
                                        

    
        
    
    
        

