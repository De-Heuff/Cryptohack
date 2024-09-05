#the extended Euclid Algorithm tells how to make GCD from two integers

# Waarden
p = 26513
q = 32321

# Bereken extended GCD
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

#Bereken GCD en u en v:
gcd, u, v = extended_gcd(p, q)

#print resultaat
print(f"gcd({p}, {q}) = {gcd}")
print(f"u and v: u = {u}, v = {v}")