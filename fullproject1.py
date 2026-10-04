veg=['brinjal','tomato','onion']
quantity=[10,20,15]
price=[65,20,30]

while True:
    cart_items=[]
    cart_qty=[]
    cart_amount=[]
    while True:
        item = input('what do you want: ')
        if item == 'done':
            if len(cart_items)>0:
                print('='*10,'SHOP','='*10)
                for it in zip(cart_items,cart_qty,cart_amount):
                    print(f'{it[0]: <10}{it[1]: <5}{it[2]: <5}')
                print('='*26)
                print('TOTAL',' '*8,sum(cart_amount))
            break
            

        if item in veg:
            qty = float(input('How many kgs: '))
            idx = veg.index(item)
            if qty<=quantity[idx]:
                amt = qty*price[idx]
                quantity[idx]= quantity[idx]-qty
                cart_items.append(item)
                cart_qty.append(qty)
                cart_amount.append(amt)
                print(item,'is added to cart')

            else:
                print('out of stock')           


        else:
            print(item,'is not available')

    ch = input('Do you want to close shop(yes/no): ')

    if ch=='yes':
        print("Generate Report: ")
        break

cost_price=[45,12,10]

while True:
    print()
    print('1. Add')
    print('2. Update')
    print('3. Delete')
    print('4. Reports')
    print('5. Exit')

    choice=input('Enter your choice: ')

    
    if choice=='1':

        item=input('Enter vegetable name: ')

        if item in veg:
            print('Item already exists')

        else:
            qty=float(input('Enter quantity: '))
            selling_price=float(input('Enter selling price: '))
            buying_price=float(input('Enter cost price: '))

            veg.append(item)
            quantity.append(qty)
            price.append(selling_price)
            cost_price.append(buying_price)

            print(item,'added successfully')

    elif choice=='2':

        item=input('Enter vegetable name to update: ')

        if item in veg:

            idx=veg.index(item)

            quantity[idx]=float(input('Enter new quantity: '))
            price[idx]=float(input('Enter new selling price: '))
            cost_price[idx]=float(input('Enter new cost price: '))

            print(item,'updated successfully')

        else:
            print(item,'not found')

   
    elif choice=='3':

        item=input('Enter vegetable name to delete: ')

        if item in veg:

            idx=veg.index(item)

            veg.pop(idx)
            quantity.pop(idx)
            price.pop(idx)
            cost_price.pop(idx)

            print(item,'deleted successfully')

        else:
            print(item,'not found')

  
    elif choice=='4':

        print()
        print('1. Vegetable Report')
        print('2. Revenue')
        print('3. Itemized Profit')

        report=input('Enter your choice: ')

        
        if report=='1':

            print()
            print('VEGETABLE REPORT')

            for item,qty,p in zip(veg,quantity,price):
                print(item,qty,p)


      
        elif report=='2':

            print()
            print('REVENUE')

            print('Total Revenue:',sum(cart_amount))

        
        elif report=='3':

            print()
            print('ITEMIZED PROFIT')

            for i in range(len(veg)):

                profit=price[i]-cost_price[i]

                print(veg[i],profit)

    
    elif choice=='5':

        print('Thank you for using VCUBE SHOP')
        break

    else:
        print('Invalid choice')
