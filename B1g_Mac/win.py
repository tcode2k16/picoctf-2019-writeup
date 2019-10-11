import pywintypes, win32file, win32con

import os


def getFileCreationTime(fname):
    wintime1 = pywintypes.Time(0)
    wintime2 = pywintypes.Time(0)
    wintime3 = pywintypes.Time(0)
    winfile = win32file.CreateFile(
        fname, win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None, win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL, None)

    wintime1, wintime2, wintime3 = win32file.GetFileTime(winfile)

    winfile.close()

    print hex(int(wintime1))[2:].decode('hex')
    print hex(int(wintime2))[2:].decode('hex')
    print hex(int(wintime3))[2:].decode('hex')




for filename in os.listdir('./test/'):
  #   print file
  # filename = './test/Item01 - Copy.bmp'
  filename = './test/' + filename
  getFileCreationTime(filename)
  # print hex(int(os.path.getmtime(filename)))[2:].decode('hex')[2:]
  # print hex(int(os.path.getctime(filename)))[2:].decode('hex')[2:]
  # print hex(int(os.path.getatime(filename)))[2:].decode('hex')[2:]

