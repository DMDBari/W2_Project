def shopping_cart():
    output = []
    removed = True
    item =''
    cost =''
    quantity=''
    item_total = 0.0
    total = 0.0
    action = ''
    print('Thank you for using our Shopping Cart')
    while action.title() != 'Quit':
        action = input('What would you like to do? (Add/Remove/Display/Clear/Quit)')
        if action.title() == 'Add':
            item = input('What item would you like to add to your cart?').capitalize()
            cost = input(f"What is the price of {item}?")
            quantity = input('How many would you like to add?')
            unit = {'item': item, 'cost': cost, 'quantity':quantity}
            output.append(unit)
            print(f"{item} has been added to the cart.")
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
            for dict in output:
                item_total = int(dict['quantity']) * float(dict['cost'])
                total += item_total
                print('-'*15)
                print(f'Item: {dict['item']}, quantity: {dict['quantity']}, total: ${item_total} ')
                print('-'*15)
            print(f'Your current total is ${round(total, 2)}')
            total = 0.0
        # elif action.title() == 'Clear':
    else:
        for items, costs, totals in output.items():
            print('-'*15)
            print(f"")
            print('-'*15)
        print('')
        return
    
shopping_cart()