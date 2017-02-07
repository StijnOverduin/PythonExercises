import string


# exercise 1
def exercise1():
    multiples = 0;
    for i in range(1000):
        if i % 3 == 0 or i% 5 == 0:
            multiples += i
    return multiples

print("exercise 1")
print(exercise1())

#exercise 2
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a%b
    return a

print("exercise 2")
print(gcd(3141, 156))
print(gcd(12345678, 987654321) ** 2)


def frac(a, b):
    answer = "b is 0"
    negative = False
    if b < 0 or a < 0:
        negative = True
    if b != 0:
        fraction = gcd(a, b)
        a = abs(a)
        b = abs(b)
        a /= fraction
        b /= fraction
        answer = "(" + str(a) + " / " + str(b) + ")"
    if negative:
        answer = "-" + answer

    return answer


print(frac(20, -25))

# exercise 3


def encode(x):
    if x in range(0, 9):
        return str(x)
    elif x in range(10, 36):
        alpha = list(string.ascii_lowercase)
        return alpha[x-10]


def to_k(n, k):
    if 2 <= k <= 35 and n >= 0:
        digits = []
        while n >= 1:
            digits.append(encode(int((n % k))))
            n /= k
        digits.reverse()
        return "".join(digits)
    else:
        return -1


# give string
def decode(x):
    numberString = "0123456789"
    numberList = []
    numberList[:0] = numberString
    if x in numberList:
          return x
    alpha = list(string.ascii_lowercase)
    if x in alpha:
        return alpha.index(x) + 10
    else:
        return -1


def from_k(s, k):
    number = int(s, k)
    answer = to_k(number, 10)
    return answer


def convert(k, m, s):
    return to_k(int(from_k(s, k)), m)


print(encode(0))
print(encode(35))
print(to_k(4095, 35))
print(decode("z"))
print(from_k("10011010", 2))
print(convert(2, 4, " 10011010"))


# exercise 4

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fibEvenSum():
    notLimit = True
    i = 0
    fibsum = 0
    while notLimit:
        if fib(i) > 4000000:
            notLimit = False
            return fibsum
        if fib(i) % 2 == 0:
            fibsum += fib(i)
        i += 1
    return fibsum

# print(fibEvenSum())


# exercise 5

def palin():
    maxim = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i * j
            if str(num) == str(num)[::-1]:
                maxim = max(maxim, i * j)

    return maxim

# print(palin())


# exercise 6

def fact(n):
    if n >= 1:
        return n * fact(n - 1)
    else:
        return 1

print(fact(28))


def binom(n, k):
    return fact(n)/(fact((n - k))*fact(k))

print(binom(12, 8))

# exercise 7

def intdiv(a):
    divisorset = set()
    for i in range(1, a + 1):
        if a % i == 0:
            divisorset.add(i)

    return divisorset

print(intdiv(20))

def primefact(a):
    primefac = list()
    d = 2
    while d*d <=a:
        while (a % d) == 0:
            primefac.append(d)
            a //= d
        d += 1
    if a > 1:
        primefac.append(a)
    return primefac


print(primefact(13195))

# exercise 8

print(primefact(600851475143)[-1])