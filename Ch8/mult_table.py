def print_range(n):
    print("   ", end="\t")
    for i in range(1,n+1):
        print(i, end="\t")
    print("\n :---"+("--")*((2*n)-1))

def mult_table(n,m):
    print(n,end=":"+"\t")
    for i in range(1,m):
        print(n*i, end="\t")
    print()

def styled_mult_table(m):
        print_range(m)
        for i in range(1,m+1):
            mult_table(i,m+1)

styled_mult_table(13)
