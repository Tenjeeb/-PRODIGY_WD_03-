# Function to convert Celsius to Fahrenheit and Kelvin
def celsius_to_fahrenheit(c):
    return(c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

# Function to convert Fahrenheit to Celsius and Kelvin
def farhenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

# Function to convert kelvin to Celsius and Fahrenheit 
def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return ( k -273.15) * 9/5 + 32

# Funcation to handle conversion based on the input unit
def convert_temperature(value, unit):
    unit = unit.lower()

    # Conversion from Celsius
    if unit == "celsius" or unit == "c":
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        print(f"{value}°C is equal to {f:.2f}°F and {k:.2f}k")

    # Conversion from Fahrenheit
    elif unit == "fahrenheit" or unit == "f":
        c = farhenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        print(f"{value}°F is equal to {c:.2f}°C and {k:.2f}k")

    # Conversion from Kelvin
    elif unit == "kelvin" or unit == "k":
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        print(f"{value}°K is equal to {c:.2f}°C and {f:.2f}k")

    # If invalid input is entered
    else:
        print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")


#---- Main program ----
try:
    temp = float(input("Enter a temperature value: "))
    unit = input("Enter the unit (Celsius, Fahrenheit, or Kelvin: )")
    convert_temperature(temp, unit)
except ValueError:
    print ("Please enter a valid numerical temperature.")