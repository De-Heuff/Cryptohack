from pwn import *

#convert hex to bytes
input_string = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

#iterate over ASCII characters
for i in range (0,128):
    result = xor(input_string, chr(i).encode("utf-8"))
    if b"crypto" in result: #b-for bytes-like object
        print(result)
        break
