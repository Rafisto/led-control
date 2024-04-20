"""
Serial Controller to communicate with the Arduino device.
"""
import serial
import time


class Serial(object):

    def __init__(self, device='/dev/ttyACM0', baud_rate=9600, restart_on_connect=True):
        """
        Initialize a Serial device specifying:
        @param device: linux device location
        @param baud_rate: serial communication baud rate
        @param restart_on_connect: wait for serial to restart on establishing a new connection
        """
        try:
            self.device = serial.Serial(device, baud_rate)
        except Exception as e:
            raise ConnectionError(f"Unable to connect to the desired device: {device}. Error message: {e}")
        # Arduino restarts a device the moment a new serial connection is established
        if restart_on_connect:
            time.sleep(2)


    def write(self, message, validator) -> None:
        """
        A function to write a serial message
        @param message: string message to send 
        @param validator: validator function to check whether the message is valid
        """
        if message is None or len(message) == 0:
            raise ValueError(f"Message must not be empty.")
        if e := validator(message):
            self.device.write(message.encode())
        else:
            raise ValueError(f"Message is not valid: {message} validator has thrown: {e}")
