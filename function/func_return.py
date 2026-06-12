
def tax_usa(price):
    return price * 0.10
    
def tax_uk(price):
    return price * 0.15
    
    
def user_country_tax(country):
    if country == 'uk':
        return tax_uk
    return tax_usa
    

country ='uk'
price =348

tax = user_country_tax(country)(price) #returing function
print(f"user price :  {tax}")

