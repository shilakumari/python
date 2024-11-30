def create_table(n):
    table=[[0]*i for i in range(n)]
    return table
print(create_table(5))#[[], [0], [0, 0], [0, 0, 0], [0, 0, 0, 0]]

def create_table2(n):
    table=[list(range(i)) for i in range(n)]
    return table
print(create_table2(5))#[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]