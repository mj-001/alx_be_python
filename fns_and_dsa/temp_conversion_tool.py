FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit -32)* FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) +32
def main():
    try:
        temperature =float(input("Enter the temperature to convert(e.g, 100F or 37C): "))
        unit= ("Is this temperature in Celsius or Fahrenheit? (C/F)").strip().upper()

        if unit=="C":
            converted_temp= convert_to_fahrenheit(temperature)
            print(f"f{temperature} C is {converted_temp} F")

        elif unit=="F":
            converted_temp=convert_to_celsius(temperature)
            print(f"f{temperature} F is {converted_temp} C")

        else:
            print("Invalid unit. Please enter 'C' OR 'F'. ")

    except ValueError:
        print("Invalid temperature.Please enter a numeric value.")

if __name__=="__main__":
    main()