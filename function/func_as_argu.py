
def tax_usa(price):
    return price * 0.10
    
def tax_uk(price):
    return price * 0.15
    
    
    
def total(func ,price):
 
    return price+ func(price)
    
    
    
price =348
print("Total price in usa: ",total(tax_usa,price))
print("Total price in  uk: ",total(tax_uk,price))