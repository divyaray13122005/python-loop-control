"""Suggest which compartment to board based on passenger type.
- Age < 18: ""General compartment or ask adult for help""
- Age 18-59 and gender is ""female"": ""Ladies compartment available""
- Age 18-59 and gender is ""male"": ""General compartment""
- Age >= 60: ""Senior citizen compartment (if available) or general"""

age = int(input("enter your age: "))
gender = input("enter your gender: (male/female) ")


if(age<18):
    print("General compartment or ask adult for help")
elif(age>=18 and age>=59):
    if(gender=="female"):    
        print("female,Ladies compartment available")
    else:
        print("male: ""General compartment")    
if(age>=60):
    print(" senior citizen compartment(if available) or general ")

