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
def exercise2(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a%b
    return a

print("exercise 2")
print(exercise2(3141, 156))
print(exercise2(12345678, 987654321)**2)

def frac(a, b):
    if b != 0:
        if exercise2(a, b) == 1:
            return a/b

print(frac(24, 25))

#exercise 3

def encode(x):
    if x in range(0, 9):
        return str(x)
    elif x in range(10, 36):
        alpha = list(string.ascii_lowercase)
        return alpha[x-10]


def to_k(n, k):
    if 2 <= k <= 35 and n >= 0:
        digits = []
        while n >=1:
            digits.append(encode(int((n % k))))
            n /= k
        digits.reverse()

        return "".join(digits)
    else:
        return -1


def decode(x):
    if type(x) is int:
        if x in range(0, 10):
            return x
        else:
            return -1
    elif type(x) is str:
        alpha = list(string.ascii_lowercase)
        if x in alpha:
            return (alpha.index(x) + 10)
        else:
            return -1


print(encode(0))
print(encode(35))
print(to_k(4095, 35))

print(decode("a"))
