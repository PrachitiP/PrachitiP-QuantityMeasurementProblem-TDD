import enum

class Feet:
    def __init__(self, feet):
        self.feet = feet

    def __eq__(self, other):
        if isinstance(other, Feet):
            return self.feet == other.feet
        elif isinstance(other, Inch):
            return self.feet == other.inch/12
        return False

class Inch:
    def __init__(self, inch):
        self.inch = inch

    def __eq__(self, other):
        if isinstance(other, Inch):
            return self.inch == other.inch
        elif isinstance(other, Feet):
            return self.inch == other.feet * 12
        return False

class QuantityMeasurement:
    def __init__(self, unit, value):
        self.unit = unit
        self.value = value

    def __eq__(self, other):
        if isinstance(other, QuantityMeasurement):
            return self.value == other.value
        return False

    def compare(self, other):
        if isinstance(self.unit, Lengths) and isinstance(other.unit, Lengths):
            if Lengths.convert(self.unit, self.value) == Lengths.convert(other.unit, other.value):
                return True
        return False

    def compareVolume(self, other):
        if isinstance(self.unit, Volumes) and isinstance(other.unit, Volumes):
            if Volumes.convert(self.unit, self.value) == Volumes.convert(other.unit, other.value):
                return True
        return False

    def compareWeight(self, other):
        if isinstance(self.unit, Weights) and isinstance(other.unit, Weights):
            if Weights.convert(self.unit, self.value) == Weights.convert(other.unit, other.value):
                return True
        return False

    def compareTemp(self, other):
        if isinstance(self.unit, Tempretures) and isinstance(other.unit, Tempretures):
            if Tempretures.convert(self.unit, self.value) == Tempretures.convert(other.unit, other.value):
                return True
        return False

    def add(self, other):
        if isinstance(self.unit, Lengths) and isinstance(other.unit, Lengths):
            return Lengths.convert(self.unit, self.value) + Lengths.convert(other.unit, other.value)
        return 0

    def addVolume(self, other):
        if isinstance(self.unit, Volumes) and isinstance(other.unit, Volumes):
            return Volumes.convert(self.unit, self.value) + Volumes.convert(other.unit, other.value)
        return 0

    def addWeight(self, other):
        if isinstance(self.unit, Weights) and isinstance(other.unit, Weights):
            return Weights.convert(self.unit, self.value) + Weights.convert(other.unit, other.value)
        return 0


class Lengths(enum.Enum):
    FEET = 12.0
    INCH = 1.0
    YARD = 36.0
    CENTIMETER = 0.4

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value

class Volumes(enum.Enum):
    LITRE = 1.0
    GALLON = 3.78
    ML = 0.001

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value

class Weights(enum.Enum):
    KG = 1.0
    GRAMS = 0.001
    TONNE = 1000

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value

class Tempretures(enum.Enum):
    CELCIUS = 100
    FAHRENHEIT = 212

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        if self.unit == self.value:
            if self.value == Tempretures.CELCIUS:
                return (value * 9 / 5) + 32
            elif self.value == Tempretures.FAHRENHEIT:
                return value * self.unit / 212
        return False

