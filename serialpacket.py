class SerialPacket:
    def __init__(self, measurement_type, value):
        self.mType = measurement_type
        self.value = value
    def get_value(self):
        return self.value
    def get_mType(self):
        return self.mType
