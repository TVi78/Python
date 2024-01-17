str=input("введите: ")
sep="!?/.,"
for i in sep:
    str=''.join(str.split(i))
print (len(set(str.split())))