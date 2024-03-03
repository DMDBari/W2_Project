def shopping_cart():
    output = {}
    item =''
    cost =''
    quantity=''
    item_total = 0.0
    total = 0.0
    action = ''
    # print('Thank you for using our Shopping Cart')
    while action.title() != 'Quit':
        action = input('What would you like to do? (Add/Remove/Display/Clear/Quit)')
        if action.title() == 'Add':
            item = input('What item would you like to add to your cart?').capitalize()
            cost = input(f"What is the price of {item}?")
            quantity = input('How many would you like to add?')
            output [item] = cost, quantity
            print(f"{item} has been added to the cart.")
        elif action.title() == 'Remove':
            item = input('What item would you like to remove?').capitalize()
            removed = output.pop(item, 'gone')
            if removed == 'gone':
                print(f'It looks like there is no {item} in the cart')
            else:
                print(f"{item} has been removed from your cart")
        elif action.title() == 'Display':
            print('Your current cart includes:\n')
            for items, costs, totals in output.items():
                item_total = float(costs) * int(totals)
                total += item_total
                print('-'*15)
                print(f'Item: {items}, quantity: {totals}, total: ${item_total} ')
                print('-'*15)
            print(f'Your current total is ${total}')
            item_total = 0.0
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