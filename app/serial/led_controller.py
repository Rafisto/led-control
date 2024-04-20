"""
A layer of abstraction over serial_controller.py
Defines specific functions for the LED controller
"""
from .serial_controller import Serial


class LedController(Serial):
    """
    A function to turn on the LEDs
    """

    def on(self):
        self.write("on", lambda d: True)

    """
    A function to turn off the LEDs
    """

    def off(self):
        self.write("off", lambda d: True)
