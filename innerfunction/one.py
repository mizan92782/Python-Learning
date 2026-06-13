
def total_price(price):
   
    #hidding logic from enternal access
    def tax():
        if price>100:
            return price*0.10
        else:
            return price * 0.15
    
    return price + tax()




print(total_price(200))
print(total_price(90))


#   print(total_price.tax(499)) ======== this wil lbe eroor, 
# that why innder fucntion also use as encapsulation
