from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter
     
key = ['140b41b22a29beb4061bda66b6747e14'.decode('hex'),
       '36f18357be4dbd77f050515c73fcf9f2'.decode('hex')]
cipher_text = ['4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'.decode('hex'),
               '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'.decode('hex'),
               '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'.decode('hex'),
               '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'.decode('hex')]
     
# Cipher text Cipher Block Chain(CBC) Decrypt
for i in range(2):
    iv = cipher_text[i][:16]
    cipher_text[i] = cipher_text[i][16:]
    decryptor = AES.new(key[0], AES.MODE_CBC, iv)
    plain = decryptor.decrypt(cipher_text[i])
     
    print 'message' + str(i + 1) + ': ' + plain
     
# Cipher text Counter Mode(CTL) Decrypt
for i in range(2,4):
    iv = cipher_text[i][:16]
    cipher_text[i] = cipher_text[i][16:]
    ctr = Counter.new(128, initial_value = long(iv.encode("hex"), 16))
    decryptor = AES.new(key[1], AES.MODE_CTR, counter = ctr)
    plain = decryptor.decrypt(cipher_text[i])
     
    print 'message' + str(i + 1) + ': ' + plain

'''
message1: Basic CBC mode encryption needs padding.
message2: Our implementation uses rand. IV
message3: CTR mode lets you build a stream cipher from a block cipher.
message4: Always avoid the two time pad!

3rd example:- 

key = "36f18357be4dbd77f050515c73fcf9f2".decode('hex')
cyphertext = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc3\
88d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
iv1 = cyphertext[:32].decode('hex')
iv2 = hex(int(cyphertext[:32], 16) + 1)[2:][:-1].decode('hex')  # iv+1
iv3 = hex(int(cyphertext[:32], 16) + 2)[2:][:-1].decode('hex')  # iv+2
iv4 = hex(int(cyphertext[:32], 16) + 3)[2:][:-1].decode('hex')  # iv+3
ct1 = cyphertext[32:64].decode('hex')
ct2 = cyphertext[64:96].decode('hex')
ct3 = cyphertext[96:128].decode('hex')
ct4 = cyphertext[128:].decode('hex')
print pycrypto_decrypt(key, iv1, ct1) + pycrypto_decrypt(key, iv2, ct2) + pycrypto_decrypt(key, iv3, ct3) + pycrypto_decrypt(key, iv4, ct4)

'''
