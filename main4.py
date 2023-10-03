# n=input()
# rev=n[::-1]
# print(rev)

# def primeFactorial(n):
#     arr=[]
#     div=2
#     while n>1:
#         while n%div==0:
#             arr.append(div)
#             n//=div
#         div+=1
#     return arr
# print(primeFactorial(54756))
# factors=primeFactorial(54756)
# dic={}
# for factor1 in factors:
#     count=0
#     for factor2 in factors:
#         if factor1==factor2:
#             count+=1
#     dic[factor1]=count
# print(dic)
# result=1
# for i,j in dic.items():
#     result*=pow(i,j//2)
# print(result)

# import math as m;
# print(m.sqrt(36))

# def prime(n):
#     arr=[]
#     for i in range(2,n+1):
#         flag=True
#         for j in range(2,i):
#             if i%j==0:
#                 flag=False
#                 break
#         if flag:
#             arr.append(i)
#             flag=True
#     return arr
# print(prime(41))

# def smallestdivisor(n):
#     div=2
#     while(div<=n):
#         if n%div==0:
#             return div
#         div+=1
# print(smallestdivisor(49))

# def gcd(n,m):
#     if n<m:
#         while n>0:
#             if m%n==0:
#                 return n
#             else:
#                 temp=n
#                 n=m%n
#                 m=n
#     else:
#         while m>0:
#             if n%m==0:
#                 return m
#             else:
#                 temp=m
#                 m=n%m
#                 n=m
# print(gcd(24,25))  
        

# def factorization(n):
#     factors=[]
#     div=2
#     while n>1:
#         while n%div==0:
#             factors.append(div)
#             n//=div
#         div+=1
#     return factors

# def gcd(factors1,factors2):
#     result=1
#     for i in factors1:
#         for j in factors2:
#             if i==j:
#                 result*=i
#                 factors2.remove(j)
#                 break
#     return result
# factors1=factorization(72)
# factors2=factorization(36)
# print(gcd(factors1,factors2))


#GCD using Repeated Division
def gcd(n,m):
    result=1
    div=2
    while div<=n and div<=m:
        while n%div==0 and m%div==0:
            result*=div
            n//=div
            m//=div
        div+=1
    return result
print(gcd(75,50))     
           
    