from collections import OrderedDict
import itertools

with open('./dump') as f:
  data = f.read().strip().split('\n')

data = [x.replace(':','').decode('hex') for x in data]
data = filter(lambda x: len(x) > 0 and x not in ['fjdsakf;lankeflksanlkfdn', 'fjdsakafsdbanlkfdn', 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'aaaaa'], data)
data = [k for k, _ in itertools.groupby(data)]
print data
print ''.join(data)

# udp.stream eq 6
# picoCTF{StaT31355_636f6e6e}

icoCTF{StaT31355e