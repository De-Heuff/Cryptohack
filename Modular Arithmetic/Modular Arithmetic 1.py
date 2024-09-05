#modulus is symmetrical. If a = b (mod n) then b = a (mod n)
#so if 11 = x mod 6 then x = 11 mod 6

def calculate_integer(x, n):
    integer = x%n
    print(integer)

calculate_integer(8146798528947, 17)
