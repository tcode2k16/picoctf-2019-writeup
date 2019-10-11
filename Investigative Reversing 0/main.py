# picoCTF{f0und_1t_eeaec48b}
data = '7069636f43544b806b357a73696436715f65656165633438627d'.decode('hex')
data = bytearray(data)

for i in range(6, 15):
  data[i] -= 5

data[15] += 3

# for i in range(16, 26):
#   data[i] -= i

print data
