# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:10:31 2019

@author: Sadben khan

scanmov

this function will take inputs and return a list containing the motions and commands to be 
written into the g-code output file.
"""

def scanmov(Sx,Sy,Sz,scan,nlyr,feedrate,samplerate,distance,layernumber,layerheight,relay):
    import numpy as np
    commands=[]
    commands.append(';Scan for layer#'+str(layernumber-1)+'\n')
    #commands.append(toolchange) #use this only if a tool change command is necessary
    commands.append('G0 '+'X'+str(Sx)+' '+'Y'+str(Sy)+' '+'Z'+str(Sz+layernumber*layerheight)+' '+'\n')
    #commands.append(delay +"\n")
    commands.append(relay)
    commands.append(nlyr+"\n")
    #commands.append(delay+"\n")
    commands.append('G0'+' '+'F'+str(feedrate)+'\n')
    #Major Development Note: Figure out CR-10 axis directions, Assume X for now
    for i in np.arange(0,distance,samplerate):
        commands.append('G0 X'+str(Sx+i)+'\n')
        #commands.append(delay+'\n')
        commands.append(scan+'\n')
       
        #commands.append(delay+'\n')
    return commands

def main():
    #toolchange="T2"
    scan=";G420" # Calls the required G-Code command to send 420 to the computer through the USB Interface
    relay= ";M226 P30 1 \n"
    nlyr=";G69"  # Calls the required G-code command to send 69 to the computer through the USB interface
    feedrate= 6400
    samplerate=0.1
    distance=1
    Sx=40 # scanner x initial position 
    Sy=35 # scanner y initial position
    Sz=33 # scanner z initial position
    #delay=";G4 P50"
    n=4
    layerheight=0.1
    commands=[]
    commands=scanmov(Sx,Sy,Sz,scan,nlyr,feedrate,samplerate,distance,n,layerheight,relay)
    f=open('testlinescan11.gcode','w')
    for i in range(0,len(commands),1):
        f.write(commands[i])
    print(commands)
    f.close()
if __name__== "__main__":
  main()