"""Question: Kolkata Metro Fare Calculator - 
Create a program that calculates metro fare based on distance traveled. For distances up to 5 km, fare is ₹10. For distances above 5 km, fare is ₹15.

Expected Output Format:
Display the fare amount with appropriate message."""


distance =  int(input(" enter distance you travelled : "))
if(distance<=5):
    fare = 10
    print(f" Fare for {distance} km: {fare}") 

else:
    fare = 20
    print(f"fare for {distance}km: {fare}")