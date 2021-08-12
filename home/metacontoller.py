# Motor Driver and GPIO Pin configuration refers to following:
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO          
from time import sleep
from constant_variables import *

class MetaController():
    def __init__(self):
        self.motor_power = 0
        self.motor_power_sensor = 0

        self.motor_speed = None
        self.motor_direction = None

        self.DutyCycle = None
        self.DCMotor = GPIO.PWM(EN, 1000)
        self.msg = """
            Welcome! Motor has started.
        """
        self.goodbye="""
            Goodbye.
        """

    def set_MotorSpeed(self):
        try:
            if self.motor_speed == LOW_SPEED:
                self.DCMotor.ChangeDutyCycle(25)
                print("Duty cycle set to LOW")
            elif self.motor_speed == MEDIUM_SPEED:
                self.DCMotor.ChangeDutyCycle(50)
                print("Duty cycle set to MEDIUM")
            elif self.motor_speed == HIGH_SPEED:
                self.DCMotor.ChangeDutyCycle(75)
                print("Duty cycle set to HIGH")
            else:
                self.DCMotor.ChangeDutyCycle(25)
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

    def dcmotor_start(self, pin):
        self.DCMotor.start(pin)

    def terminate(self):
        GPIO.cleanup()
        print("EVERYTHING TERMINATED")

    def run(self):
        if PSEUDO_MEMBRANE_SWITCH == 0:
            self.Rotate_Stop()
            print("Rotate Stop!")

        elif PSEUDO_MEMBRANE_SWITCH == 1:
            tmp =0
            self.motor_power_sensor += 1
            if self.motor_power_sensor != tmp:
                self.motor_power +=1
                tmp =0
                
            self.set_MotorSpeed()
            self.Rotate_CCW()
            print("Rotate CCW")


        elif PSEUDO_MEMBRANE_SWITCH == 2:
            self.motor_speed = MEDIUM_SPEED

            self.set_MotorSpeed()
            self.Rotate_CW()
            print("Rotate CW")

        else:
            self.Rotate_Stop()