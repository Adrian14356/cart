products=[{'product_id':134, 'quantity':2, 'price':158, 'free_delivery':True},{'product_id':125, 'quantity':1, 'price':280, 'free_delivery':True}, {'product_id':589, 'quantity':4, 'price':610, 'free_delivery':False}]
cart={'client_id':'Robert1234', 'data_create':'2021-08-12', 'data_accessed':'2021-08-13'}
free_delivery=True # if we have one or more item with True inside free delivery print True 
for item in products:
    if item['free_delivery']:
        free_delivery=True
print('Is the delivery free?', free_delivery)
free_delivery=False #if we have just one item with False inside free delivery print false 
for item in products:
    if item['free_delivery']:
        free_delivery=False
print('Is the delivery free?', free_delivery)



