logs = [
 ("Ali", "LOGIN", 200),
 ("Ali", "DOWNLOAD", 200),
 ("Sara", "LOGIN", 403),
 ("Reza", "LOGIN", 200),
 ("Sara", "LOGIN", 403),
 ("Sara", "LOGIN", 403),]
#for name, status, value in ogs:

def status_login(logs):
    l_infor={}
    sc=0
    not_sc=0
    l_mashkok=[]
    #ساخت دیکشنری برای وارد کردن اطلاعات هر کاربر
    for name, status, value in logs: 
            if name not in l_infor:
                l_infor[name]={'success':0 , 'failed':0, 'total':0}
                # تعداد لاگین موفق
            if status=="LOGIN" and value==200:
                l_infor[name]['success']+=1
                sc+=1
                # تعدادد لاگین ناموفق
            if status=='LOGIN' and value==403:
                l_infor[name]['failed']+=1
                not_sc+=1
            l_infor[name]['total']+=1
            #بررسی مشکوک بودن
    for name in l_infor:
        if l_infor[name]['failed']>=3:
            l_mashkok.append(name)
       # else:
          #{status['success']:<5|{status['failed']<5}|{status[total]<5}| {status[total]<5})  
    return l_infor,sc,not_sc,l_mashkok
l_infor,a,b,mashkok=status_login(logs)
#print(a,b,c) 
print("------------ گزارش نهایی---------------")   

print("تعداد لاگین موفق:", a)
print("تعداد لاگین ناموفق:", b)
for name in l_infor:
    print(name,"تعداد" ,l_infor[name]['total'], "عملیات انجام داده است")
#for name in l_infor:
print(f"[!]هشدار : کاربر {mashkok} مشکوک است . خطای 403")