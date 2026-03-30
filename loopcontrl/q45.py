"""Question: Darjeeling Tea Grade Classifier
Write a program to classify Darjeeling tea based on price and quality rating.

Input: Take price per kg (float) and quality rating (1-10) as input
Output: Print tea grade: ""Premium"", ""Standard"", or ""Basic""

Logic:
If price > 1000:
    If quality >= 8: Premium
    Else: Standard

Else:
    If quality >= 6: Standard
    Else: Basic"""

price = float(input(" price per kg : "))
quality = int(input(" enter quality rating (1-10): "))

if(price >1000.0):
    if(quality>= 8):
        print("premium")
    else:
        print("standard")
else:
    if(quality>=6):
        print("standard")
    else:
        print("basic")        



    