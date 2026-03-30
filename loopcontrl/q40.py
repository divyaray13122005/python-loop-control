"""Question: College Admission Eligibility - 
Write a program to check college admission eligibility. Minimum marks required is 75% for general category and 
65% for reserved category.
Take input for marks and reservation category from user.
Expected Output Format:
Display eligibility status of candidate."""

marks = int(input("enter your marks: "))
category = input("enter your category: (general/reserved) ")
if(marks >=75 and category == "general"):
    print(" you are pass ")
elif(marks <=65 and category == "reserved"):
    print("you are definately pass")
else:
    print("your are not pass")        
 