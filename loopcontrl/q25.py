"""Question: Bengali Sweet Shop Discount
A sweet shop offers 10% discount if purchase is above ₹500.
 Write a program to ask the user for the purchase amount and then calculate final amount after discount.

Expected Output Format:
Display original amount, discount, and final amount"""

amount = float(input("  enter the amout you have purchased : "))
if(amount >=500):
    discount = amount*0.10
else:
    discount = 0

final_amount= amount - discount
print(f"your discount:{discount} ")
print(f"your final amount: {final_amount}")

    
    
    