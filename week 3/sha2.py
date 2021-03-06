from Crypto.Hash import SHA256

block_size = 1024

f = open('video.mp4', 'rb')
f.seek(0,2)                 # (offset, mode)
size = f.tell()
print size
last_block_size = size % block_size

lista = range(0,size, block_size)
lista.reverse()            

last_hash = ""
for l in lista:
    f.seek(l,0)
    block = f.read(block_size)
    h = SHA256.new()
    h.update(block)
    h.update(last_hash)
    last_hash = h.digest()

print last_hash.encode('hex')

