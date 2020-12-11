from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Feet
from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Inch
from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import QuantityMeasurement
from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Lengths
from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Volumes
from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Weights
from com.bridgelabz.QuantityMeasurement.QuantityMeasurement import Tempretures

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
    cm = QuantityMeasurement(Lengths.CENTIMETER, 30.0)
    assert feet.compare(cm)

#Compare One Yard and Ninety Centimeter and Return True
def test_givenOneYardAndNinetyCm_WhenCompared_ShouldReturnTrue():
    yard = QuantityMeasurement(Lengths.YARD, 1.0)
    cm = QuantityMeasurement(Lengths.CENTIMETER, 90.0)
    assert yard.compare(cm)


#UC4-TC1- Add Two Inch and Two Inch and Should Return Sum
def test_givenTwoInchAndTwoInch_WhenAdded_ShouldReturnSumInInches():
    first_inch = QuantityMeasurement(Lengths.INCH, 2.0)
    second_inch = QuantityMeasurement(Lengths.INCH, 2.0)
    assert first_inch.add(second_inch) == 4.0

#TC2- Add One Feet and Two Inch and Should Return Sum
def test_givenOneftAndTwoInch_WhenAdded_ShouldReturnSumInInches():
    feet = QuantityMeasurement(Lengths.FEET, 1.0)
    inch = QuantityMeasurement(Lengths.INCH, 2.0)
    assert inch.add(feet) == 14.0

#TC3- Add One Feet and One Feet and Should Return Sum
def test_givenOneftAndOneFt_WhenAdded_ShouldReturnSumInInches():
    first_feet = QuantityMeasurement(Lengths.FEET, 1.0)
    second_feet = QuantityMeasurement(Lengths.FEET, 1.0)
    assert first_feet.add(second_feet) == 24.0

#TC4- Add Two Inch and Two Point Five Centimeter and Should Return Sum
def test_givenTwoInchAndTwoPointFiveCm_WhenAdded_ShouldReturnSumInInches():
    inch = QuantityMeasurement(Lengths.INCH, 2.0)
    cm = QuantityMeasurement(Lengths.CENTIMETER, 2.5)
    assert inch.add(cm) == 3.0

#TC5- Compare One Litre and One Litre and Should Return True
def test_givenOneLitreAndOneLitre_WhenCompared_ShouldReturnTrue():
    first_litre = QuantityMeasurement(Volumes.LITRE, 1.0)
    second_litre = QuantityMeasurement(Volumes.LITRE, 1.0)
    assert first_litre == second_litre

#TC1- Compare One Gallon and Three Point Seven Eight Litres and Should Return True
def test_givenOneGallonAndThreePointSeven_WhenCompared_ShouldReturnTrue():
    gallon = QuantityMeasurement(Volumes.GALLON, 1.0)
    litre = QuantityMeasurement(Volumes.LITRE, 3.78)
    assert gallon.compareVolume(litre)

#TC2- Compare One Litre and Thousand ML and Should Return True
def test_givenOneLitreAndThousandMl_WhenCompared_ShouldReturnTrue():
    litre = QuantityMeasurement(Volumes.LITRE, 1.0)
    ml = QuantityMeasurement(Volumes.ML, 1000.0)
    assert litre.compareVolume(ml)

#UC6- Add One Gallon and Three POint Seven Litre and Should Return Sum
def test_givenOneGallaonAndThreePointSevenLitre_WhenAdded_ShouldReturnSumInLitres():
    litre = QuantityMeasurement(Volumes.LITRE, 3.78)
    gallon = QuantityMeasurement(Volumes.GALLON, 1.0)
    assert litre.addVolume(gallon) == 7.56

#UC6- Add One Litre and Thousand ML and Should Return Sum
def test_givenOneLitreAndThousandMl_WhenAdded_ShouldReturnSumInLitres():
    litre = QuantityMeasurement(Volumes.LITRE, 1.0)
    ml = QuantityMeasurement(Volumes.ML, 1000.0)
    assert litre.addVolume(ml) == 2.0

#UC7- Compare One KG and One KG and Should Return True
def test_givenOneKgAndOneKg_WhenCompared_ShouldRreturnTrue():
    first_kg = QuantityMeasurement(Weights.KG, 1.0)
    second_kg = QuantityMeasurement(Weights.KG, 1.0)
    assert first_kg.compareWeight(second_kg)

#TC1- Compare One KG and Thousand Grams and Should Return True
def test_givenOneKgAndThousandGrams_WhenCompared_ShouldRreturnTrue():
    kg = QuantityMeasurement(Weights.KG, 1.0)
    grams = QuantityMeasurement(Weights.GRAMS, 1000.0)
    assert kg.compareWeight(grams)

#TC2- Compare One Tonne and Thousand KG and Should Return True
def test_givenOneTonneAndThousandKg_WhenCompared_ShouldRreturnTrue():
    tonne = QuantityMeasurement(Weights.TONNE, 1.0)
    kg = QuantityMeasurement(Weights.KG, 1000.0)
    assert kg.compareWeight(tonne)

#TC3- Add One Tonne and Thousand Gram and Return Sum
def test_given_oneTonneAndThousandGram_WhenAdded_ShouldReturnSumInKgs():
    tonne = QuantityMeasurement(Weights.TONNE, 1.0)
    kg = QuantityMeasurement(Weights.GRAMS, 1000.0)
    assert kg.addWeight(tonne) == 1001.0

#UC8- Compare One Celcius and One Celcius and Should Return True
def test_givenOneCelciusAndOneCelcius_WhenCompared_ShouldReturnTrue():
    first_celsius = QuantityMeasurement(Tempretures.CELCIUS, 1.0)
    second_celcius = QuantityMeasurement(Tempretures.CELCIUS, 1.0)
    assert first_celsius.compareTemp(second_celcius)

#UC8- Compare One Farenheit and One Farenheit and Should Return True
def test_givenOneFarenheitAndOneFarenheit_WhenCompared_ShouldReturnTrue():
    first_Farenheit = QuantityMeasurement(Tempretures.FAHRENHEIT, 1.0)
    second_Farenheit = QuantityMeasurement(Tempretures.FAHRENHEIT, 1.0)
    assert first_Farenheit.compareTemp(second_Farenheit)

#UC8- Compare Hundered Celcius and TwoHunderedAndTwelve Farenheit and Should Return True
def test_givenHunderedCelciusAndTwoHunderedAndTwelveFarenheit_WhenCompared_ShouldReturnTrue():
    celsius = QuantityMeasurement(Tempretures.CELCIUS, 100.0)
    farenheit = QuantityMeasurement(Tempretures.FAHRENHEIT, 212)
    assert celsius.compareTemp(farenheit)

#UC8- Compare TwoHunderedAndTwelve Farenheit and Hundered Celcius and Should Return True
def test_givenTwoHunderedAndTwelveFarenheitAndHunderedCelcius_WhenCompared_ShouldReturnTrue():
    farenheit = QuantityMeasurement(Tempretures.FAHRENHEIT, 212)
    celcius = QuantityMeasurement(Tempretures.CELCIUS, 100)
    assert celcius.compareTemp(farenheit)
