/*
____________  ___  ___  ___ _____ _____ 
|  ___| ___ \/ _ \ |  \/  ||  ___/  ___|
| |_  | |_/ / /_\ \| .  . || |__ \ `--. 
|  _| |    /|  _  || |\/| ||  __| `--. \
| |   | |\ \| | | || |  | || |___/\__/ /
\_|   \_| \_\_| |_/\_|  |_/\____/\____/ 
                                        
 Sadben Khan , Program v1 07/02/19             */

// scanner.cpp :This shit is fucked and barely works, just take it and go and never contact me for help

////headers
#include "pch.h" //precompiled header
#include <iostream> //input output through command line
#include <WinSock2.h> // windows TCP/IP Library
#include <Windows.h> //i hate windows
#include <fstream> //file writing
#include <vector> //vector library
#include <string> //self explanitory, 
#pragma comment(lib, "ws2_32.lib")
#pragma comment(lib,"LJV7_IF.lib")
#include "LJV7_IF.h" //Keyence Driver
#include "LJV7_ErrorCode.h" //Error code file for Keyence Driver
using namespace std;
//header complete


int main()
{
	
	HINSTANCE dll = LoadLibrary(L"LJV7_IF.dll");

	/*if (dll == NULL)
	{
		std::cout << "Dll Not loaded";
	}
	else
	{
		std::cout << "Dll Loaded"<<endl;
		std::cout << "DLL version: "<< LJV7IF_GetVersion()<<endl;
	}
*/
	LJV7IF_Initialize(); //start dll file
	long lDeviceId = 1;
	//profile variable definitions
	LJV7IF_PROFILE_INFO pprofileInfo;
	DWORD dwProfileDataSize = 3230; // figure out how big the buffer should actually be, 
	std::vector<int> vecProfileData(807);//dwProfileDataSize / (sizeof(unsigned int))); header and footer included, see refrence manual which is pretty shit
	LJV7IF_MEASURE_DATA aMeasureData[LJV7IF_OUT_COUNT];
	////////////////

	 long outusb= LJV7IF_UsbOpen(lDeviceId);
	  //std::cout << "Usb Open Error code: " << outusb ;
	
	LJV7IF_ClearMemory(lDeviceId);

				//trigger laser
				
				//long out2 = 
					LJV7IF_Trigger(lDeviceId);
				//std::cout << "Trigger error code: " << out2 << endl;
	
					//std::cout << buffer << endl;

				//long outprofile = 

				LJV7IF_GetProfileAdvance(lDeviceId, &pprofileInfo, (DWORD*)&vecProfileData.at(0), dwProfileDataSize, aMeasureData);

				//
				//std::cout << " Advanced Profile Error code: " << outprofile << endl;
			
				//for (int i = 6; i < vecProfileData.size() - 1; i++)
				//{
				//	output << vecProfileData[i] << ","; // units in nm

				//}
				//output << endl;
				int output[807];

				for (int i = 6; i < vecProfileData.size() - 1; i++)
				{
					output[i]=vecProfileData[i]; // units in nm
					cout<< vecProfileData[i] << ','; // units in nm
				}

				LJV7IF_ClearMemory(lDeviceId);
			
				//return output;
	
}


