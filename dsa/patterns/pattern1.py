'''
Print this Pattern =>
1
12
123
1234
12345
'''

def pattern_print(rows: int):
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

pattern_print(5)


'''
2
4 6
8 10 12
14 16 18 20 
22 24 26 28 30 
'''

def even_pattern_print(rows: int):
    print()
    print("Even Pattern =>")
    num = 2
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print(num, end=" ")
            num += 2
        print()

even_pattern_print(5)