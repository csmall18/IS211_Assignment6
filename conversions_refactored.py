# Cameorn Small
# Week 6
import conversions

temp = ["Celsius", "Fahrenheit", "Kelvin"]
distance = ["miles", "yards", "meters"]

class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    temp1_match = False
    temp2_match = False
    dist1_match = False
    dist2_match = False
    compatible_temps = False
    compatible_dists = False

    if fromUnit == toUnit:
        print(f"{value} {fromUnit} is equal to {value} {toUnit}")
        return value

    for units in temp:
        if fromUnit == units:
            temp1_match = True
        if toUnit == units:
            temp2_match = True

    if temp1_match and temp2_match: # After unit match, calculate the conversion
        compatible_temps = True
        if fromUnit == "Celsius" and toUnit == "Fahrenheit":
            result = conversions.convertCelsiusToFahrenheit(value)
            return result
        if fromUnit == "Fahrenheit" and toUnit == "Celsius":
            result = conversions.convertFahrenheitToCelsius(value)
            return result
        if fromUnit == "Celsius" and toUnit == "Kelvin":
            result = conversions.convertCelsiusToKelvin(value)
            return result
        if fromUnit == "Kelvin" and toUnit == "Celsius":
            result = conversions.convertKelvinToCelsius(value)
            return result
        if fromUnit == "Fahrenheit" and toUnit == "Kelvin":
            result = conversions.convertFahrenheitToKelvin(value)
            return result
        if fromUnit == "Kelvin" and toUnit == "Fahrenheit":
            result = conversions.convertKelvinToFahrenheit(value)
            return result    

    for units in distance:
        if fromUnit == units:
            dist1_match = True
        if toUnit == units:
            dist2_match = True

    if dist1_match and dist2_match: # After unit match, calculate the conversion
        compatible_dists = True
        if fromUnit == "miles" and toUnit == "yards":
            result = conversions.milesToYards(value)
            print(f"{value} miles is equal to {result} yards")
            return result
        if fromUnit == "yards" and toUnit == "miles":
            result = conversions.yardsToMiles(value)
            print(f"{value} yards is equal to {result} miles")
            return result
        if fromUnit == "miles" and toUnit == "meters":
            result = conversions.milesToMeters(value)
            print(f"{value} miles is equal to {result} meters")
            return result
        if fromUnit == "meters" and toUnit == "miles":
            result = conversions.metersToMiles(value)
            print(f"{value} meters is equal to {result} miles")
            return result
        if fromUnit == "yards" and toUnit == "meters":
            result = conversions.yardsToMeters(value)
            print(f"{value} yards is equal to {result} meters")
            return result
        if fromUnit == "meters" and toUnit == "yards":
            result = conversions.metersToYards(value)
            print(f"{value} meters is equal to {result} yards")
            return result

    if (compatible_temps == False) or (compatible_dists == False):
        print("Conversion not possible")
        raise ConversionNotPossible("Conversion not possible")

    return 0
