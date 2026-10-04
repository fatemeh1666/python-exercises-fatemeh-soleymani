transactions = [
 ("Ali", "deposits", 5000000),
 ("Ali", "withdraw", 1000000),
 ("Sara", "deposits", 8000000),
 ("Ali", "withdraw", 500000),
 ("Sara", "withdraw", 2000000),
 ("Reza", "deposits", 10000000)
]
d={}
final_repo={}
def analuze_transactions(transactions):
    
    for name, t,amount in transactions:
        if name not in d:
            d[name]={'deposits':0,'withdraw':0,'count':0}
        d[name]['count']+=1
        if t=='deposits' :
            d[name]['deposits']+= amount
        if t=='withdraw':
           d[name]["withdraw"]+=amount 
    #deposite=d[]     
        final_repo[name]={'deposits':d[name]['deposits'],
            "withdraw":d[name]['withdraw'],
            'balance_change':d[name]['deposits']-d[name]['withdraw'],
            'transactions':d[name]['count']}
        
    return d,final_repo
result=analuze_transactions(transactions)
import json
print(json.dumps(result, indent=4))   

 
def find_status(final_repo1):
    ##############بیشترین واریز
    max_deposite=0
    for i in final_repo1:
      if final_repo1[i]['deposits'] > max_deposite:
       max_deposite= final_repo1[i]['deposits']
  
    ###################بیشترین برداشت 
    max_withdraw=0
    for i in final_repo1:
      if final_repo1[i]['withdraw'] > max_withdraw:
       max_withdraw= final_repo1[i]['withdraw']
       ########################فعال ترین کاربر
       
    max_transactions=0
    humn=str
    for i in final_repo1:
        if final_repo1[i]['transactions'] > max_transactions:
           max_transactions= final_repo1[i]['transactions']
           humn=final_repo1[i]['transactions']
    return max_deposite, max_withdraw , max_transactions, humn
        
print(find_status(final_repo))