n=int(input("Enter number of rows:"))
ctr=1
for i in range(n):
    for j in range(i):

        if(i%2==0):
            print(ctr, end=" ")
            ctr += 1
        else:
            print(chr(ord('A')-1+ctr), end=" ")     #chr int to ASCII
            ctr += 1        #
    print()


