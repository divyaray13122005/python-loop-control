"""Help negotiate book prices at College Street based on book condition.
- New book: Pay marked price
- Like new: ""Ask for 10% discount""
- Good condition: ""Ask for 20% discount""
- Fair condition: ""Ask for 30% discount""
- Poor condition: ""Ask for 50% discount or look elsewhere"""


book_type = (input(" enter book condition:  "))
if(book_type == "new book" ):
    print("pay marked price")
elif(book_type == "good condition"):
    print(" ask for 20% discount ")
elif(book_type == "fair condition"):
    print(" ask for 30% ")
elif(book_type == "poor condition"):
    print("ask for 50% discount or look elsewhere")
else:
    print("book not available")                