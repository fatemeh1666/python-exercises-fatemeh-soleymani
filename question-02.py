import random
t=['sang','kaghaz','gheychi']
while True:   
    h=random.choice(['sang','kaghaz','gheychi'])
    print(' random of computer is:',h)
    g=input('یکی از گزینه ها را وارد کن:')
    if h=='sang' and g=='kaghaz':
       print('computer is win')
    if h=='sang' and g=='gheychi':
       print('computer is win')
       
    if h=='kaghaz' and g=='gheychi':
       print('human is win')
    if h=='kaghaz' and g=='sang':
          print('human is win')
          
    if h=='gheychi' and g=='sang':
          print('human is win')
    if h=='gheychi' and g=='kaghaz':
          print('computer is win')
          
    
    if( h=='kaghaz' and g=='kaghaz') or (h=='gheychi' and g=='gheychi') or (h=='sang' and g=='sang') :
        continue
   
    #if g!= 'sang' or 'gheychi' or ' kaghaz':
   #             print('مقدار صحیح وارد کنید')
    if g not in t:
       print('مقدار صحیح وارد کنید')
    if g=='exit':
            break