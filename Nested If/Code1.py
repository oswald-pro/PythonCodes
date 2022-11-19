country = input("Enter your country name:")
products_price = int(input("Enter the cost of the products:"))


if country == "US"
    # print("Shipping cost is $50 ")
    if products_price <= 100:
        print ("Shipping cost is $25")
    elif products_price == 150:
        print ("Shipping cost is $5")

    else:
        print("Free")
    
elif country == 'UK':
    if products_price <=100:
        print ('Shipping cost is $100')
    else:
        print ('Free')
else:
    print ("Sorry ! we deliver our product only in US and UK")'''
