"""Question: Mumbai auto rickshaw fare
Take the input for travel distance from user. Auto rickshaw charges ₹25 for first 2 km and ₹8 for each additional
 km. Calculate total fare.

Expected Output Format:
Display breakdown and total fare amounts properly."""


distance = int(input(" enter distance you travelled : "))
if(distance == 2):
    print("your fare for 1st 2km is 25")
elif(distance > 2):
    additional_distance = distance - 2
    fare2 = additional_distance*8
    print(f"your fare for next additional distance: {fare2}")

