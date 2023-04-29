# 3. A temperature converter.
# Write a python program to take user inputs for temperature and unit.
# Then provide the converted result.
input_val = input("Enter the temperature : ")
input_val2 = input("Enter the unit celcious or fahrenheit (C/F) : ")
temperature = float(input_val)
unit = input_val2.capitalize()
if unit == "C":
    f = 32 + (temperature * 9/5)
    print("Temperature in fahrenheit : ", float(f))
elif unit == "F":
    c = (temperature - 32) * 5/9
    print("Temperature in celcious : ", float(c))
else:
    print("Invalied! unit code")
