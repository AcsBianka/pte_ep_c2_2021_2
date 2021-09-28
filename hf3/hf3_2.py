input_product_price = input("Adja meg a termék árát:")
int_price = int(input_product_price)

if int_price <= 10000:
    print("A termék 10% kedvezményt kap, akciós ára:",int_price*0.9, "Ft")
else:
    print("A termék 20% kedvezményt kap, akciós ára:",int_price*0.8, "Ft")

