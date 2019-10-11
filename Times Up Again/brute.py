from pwn import *
context.log_level = 'error'

while True:
  sh = process(['/bin/bash', '-c', 'echo "0" | ./times-up-again'], cwd='/problems/time-s-up--again-_6_3b092353ed59a3db99109f8c0f6f5cd0')
  data =  sh.recvall()
  if 'Congrats' in data:
    print data
    exit()
  else:
    print '.',