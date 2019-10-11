# from collections import OrderedDict
# import itertools

# with open('./dump') as f:
#   data = f.read().strip().split('\n')

# data = [x.replace(':','').decode('hex') for x in data]
# # data = filter(lambda x: len(x) > 0 and x not in ['fjdsakf;lankeflksanlkfdn', 'fjdsakafsdbanlkfdn', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'aaaaa'], data)
# # data = [k for k, _ in itertools.groupby(data)]
# print data
# print ''.join(data)

from pwn import *
context.log_level = 'error'
out = ''
for i in range(100):
  data = process(['tshark', '-r', 'capture.pcap', '-Y', 'udp.stream eq {}'.format(i), '-T', 'fields', '-e', 'data.data']).recvall().strip()
  # if len(data) == 2:
  #   out += unhex(data)
  #   print out
  data = filter(lambda x: len(x)>0, data.split('\n'))
  data = ''.join(data).replace(':','')
  print unhex(data)