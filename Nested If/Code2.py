# Nested If with the use of range method
country = input("Enter your country name:")
products_price = int(input("Enter the cost of the products:"))


if country == "US":
    if products_price in range(0, 100):
        print("Shipping cost for US is $25")
    elif products_price in range(101, 150):
        print("Shipping cost is $5")
    else:
        print("Free shipping for US")
    
elif country == "UK":
    if products_price in range(0, 50):
        print('Shipping cost for UK is $50')
    else:
        print('Free shipping for UK')
else:
    print("Sorry ! we deliver our product only in US and UK.")
