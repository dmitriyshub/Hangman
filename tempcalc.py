
#the final answer
temp = input('enter the temperature: ').upper() # upper method makes the letters in UPPER case
if temp[-1:] == 'C':
    # checks if Temperature is in Celsius format and reverse to farenheit
    farenheit = (float(temp[:-1]) * 9) / 5 + 32
    print(farenheit,"F")
elif temp[-1:] == 'F':
    # checks if Temperature is in Farenheit format
    celsius = (float(temp[:-1]) - 32 )/ 1.8
    print(celsius,"C")
else:
    # wrong input
    print("Wrong Input")






""" others attempts:
1:
degree = input("Enter temperature in celsius or farenheit: ")
temperature_type = str(degree[-1])
print(temperature_type)
temperature = degree[:-1]
print(temperature)
temperature = float(temperature)
print(temperature)

if 'f' or 'F' in temperature_type:
    celsius = (temperature - 32) * 5/9
    temperature_type = 'C'
    print(celsius,temperature_type)


print(temperature,temperature_type)

if 'c' or 'C' in temperature_type:
    fahrenheit = (temperature * 9 / 5) + 32
    temperature_type = 'F'
    print(fahrenheit,temperature_type)
"""




"""
2:
temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = float(temp[:-1])
i_convention = temp[-1]
i_convention = i_convention.upper()
if i_convention == "C":
  result = float(round((9 * degree) / 5 + 32))
  o_convention = "F"
elif i_convention == "F":
  result = float(round((degree - 32) * 5 / 9))
  o_convention = "C"
else:
  print("Input proper convention.")
  quit()
print(result,o_convention)"""




