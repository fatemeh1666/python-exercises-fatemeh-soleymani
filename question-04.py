transactions = [
 ("Ali", "deposit", 50000000, 10),
 ("Ali", "withdraw", 2000000, 11),
 ("Ali", "withdraw", 3000000, 12),
 ("Ali", "withdraw", 4000000, 13),
 ("Ali", "withdraw", 5000000, 14),
 ("Ali", "withdraw", 6000000, 15),
 ("Sara", "deposit", 50000000, 20),
 ("Sara", "withdraw", 60000000, 21),
 ("Reza", "deposit", 150000000, 30)
]
limit=100000000

def check_large_transaction(transactions,limit):
    #بررسی موجودی بیش از 100 میلیون
        l_large=[]
       
        for username, t_type, amount, time in transactions:
            if  amount>=limit :
                l_large.append(f"مبلغ بیشتر از 100 میلیون است :{username} ")
             
        return l_large

result_check_large=check_large_transaction(transactions,limit)
#print(result_check_large)
def check_repeated_withdraw(transactions):   
   # بررسی بیش از 3 برداشت پشت سر هم برای یک کاربر## 
     withdraw_counts={}
     flags=[]
     for username, t_type, amount, time in transactions:
    #     if t_type=='withdraw':
     #        withdraw_counts[username]=withdraw_counts.get(username,0)+1
       if username in withdraw_counts:
          withdraw_counts[username]=withdraw_counts[username]+1
       else:
          withdraw_counts[username]=1 #{'Ali': 6, 'Sara': 2, 'Reza': 1}
     for username in withdraw_counts :
         if withdraw_counts[username]>=3:
             flags.append(f"  بیشتر از3 بار برداشت انجام داده است: {username}")
      
     return flags
#print(check_repeated_withdraw(transactions))         
def check_balance(transations):
    """بررسی اینکه ایا مبلغ برداشت بیش از موجودی است"""
    balance_sheet={}#برای نگهداری موجودی هر کاربر
    flg=[] 
    for username, t_type, amount, time in transactions:
     if username not in balance_sheet:
         balance_sheet[username]=0
     if t_type=='deposit':
         balance_sheet[username]+=amount
     elif t_type=='withdraw':
         if amount> balance_sheet[username]:
           flg.append(username)
         else:
             balance_sheet[username]-=amount
          
    return('میزان برداشت این فرد بیش از موجودی است:',flg[0])
#print(check_balance(transactions))

def detect_fraud(transactions):
    a=[]
    b=[]
    c=[]
    a=check_large_transaction(transactions,limit)
    b=check_repeated_withdraw(transactions)
    c=check_balance(transactions)
    return a,b,c
# در این تابع تراکنش های تکراری را حذف نکردم. مثلا اگر تراکنش بزرگ بود وبرداشت پشت سرهم
print("تراکنش های مشکوک:")
print(detect_fraud(transactions))