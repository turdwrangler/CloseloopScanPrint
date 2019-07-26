# -*- coding: utf-8 -*-
"""
____________  ___  ___  ___ _____ _____ 
|  ___| ___ \/ _ \ |  \/  ||  ___/  ___|
| |_  | |_/ / /_\ \| .  . || |__ \ `--. 
|  _| |    /|  _  || |\/| ||  __| `--. \
| |   | |\ \| | | || |  | || |___/\__/ /
\_|   \_| \_\_| |_/\_|  |_/\____/\____/ 
                                        
 Sadben Khan , Program v1 07/02/19             */
Created on Thu Jul 25 15:45:09 2019
Python code using ctypes to call the laser scanner function
@author: IRB1200\
\\scanner\\x64\\Debug
"""

import subprocess
import os
def scanlines():
    dirname=os.getcwd()
    scanline=subprocess.check_output([dirname+'\\scanner\\x64\\Debug\\scanner.exe','-l']).splitlines()
    return scanline

if __name__ == "__main__":
    scanline=scanlines()
    print("Welcome to the rice fields mother fucker!")
    print(scanline)
    