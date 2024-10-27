#1) Find multiplicative inverse using extended_GCD
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

#calculate multiplicative inverse of a mod m
def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Inverse bestaat niet")
    return x % m

#Function for solving congruences with Chinese Remainder Theorem
def chinese_remainder_theorem(congruences, moduli):
    N = 1  # Bereken het product van alle moduli
    for mod in moduli:
        N *= mod

    result = 0
    for i in range(len(congruences)):
        ni = N // moduli[i]  # Bereken deelmodulus
        mi = mod_inverse(ni, moduli[i])  # Vind de inverse van ni mod moduli[i]
        result += congruences[i] * ni * mi  # Voeg de term toe aan het resultaat

    return result % N  # Het resultaat modulo het product van alle moduli

congruences = [2, 3, 5]  # Dit zijn de a's in de congruenties
moduli = [5, 11, 17]  # Dit zijn de moduli (5, 11, 17)

x = chinese_remainder_theorem(congruences, moduli)
print(f"De oplossing voor x is: x ≡ {x} (mod 935)")
