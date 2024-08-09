#There are four main properties to consider using the XOR operator:
# Commutative means that the order of XOR operations is not important.
# Associative means that a chain of operations can be carried out without order (no brackets)
# Identiy = XOR with 0 does nothing (A^0 = A)
# Self inverse = X with XOR returns zero


from pwn import *
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key1_2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_key123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

#If A^B=C, A^C=B and C^B =A, if  we XOR result of Key_2^Key_1 we should get Key2.
#First decode all hex values to bytes. Then retrieve Key2 and Key 3

key2 = xor(bytes.fromhex(key1_2), key1)
key3 = xor(bytes.fromhex(key2_3), key2)

#XOR'ing all keys together
key1_2_3 = xor(bytes.fromhex(key1_2), key3)

#XOR result with final value
flag = xor(bytes.fromhex(flag_key123), key1_2_3)

print(flag)
