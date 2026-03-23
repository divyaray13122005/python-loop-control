"""Help negotiate fish prices at local markets based on quantity.
- 1 kg: Pay full price
- 2-4 kg: ""Ask for 5% discount""
- 5-9 kg: ""Ask for 10% discount""
- 10+ kg: ""Ask for 15% discount and free cleaning"""

weight = float(input(" weight of fish : "))
if(weight == 1):
    print("full price")
elif(weight >=2 and weight <=4 ):
    print("give me 5% discount")
elif(weight >=5 and weight<=9):
    print("give me 10% dsicount")
elif(weight>10):
    print("give me 15% discount and free cleaning")
else:
    print("free mein hi dedo")               
