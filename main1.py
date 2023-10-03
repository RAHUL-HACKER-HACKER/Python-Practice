#print("hello")
'''name="rahul"
id =200
print("id:"+str(id))'''

# a=50
# if a>=60:
#     print("Pass")
# else:
#     print("Fail")
    
    
arr=[30,40,"hello"]
print(arr)
for i in range(len(arr)):
    print(arr[i],end=" ")

#or 
print()
for value in arr:
    print(value,end=" ")

print()
for i in range(10+1):
    print(i,end=" ")
    
print()
j=0
while j<=10:
    print(j,end=" ")
    j+=2
    
    

def fibb(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    return fibb(n-1)+fibb(n-2)
n=int(input())
print("fibb series:")
for i in range(1,n+1):
    print("values:",fibb(i),end=" ")

#or
def fibb(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    return fibb(n-1)+fibb(n-2)
n=int(input())
print("fibb series:")
for i in range(1,n+1):
    print("values:"+str(fibb(i)),end=" ")
