def print_range(n):
    """prints a table header"""
    print("   ", end="\t")
    for i in range(1,n+1):
        print(i, end="\t")
    print("\n :---"+("--")*((2*n)-1))

def multiples(n,m):
    """prints m multiples of m"""
    print(n,end=":"+"\t")
    for i in range(1,m):
        print(n*i, end="\t")
    print()

def styled_mult_table(m)
    """prints the header along with a table showing m multiples of m"""
        print_range(m)
        for i in range(1,m+1):
            multiples(i,m+1)

styled_mult_table(13)
