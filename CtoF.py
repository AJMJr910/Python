#Convert the temperature from Celcius to Fahrenheit
#First get the Celcius temperature 

temp_C = int(input("Temperature in Celcius: "))


#Next, convert to F
temp_F = (9/5)*temp_C+32


#Display the results
print("The Fahrenheit temperature is ",(format(temp_F, '.2f')),".",sep='')
if temp_F < 40 or temp_F > 400:
    print("FUCK!")  
else:
    print("Nice weather we're having!")