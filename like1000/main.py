from os import system
# picoCTF{l0t5_0f_TAR5}
system('unar ./1000.tar'.format())
for i in range(999, -1, -1):
  system('unar ./{}/{}.tar'.format(i+1, i))