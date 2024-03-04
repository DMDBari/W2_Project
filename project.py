def shopping_cart():
    output = []
    removed = True
    item =''
    cost =''
    quantity=''
    item_total = 0.0
    total = 0.0
    action = ''
    clear = ''
    change = True
    print('Thank you for using our Shopping Cart App')
    while action.title() != 'Quit':
        action = input('What would you like to do? (Add/Remove/Display/Clear/Quit)')
        if action.title() == 'Add':
            item = input('What item would you like to add to your cart?').capitalize()
            cost = input(f"What is the price of {item}?")
            quantity = input('How many would you like to add?')
            unit = {'item': item, 'cost': cost, 'quantity':quantity}
            for dictionary in output:
                if unit['item'] == dictionary['item']:
                    dictionary['cost'] = cost
                    dictionary['quantity'] = quantity
                    change = False
                    break
            if change:
                output.append(unit)
                print(f"{item} has been added to your cart")
            else:
                change = True
                print(f"{item} has been updated")
        elif action.title() == 'Remove':
            item = input('What item would you like to remove?').capitalize()
            for i in range(len(output)):
                if output[i]['item'] == item:
                    del output[i]
                    print(f"{item} has been removed from your cart.")
                    removed = False
                    break
            if removed:
                print(f"It appears that {item} was not in your cart.")
            else:
                removed = True
        elif action.title() == 'Display':
            print('Your current cart includes:\n')
            for dictionary in output:
                item_total = int(dictionary['quantity']) * float(dictionary['cost'])
                total += item_total
                print('-'*15)
                print(f'Item: {dictionary['item']}, quantity: {dictionary['quantity']}, total: ${item_total} ')
                print('-'*15)
            print(f'Your current total is ${round(total, 2)}')
            total = 0.0
        elif action.title() == 'Clear':
            clear = input("Are you sure?  This will permenantly delete all items in cart. (Yes/No)")
            if clear.title() == 'Yes':
                output = []
    else:
        print('Your current cart includes:\n')
        for dictionary in output:
            item_total = int(dictionary['quantity']) * float(dictionary['cost'])
            total += item_total
            print('-'*15)
            print(f'Item: {dictionary['item']}, quantity: {dictionary['quantity']}, total: ${item_total} ')
            print('-'*15)
        print(f'Your current total is ${round(total, 2)}')
        print('Thank you for using our Shopping Cart App')
        return
    
shopping_cart()