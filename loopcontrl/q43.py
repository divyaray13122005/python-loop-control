"""Question : Kolkata Metro Line Fare Calculator - 
Write a program to calculate metro fare in Kolkata based on the number of stations traveled.

Input: Take the number of stations as input from the user
Output: Print the fare amount

Logic:
If stations ≤ 5: fare is ₹10
If stations > 5 and ≤ 10: fare is ₹15
If stations > 10: fare is ₹20"""

stations = int(input(" enter no. of station : "))
if(stations<= 5 ):
    print("fare is 10 rs.")
elif(stations>5 and stations<=10):
    print("fare is 15rs.")
elif(station>10):
    print("fare is 20rs.")
else:
    print("free hai ticket.")            