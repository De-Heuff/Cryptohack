# given any integer a, it is enough to calculate a ** (p-1/2) mod p is enough to determine
# if a is a quadratic residue.

def legendre_symbol(a, p):
    legendre = pow(a, (p - 1) // 2, p)
    if legendre == 1:
        return True  # a is een kwadratisch residu mod p
    elif legendre == p - 1:
        return False  # a is een kwadratisch non-residu mod p
    else:
        return None  # Dit zou niet moeten voorkomen voor een prime p

def tonelli_shanks(n, p):
    """Vindt een vierkantswortel van n modulo p met het Tonelli-Shanks algoritme."""
    if legendre_symbol(n, p) is False:
        return None  # Geen vierkantswortel bestaat

    # Speciale gevallen
    if p == 2:
        return n % 2
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)

    # Algoritme van Tonelli-Shanks
    s = 0
    q = p - 1
    while q % 2 == 0:
        s += 1
        q //= 2
    z = 2
    while legendre_symbol(z, p) != False:
        z += 1
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)
    while t != 0 and t != 1:
        t2i = t
        i = 0
        for i in range(1, m):
            t2i = pow(t2i, 2, p)
            if t2i == 1:
                break
        b = pow(c, 1 << (m - i - 1), p)
        m = i
        c = pow(b, 2, p)
        t = (t * c) % p
        r = (r * b) % p
    return r

def calc_square_root(a, p):
    """Bereken de vierkantswortel van a modulo p als het Legendre-symbool a/p == 1."""
    if legendre_symbol(a, p):
        sqrt = tonelli_shanks(a, p)
        if sqrt is not None:
            return sqrt
    return None

with open("output.txt", 'r') as output:
    # Lees alle regels van het bestand, en filter lege regels
    lines = [line.strip() for line in output if line.strip()]

    # Debugging: print de regels van het bestand om te zien wat er binnenkomt
    # print(f"Bestandsinhoud zonder lege regels:\n{lines}")

    # Verwerk de eerste regel: verwijder 'p =' en haal alleen de lange integer
    p = int(lines[0].split('=')[1].strip())  # Split op '=' en neem het tweede deel (de integer)

    # Combineer alle overgebleven regels tot één string om de integerlijst te verwerken
    integer_string = ','.join(lines[1:])  # Neem alle regels vanaf de tweede regel, en combineer ze met komma's

    # Verwijder eventuele ongewenste tekens en splits de string op komma's
    # Dit verwijdert lege items en items die geen geldige integers zijn
    integer_list = []
    for item in integer_string.split(','):
        item = item.strip()  # Verwijder whitespace rondom het item
        if item and item.isdigit():  # Controleer of het item een geldig getal is
            integer_list.append(int(item))

    # Debugging: print de ingelezen lijst
    # print(f"Ingelezen integer lijst: {integer_list}")

for integer in integer_list:
    if legendre_symbol(integer, p):
        sqrt = calc_square_root(integer, p)
        if sqrt is not None:
            print(f"Vierkantswortel is {sqrt}")
        else:
            print("Geen vierkantswortel")
    else:
        print("Geen kwadratisch residu")






