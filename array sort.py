'''
a=[]
n=int(input("Enter array size:"))
for i in range(0,n): 
#for i in range(1,n+1):
    b=char(input("Enter arrray elements:"))
    a.append(b)
a.sort()
print("Largest element in your array is:",a[n-1])
'''

a=[(int(x) for x in input("enter elements of Array With spaces--").split())]
a.sort()
print("The largest number Iss  ",a.pop())



