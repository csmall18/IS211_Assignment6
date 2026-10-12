# Cameron Small
# Week 6

import conversions
import conversions_refactored

conversions.convertFahrenheitToCelsius(212)
conversions.convertFahrenheitToKelvin(212)
conversions.convertKelvinToCelsius(373.15)
conversions.convertKelvinToFahrenheit(373.15)
conversions.convertCelsiusToFahrenheit(100)
conversions.convertCelsiusToKelvin(100)

conversions_refactored.convert("Fahrenheit", "Celsius", 212)
conversions_refactored.convert("Fahrenheit", "Kelvin", 212)
conversions_refactored.convert("Kelvin", "Celsius", 373.15)
conversions_refactored.convert("Kelvin", "Fahrenheit", 373.15)
conversions_refactored.convert("Celsius", "Fahrenheit", 100)
conversions_refactored.convert("Celsius", "Kelvin", 100)
conversions_refactored.convert("miles", "yards", 1)
conversions_refactored.convert("yards", "miles", 1760)
conversions_refactored.convert("miles", "meters", 1)
conversions_refactored.convert("meters", "miles", 1609.34)
conversions_refactored.convert("yards", "meters", 1)
conversions_refactored.convert("meters", "yards", 0.9144)

conversions_refactored.convert("miles", "miles", 212) # Test converting the same unit
conversions_refactored.convert("Fahrenheit", "miles", 212) # Test converting incompatible units
