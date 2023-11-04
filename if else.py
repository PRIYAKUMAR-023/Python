if(100>99):
    print("True")
else:
    print("No")

#comparison operator


print("eat"=='eat')

print("eat"=="east")

meghana=input()
if (meghana=='died'):
    print("surya weds priya")
else:
    print("surya weds meghana")  


income=int(input("your income:"))
if(income>7000):
    print("Scholarship avaliable")
else:
    print("Not eligible for scholarship")



x=int(input())
if(x%3 and x%5):
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")

#Or

X=int(input())
if(x/3 and x/5):
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")

#or

x=int(input())
if(x%3==0 and x%5==0):
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")


Number=int(input())
if(Number%2==0):
    print("Number is even")
else:
    print("number is odd")

score=int(input("enter score:"))
if(score<35):
    print("Poor student")
if(score>35 and score<70):
    print("Average student")
else:
    print("Good student")

#or



score=int(input(enter score:))
if(score<35):
    print("Poor student")
if(score>35 and score<70):
    print("Average student")
if(score<70):
    print("Good student")



rank=int(input("enter rank:"))
if(rank>10):
    print("avg student")
elif(rank==3):
    print("topper 3")
elif(rank==2):
    print("topper 2")
elif(rank==1):
    print("topper of the class")
else:
    print("Invvalid input")