"""
A layer of abstraction over serial_controller.py
Defines specific functions for the LED controller
"""
from .serial_controller import Serial
from .validators import Validators


class LedController(Serial):

    def on(self):
        """
        A function to turn on the LEDs
        """
        self.write("on", lambda d: True)


    def off(self):
        """
        A function to turn off the LEDs
        """
        self.write("off", lambda d: True)
        
    def set_color(self, color):
        """
        A function to set the color of the LEDs
        @param color: a string representing the color in the form of 'x;y;z'
        """
        self.write(color, Validators.validate_color)