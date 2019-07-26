# -*- coding: utf-8 -*-
"""
Custom Scan G-code Generator 
Date:10/07/19
Written by: Sadben

Description

This code is used to create custom G-code for moving laser scanner  using the repetier hardware
Future Release will include:
    Import G-code then modify per layer
    
    Code Functionality :
        
        1. File is inputted after main(filename.gcode,# layers,spacing)
         1.1 A copy of the file will be made for backup purposes (optional)
        2. G-code file is read through to find new layer Tags
        3. When a New Layer tag is reached , Scan(z,TCP) is called
        4. Scan.py will append the motion code to the existing g-code file

"""
#import libraries


def gcodeprocessor(filename):   
    import numpy as np
    from scanmov import scanmov
    #filename='12.gcode'
    # G-Code command list # Pull this from a .dat file later 
    scan="M118 420" # Calls the required G-Code command to send 420 to the computer through the USB Interface
    nlyr="M118 69"  # Calls the required G-code command to send 69 to the computer through the USB interface
    feedrate= 6400
    samplerate=0.1
    distance=180
    Sx=40 # scanner x initial position 
    Sy=35 # scanner y initial position
    Sz=33 # scanner z initial position
    #delay="M400"
    relay= "M400"
    layerheight=0.14
    
    f=open(filename,'r')
    lines = f.readlines()
    f.close()
    n=1 # layer number
    
    line_numbers=np.array([0]) #variable to hold the line number where layer change occurs
    for i in range(0,len(lines),1):    
        #check line for New layer tag
        if lines[i]==('; layer '+ str(n)+'\n'): # find new layers
            # append to new array 
            line_numbers=np.append(line_numbers,[i])
            n=n+1
        elif lines[i]==('; layer end\n'): # find the position of the last layer
            line_numbers=np.append(line_numbers,[i])
    
    ### Split the code into layer blocks 
    f=open('output.gcode','w') #create output file for new g-code with modifications
    
    for i in range(1,n+1,1):
        #append imported G-code files with the layer scan gcode
        for j in np.arange(line_numbers[i-1],line_numbers[i]+1,1):
            #print(j)
            f.write(lines[int(j)])
        commands=scanmov(Sx,Sy,Sz,scan,nlyr,feedrate,samplerate,distance,n,layerheight,relay) #generate path move commands
        
        for l in range(0,len(commands)-1,1):
            f.write(commands[l])
    
    for k in np.arange(line_numbers[n],float(len(lines)),1):
        f.write(lines[int(k)])
        
    f.close()
    #return line_numbers,lines
    