FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit -32)* FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) +32

temperature_input =(input("Enter the temperature you wish to convert: "))

if temperature_input[-1].upper()=="F":
    fahrenheit=float(temperature_input[:-1])
    celsius=convert_to_celsius(fahrenheit)
    print(f"{fahrenheit} F is equal to {celsius} C")

elif temperature_input[-1].upper() == "C":
     celsius = float(temperature_input[:-1])
     fahrenheit = convert_to_fahrenheit(celsius)
     print(f"{celsius} C is equal to {fahrenheit} F")

else:
    print("Invalid options.Kindly specify between C or F")
