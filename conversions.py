# Cameorn Small
# Week 6

def convertCelsiusToKelvin(celsius):
    # Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins
    kelvins = celsius + 273.15
    print(f"{celsius}°C is equal to {kelvins}K")
    return kelvins


def convertCelsiusToFahrenheit(celsius):
    # Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
    return fahrenheit

def convertFahrenheitToCelsius(fahrenheit):
    # Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")
    return celsius

def convertFahrenheitToKelvin(fahrenheit):
    # Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvins
    celsius = (fahrenheit - 32) * 5/9
    kelvins = celsius + 273.15
    print(f"{fahrenheit}°F is equal to {kelvins}K")
    return kelvins

def convertKelvinToCelsius(kelvin):
    # Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius
    celsius = kelvin - 273.15
    print(f"{kelvin}K is equal to {celsius}°C")
    return celsius

def convertKelvinToFahrenheit(kelvin):
    # Takes in a float representing a Kelvin measurement, and returns that temperature converted into Fahrenheit
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"{kelvin}K is equal to {fahrenheit}°F")
    return fahrenheit

# Distance conversion functions

def milesToYards(miles):
    # Takes in a float representing a distance in miles, and returns that distance converted into yards
    yards = miles * 1760
    print(f"{miles} miles is equal to {yards} yards")
    return yards

def milesToMeters(miles):
    # Takes in a float representing a distance in miles, and returns that distance converted into meters
    meters = miles * 1609.34
    print(f"{miles} miles is equal to {meters} meters")
    return meters

def yardsToMiles(yards):
    # Takes in a float representing a distance in yards, and returns that distance converted into miles
    miles = yards / 1760
    print(f"{yards} yards is equal to {miles} miles")
    return miles

def yardsToMeters(yards):
    # Takes in a float representing a distance in yards, and returns that distance converted into meters
    meters = yards * 0.9144
    print(f"{yards} yards is equal to {meters} meters")
    return meters

def metersToMiles(meters):
    # Takes in a float representing a distance in meters, and returns that distance converted into miles
    miles = meters / 1609.34
    print(f"{meters} meters is equal to {miles} miles")
    return miles

def metersToYards(meters):
    # Takes in a float representing a distance in meters, and returns that distance converted into yards
    yards = meters / 0.9144
    print(f"{meters} meters is equal to {yards} yards")
    return yards
