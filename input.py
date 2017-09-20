#Getting input from the keybaord
#variable=input(prompt)
name=input('What is your name? ')
age=input('What is your age? ')
town=input('What town do you live in? ')

print('Your name is ',name,', you are ', age,', and you live in ',town,'.', sep='')

#Everything entered in input variables are strings, meaning if you need to use them in math equations it won't work.
#To address this you can set a variable as an integer (whole number) or a float (decimal number) when it is input

#name = input('What is your name? ')
#age = int(input('What is your age? '))
#income = float(input('What is your income? '))

#Display data
#print('Here is the data you entered: ')
#print('Name: ', name)
#print('Age: ', age)
#print('Income: ',income)