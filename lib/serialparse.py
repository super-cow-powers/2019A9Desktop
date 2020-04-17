"""
Copyright David Miall, 2020
"""

class SerialPacket:
    def __init__(self, measurement_type, value):
        self.mType = measurement_type
        self.value = value
    def get_value(self):
        return self.value
    def get_mType(self):
        return self.mType

def required_conf(): #Returns a list of the required conf files
    list = ["serial_dev.conf"]
    return list

def required_modules():
    list = 0
    return list
    
def serialparse(serial_dev):
    packet=serialparse_packet(serial_dev)
    print(str(packet.get_value())+packet.get_mType())
    return 0
def serialparse_packet(serial_dev):
    import string
    if serial_dev == -1:
        return 0
    else : 
        output = serial_dev.readline().decode("utf-8", "ignore")
        output = ''.join(filter(lambda x: x in set(string.printable), output))
        output = output[:-1]
    output = output.split()
    output[0]=float(output[0])
    if output[1] == 'v':
        mType = 'v'
        mult = 1
    elif output[1] == 'mv':
        mType = 'mv'
        mult = 0.001
    elif output[1] == 'a':
        mType = 'a'
    elif output[1] == 'ma':
        mType = 'ma'
        mult = 0.001
    elif output[1] == 'ohm':
        mType = 'ohms'
        mult = 1
    elif output[1] == 'hz':
        mType = 'hz'
        mult = 1

    packet = SerialPacket(mType, output[0]*mult)
    return packet
