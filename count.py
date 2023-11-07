count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
print(count) 


count_1=0
count_2=0
for i in range(1,6):
    if(i%2==0):
        count_1=count_1+1
    else:
        count_2=count_2+1
print(count_1)  #even
print(count_2)  #odd    


count=0
for n in range(1,100):
    if(n%3==0 and n%5==0):
        count=count+1
print(count)


count_1=0
count_2=0
for i in range(1,6):
    if(i%2==0):
        count_1=count_1+1
    if(i%2==1):
        count_2=count_2+1
print(count_1)  #even
print(count_2)  #odd    