def legendre_symbol(a, p):
    """Bereken het Legendre-symbool (a/p)."""
    return pow(a, (p - 1) // 2, p)

def tonelli_shanks(n, p):
    """Vind een vierkantswortel van n modulo p met het Tonelli-Shanks algoritme."""

    assert legendre_symbol(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre_symbol(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r

def read_input(file_path):
    """Lees de prime p en het getal a uit een bestand."""
    with open(file_path, "r") as f:
        lines = f.readlines()

        # Verwerk 'a' als een lijst van integers
        a_values = lines[0].split('=')[1].strip().split(',')  # Splits de lijst op komma's
        a = [int(x.strip()) for x in a_values]  # Zet elk item in de lijst om naar een integer

        # Verwerk 'p' als een enkele integer
        p = int(lines[1].split('=')[1].strip())

    return a, p

file_path = 'output_modular_square_root.txt'
a_list, p = read_input(file_path)

# Roep tonelli_shanks aan voor elk getal in de lijst a
for a in a_list:
    try:
        sqrt = tonelli_shanks(a, p)
        print(f"De vierkantswortel van {a} modulo {p} is {sqrt}")
    except AssertionError as e:
        print(f"Geen vierkantswortel voor {a}: {e}")

