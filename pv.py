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
        self.angle = m.radians(angle)


class PV_Panel():
    def __init__(self, length, height, power):
        self.length = length/1000
        self.height = height/1000
        self.power = power
        

roof = Roof(0,0,0)
roof.width = int(input("Building Width: "))
roof.height = int(input("Building Length: "))
roof.angle = int(input("Roof Angle: "))

pv = PV_Panel(0,0,0)
pv.length = int(input("Panel Length: "))
pv.height = int(input("Panel Height: "))
pv.power = int(input("Panel Power: "))

roof_length = roof.width/(m.cos(roof.angle))
total_panels_width = width = 2*((roof_length/2)//pv.length)
total_panels_height = roof.height//(pv.height)
panels = total_panels_height*total_panels_width
capacity =pv.power*panels
print(capacity)
                                        



    
        
    
    
        

