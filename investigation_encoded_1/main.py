import string
from pwn import *
# flag: 'encodedgxmurhtuou '

context.log_level = 'error'

v1 = '000000000C000000080000000E000000140000000A00000022000000040000002C0000000C000000300000000C0000003C0000000A00000048000000060000005200000010000000580000000C000000680000000C000000740000000A00000080000000080000008A0000000E000000920000000E000000A000000010000000AE0000000A000000BE00000008000000C800000006000000D00000000A000000D60000000C000000E00000000C000000EC0000000E000000F800000010000000060100000E000000160100000400000024010000'
v1 = unhex(v1)
temp = []
for i in range(0, len(v1), 4):
  temp.append(u32(v1[i:i+4]))
temp = temp[::2]
print len(temp)
v1 = temp

v2 = '08000000000000000C000000080000000E000000140000000A00000022000000040000002C0000000C000000300000000C0000003C0000000A00000048000000060000005200000010000000580000000C000000680000000C000000740000000A00000080000000080000008A0000000E000000920000000E000000A000000010000000AE0000000A000000BE00000008000000C800000006000000D00000000A000000D60000000C000000E00000000C000000EC0000000E000000F800000010000000060100000E000000160100000400000024010000'
v2 = unhex(v2)
temp = []
for i in range(0, len(v2), 4):
  temp.append(u32(v2[i:i+4]))
temp = temp[::2]
print len(temp)
v2 = temp
print v2

secret = 'B8EA8EBA3A88AE8EE8AA28BBB8EB8BA8EE3A3BB8BBA3BAE2E8A8E2B8AB8BB8EAE3AEE3BA8000000000000000000000000000000000000000000000000000000008'
secret = unhex(secret)

def getValue(a1):
  return (ord(secret[a1 // 8]) >> (7 - a1 % 8)) & 1;


def test(a):
  with open('./flag.txt', 'wb') as f:
    f.write(a)
  process('./mystery')
  with open('./output', 'rb') as f:
    data = bits(f.read())
  return data



d = []


print 'start'
for each in range(27):
  out = []
  for i in range(v1[each], v2[each]+v1[each]):
    out.append(getValue(i))
  print 'expect {}'.format(out)
  print '       {}'.format(test(chr(each+ord('a'))))
  d.append([each, ''.join(map(str, out))])
print 'end'

d.sort(key=lambda x: len(x[1]), reverse=True)

print d

with open('./real_output', 'rb') as f:
  data = ''.join(map(str,bits(f.read())))
print data
i = 0
flag = ''
while i < len(data):
  for index, enc in d:
    # print index
    # print enc
    if data[i:i+len(enc)] == enc:
      flag += chr(ord('a')+index)
      i += len(enc)
      print flag
print flag

print 'start'
for i in range(1,9):
  print test(' '*i)