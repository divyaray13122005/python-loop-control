"""Question : Monsoon Weather Advisory
Write a program that takes the value for rainfall amount from user.
 It gives weather advisory based on rainfall (in mm): Light rain (0-25), Moderate rain (26-75), Heavy rain (76+).

Expected Output Format:
Display rain category and appropriate advisory"""


amount = int(input(" enter rainfall amount "))
if(amount<=25):
    print("light rain")
elif(amount <=26 and amount >=75):
    print("moderate rain")
elif(amount >76):
    print("heavy rainfall")
else:
    print("no rainfall")    
    