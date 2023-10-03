#factorial of given number
import random


def factorial(n):
    arr=[]
    div=2
    while n>1:
        while n%div==0:
            arr.append(div)
            n//=div
        div+=1
    return arr

print(factorial(146))
            
#squre root of given perfect number using factorisation
def squreRoot(n):
    arr=[]
    div=2
    while n>1:
        while n%div==0:
              arr.append(div)
              n//=div 
        div+=1
    result=1
    for i in range(0,len(arr),2):
        result*=arr[i]
    return result
print(squreRoot(36))

#find squre root using newtons raphson method
def newtonSqureRoot(n):
    guess=n
    while abs(n-guess*guess)>0.001:
        guess=1/2*(guess+n/guess)
    return guess
print(f"{newtonSqureRoot(100):.3f}")

#check a given number is prime
def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(isPrime(73))      

#print prime number between given number
def rangePrime(start,end):
    arr=[]
    for i in range(start,end):
        if isPrime(i):
            arr.append(i)
    return arr
print(rangePrime(10,100))

#print nth fibbonacci  
def fibb(n):
    if n<0:
        return -1
    elif n==0:
        return 0
    elif n==1:
        return 1
    return fibb(n-1)+fibb(n-2)
print(fibb(5))

#print fibbonacci series
def fibbSeries(n):
    arr=[]
    for i in range(n):
        arr.append(fibb(i))
    return arr
print(fibbSeries(5))

#find gcd or hcf 
def gcd(n1,n2):
    if(n1>n1):
        while n2>0:
            if n1%n2==0:
                return n2
            else:
                temp=n2
                n2=n1%n2
                n1=temp  
    else:
        while n1>0:
            if n2%n1==0:
                return n1
            else:
                temp=n1
                n1=n2%n1
                n2=temp 
print(gcd(24,36))

# Generate a random float between 0 and 1
random_float = random.random()
print("Random float:", random_float)
random_int = random.randint(1, 10)  # Generates a number between 1 and 10 (inclusive)
print("Random integer:", random_int)



#find gcd using prime factorization
def gcdUsingFac(arr1,arr2):
    result=1
    for i in arr1:
        for j in arr2:
            if i==j:
                result*=i
                arr2.remove(j)
                break
    return result
arr1=factorial(25)
arr2=factorial(100)
print(gcdUsingFac(arr1,arr2))

#gcd using factor
def gcdfac(num1,num2):
    result=1
    for i in range(1,num1+1):
        if num1%i==0 and num2%i==0:
            result=i
    return result
print(gcdfac(25,75))


  

#smallest divisor
def smallestDivisor(n):
    if n==2:
        return n

    for i in range(2,n+1):
        if n%i==0:
            return i
        
    return -1
print(smallestDivisor(50))

#GCD using Repeated Division
def gcdRep(n,m):
    result=1
    div=2
    while div<=n and div<=m:
        while n%div==0 and m%div==0:
            result*=div
            n//=div
            m//=div
        div+=1
    return result
print(gcdRep(36,24))

#gcd using recursion
def gcdrec(n,m):
    if m==0:
        return n
    gcdrec(m,n%m)
print(gcdfac(24,36))


# general method to find the Least Common Multiple or lcm
def lcm(n,m):
    result=1
    div=2
    while div<=n and div<=m:
        while n%div==0 and m%div==0:
            result*=div
            n//=div
            m//=div
        div+=1
    return result*n*m
print(lcm(45,15))

#lcm by factorial method
def lcmfac(arr1,arr2):
    cArr1=arr1.copy()
    lcmvalue=1
    for i in cArr1:
        for j in arr2:
            if i==j:
                lcmvalue*=i
                arr1.remove(i)
                arr2.remove(j)
    for i in arr1:
        lcmvalue=lcmvalue*i
    for j in arr2:
        lcmvalue=lcmvalue*j
    return lcmvalue
arr1=factorial(16)
arr2=factorial(28)
print(lcmfac(arr1,arr2))

#find lcm by easy method
def easyLcm(n,m):
    greater=n
    if m>n:
        greater=m
    while True:
        if greater%n==0 and greater%m==0:
            lcm=greater
            break
        greater+=1
    return lcm
print(lcm(16,28))  


#gcd or hcf using by easy method
def hcf(num1,num2):
    smaller=num1
    if num2<num1:
        smaller=num2
    for i in range(1,smaller+1):
        if num1%i==0 and num2%i==0:
            hcf=i
    return hcf
print(gcdfac(80,30))  


#Array Order Reversal using prebuid method
arr=[1,3,4,5,100]
arr.reverse()
print(arr)

#Array order reversal
def reverseArray(arr):
    arr2=[]
    for i in range(len(arr)):
        arr2.append(arr[len(arr)-i-1])
    return arr2
arr=[1,2,3,4,5,6,300,400]
print(reverseArray(arr))


# Reversing a list using slicing technique
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst

lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

#Array Counting in python
def count(arr):
    count=len(arr)
    return count
arr=[3,4,5,6]
print(count(arr))

#array counting
def count(arr):
    count=0
    for i in arr:
        count+=1
    return count
arr=[3,4,5,6,10]
print(count(arr))

#Finding the Maximum number in a set
def maxnum(set):
    ls=list(set)
    max=ls[0]
    for i in ls:
        if i>max:
            max=i
    return max
set={3,4,6,19,20,400,100}
print(maxnum(set))

#finding max num in a set
def maxnum(set):
    Max=max(set)
    return Max
set={3,4,6,19,20,600,100}
print(maxnum(set))

#remove doublicate of given array
import array as ar
def remDoub(arr):
    newarr=[]
    for i in arr:
        if i not in newarr:
            newarr.append(i)
    return newarr
arre=ar.array('i',[12,2,3,4,5,5,6,6,7,7,9,7])
print(remDoub(arre))

#Finding the Kth smallest element in python
def kth(arr,k):
    arr.sort()
    return arr[k-1]
arr=[3,6,2,0,5,6]
k=4
print(kth(arr,k))

#fining the kth smallest element in python
def kth(arr,k):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    return arr[k-1]

arr=[3,6,2,0,5,6]
k=5
print(kth(arr,k))


            
   
 


