def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
celsius = 37
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C = {fahrenheit}°F")

fahrenheit_val = 98.6
celsius_val = fahrenheit_to_celsius(fahrenheit_val)
print(f"{fahrenheit_val}°F = {celsius_val}°C")