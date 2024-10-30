#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright 2024 University of Oxford. All Rights Reserved.
The authors, being Dr Scot Wheeler, have asserted their moral rights.

This is the module docstring. It can be used to introduce the purpose and
key functionality of the module. It will appear in documentation/help.
As an example, in the spyder help window (top right subwindow be default), 
type scipy.optimize to see an example of the docstring for the 
optimize module of the scipy library.

The very first line of the script is an optional shebang line. It tells the 
operating system which interpreter to use to execute the code if the script 
was treated as a stadalone executable.
"""

# import required libraries
import math
import numpy as np
import pandas as pd

# =============================================================================
# Basic conditional battery function
# =============================================================================
def battery_charge_action(soc, power, E_tot, P_max, T):
    """
    This is a docstring. Use it to explain to the user what a function does.
    It will automatically be read by 'help' functions such as in spyder.
    
    This function decides if to charge or discharge a battery based on a 
    simple conditional battery model, within a single time period of length T
    hours.

    Parameters
    ----------
    soc: float
        The state of charge (in energy units kWh) of battery at start of period.
    power: float
        The power demand (units of power e.g. kW)
    E_tot: float
        The energy capacity of the battery (in energy units kWh)
    P_max: float
        The maximum power capacity of the battery (in power units kW)
    T: float
        The length of time of a single period. Default is 1.

    Returns
    --------
    soc: float
        The updated state of charge of a battery at the end of period.
    net_demand: float
        The net demand post battery operation.
    """
    
    E_demand = T*power
    soc_iterate = soc
    delta_Energy = 0
    
    if power > 0:  # excess demand - discharge the battery
        # calculate the energy discharged within a single time period.
        # think about the physical constraints of the battery (e.g. energy stored, power capacity)
        # think about if your energy is positive or negative
        delta_Energy = min(E_demand, P_max*T, soc) 
        
            
        
    elif power < 0:  # excess generation - charge the battery
        # calculate the energy charged within a single time period.
        # think about the physical constraints of the battery (e.g. energy stored, power capacity)
        # think about if your energy is positive or negative
        delta_Energy = min(E_demand, -P_max*T, E_tot - soc)
    
    # update soc and calculate net_power
        
    soc -= delta_Energy
    net_power = delta_Energy/T
    
    return soc, net_power


# =============================================================================
# Basic conditional battery class
# =============================================================================
class Battery():
    """
    Battery object docstring
    """

    def __init__(self, b_id, E_tot=13.5, P_max=11.5, soc_0=7.0, model="Tesla Powerwall"):
        self.id = b_id
        self.model = model
        self.E_tot = E_tot
        self.P_max = P_max
        self.soc_0 = soc_0
        self.soc = soc_0  # initialise to initial SOC

    def battery_charge_action(self, power, T):

        # add you conditional battery model from above, adjusting to include
        # the self keyword.
        if power > 0:  # excess demand - discharge the battery
            deltaE = -1 * min(self.P_max * T, self.soc, power * T)
        elif power < 0:  # excess generation - charge the battery
            deltaE = min(self.P_max * T, (self.E_tot - self.soc), -1 * power * T)
        else:
            deltaE = 0
        self.soc += deltaE
        net_power = power + (deltaE / T)
        return net_power


if __name__ == "__main__":
    # =============================================================================
    # This section is a common way to incorporate code that you want to run if the 
    # script is executed directly, but will be ignored if the script is 
    # imported as a module into another. 
    # 
    # It separates the executable part of the script from the part that defines
    # reusable components e.g. functions.
    # 
    # This is useful way of testing the code or providing examples of how to 
    # use the code.
    # =============================================================================
    
    
    
    pass