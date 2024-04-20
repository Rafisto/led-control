import os, pty

from app.serial.led_controller import LedController

# mock a serial controller
master, slave = pty.openpty()
serial_name = os.ttyname(slave)


# test serial connection
def test_led_controller_connection():
    controller = LedController(serial_name)


# test non-existing serial_name
def test_non_existing_serial_controller():
    try:
        LedController(serial_name + "_non-existing", restart_on_connect=False)
        raise Exception("The controller should've thrown an error")
    except ConnectionError as e:
        assert str(e).startswith("Unable to connect to the desired device")


# test turning the LEDs on
def test_led_on():
    controller = LedController(serial_name, restart_on_connect=False)
    controller.on()


# test turning the LEDs off
def test_led_off():
    controller = LedController(serial_name, restart_on_connect=False)
    controller.off()
