v1 = int (input("digite um valor"))
v2 = int (input("digite um valor"))
v3 = int (input("digite um valor"))
if v1>v2 and v1>v3:
    if v2>v3:
        print(v1,v2,v3)
    else:
        print(v1,v3,v2)
elif v2>v1 and v2>v3:
    if v1>v3:
        print(v2,v1,v3)
    else:
        print(v2,v3,v1)
else:
    if v2>v1:
        print(v3,v2,v1)
    else:
        print (v3,v1,v2)