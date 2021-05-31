for i in range(4):
    for j in range(4):
        if(i<j):
            print(chr(65+14+j), end=" ")
        else:
            print(chr(65+j), end=" ")
    print()