"""Question: Kolkata Tram Service Status
Write a program to check tram service status based on weather and time.

Input: Take weather (string: ""clear"", ""rain"", ""storm"") and hour (0-23) as input
Output: Print service status
Logic:
If storm: ""Service suspended""
Else if rain:
    If hour between 6-22: ""Limited service""
    Else: ""No service""
Else (clear):
    If hour between 5-23: ""Full service""
    Else: ""No service"""

weather = input("weather : (clear/rain/storm): ")
hour = int(input("hour = (0-23): "))
if(weather == "storm"):
    print("service suspended")

elif(weather == "rain"):
    if(6 <=hour <=22):
        print("limited service")
    else:
        print("no service")

elif(weather == "clear"):
    if(hour>=5 and hour<=23):
        print("full service")
    else:
        print("no service")                     
