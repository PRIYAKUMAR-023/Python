"""salary=int(input("Enter your salary:"))
Age=int(input("Enter your age:"))
if(salary>=20000 or Age<=25):
    Loan_amount=int(input("Enter your loan amount:"))
    if(Loan_amount>=50000):
        print("MAximum amount is 50000 only")
    else:
        print("you are not eligible for loan")
else:
    print("Not Eligible for loan")"""


Tamil=int(input("Enter tamil mark:"))
English=int(input("Enter english mark:"))
Maths=int(input("Enter maths mark:"))
Science=int(input("Enter science mark:"))
Social=int(input("Enter social mark:"))
Total=(Tamil+English+Maths+Science+Social)
Average=(Total/5)
if(Average<35):
    print("Additional class is required")
else:
    print("you are good to go")