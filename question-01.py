text='Good Morning to yoy to 1002'

l=text.split()
d_text=text.strip()
def analyze_text(text):
    u=0
    k=0
    y=0
    p=0
    w=0
    print(l)
    for i in text:
        
        if i.islower():
                k+=1
        if i.isupper():
                  u+=1
        if i.isdigit():
             y+=1
             ############################پرتکرار ترین کلمه
    b_mx=0
    b2=0
    c_ind=0
    d=0
    for i in range(0,len(l)):
        b2=l.count(l[i])
        if b2>b_mx:
            b_mx=b2
            c_ind=i
            #################پرتکرار ترین حرف
    b_mn=0
    b3=0
    c_ind2=0
    d=0
    for i in range(0,len(text)):
        b3=text.count(text[i])
        
        if b3>b_mn:
            b_mn=b3
            c_ind2=i 
   ############################طولانی ترین کلمه###################################         
    b_max=0
    c_index=0
    l_b_max=[]
    l_new_index=[]
    for i in range(0,len(l)):
        if len(l[0])<len(l[i]):
          b_max=len(l[i])
          c_index=i
          l_b_max.append(b_max)
          l_new_index.append(i)
    #for i in range(0,len(l)):
        if len(l[0])<len(l[i]):
            b_max=len(l[i])
            c_index=0
            l_b_max.append(b_max)
            l_new_index.append(0)
    #print('max_charrrr',b_max,'indexxxxx',c_index)
    #print(l_b_max)
    d_c=0
    for j in range (0,len(l_b_max)):
                    if l_b_max[j]==b_max:
                       
                        d_c=l_new_index[j]
                        break
                    #########################کوتاه ترین کلمه
    b_min=0
    c_index1=0
    l_b_min=[]
    l_new_index1=[]
    for i in range(0,len(l)):
        if len(l[0])>len(l[i]):
          b_min=len(l[i])
          c_index1=i
          l_b_min.append(b_min)
          l_new_index1.append(i)
        if len(l[0])<len(l[i]):
              b_min=len(l[0])
              c_index1=0
              l_b_min.append(b_min)
              l_new_index1.append(0)
    #print('min_charrrr',b_min,'indexxxxx111111',c_index1)
    #print(l_b_min)
    dd=0
    for j in range (0,len(l_b_min)):
                    if l_b_min[j]==b_min:
                        dd=l_new_index1[j]
                        break                
     ###########################333palindrom
    
    
    for i in range (len(l)):
        l[i]=l[i].lower()
  
    s_number=0
    for i in range (len(l)):
     s=0
     lengh=len(l[i])
     for j in range(lengh//2):
        if l[i][j]!= l[i][lengh-1-j]:
               s+=1
     if s==0:          
       s_number+=1          
    return k,u,y,b_mx,c_ind,b_mn,c_ind2,d_c,b_max,s_number,b_min,dd
m,n,t,b_mx_out,c_ind_out,b_mn_out,c_ind2_out,d_c_out,b_max_out,s_number_out,b_min_out,dd_out=analyze_text(text)
#print(m,n,t)
print('word:',len(l))
print('letters',m+n)  
print('digit:',t) 
print('Most_common_word:',l[c_ind_out] , '-->',b_mx_out) 
print('Most_common_letter:' ,text[c_ind2_out],'-->',b_mn_out)  
print('longestword:',l[d_c_out],'.....length:',b_max_out) 
print('shortest word:',l[dd_out],'.....length:',b_min_out)
print('total uppercase:',n)
print('total lowercase:',m)
print('number of palindrom word',s_number_out)