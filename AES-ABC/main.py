# picoCTF{d0Nt_r0ll_yoUr_0wN_aES}
import math


BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))


def to_bytes(n):
  s = hex(n)
  s_n = s[2:]
  if 'L' in s_n:
    s_n = s_n.replace('L', '')
  if len(s_n) % 2 != 0:
    s_n = '0' + s_n
  decoded = s_n.decode('hex')

  pad = (len(decoded) % BLOCK_SIZE)
  if pad != 0:
    decoded = "\0" * (BLOCK_SIZE - pad) + decoded
  return decoded


def remove_line(s):
  # returns the header line, and the rest of the file
  return s[:s.index('\n') + 1], s[s.index('\n')+1:]


def parse_header_ppm(f):
  data = f.read()

  header = ""

  for i in range(3):
    header_i, data = remove_line(data)
    header += header_i

  return header, data


with open('./body.enc.ppm','rb') as f:
  header, data = parse_header_ppm(f)

blocks = [data[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE]
          for i in range(len(data) / BLOCK_SIZE)]

for i in range(len(blocks)-1, 0, -1):
  cur = blocks[i]
  prev = blocks[i-1]
  cur = (int(cur.encode('hex'), 16)-int(prev.encode('hex'), 16))%UMAX
  blocks[i] = to_bytes(cur)

with open('./flag.ppm','wb') as f:
  f.write(header)
  f.write("".join(blocks))