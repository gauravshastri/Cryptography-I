import os ,sys
from Crypto.Hash import SHA256
import binascii

def getblock(f):
    for offset in reversed(range(0, os.path.getsize('video.mp4'), 1024)):
        f.seek(offset)
        yield f.read(1024)

fh1 = open('video.mp4', "rb")
fh2 = open('hash.txt',"r+")


h2=''

for block in getblock(fh1):
	block+= binascii.unhexlify(h2)#to convert hex into binary
	h = SHA256.new(block)
	h2=h.hexdigest()
	fh2.write(h2+'\n')

fh1.close()
fh2.close()
