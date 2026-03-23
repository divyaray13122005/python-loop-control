"""Ask the user to enter a movie rating out of 5 and provide a message based on the following conditions - 
5.0: ""Bhai masterpiece dekh liya 🔥""
4.0 to 4.9: ""Bhai badiya movie thi 👌""
3.0 to 3.9: ""Theek thaak thi, timepass 😐""
2.0 to 2.9: ""Meh! Bore ho gaya yaar 😴""
Below 2.0: ""Mat dekhna bhai, time barbaad 🚫"""

movie_rating = float(input(" enter the movie rating u want to give (1-5): "))
if(movie_rating == 5):
    print(" bhai masterpiece dekh liya ")
elif( movie_rating >=4 and movie_rating <5):
    print(" bhai badiya movie thi ")
elif( movie_rating >=3 and movie_rating < 4):
    print(" theek thaak thi, time pass ")
elif(movie_rating >= 2 and movie_rating < 2.9):
    print(" meh! bore ho gya yaar ")
elif(movie_rating<2):
    print(" mat dekhna bhai, time barbaad ")
else:
    print(" go watch yourself ")                
