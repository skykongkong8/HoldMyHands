from constant_variables import PWM_DRIVE_LEFT, PWM_DRIVE_RIGHT, REVERSE_LEFT_PIN,REVERSE_RIGHT_PIN, FORWARD_RIGHT_PIN, FORWARD_LEFT_PIN,
from gpiozero import PWMOutputDevice  


class MetaController():
    def __init__(self):
        DriveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)  
        DriveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)    
        ForwardLeft = PWMOutputDevice(FORWARD_LEFT_PIN)  
        ReverseLeft = PWMOutputDevice(REVERSE_LEFT_PIN)  
        ForwardRight = PWMOutputDevice(FORWARD_RIGHT_PIN)  
        ReverseRight = PWMOutputDevice(REVERSE_RIGHT_PIN)    
    
    def allStop(self):  	
        """Everything goes to Zero and False"""
        self.ForwardLeft.value = False  	
        self.ReverseLeft.value = False  	
        self.ForwardRight.value = False  	
        self.ReverseRight.value = False  	
        self.DriveLeft.value = 0  	
        self.DriveRight.value = 0   

    def forwardDrive(self):  	
        self.ForwardLeft.value = True  	
        self.ReverseLeft.value = False  	
        self.ForwardRight.value = True  	
        self.ReverseRight.value = False  	
        self.DriveLeft.value = 1.0  	
        self.DriveRight.value = 1.0    

    def reverseDrive(self):  	
        self.ForwardLeft.value = False  	
        self.ReverseLeft.value = True  	
        self.ForwardRight.value = False  	
        self.ReverseRight.value = True  	
        self.DriveLeft.value = 1.0  	
        self.DriveRight.value = 1.0    

    def spinLeft(self):  	
        self.ForwardLeft.value = False  	
        self.ReverseLeft.value = True  	
        self.ForwardRight.value = True  	
        self.ReverseRight.value = False  	
        self.DriveLeft.value = 1.0  	
        self.DriveRight.value = 1.0    

    def spinRight(self):  	
        self.ForwardLeft.value = True  	
        self.ReverseLeft.value = False  	
        self.ForwardRight.value = False  	
        self.ReverseRight.value = True  	
        self.DriveLeft.value = 1.0  	
        self.DriveRight.value = 1.0    
        
    def forwardTurnLeft(self):  	
        self.ForwardLeft.value = True  	
        self.ReverseLeft.value = False  	
        self.ForwardRight.value = True  
        self.ReverseRight.value = False  	
        self.DriveLeft.value = 0.2  	
        self.DriveRight.value = 0.8    

    def forwardTurnRight(self):  	
        self.ForwardLeft.value = True
        self.ReverseLeft.value = False  	
        self.ForwardRight.value = True  	
        self.ReverseRight.value = False  	
        self.DriveLeft.value = 0.8  	
        self.DriveRight.value = 0.2    

    def reverseTurnLeft(self):  	
        self.ForwardLeft.value = False  	
        self.ReverseLeft.value = True  	
        self.ForwardRight.value = False  	
        self.ReverseRight.value = True  	
        self.DriveLeft.value = 0.2  	
        self.DriveRight.value = 0.8    

    def reverseTurnRight(self):  	
        self.ForwardLeft.value = False  	
        self.ReverseLeft.value = True  	
        self.ForwardRight.value = False  	
        self.ReverseRight.value = True  	
        self.DriveLeft.value = 0.8  	
        self.DriveRight.value = 0.2    
    
    def emergency_protocol(self):
        pass