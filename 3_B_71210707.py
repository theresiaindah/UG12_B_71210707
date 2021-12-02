#task 1
a = (input("input : "))
b = 2 * len(a)-2
c =''

print("Output: ")

for index_a in range (0, len(a)-1):
    
    for index_b in range (0, b):
        print('', end ='')

    b -= 2
    for index_b in range (0, index_a + 1):
        print(f'{a[index_b]} ', end= '')
    
    print ('')

b = -1

for index_a in range (len(a)-1, -1,-1):
    for index_b in range (b, -1, -1):
        print('', end = '')
    
    b += 2
    for index_b in range (0, index_a + 1):
        print(f'{a[index_b]}', end='')

    print ('')