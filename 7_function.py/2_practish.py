
# ⁡⁣⁣⁢factorial⁡

def factorial(n):
    fact = 1
    for i in range(1,(n + 1)):
        fact = fact * i
    return fact
print(factorial(5))


# ⁡⁣⁣⁢factorial⁡ 

def factor(k):
    fac = 1
    for a in range(1,(k +1)):
        fac = fac * a
    return fac
print(factor(10))


# ⁡⁣⁣⁢factorial with recursive⁡

def recursive(i):
    if(i == 0 or i == 1):
        return 1
    return i * recursive(i - 1)
print(recursive(4))


# ⁡⁣⁣⁢print number n⁡
def num(n):
    for i in range(1,n + 1):
        print(i)
num(5)



#⁡⁣⁣⁢ find sum of digit⁡

def digitSum(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total
print(digitSum(1234))

