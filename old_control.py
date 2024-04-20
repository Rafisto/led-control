import serial
import sys
import time

aliases = {
    "red": "255;0;0",
    "green": "0;255;0",
    "blue": "0;0;255",
    "yellow": "255;255;0",
    "cyan": "0;255;255",
    "pink": "255;0;255",
    "orange": "255;165;0",
    "magenta": "255;192;203",
    "brown": "165;42;42",
    "lightblue": "173;216;230",
    "gold": "255;215;0"
}

class Control(object):
    def __init__(self):
        self.com = serial.Serial('/dev/ttyACM0',9600)
        time.sleep(2)

    def write(self, message: str) -> None:
        self.com.write(message.encode())

    def on(self):
        self.write("on")


    def off(self):
        self.write("off")

    
    def set_color(self, c: str):
        if c in aliases:
            self.write(aliases[c])


if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv) > 4:
        print("Usage: python old_control.py colors")
        print("Usage: python old_control.py <message>")
        print("Usage: python old_control.py <color_alias>")
        print("Usage: python old_control.py <r> <g> <b>")
        sys.exit(1)
    elif len(sys.argv) < 4:
        message = sys.argv[1]
        if message in aliases.keys():
            message = aliases[message]
        if message == "colors":
            for color, rgb_values in aliases.items():
                r, g, b = map(int, rgb_values.split(';'))
                ansi_color = f"\033[38;2;{r};{g};{b}m ██{color} \033[0m"
                print(ansi_color, end='')
            print('\n')
            sys.exit(0)
    elif len(sys.argv) == 4:
        message = f"{sys.argv[1]};{sys.argv[2]};{sys.argv[3]}"

    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(2)

    ser.write(message.encode())
    ser.close()

