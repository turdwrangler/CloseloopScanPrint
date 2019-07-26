import serial
from gcodeprocessor import gcodeprocessor
import subprocess
import os

if __name__ == "__main__":
    filename="input.gcode"
    dirname=os.getcwd()
    gcodeprocessor(filename)
    ser = serial.Serial('COM8', 9600)
    check = "G-Code"
    f = open("output.gcode")
    scanlineout=open(dirname+"//scanoutput//layer0.csv",'w')
    lines = f.readlines()
    f.close()
    i=0
   
    filenumber=0;

    for i in range(0,len(lines),1):
        
        while (check != "$\n"):
            check = ser.read_until()
            check = check.decode()
            print(check)
    
        if (lines[i] == "M118 69\n"):
            print ("New Layer: "+filenumber+'\n')
            scanlineout.close()
            scanlineout=open(dirname+"//scanoutput//layer"+filenumber+".csv",'w')
            filenumber=filenumber + 1
            
            
        if (lines[i] == "M118 420\n"):
            print("Scaned")
            scanline=subprocess.check_output([dirname+'\\scanner\\x64\\Debug\\scanner.exe','-l']).splitlines()
            scanlineout.write(scanline[0].decode()+'/n')
            
        if(lines[i].find(";")==0):
            print("ignoring comment")
        else:
            ser.write(lines[i].encode())
            check=""  
        print(lines[i])
        
    
    ser.close()
    print("Print finished")