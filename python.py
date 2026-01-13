items=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in items:
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
print(even)
print(odd)
    
        