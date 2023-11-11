a=[1,2,3,4]
print(a)

# Add the values

a.append(7) 
a.append(6)
print(a)


#position of the value

print(a[3]) 


# add the values in paticular place 

a.insert(1,5)
print(a)

#change the value

a[5]=80
print(a)

#remove values

a.pop()
print(a)


# merge two list
b=[4,7,8,9]
a.extend(b)
print(a)