header = '89504e470d0a1a0a'
header = map(ord,header.decode('hex'))

with open('./out.png','rb') as f:
  data = bytearray(f.read())

for i, each in enumerate(header):
  data[i] = each

# data = str(data).replace('495224f0'.decode('hex'), '38d82c82'.decode('hex'))

print '495224f0'.decode('hex') in data
with open('./flag.png','wb') as f:
  f.write(data)
