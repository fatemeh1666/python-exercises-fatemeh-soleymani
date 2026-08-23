import random
h=random.randint(1,10)
print(h)
while True:
   # print('enter number')
    g=int(input( 'enter number:'))
    if g>h:
        print('enter  smaller number:')
    if g<h:
        print('enter bigger number:')
    if g==h:
        print('tabrik')
        break