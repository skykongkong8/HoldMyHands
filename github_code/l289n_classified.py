# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/
# https://github.com/jumejume1/pi-l298n-dc-motor/blob/master/l298n_dc.py

import RPi.GPIO as GPIO          
from time import sleep
from constant_variables import *



class MetaController():
    def __init__(self):
        self.motor_power = 0
        self.motor_speed = None
        self.motor_direction = None
        self.DutyCycle = None
        
        self.DCMotor = GPIO.PWM(EN, 1000)

    def set_MotorSpeed(self):
        try:
            if self.motor_speed == LOW_SPEED:
                p.ChangeDutyCycle(25)
                print("Duty cycle set to LOW")
            elif self.motor_speed == MEDIUM_SPEED:
                p.ChangeDutyCycle(50)
                print("Duty cycle set to MEDIUM")
            elif self.motor_speed == HIGH_SPEED:
                p.ChangeDutyCycle(75)
                print("Duty cycle set to HIGH")
            else:
                p.ChangeDutyCycle(25)
                print("Speed input undetected! Set to DEFAULT : LOW")
        except:
            print("Error : Motor speed setting Failed!")

    def classify_motor_speed(self):
        if self.motor_power == 1:
            self.motor_speed = LOW_SPEED
        elif self.motor_power == 2:
            self.motor_speed - MEDIUM_SPEED
        elif self.motor_speed == 3:
            self.motor_speed = HIGH_SPEED
        else:
            self.motor_speed == LOW_SPEED
        

    def Rotate_CCW(self):
        GPIO.output(IN_1,GPIO.HIGH)
        GPIO.output(IN_2,GPIO.LOW)

    def Rotate_CW(self):
        GPIO.output(IN_1,GPIO.LOW)
        GPIO.output(IN_2,GPIO.HIGH)

    def Rotate_Stop(self):
        GPIO.output(IN_1,GPIO.LOW)
        GPIO.output(IN_2,GPIO.LOW)

    def MotorStart(self):
        if self.motor_direction == 'CCW':
            self.Rotate_CCW()
        elif self.motor_direction == 'CW':
            self.Rotate_CW()
        else:
            self.Rotate_Stop()

    def Test_Run(self):
        print("Test Run")
        GPIO.output(IN_1, GPIO.HIGH)
        GPIO.output(IN_2, GPIO.LOW)
        print("Print forward")
        sleep(3)

        GPIO.output(IN_1, GPIO.LOW)
        GPIO.output(IN_2, GPIO.HIGH)
        print("backward")
        sleep(3)

    def terminate(self):
        GPIO.cleanup()
        print("EVERYTHING TERMINATED")


if __name__ == "__main__":
    Motor = MetaController()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IN_1, GPIO.OUT)
    GPIO.setup(IN_2, GPIO.OUT)
    GPIO.setup(EN, GPIO.OUT)

    GPIO.output(IN_1, GPIO.LOW)
    GPIO.output(IN_2, GPIO.LOW)

    p=GPIO.PWM(EN, 1000)

    p.start(EN)
    
    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
    print("\n")    

    while True:
        try:
            if PSEUDO_MEMBRANE_SWITCH == 0:
                Motor.Rotate_Stop()

            elif PSEUDO_MEMBRANE_SWITCH == 1:
                Motor.motor_power += 1
                Motor.set_MotorSpeed()
                Motor.Rotate_CCW()

            elif PSEUDO_MEMBRANE_SWITCH == 2:
                Motor.motor_speed = MEDIUM_SPEED

                Motor.set_MotorSpeed()
                Motor.Rotate_CW()

            else:
                Motor.Rotate_Stop()

        except KeyboardInterrupt:
            print("Error : Keyboard Interrupt Error!\n")
        except:
            print("Error : Unknown Error!\n")
        
        finally:
            Motor.terminate()