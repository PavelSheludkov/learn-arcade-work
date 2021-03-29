for i in range(1,10):
    for js in range(10-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        print(j, end=" ")
    for k in range(i-1,0,-1):
        print(k, end=" ")
    for ks in range(10-i):
        print(" ", end=" ")
    print()
for i in range(9,1,-1):
    for js in range (11-i):
        print(" ", end=" ")
    for j in range(1, i-1):
        print(j, end=" ")
    for k in range(i-1,0,-1):
        print(k, end=" ")
    print()