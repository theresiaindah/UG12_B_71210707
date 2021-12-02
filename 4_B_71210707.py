q = int(input('input : '))
r = 2 * q - 2
print ('Output :')

for index_q in range (0, q):
    for index_r in range (0, r):
        print(' ', end='')
    r -= 2

    for index_r in range (0, index_q + 1):
        if index_r == (index_r - 1) or index_q == (q + 1) or index_r == index_q:
            print('* ', end='')
        elif index_r == (index_r - 1) or index_q == (q - 1):
            print('* ', end='')
        elif index_r == 0:
            print('* ', end='')
        else:
            print(' ', end= ' ')

    print ('')
