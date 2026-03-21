## Question: Electricity Bill Calculator
##Calculate electricity bill for households in West Bengal. Up to 100 units: ₹3/unit, above 100 units: ₹5/unit.

##Expected Output Format:
##Display total bill amount

units = int(input("enter your unit:"))
amounts = 0
if( units<100):
    amount = units *3
if(units>100):
    amount = units *5

print(f"amount =  {amount}")

