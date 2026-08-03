i= int(input('enter cost:'))
if 1000000<i:
     i=i-(i*0.15)
     print('cost is:',i)
if 500000<i<1000000:
       i=i-(i*0.1)
       print('cost is:',i)
if i<500000:
            i=i
            print('main cost is:',i)