from gpiozero import PWMOutputDevice  
from gpiozero import DigitalOutputDevice  
from time import sleep
import RPi.GPIO as g

# ALL GPIO PINS DEFINITION
PWM_DRIVE_LEFT = 21		
FORWARD_LEFT_PIN = 26	
REVERSE_LEFT_PIN = 19	 
PWM_DRIVE_RIGHT = 5	
FORWARD_RIGHT_PIN = 13	
REVERSE_RIGHT_PIN = 6

# Initial cycle frequency to 0 ~ 1000  
DriveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)  
DriveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)    
 
ForwardLeft = PWMOutputDevice(FORWARD_LEFT_PIN)  
ReverseLeft = PWMOutputDevice(REVERSE_LEFT_PIN)  
ForwardRight = PWMOutputDevice(FORWARD_RIGHT_PIN)  
ReverseRight = PWMOutputDevice(REVERSE_RIGHT_PIN)    
def allStop():  	
    ForwardLeft.value = False  	
    ReverseLeft.value = False  	
    ForwardRight.value = False  	
    ReverseRight.value = False  	
    DriveLeft.value = 0  	
    DriveRight.value = 0   
def forwardDrive():  	
    ForwardLeft.value = True  	
    ReverseLeft.value = False  	
    ForwardRight.value = True  	
    ReverseRight.value = False  	
    DriveLeft.value = 1.0  	
    DriveRight.value = 1.0    
def reverseDrive():  	
    ForwardLeft.value = False  	
    ReverseLeft.value = True  	
    ForwardRight.value = False  	
    ReverseRight.value = True  	
    DriveLeft.value = 1.0  	
    DriveRight.value = 1.0    
def spinLeft():  	
    ForwardLeft.value = False  	
    ReverseLeft.value = True  	
    ForwardRight.value = True  	
    ReverseRight.value = False  	
    DriveLeft.value = 1.0  	
    DriveRight.value = 1.0    
def spinRight():  	
    ForwardLeft.value = True  	
    ReverseLeft.value = False  	
    ForwardRight.value = False  	
    ReverseRight.value = True  	
    DriveLeft.value = 1.0  	
    DriveRight.value = 1.0    
    
def forwardTurnLeft():  	
    ForwardLeft.value = True  	
    ReverseLeft.value = False  	
    ForwardRight.value = True  
    ReverseRight.value = False  	
    DriveLeft.value = 0.2  	
    DriveRight.value = 0.8    
def forwardTurnRight():  	
    ForwardLeft.value = True
    ReverseLeft.value = False  	
    ForwardRight.value = True  	
    ReverseRight.value = False  	
    DriveLeft.value = 0.8  	
    DriveRight.value = 0.2    
def reverseTurnLeft():  	
    ForwardLeft.value = False  	
    ReverseLeft.value = True  	
    ForwardRight.value = False  	
    ReverseRight.value = True  	
    DriveLeft.value = 0.2  	
    DriveRight.value = 0.8    
def reverseTurnRight():  	
    ForwardLeft.value = False  	
    ReverseLeft.value = True  	
    ForwardRight.value = False  	
    ReverseRight.value = True  	
    DriveLeft.value = 0.8  	
    DriveRight.value = 0.2    
def main():  	
    allStop()  	
    forwardDrive()  	
    sleep(5)  	
    reverseDrive()  	
    sleep(5)  	
    spinLeft()  	
    sleep(5)  	
    spinRight()  	
    sleep(5)  	
    forwardTurnLeft()  	
    sleep(5)  	
    forwardTurnRight()  	
    sleep(5)  	
    reverseTurnLeft()  	
    sleep(5)  	
    reverseTurnRight()  	
    sleep(5)  	
    allStop()      

def mode_selection(switches):
    for i in range(len(switches)):
        if switches[i] == True:
            return i
    return -1

def action(mode):
    if mode == -1:
        return allStop()
    elif mode == 1:
        return spinLeft()
    elif mode == 2:
        return spinRight()
    

global switches
switches = [False, False, False] #가상 스위치 나열

if __name__ == "__main__":      
    #Runs at main lib module
    main()
    mode = mode_selection(switches)
    try:
        action(mode)
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        g.cleanup()

