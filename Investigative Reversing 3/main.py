with open('./encoded.bmp', 'rb') as f:
  data = f.read()

data = data[723:723+(50*9)]

out = ''

for i in range(50):
  c = 0
  for j in range(8):
    c = c | (ord(data[i*9+(7-j)])&1)
    c = c << 1
  c = c >> 1
  out += chr(c)
  print c
  print out

 # picoCTF{4n0th3r_L5b_pr0bl3m_0000000000000aa9faea3} 
