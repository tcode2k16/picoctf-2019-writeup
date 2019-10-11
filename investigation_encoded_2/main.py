import string
from pwn import *
# t1m3f1i3500000000000501af001
context.log_level = 'error'

v1 = '000000000400000012000000280000003C0000005200000064000000780000008E0000009E000000B4000000C8000000DA000000EA000000FC0000000E0100001E01000034010000480100005A0100006A01000072010000800100008C0100009A010000AA010000BC010000C8010000D6010000E0010000EA010000F0010000000200000A02000016020000220200003002000034020000'
v1 = unhex(v1)
print len(v1)
temp = []
for i in range(0, len(v1), 4):
  temp.append(u32(v1[i:i+4]))
# temp = temp[::2]
print len(temp)
v1 = temp
print v1

secret = '8BAA2EEEE8BBAE8EBBAE3AEE8EEEA8EEAEE3AAE3AEBB8BAEB8EAAE2EBA2EAE8AEEA3ABA3BBBB8BBBB8AEEE2AEE2E2AB8AA8EAA3BAA3BBA8EA8EBA3A8AA28BBB8AE2AE2EE3AB80000000000000000000000000000000000000000000000000000'
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


def enc(v):
  v = ord(v)
  if v == 32:
    v = 133
  if v > 47 and v <= 57:
    v += 75
  v -= 97
  if v != 36:
    v = (v+18)%36
  out = []
  for i in range(v1[v], v1[v+1]):
    out.append(getValue(i))
  return out

d = []

str_list = string.lowercase+' '+string.digits
print 'start'
for each in str_list:
  out = enc(each)
  print 'expect {}'.format(out)
  # print '       {}'.format(test(str_list[each]))
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
  for char, enc in d:
    # print index
    # print enc
    if data[i:i+len(enc)] == enc:
      flag += char
      i += len(enc)
      print flag
print flag

# print 'start'
# for i in range(1,9):
#   print test(' '*i)