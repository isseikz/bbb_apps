#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
RMTR1 = "P9_13"
RMTR2 = "P9_12"
RMTRSPEED = "P9_14"
LMTR1 = "P9_15"
LMTR2 = "P9_16"
LMTRSPEED = "P9_22"
motormode = None

def send_motorgpio(rmtrs1, rmtrs2, lmtrs1, lmtrs2):
    GPIO.output(RMTR1, rmtrs1)
    GPIO.output(RMTR2, rmtrs2)
    GPIO.output(LMTR1, lmtrs1)
    GPIO.output(LMTR2, lmtrs2)

def set_motorspeed(speed):
    PWM.set_duty_cycle(RMTRSPEED, speed)
    PWM.set_duty_cycle(LMTRSPEED, speed)

def stop_motor():
    send_motorgpio(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW)
    set_motorspeed(0)

def slow_down():
    send_motorgpio(GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH)
    set_motorspeed(0)

def drive_motor(rmtrs1, rmtrs2, lmtrs1, lmtrs2, mstate):
    global motormode
    if(motormode != None) and (motormode != mstate):
        stop_motor()
        time.sleep(0.1)
    send_motorgpio(rmtrs1, rmtrs2, lmtrs1, lmtrs2)
    motormode = mstate

def go_forward(speed):
    drive_motor(GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW, 'F')
    set_motorspeed(speed)

def go_backward(speed):
    drive_motor(GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, 'B')
    set_motorspeed(speed)

def turn_right(speed):
    drive_motor(GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, 'R')
    set_motorspeed(speed)

def turn_left(speed):
    drive_motor(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH, 'L')
    set_motorspeed(speed)

def initialize_motor():
    GPIO.setup(RMTR1, GPIO.OUT)
    GPIO.setup(RMTR2, GPIO.OUT)
    GPIO.setup(LMTR1, GPIO.OUT)
    GPIO.setup(LMTR2, GPIO.OUT)
    PWM.start(RMTRSPEED, 0, 20)
    PWM.start(LMTRSPEED, 0, 20)
    stop_motor()

def finalize_motor():
    stop_motor()
    GPIO.cleanup()
    PWM.stop(RMTRSPEED)
    PWM.stop(LMTRSPEED)
    PWM.cleanup()

def main():
    initialize_motor()
    go_forward(100)
    time.sleep(1.0)
    go_backward(100)
    time.sleep(1.0)
    slow_down()
    time.sleep(1.0)
    turn_right(70)
    time.sleep(1.0)
    turn_left(100)
    time.sleep(1.0)
    stop_motor()
    finalize_motor()

if __name__ == '__main__':
    main()
