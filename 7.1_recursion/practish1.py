

# def demo(i=0):
#     if i==10:
#         return
#     print(i)
#     demo(i+1)
# demo()

# n=int(input('enter:'))
# fact=1
# while n!=0:
#     fact*=n
#     n-=1
# print(fact)

# def rec(n,fact=1):
#     if n==1:
#         print(fact)
#         return
#     fact*=n
#     rec(n-1,fact)
# rec(int(input('enter:')))
    
# def rev(n,r=0):
#     if n<=0:
#         return r
#     ld=n%10
#     r=r*10+ld
#     return rev(n//10,r)
# print(rev(8764))

# def revs(s,i=0,r=''):
#     if i>=len(s):
#         return r
#     r=s[i]+r
#     return revs(s,i+1,r)
# print(revs('kanji'))

# s=0
# n=int(input('enter:'))
# i=1
# while i<n:
#     if n%i==0:
#         s+=i
#     i+=1
# # if s==n:
# #     print('prefect')
# # else:
# #     print('not')
# print('prefect' if s==n else 'not')

# def per(n,s=0,i=1):
#     if i>=n:
#         return 'prefect' if s==n else 'not'
#     if n%i==0:
#         s+=i
#     return per(n,s,i+1)
# print(per(22))


# def fibonacii(n,a = 0,b = 1,i = 0):
#     if(i >= n):
#         return
#     print(a)
#     c = a + b
#     a,b = b,c
#     return fibonacii(n,a,b,i+1)
# fibonacii(5)




