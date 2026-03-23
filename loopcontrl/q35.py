"""Suggest appropriate clothing for Kolkata weather.
- Temperature > 35°C: ""Wear light cotton clothes and carry water""
- Temperature 25-35°C: ""Comfortable weather - normal clothes""
- Temperature 15-24°C: ""Pleasant weather - light jacket recommended""
- Temperature < 15°C: ""Cold weather - wear warm clothes"""

temp = float(input(" enter temp of your area: "))
if(temp>=35):
    print("Wear light cotton clothes and carry water")
elif(temp>=25 and temp<35):
    print("Comfortable weather - normal clothes")  
elif(temp>=15 and temp<24):
    print("Pleasant weather - light jacket recommended")     
elif(temp<15):
    print("Cold weather - wear warm clothes")  
else:
    print("freeze ho jayenge")    
