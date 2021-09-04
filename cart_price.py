products=[{'product_id':134, 'quantity':2, 'price':158, 'free_delivery':True},{'product_id':125, 'quantity':1, 'price':280, 'free_delivery':True}, {'product_id':589, 'quantity':4, 'price':610, 'free_delivery':False}]
cart={'client_id':'Robert1234', 'data_create':'2021-08-12', 'data_accessed':'2021-08-13'}
cart_price=0
for item in products:
    if item['price']:
        cart_price += item['price']* item['quantity']
print('Cart price:', cart_price)

