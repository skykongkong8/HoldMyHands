import RPi.GPIO as GPIO          
from constant_variables import *
from metacontoller import MetaController

def GPIO_initialization():
    """Initial Configuration of GPIO PIN"""
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(IN_1, GPIO.OUT)
    GPIO.setup(IN_2, GPIO.OUT)
    GPIO.setup(EN, GPIO.OUT)

    GPIO.setup(PSEUDO_MEMBRANE_SWITCH['RED_STOP'], GPIO.IN)
    GPIO.setup(PSEUDO_MEMBRANE_SWITCH['YELLOW_CW'], GPIO.IN)
    GPIO.setup(PSEUDO_MEMBRANE_SWITCH['GREEN_CCW'], GPIO.IN)

    GPIO.output(IN_1, GPIO.LOW)
    GPIO.output(IN_2, GPIO.LOW)


if __name__ == "__main__":

    GPIO_initialization()
    
    """MetaController Instance"""
    Motor = MetaController()
    Motor.dcmotor_start(EN)
    print(Motor.msg)

    while True:
        try:
            Motor.run()

        except KeyboardInterrupt as e:
            print("Error : {e}\n".format(e))
        except:
            print("Error : Unknown Error!\n")

        finally:
            print(Motor.Goodbye)
            Motor.terminate()
            