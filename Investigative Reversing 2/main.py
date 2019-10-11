with open('./encoded.bmp', 'rb') as f:
  data = f.read()

data = data[2000:2000+(50*8)]

out = ''

for i in range(50):
  c = 0
  for j in range(8):
    c = c | (ord(data[i*8+(7-j)])&1)
    c = c << 1
  c = c >> 1
  out += chr(c+5)
  print c
  print out

# picoCTF{n3xt_0n30000000000000000000000000f69eb8c8}

