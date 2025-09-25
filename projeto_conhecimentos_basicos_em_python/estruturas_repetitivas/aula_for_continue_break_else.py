for i in range(10):
    if i == 3:
        print('Pulando o 3')
        continue
    if i == 8:
        print('Parando no 8, else não executara porque tem o break!')
        break
    
    print(i)

    for j in range(1, 3):
        print(i, j)
else:
    print('Cheguei no else')