import os


for filename in os.listdir('./test/'):
  #   print file
  # filename = './test/Item01 - Copy.bmp'
  filename = './test/' + filename
  print hex(int(os.path.getmtime(filename)))[2:].decode('hex')[2:]
  print hex(int(os.path.getctime(filename)))[2:].decode('hex')[2:]
  print hex(int(os.path.getatime(filename)))[2:].decode('hex')[2:]

