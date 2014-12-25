import binascii
import sys

def byte_to_binary(n):
    return ''.join(str((n & (1 << i)) and 1) for i in reversed(range(8)))

def hex_to_binary(h):
    return ''.join(byte_to_binary(ord(b)) for b in binascii.unhexlify(h))

def strxor(a, b):     # xor two strings of different lengths

    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
'''
ord(c) - takes one character c and returns its ASCII value
chr(v) - exactly the opposite. Takes one value in the range 0..255 and returns one character
hex(n) - returns the hexadecimal representation (string) of the number n. It will start with '0x' and then the characters of the representation. The number of characters is as much as needed, no leading zeros. This means hex(5) is 3 characters, and hex(70) is 4 characters. Try it out.
bin(n) - the same for binary. returns a string of the binary representation of n. starting with '0b'
0b1110011 - run it in the interpreter. This is simply a way to write a number in binary form. Python immediately translates it to an integer type as any other integer
0x6e643 - same as above for hexadecimal representation
int(s, b) - translates the string s to an integer, assuming the string s is the representation in the base of size b
list(x) - whatever type of sequence x is, make a string with the same sequence
''.join(seq) - takes a sequence of strings (or characters for that matter) and return one string concatenated of them all
'''

cts = [
    (
        '315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b163'
        '49c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857'
        '553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc415'
        '56bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d5'
        '24400a19b159610b11ef3e'
    ),

    (
        '234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b'
        '07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205'
        '132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b'
        '028aa76eb7b4ab24171ab3cdadb8356f'
    ),

    (
        '32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b'
        '07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257'
        '527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb'
    ),

    (
        '32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a'
        '029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f457'
        '5432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d8354'
        '02bca670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea'
        '2e4c1404e1315a1010e7229be6636aaa'
    ),

    (
        '3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe568'
        '08c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d'
        '562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b'
        '40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070'
    ),

    (
        '32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a'
        '19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512'
        '472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d119'
        '02aebc66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce'
        '35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983'
        '122b11be87a59c355d25f8e4'
    ),

    (
        '32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b'
        '01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea12'
        '5d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f8341'
        '4aaaf261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce'
        '2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894'
        '473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce'
    ),

    (
        '315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce568'
        '01d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04'
        '132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c547'
        '4da2f276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3'
    ),

    (
        '271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e'
        '04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716'
        '132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f15'
        '43efa270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a'
        '2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027'
    ),

    (
        '466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39'
        '598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf357'
        '5c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83'
    )
]

#cts = [bytearray.fromhex(ct) for ct in cts]
#for i in cts:
#	print hex_to_binary(i)+"\n"

m=bin(0)
x='32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904'
print "hi"

for i in cts:
	m=strxor(x,i).encode("hex")
	print m+"\n"

#print m^bin(ord(' '))
#p='723c0a1c5722514b5a1b0a511e3851020f11447b1f0c546e065f0c0e0c5f405d534154545343158fcebc4a501a570a170c0b540045404a04544c12161c0619124a5d455a56190652094a134b0d4e051d495d5a'
#p='0702035500530108075c5b590053030400010406000d0001045f065700570002000b070704010759070f05015a5d0655005a05020052025c000b055c0403050f055804070500005005580404075c5302555357010456000303550250000f0403005000035c040502040504020104020d075b0455010701520407000303500109045500025e575c575a000309000400500050015a0103015f00505d55000558500455000f0556'
#m=strxor('00100000',p.decode("hex")).encode("hex")
#print binascii.unhexlify(m)

'''
We can factor the number 15 with quantum computers. We can also factor the number 1
Euler would probably enjoy that now his theorem becomes a corner stone of crypto - 
The nice thing about Keeyloq is now we cryptographers can drive a lot of fancy cars
The ciphertext produced by a weak encryption algorithm looks as good as ciphertext 
You don't want to buy a set of car keys from a guy who specializes in stealing cars
There are two types of cryptography - that which will keep secrets safe from your l
There are two types of cyptography: one that allows the Government to use brute for
We can see the point where the chip is unhappy if a wrong bit is sent and consumes 
A (private-key)  encryption scheme states 3 algorithms, namely a procedure for gene
The Concise OxfordDictionary (2006) defines crypto as the art of  writing o r sol
The secret message is: When using a stream cipher, never use the key more than once
'''

'''
0x54 0x68 0x65 0x20 0x73 0x65 0x63 0x72 0x65 0x74 0x20 0x6d 0x65 0x73 0x73 0x61 0x67 0x65 0x20 0x69 0x73 0x3a 0x20 0x57 0x68 0x65 0x6e 0x20 0x75 0x73 0x69 0x6e 0x67 0x20 0x61 0x20 0x73 0x74 0x72 0x65 0x61 0x6d 0x20 0x63 0x69 0x70 0x68 0x65 0x72 0x2c 0x20 0x6e 0x65 0x76 0x65 0x72 0x20 0x75 0x73 0x65 0x20 0x74 0x68 0x65 0x20 0x6b 0x65 0x79 0x20 0x6d 0x6f 0x72 0x65 0x20 0x74 0x68 0x61 0x6e 0x20 0x6f 0x6e 0x63 0x65
'''
