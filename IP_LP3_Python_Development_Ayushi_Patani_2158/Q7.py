# ​Write a Python program to convert temperatures to and from celsius, Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in Fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

c = float(input("Enter temperature in celsius: "))
f = float(input("Enter temperature in fahrenheit: "))
f_temp = ((c/5)*9) + 32
c_temp = ((f-32)/9)*5
f_temp = int(f_temp)
c_temp = int(c_temp)
print(str(c)+'\u00b0'+"C is "+str(f_temp)+" in Fahrenheit");
print(str(f)+'\u00b0'+"F is "+str(c_temp)+" in Celsius")

# output:
# Enter temperature in celsius: 60
# Enter temperature in fahrenheit: 45
# 60.0°C is 140 in Fahrenheit
# 45.0°F is 7 in Celsius