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
            Welcome! Motor is initialized.
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
        if self.motor_power == 0:
            self.motor_speed = LOW_SPEED
        elif self.motor_power == 1:
            self.motor_speed - MEDIUM_SPEED
        elif self.motor_speed == 2:
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

    def membrane_switch_checker(self):
        stop = GPIO.input(PSEUDO_MEMBRANE_SWITCH['RED_STOP'])
        cw = GPIO.input(PSEUDO_MEMBRANE_SWITCH['YELLOW_CW'])
        ccw = GPIO.input(PSEUDO_MEMBRANE_SWITCH['GREEN_CCW'])
        return [stop, cw, ccw]

    def is_anything_on(self, list):
        for pin in list:
            if pin == ON:
                return pin
        return OFF

    def count_button_press(self, button, cnt):
        if button == ON:
            cnt += 1
            if cnt >= 3:
                # count by 0, 1, 2 and go back to 0
                cnt = 0
        return cnt

    def _switch_checker(self):
        button_list = self.membrane_switch_checker()
        pin = self.is_anything_on(button_list)
        if pin:
            return pin

    def green_switch_checker(self, cnt):
        green = GPIO.input(GREEN_CCW)
        if green:
            cnt += 1
            if cnt >= 3:
                cnt =0
        return cnt

    def red(self):
        self._switch_checker()
        self.Rotate_Stop()

    def green(self):
        self.set_MotorSpeed()
        self.Rotate_CCW()

    def yellow(self):
        self.set_MotorSpeed()
        self.Rotate_CW()


    def run(self):
        membrane_switch_status = self.membrane_switch_checker()

        if membrane_switch_status[RED] == ON:
            print("Rotate Stop!")
            while True:
                if self._switch_checker() in [GREEN, YELLOW]:
                    break
                self.red()

        elif membrane_switch_status[GREEN] == ON:
            print("Rotate CCW")
            self.motor_speed = LOW_SPEED
            while True:
                if self._switch_checker() in [RED, YELLOW]:
                    break
                self.motor_power = self.green_switch_checker(self.motor_power) 
                self.green


        elif membrane_switch_status[YELLOW] == ON:
            print("Rotate CW")
            self.motor_speed = MEDIUM_SPEED
            while True:
                if self._switch_checker() in [GREEN, RED]:
                    break
                self.yellow()

        else:
            self.Rotate_Stop()