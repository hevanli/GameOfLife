m1 = [[0 for _ in range(10)] for _ in range(10)]
m2 = [[i for i in range(10)] for _ in range(10)]

def printM(m):
    for row in m:
        for value in row:
            print(value,end="")
        print()

def copy_matrixes(m1, m2):
    '''
    copies the contents of m1 onto m2
    '''
    for i, row in enumerate(m1):
            for j, value in enumerate(row):
                m2[i][j] = value

copy_matrixes(m1, m2)

printM(m1)
printM(m2)
