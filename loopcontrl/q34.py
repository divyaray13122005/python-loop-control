"""Suggest best travel times to cross Howrah Bridge based on traffic patterns.
- 5 AM to 7 AM: ""Light traffic - smooth journey""
- 8 AM to 11 AM: ""Heavy traffic - expect delays""
- 12 PM to 4 PM: ""Moderate traffic - reasonable time""
- 5 PM to 9 PM: ""Peak traffic - consider alternate route""
- 10 PM to 4 AM: ""Very light traffic - fastest route"""

time = int(input(" enter your time "))
if(time>=5 and time<7):
    print("Light traffic - smooth journey")
elif(time>=8 and time<11):
    print("Heavy traffic - expect delays")
elif(time>=12 and time<16):
    print("Moderate traffic - reasonable time")    
elif(time>=17 and time<21):
    print("Peak traffic - consider alternate route")
elif(time>=22 and time<4):
    print("Very light traffic - fastest route")      
else:
    print("waise to hamesha hi traffic raheta hai")      