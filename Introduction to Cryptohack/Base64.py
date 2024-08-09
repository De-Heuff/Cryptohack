#Base64 allows us to represent binary data as an ASCII-string using an alphabet of 64 characters.
#Common usage in text-based systems, where characters can be misintrpreted in transferring media.
#Base64 uses 6 bit grouping to ensure encoded data is printable and humanly readable.

import base64
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytes_string = bytes.fromhex(hex_string)
base64_string = base64.b64encode(bytes_string)
print(base64_string)


