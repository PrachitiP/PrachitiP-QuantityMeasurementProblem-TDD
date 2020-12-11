from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Feet
from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Inch
from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import QuantityMeasurement
from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Lengths

import pytest

def test_givenZeroFtAndZeroFt_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = Feet(0.0)
    assert first_feet == second_feet

def test_givenZeroFtAndNone_WhenCompared_ShouldReturnFalse():
    first_feet = Feet(0.0)
    assert first_feet is not None

def test_givenTwoSameFeetValues_WhenComparedForReference_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = first_feet
    assert first_feet == second_feet

def test_givenZeroFtAndFloatValue_WhenCompared_ShouldReturnFalse():
    first_feet = Feet(0.0)
    second_feet = float(0.0)
    assert  first_feet != second_feet

def test_givenOneFtAndOneFt_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(1.0)
    second_feet = Feet(1.0)
    assert first_feet == second_feet

def test_givenOneFtAndTwoFt_WhenCompared_ShouldReturnFalse():
    first_feet = Feet(1.0)
    second_feet = Feet(2.0)
    assert first_feet != second_feet

def test_givenZeroInchAndZeroInch_WhenCompared_ShouldReturnTrue():
    first_inch = Inch(0.0)
    second_inch = Inch(0.0)
    assert first_inch == second_inch

def test_givenZeroInchAndNone_WhenCompared_ShouldReturnFalse():
    first_inch = Inch(0.0)
    assert first_inch is not None

def test_givenTwoSameInchValues_WhenComparedForReference_ShouldReturnTrue():
    first_inch = Inch(0.0)
    second_inch = first_inch
    assert first_inch == second_inch

def test_givenZeroInchAndFloatValue_WhenCompared_ShouldReturnFalse():
    first_inch = Inch(0.0)
    second_inch = float(0.0)
    assert  first_inch != second_inch

def test_givenOneInchAndOneInch_WhenCompared_ShouldReturnTrue():
    first_inch = Inch(1.0)
    second_inch = Inch(1.0)
    assert first_inch == second_inch

def test_givenOneInchAndTwoInch_WhenCompared_ShouldReturnFalse():
    first_inch = Inch(1.0)
    second_inch = Inch(2.0)
    assert first_inch != second_inch

#UC1
def test_givenOneFtAndTwelveInch_WhenCompared_ShouldReturnTrue():
    feet = Feet(1.0)
    inch = Inch(12.0)
    assert feet == inch
def test_givenTwelveInchAndOneFt_WhenCopared_ShouldReturnTrue():
    inch = Inch(12.0)
    feet = Feet(1.0)
    assert inch == feet

#UC2-Compare Three Feet And One Yard and Return True
def test_givenThreeFtAndOneYard_WhenCompared_ShouldReturnTrue():
    feet = QuantityMeasurement(Lengths.FEET, 3.0)
    yard = QuantityMeasurement(Lengths.YARD, 1.0)
    assert feet.compare(yard)

#UC2-TC1- Compare One Feet and One Feet and Return True
def test_givenOneFtAndOneYard_WhenCompared_ShouldReturnFalse():
    feet = QuantityMeasurement(Lengths.FEET, 1.0)
    yard = QuantityMeasurement(Lengths.YARD, 1.0)
    assert feet.compare(yard) == False

#UC2-TC2- Compare One Inch and One Yard and Return False
def test_givenOneInchAndOneYard_WhenCompared_ShouldReturnFalse():
    inch = QuantityMeasurement(Lengths.INCH, 1.0)
    yard = QuantityMeasurement(Lengths.YARD, 1.0)
    assert inch.compare(yard) == False

#UC2-TC3- Compare One Yard and Thirty Six Inch and Return True
def test_givenOneYardAndThirtySixInch_WhenCompared_ShouldReturnTrue():
    yard = QuantityMeasurement(Lengths.YARD, 1.0)
    inch = QuantityMeasurement(Lengths.INCH, 36.0)
    assert yard.compare(inch)

#UC2-TC4- Compare Thirty Six Inch and One Yard and Return True
def test_givenThirtySixInchAndOneYard_WhenCompared_ShouldReturnTrue():
    inch = QuantityMeasurement(Lengths.INCH, 36.0)
    yard = QuantityMeasurement(Lengths.YARD, 1.0)
    assert inch.compare(yard)

#UC2-TC5- Compare One Yard and Three Feet and Return True
def test_givenOneYardAndThreeFt_WhenCompared_ShouldReturnTrue():
    yard = QuantityMeasurement(Lengths.YARD, 1.0)
    feet = QuantityMeasurement(Lengths.FEET, 3.0)
    assert yard.compare(feet)

#UC3- Compare One Centimeter and One Centimeter and Return True
def test_givenOneCmAndOneCm_WhenCompared_ShouldReturnTrue():
    first_cm = QuantityMeasurement(Lengths.CENTIMETER, 1.0)
    second_cm = QuantityMeasurement(Lengths.CENTIMETER, 1.0)
    assert first_cm.compare(second_cm)

#Compare Two Inch and Five Centimeter and Return True
def test_givenTwoInchAndFiveCm_WhenCompared_ShouldReturnTrue():
    inch = QuantityMeasurement(Lengths.INCH, 2.0)
    cm = QuantityMeasurement(Lengths.CENTIMETER, 5.0)
    assert inch.compare(cm)

#Compare One Inch and One Centimeter and Return True
def test_givenOneInchAndOneCm_WhenCompared_ShouldReturnFalse():
    inch = QuantityMeasurement(Lengths.INCH, 1.0)
    cm = QuantityMeasurement(Lengths.CENTIMETER, 1.0)
    assert not inch.compare(cm)

#Compare One Feet and Thirty Centimeter and Return True
def test_givenOneFeetAndThirtyCm_WhenCompared_ShouldReturnTrue():
    feet = QuantityMeasurement(Lengths.FEET, 1.0)
    cm = QuantityMeasurement(Lengths.CM, 30.0)
    assert feet.compare(cm)

#Compare One Yard and Ninety Centimeter and Return True
def test_givenOneYardAndNinetyCm_WhenCompared_ShouldReturnTrue():
    yard = QuantityMeasurement(Lengths.YARD, 1.0)
    cm = QuantityMeasurement(Lengths.CM, 90.0)
    assert yard.compare(cm)

