'''
In-Class Exercise 1: Temperature Converter
Date: August 26, 2024

* Make sure you submit this file as "day_1_converter.py"

----------------------------------------------------------
Authors:
- Isaac Sussman
- Ethan Zeh
----------------------------------------------------------

End Product: Program with a text-based UI that converts between different units of temperature. 

Spec:
- Complete the function celcius_to_fahrenheit() that converts a temperature in Celcius to the equivalent temperature in Farenheit.
    F = (C - 32) * (9/5)
- Ask the user to input a temperature in Celcius, convert it to the equivalent temperature in Fahrenheit, and then print the temperature in Fahrenheit.
- Create another function that converts a temperature in Farenheit to Celcius.
- Allow the user to choose whether they want to convert from Celcius to Fahrenheit or from Fahrenheit to Celcius, and then do the corresponding conversion
- Create a loop that allows the user to do as many conversions as they like until they type "quit".
~~~BONUS~~~
- Add conversion functionality for other temperatures as well: 
    • Kelvin
    • Rankine
    • Réaumur
    • Delisle
'''

# Functions
## Converts Celcius to Farenheit
def fahrenheit_to_celsius(temperature) :
    return (temperature - 32) * (9/5)

def celsius_to_fahrenheit(temperature) :
    return (temperature * (5/9)) + 32

# ˚

# The Program
if __name__ == "__main__" :
    ## Introduction
    print('''
    ----------------------------------------------
    | Welcome to the Temperature Conversion Device |
    | Author: Isaac Sussman and Ethan Zeh          |
    | Date: 8/26/24                                |
    ----------------------------------------------
    ''', end="\n")
    temp = input("Input Temperature in C˚: ")
    

    ## Main ##
