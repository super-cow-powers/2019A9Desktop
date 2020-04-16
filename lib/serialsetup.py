

def required_conf(): #Returns a list of the required conf files
    list = ["serial_dev.conf"]
    return list
def required_modules(): #Returns a list of the required conf files
    return 0

    
def serialsetup():
    print("Not directly runnable")

def return_dev():
    import serial
    f = open("conf/serial_dev.conf", "r")
    dev = f.read()
    try:
        ser = serial.Serial(dev, 9600)
    except serial.serialutil.SerialException:
        print("No device at " + dev)
        return -1
    return ser

def close(dev):
    dev.close()
