"""Question : Elish Maach Market Price - 
Write a program to determine elish maach price based on size and season.

Input: Take fish size (string: ""small"", ""medium"", ""large"") and season (string: ""monsoon"" or ""other"") as input
Output: Print price per kg

Logic:
If monsoon season: Small: ₹800/kg, Medium: ₹1000/kg, Large: ₹1200/kg
If other season: Small: ₹1200/kg, Medium: ₹1500/kg, Large: ₹1800/kg"""
size = input("fish size : ( small/medium/large ):")
season = input("season : ( monsoon/other ) : ")
if(season == "monsoon"):
    if(size== "small"):
        print("800per kg")
    elif(size== "medium"):
        print("1000per kg")
    elif(size == "large"):
        print("1200per kg")
elif(season == "other"):
    if(size == "small"):
        print("1200per kg")
    if(size == "medium"):
        print("1500per kg")
    if(size == "large"):
        print("1800per kg")
else:
    print("free mein leke jao")