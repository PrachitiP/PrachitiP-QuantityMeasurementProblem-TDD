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

    def compare(self, other):
        if isinstance(self.unit, Lengths) and isinstance(other.unit, Lengths):
            if Lengths.convert(self.unit, self.value) == Lengths.convert(other.unit, other.value):
                return True
        return False
    
    def add(self, other):
    if isinstance(self.unit, Lengths) and isinstance(other.unit, Lengths):
        return Lengths.convert(self.unit, self.value) + Lengths.convert(other.unit, other.value)
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
