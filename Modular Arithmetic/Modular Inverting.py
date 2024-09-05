#multiplicative inverse = a*x = 1 (mod p)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b%a, a)
        x = y1 - (b//a) * x1
        y = x1
        return gcd, x, y

def multiplicative_inverse(a, p):
    gcd, x, y = extended_gcd(a, p)
    if gcd != 1:
        raise Exception("Inverse does not exist")
    else:
        return x%p

inverse = multiplicative_inverse(3, 13)
print(inverse)


