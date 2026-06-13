def calculate_prices_tax(price):
    return price + price* 0.10




#product price 
price =[430,234,333,664,323]

#calculate price for all product

final_price = map(calculate_prices_tax,price)


# as map return obect wr dont see resutl
print(final_price)




# make list and get resutl
print(list(final_price))



