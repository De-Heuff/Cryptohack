#inlezen van de waarden uit de data
#manipuleer de vergelijking zodat p en q opgelost kunnen worden

import math

# Gegevens inlezen
file_path = "data.txt"  # Zorg dat het bestand de juiste waarden bevat
with open(file_path, "r") as f:
    lines = f.readlines()
    N = int(lines[0].split('=')[1].strip())
    e1 = int(lines[1].split('=')[1].strip())
    e2 = int(lines[2].split('=')[1].strip())
    c1 = int(lines[3].split('=')[1].strip())
    c2 = int(lines[4].split('=')[1].strip())

#uitschrijven van Newtons Binomium
c1_eq = pow(c1, e2, N)
c2_eq = pow(c2, e1, N)

e1_eq = pow(5, e1 * e2, N)
e2_eq = pow(2, e1 * e2, N)

D = (c1_eq * e1_eq - c2_eq * e2_eq) % N
q = math.gcd(D, N)
p = N // q

print(f"crypto{{{p},{q}}}")




