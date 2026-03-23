"""Write a program that suggests which Kolkata Metro line to take based on your destination.
- If destination is ""Esplanade"" or ""Park Street"" → ""Take Blue Line""
- If destination is ""Kalighat"" or ""Rabindra Sarobar"" → ""Take Blue Line (Extension)""
- If destination is ""Salt Lake Stadium"" → ""Take Green Line""
- Otherwise → ""Check metro map for other lines"""

destination = input(" enter your destination  : ")
if destination ==  "esplanade" or "parkstreet" :
    print(" take blue line ")
elif destination == "kalighat" or "rabindra sarobar":
    print("take blueline extension") 
elif destination == "salt lake":
    print("take green line ")     
else:
    print(" check metro map for other lines ")