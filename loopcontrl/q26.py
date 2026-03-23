"""Question: Elish Maach Market Price Check
Write a program that takes the weight of a fish from the user.
At a fish market in Sealdah, elish maach costs ₹800/kg if weight > 1kg, otherwise ₹900/kg. Calculate total cost.

Expected Output Format:
Display price per kg and total cost"""

weight_of_fish = int(input(" enter the weight of your fish : "))
if(weight_of_fish >=1):
    cost = 800*weight_of_fish
else:
    cost = 900
    print(f"total cost of fish : {cost}")    

