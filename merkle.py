from Crypto.Cipher import AES
from random import randint

#private values
s = 25      #len(secret)
N = 100000  #len(secrets)
n = 64      #len(msg)

#Placeholder
msgs = []
keys = []
secrets = []

#ALICE (Encryption)
for i in range(0, N):
    secret = str(randint(1000000000000000000000000, 9999999999999999999999999))
    key = str(randint(1000, 9999))

    enc_suite = AES.new(key*4, AES.MODE_CBC, key*4)
    msg = enc_suite.encrypt('0'*(n-s) + secret)

    msgs.append(msg)
    keys.append(key)
    secrets.append(secret)

#ALICE sends "msgs" Block to BOB

#BOB (Brute force Decryption)
decrypted_msg = ''
rand_msg_solve = randint(0, N)

while not decrypted_msg.find('0'*(n-s)) == 0:
    key = str(randint(1000, 9999))
    dec_suite = AES.new(key*4, AES.MODE_CBC, key*4)
    decrypted_msg = dec_suite.decrypt(msgs[rand_msg_solve])


print 'Bob decrypted secret:\t\t' + decrypted_msg[(n-s):]
print 'Alice secret (' + str(rand_msg_solve) + '):\t\t' + secrets[rand_msg_solve]
