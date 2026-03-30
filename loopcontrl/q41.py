"""Question: Book Fair Discount
At Kolkata Book Fair, books under ₹200 get no discount, books ₹200-₹500 get 5% discount, books above ₹500 get 10%
 discount. Ask the user to input the book price.

Expected Output Format:
Display original price, discount amount, and final price of the book."""


book_price = float(input(" enter the book price : "))
if(book_price >=200 and book_price <500):
    discount = book_price*0.05
elif(book_price >500):
    discount = book_price*0.10
else:
    discount = 0    
final = book_price - discount
print(f"your discount:{discount} ")
print(f"your book price:{final}")