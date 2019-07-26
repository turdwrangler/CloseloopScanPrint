import serial
from gcodeprocessor import gcodeprocessor

if __name__ == "__main__":
    filename="input.gcode"
    gcodeprocessor(filename)
    ser = serial.Serial('COM17', 9600)
    check = "G-Code"
    f = open("output.gcode")
    lines = f.readlines()
    f.close()
    i=0

    for i in range(0,len(lines),1):
        
        while (check != "$\n"):
            check = ser.read_until()
            check = check.decode()
            print(check)
    
        if (lines[i] == "M118 69\n"):
            print ("Found the 69")
            
        if (lines[i] == "M118 420\n"):
            print("Found the 420")
            
        ser.write(lines[i].encode())
        print(lines[i])
        check=""  
    
    ser.close()
    print("Print finished")