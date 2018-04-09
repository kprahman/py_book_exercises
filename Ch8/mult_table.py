def print_range(n):
    print("   ", end="\t")
    for i in range(1,n+1):
        print(i, end="\t")
    print("\n :---"+("--")*((2*n)-1))

print_range(12)

def mult_table(n):
    print(n,end=":"+"\t")
    for i in range(1,13):
        print(n*i, end="\t")
    print()

for i in range(1,13):
    mult_table(i)


format = ""