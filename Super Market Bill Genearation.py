import pandas as pd
itemAvaialablieDict={}
shoppingDict={}
userName=input('Enter UserName: ')
print('\n')
WelcomeMsg=f'Welcome to grocery store {userName}'
len_title=len(WelcomeMsg)
print(len_title*'*')
print(WelcomeMsg)
print(len_title*'*')
print('*'*15,'Availabe items in the store','*'*15)
my_file=open('grocery store.txt')
file_line=my_file.readline()
itemsAvailable=my_file.readlines()
my_file.close()
# print(file_reads)
for item in itemsAvailable:
    item_name=(item.split()[0])
    item_price=(item.split()[1])
    print(f'{item_name}:{item_price}')
    itemAvaialablieDict.update({item_name: float(item_price)})
# print(itemAvaialablieDict)
print('*'*15)
proceed_shopping=input('Want to buy anything? (yes/no): ')
while proceed_shopping.lower()=='yes':
    item_added=input('Add an item: ')
    if item_added.lower() in itemAvaialablieDict:
        item_qty=int(input('Add the quantity: '))
        shoppingDict.update({item_added:{'quantity':item_qty,'subtotal':itemAvaialablieDict[item_added.lower()]*item_qty}})
        print(shoppingDict)
    else:
        print('Unable to available item')
    proceed_shopping=input('Want to buy anything? (yes/no): ')
else:
    print('\n\n')
    print('*****Bill Summary***** ')
    print('\n')
    print('Item     Quantity        SubTotal')
    total=0
    gst=18
    for key in shoppingDict:
        print(f"{key}   {shoppingDict[key]['quantity']} {shoppingDict[key]['subtotal']}")
        total=total+shoppingDict[key]['subtotal']
        print(f'Total: {total}')
        # print('\n')
        # print(t.count('subtotal'))
        # print(' '*len(t-15))
        # gst=(total*5)/100
        # Grandtotal=total+gst
    print('Hope to see you back soon!')
    print('Thank You')
