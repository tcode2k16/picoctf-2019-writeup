arr = []
for i in range(5, 0, -1):
  with open('./Item0{}_cp.bmp'.format(i), 'rb') as f:
    data = f.read()[2019:2019+10*8+40*1]
    arr.extend(data)


# data = data[723:723+(50*9)]

out = ''

for i in range(50):
  c = 0
  for j in range(8):
    c = c | (ord(arr[i*12+(7-j)])&1)
    c = c << 1
  c = c >> 1
  out += chr(c)
  print c
  print out

 # picoCTF{N1c3_R3ver51ng_5k1115_00000000000ade0499b}