i= int(input('enter distance(k/m):'))
if i<2:
    cost=20
else:
    cost=(i-2)*5+20
    print('cost is:',cost)