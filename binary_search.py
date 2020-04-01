from array import *

ar=array('i',[])
found=False
print("===================== BINARY SEARCH ==================")
n=int(input("\n Enter the number of elements in array: "))
print("enter the elements of array in sorted form")
for i in range(n):
    x=int(input())
    ar.append(x)

s=int(input("Enter the searhing element in array"))
low=0
upp=n-1
mid=(low+upp)//2
while low<=upp:
    if ar[mid]==s:
        found=True
        print("element found at position ",mid+1)
        break   
    if(ar[mid]<s):
        low=mid+1
        mid=(low+upp)//2
    else:
        upp=mid-1
        mid=(low+upp)//2

if(low>upp):
    print("element is not present")
