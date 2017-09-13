class TemperatureConvertor(object):
    def __init__(self, temp, initial_unit="C"):
        self.temp = temp
        self.unit = initial_unit

    @property
    def fah(self):
        if self.unit == "F":
            return self.temp
        else:
            return self.temp * 1.8 + 32


    @fah.setter
    def fah(self, value):
        self.unit = "F"
        self.temp = value

    @property
    def cel(self):
        if self.unit == "C":
            return self.temp
        else:
            return (self.temp - 32) / 1.8

    @cel.setter
    def cel(self, value):
        self.unit = "C"
        self.temp = value
