from perm import*
from Exercises7Feb import gcd

q = test_permutation(20)
print(q)

p = [1, 2, 3, 0, 5, 4, 6, 7, 8, 9]
print(p)
print_permutation(p)
print(is_trivial(p))
print(p[0])
print(cycles(p))

r = trivial_permutation(10)
print(r)
print(r[0])
print(is_trivial(r))

p = permutation_from_cycles(10, [[0, 1, 2, 3], [4, 5]])
print(p)
print_permutation(p)


def composition(p, q):
        result = []
        for i in range(0, len(p)):
            result.append(q[p[i]])
        return result
p = [1, 2, 3, 0, 5, 6, 4, 8, 7]
print_permutation(p)
q = composition(p, p)
print_permutation(q)


def inverse(p):
    p = list(p)
    result = [0] * len(p)
    for i, e in enumerate(p):
        result[e] = i
    return result

p = [3, 8, 5,0, 9, 4, 6, 1, 7, 2]
print(inverse(p))


def power(p, i):
    result = p
    if i == 0:
        result = trivial_permutation(len(p))
    elif i > 0:
        while i > 1:
            result = composition(result, p)
            i -= 1
    else:
        while i < 0:
            result = inverse(result)
            i += 1
    return result

p = [0, 3, 4, 2, 5, 6, 8, 9, 7, 1]
print(power(p, 1))

def period(p):
    i = 1
    notFound = True
    while notFound:
        if is_trivial(power(p, i)):
            notFound = False
        else:
            i += 1
    return i

print("laatste")
p = [0, 3, 4, 2, 5, 6, 8, 9, 7, 1]
print(period(test_permutation(20)))