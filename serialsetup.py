"""
Copyright David Miall, 2020
"""
def return_dev():
    import serial
    f = open("conf/serial_dev.conf", "r")
    dev = f.read()
    try:
        ser = serial.Serial(dev, 9600)
    except serial.serialutil.SerialException:
        print("No device at " + dev)
        print("Enter 'rescan' to recheck for device")
        return -1
    return ser

def close(dev):
    dev.close()

