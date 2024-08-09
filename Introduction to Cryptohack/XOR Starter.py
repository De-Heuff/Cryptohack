#XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise.
#XOR-denotation in programme language = ^

string = "label"
new_string = ""

for ch in string:
    new_string += (chr(ord(ch)^13))

print(new_string)



