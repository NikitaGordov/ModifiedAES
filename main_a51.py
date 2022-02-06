import A51

#byteArg = b'\xff\xfe\xfd'
byteArg = b'abc'
plaintextByteArg = b'\xa4\x96G'
finalKey = A51.initialize_and_process(byteArg) #seed for final key
byteEnc = A51.encrypt(plaintextByteArg, finalKey)
byteDec = A51.decrypt(byteEnc, finalKey)

print("----------------------------------------------------------")
print("----------------------------------------------------------")

print("byteEnc in main", byteEnc)
print("len byteEnc", len(byteEnc))


print("byteDec in main", byteDec)

