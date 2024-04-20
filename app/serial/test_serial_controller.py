import os, pty

from app.serial.serial_controller import Serial

# mock a serial controller
master, slave = pty.openpty()
serial_name = os.ttyname(slave)


# test serial connection
def test_serial_controller():
    ser = Serial(serial_name)
    assert ser is not None


# test non-existing serial_name
def test_non_existing_serial_controller():
    try:
        Serial(serial_name + "_non-existing", restart_on_connect=False)
        raise Exception("The controller should've thrown an error")
    except ConnectionError as e:
        assert str(e).startswith("Unable to connect to the desired device")


# test writing to serial with validated query
def test_serial_controller_write():
    ser = Serial(serial_name, restart_on_connect=False)
    ser.write("hello", lambda x: True)
    ser.write("world", lambda x: True)


# test writing to serial with invalid query
def test_serial_controller_invalid():
    ser = Serial(serial_name, restart_on_connect=False)
    try:
        ser.write("hello", lambda x: False)
        raise Exception("The controller should've thrown an error")
    except ValueError as e:
        assert str(e).startswith("Message is not valid")


# test writing edge case
def test_serial_controller_write_edge_case():
    ser = Serial(serial_name, restart_on_connect=False)
    try:
        ser.write("", lambda x: True)
        raise Exception("The controller should've thrown an error")
    except ValueError as e:
        assert str(e) == "Message must not be empty."
