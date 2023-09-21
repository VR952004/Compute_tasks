n=int(input("Enter the number of rows:"))

for i in range(1,n+1,1):
    if i==1:
        for j in range(n-i):
            print(" ",end="")
        print("*",end="")

    elif i==n:
        for j in range(n):
            print("* ",end="")

    else:
        for j in range(n - i):
            print(" ",end="")

        for j in range(1, 2*i, 1):
            if j==1 or j==2*i-1:
                print("*",end="")
            else:
                print(" ",end="")

    print()
