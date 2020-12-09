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

