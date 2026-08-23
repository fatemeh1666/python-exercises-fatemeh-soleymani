a1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=input('enter passeord:')
c2=0
c1=0
while True:
   if len(s)!=8:
         print('رمز باید 8رقمی باشد')
         break

   for i in s[0:4]:
     if i  in a1:
       c1+=1
    

   for i in s[4:8]:
    if i.isdigit():
      c2+=1
   if c1==4 and c2==4:
       print('رمز معتبر است')
       
   if c1!=4 or c2!=4:
       print('رمز نامعتبر است')
   break    