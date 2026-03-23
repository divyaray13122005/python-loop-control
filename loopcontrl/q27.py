"""Take a number (1–7) and print the day name accordingly.
If the user enters 1, print Monday. If the user enters 2 print Tuesday. Do this for the numbers 3 to 7 as well.
 If the user enters a number out of the range, provide an appropriate message of your choice."""


number = int(input("  enter the day no. you want from (1-7) : "))
if(number==1):
    print("monday")
elif number == 2:
    print("tuesday")
elif number == 3:
      print("wednesday")
elif number == 4:
    print("thursday")
elif number == 5:
    print("friday")
elif number == 6:
    print("saturday")
elif number == 7:
    print("sunday")
else:
    print("your wish")                     

