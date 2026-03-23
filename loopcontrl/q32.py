"""Predict crowd levels at pandal hopping based on time of day.
- 6 AM to 10 AM: ""Light crowd - perfect for photography""
- 11 AM to 4 PM: ""Moderate crowd - good time to visit""
- 5 PM to 10 PM: ""Heavy crowd - expect long queues""
- 11 PM to 5 AM: ""Very light crowd - peaceful experience"""

time = int(input(" enter your time : "))
if(time>=6 and time<10):
    print("Light crowd - perfect for photography") 
elif(time>=11 and time<16):
    print("Moderate crowd - good time to visit")
elif(time>=17 and time<22):
     print("Heavy crowd - expect long queues")  
elif(time>=23 and time<5):
    print("Very light crowd - peaceful experience")     
else:
    print(" jake khud delhlo ")    
