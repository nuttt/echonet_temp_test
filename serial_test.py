#!/usr/bin/python
import serial
import RPi.GPIO as gpio

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()

def teardown():
  gpio.cleanup()
  ser.close()

def setup():
  # RPI Pin Config
  gpio.setmode(gpio.BOARD)
  reset_pin = 26
  gpio.setup(reset_pin, gpio.OUT)

  # resetting Arduino
  gpio.output(reset_pin, False)
  gpio.output(reset_pin, True)

  # flush old tty input
  ser.flush()
  ser.flushInput()

# main code
try:
  setup()
  while True:
    response = ser.readline().strip()
    try:
      temp = float(response)
      print temp
      teardown()
      break
    except ValueError:
      pass

except KeyboardInterrupt:
  teardown()

