def proccess_order(customer,*products,**options):
    products_list=list(products)
    price=100
    discount=options.get("discount",0)#اگر تخفیف نبود 0 درنظر بگیرد
    tax=options.get('tax',0)##اگر مالیات نبود 0 درنظر بگیرد
    shipping=options.get('shipping',0)#اگر هزینه ارسال نبود0درنظر بگیرد
    #for i in range(len(products_list)):
    base_total=len(products_list)*price
    after_discount=base_total-(base_total*(discount/100))
    after_tax=after_discount+ (after_discount*(tax/100))
    final_price=after_tax+shipping
    
    d={"customer":customer,
      "products":products_list,
      "discount":discount,
      "tax":tax,
      "shipping":shipping,
      "final_price":final_price}    
    
    return d
print(proccess_order('ali','keyboard','laptop','mouse',discount=10,tax=9,shipping=200000))