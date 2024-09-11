#Write code to calculate when integer a is a**2 = 18 when modulo = p.
#If finite field, there should be 2 integers!

def find_square_root(target_value, p):
    solutions = []
    for a in range(p):
        if (a**2) % p == target_value:
            solutions.append(a)
            solutions.append(p - a)
            break
    if solutions:
        print(solutions)
    else:
        return None
        print(f"Geen vierkantswortel van {target_value} gevonden in mod {p}")

find_square_root(6, 29)








