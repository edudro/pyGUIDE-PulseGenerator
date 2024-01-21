#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 11:41:17 2019

@author: Eduardo

"""
import PyDAQmx
from PyDAQmx import TaskHandle, byref, DAQmxFunctions, DAQmxConstants
from PyDAQmx.DAQmxFunctions import *
import time
from scipy import signal
import scipy
import numpy

class ContinuousPulseTrainGeneration():
    
    """ Class to create a continuous pulse train on a counter
    
    Usage:  pulse = ContinuousTrainGeneration(period [s],
                duty_cycle (default = 0.5), counter (default = "dev1/ctr0"),
                reset = True/False)
            pulse.start()
            pulse.stop()
            pulse.clear()
    """ 
    
    def __init__(self, frequency=1., duty_cycle=0.5,
                 channel = "Dev1/ctr0", reset = False):

        if reset:
            DAQmxFunctions.DAQmxResetDevice(channel.split('/')[0])
        
        taskHandle = TaskHandle(0)

        DAQmxFunctions.DAQmxCreateTask("", byref(taskHandle))  

        #
        #  CREATE AO Voltage Channel: Pulse Channel Frequency
        #                                                 
        DAQmxFunctions.DAQmxCreateCOPulseChanFreq(taskHandle,channel,
                                                  "",  
                                                  DAQmxConstants.DAQmx_Val_Hz,
                                                  DAQmxConstants.DAQmx_Val_Low, 
                                                  0.0,
                                                  frequency,
                                                  duty_cycle)

                                                  
        DAQmxFunctions.DAQmxCfgImplicitTiming(taskHandle, 
                                              DAQmxConstants.DAQmx_Val_ContSamps,
                                              1000)


        # DAQmx Write Code
        self.taskHandle = taskHandle
        
    def start(self):
        DAQmxFunctions.DAQmxStartTask(self.taskHandle)
    
    def stop(self):
        DAQmxFunctions.DAQmxStopTask(self.taskHandle)
    
    def clear(self):
        DAQmxFunctions.DAQmxClearTask(self.taskHandle)


if __name__=="__main__":
    import scipy
    import numpy

    pulse_gene1 = ContinuousPulseTrainGeneration(100,0.1, "Dev1/ctr0", reset=True)

    pulse_gene1.start()
    a = input("Generating pulse train. Press Enter to interrupt\n")
    #pulse_gene1.wait()
    pulse_gene1.stop()
    pulse_gene1.clear()