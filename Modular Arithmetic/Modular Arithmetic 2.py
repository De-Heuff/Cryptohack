#if Modulo is prime, the integers define a field;
#if modulo is not prime, the integers define a ring
#Fermatts little theorem = a^(p-1) = 1 (mod p)

def calculate_integer(p, a):
    c = p-1
    b = a**c
    outcome = b%p
    print(outcome)

calculate_integer(65537, 273246787654)




