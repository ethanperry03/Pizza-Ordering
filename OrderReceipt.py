'''
Ethan Perry
4/27/2022
'''

def pizza_cost(za):
#-------------cost/quant/print for pizza-------------------
    subtotal = [0]
    temp_pcost = 0
    
    if len(za) != 0:
        for k in range(len(za)):
            output_str = ''
            temp_pcost = 13.00
            for i in range(len(za[k])):
                if za[k][i] == "Mushroom":
                    temp_pcost += 0.50
                    output_str = output_str + "Mushroom"+", "
                elif za[k][i] == "Olive":
                    output_str = output_str + "Olive"+", "
                    temp_pcost += 0.50
                elif za[k][i] == "Anchovy":
                    output_str = output_str + "Anchovy"+", "
                    temp_pcost += 2.00
                elif za[k][i] == "Ham":
                    output_str = output_str + "Ham"+", "
                    temp_pcost += 1.50
                elif za[k][i] == "Pepperoni":
                    output_str = output_str + "Pepperoni"+", "
                    temp_pcost += 1.00 
                subtotal.append(temp_pcost)
            output_str = output_str[0:-2]
            output_cost = format(temp_pcost, '.2f')
            print(f"{'Pizza':<8}{output_str:<45}{output_cost:<15}{1:<15}{output_cost:>5}")
    
    print(output_str)
    return(subtotal)


def drinks_cost(drinks):
#-----------------cost/quant/print for drinks---------------------
    sdrinks = 0
    mdrinks = 0
    ldrinks = 0
    drink_total = 0
    subtotal = [0]
    
    for k in range(len(drinks)):
        for i in range(len(drinks[k])):
            if drinks[k][i] == 'small':
                sdrinks += 1
                drink_total += 2.00
            elif drinks[k][i] == "medium":
                mdrinks += 1
                drink_total += 3.00
            elif drinks[k][i] == "large":
                ldrinks += 1
                drink_total += 3.50

    drinkscosts = format(sdrinks * 2.00, '.2f')
    drinkscostm = format(mdrinks * 3.00, '.2f')
    drinkscostl = format(ldrinks * 3.50, '.2f')

    if sdrinks > 0:
        print(f"{'Drink':<8}{'Small':<45}{' 2.00':<15}{sdrinks:<15}{drinkscosts:>5}")
    if mdrinks > 0:
        print(f"{'Drink':<8}{'Medium':<45}{' 3.00':<15}{mdrinks:<15}{drinkscostm:>5}")
    if ldrinks > 0:
        print(f"{'Drink':<8}{'Large':<45}{' 3.50':<15}{ldrinks:<15}{drinkscostl:>5}")
        
    subtotal.append(drink_total)    
    
    return subtotal
           
            
def wings_cost(wings):
    #-----------------------cost/quant/print for wings-------------------  
    swings = 0
    mwings = 0
    lwings = 0
    wing_total = 0
    subtotal = [0]
    
    for k in range(len(wings)):
        for i in range(len(wings[k])):
            if wings[k][i] == '10pcs':
                swings += 1
                wing_total += 5.00
            elif wings[k][i] == "20pcs":
                mwings += 1
                wing_total += 9.00
            elif wings[k][i] == "40pcs":
                lwings += 1
                wing_total += 17.50
                
    wingscosts = format(swings * 5.00, '.2f')
    wingscostm = format(mwings * 9.00, '.2f')
    wingscostl = format(lwings * 17.50, '.2f')
    
    if swings > 0:
        print(f"{'Wings':<8}{'10pcs':<45}{' 5.00':<15}{swings:<15}{wingscosts:>5}")
    if mwings > 0:
        print(f"{'Wings':<8}{'20pcs':<45}{' 9.00':<15}{mwings:<15}{wingscostm:>5}")
    if lwings > 0:
        print(f"{'Wings':<8}{'40pcs':<45}{'17.50':<15}{lwings:<15}{wingscostl:>5}")
    
    subtotal.append(wing_total)
        
    return subtotal


def total_cost(za, drinks, wings):
    
    listtotal = []
    subtotal = 0
    
    print(f"\nThank you for placing your order. Below is a summary.",f"\n{'-'*89}",
          f"\n\n{'Item':<8}{'Description':<45}{'Unit Price':<15}{'Quantity':<15}{'Amount':<10}")
    
    listtotal.append(pizza_cost(za))
    listtotal.append(drinks_cost(drinks))
    listtotal.append(wings_cost(wings))

    for i in range(len(listtotal)):
        for k in range(len(listtotal[i])):
            subtotal += listtotal[i][k]

    subtotalrounded = format(float(subtotal), '.2f')
    taxed = subtotal * .0625
    taxedrounded = format(taxed, '.2f')
    total = subtotal + taxed
    totalrounded = format(total, '.2f')

    print(f"\n{'Subtotal':>78}{subtotalrounded:>10}\n",
          f"{'Tax(6.25%)':>77}{taxedrounded:>10}\n",
          f"{'Total':>77}{totalrounded:>10}\n"
          f"{'-'*89}\n"
          f"Your final total is ${totalrounded}. Thank you for shopping with us.")
        
        
#----------------amount functions----------------------

def amt_pizzas():
    pizzas_list = []
    index = 1
    output_str = ''
    
    while index != 0:
        
        print(f"Please select your toppings for the pizza:\n",
              f"  1) Pepperoni: $1.00\n", 
              f"  2) Mushroom:  $0.50\n", 
              f"  3) Olive:     $0.50\n", 
              f"  4) Anchovy:   $2.00\n", 
              f"  5) Ham:       $1.50\n",
              f"  0) I am done with toppings.",)
        
        index = int(input('> '))
        
        # building list for cost calculation
        if index == 1:
            pizzas_list.append('Pepperoni')
            print(f"You have selected for Pepperoni your pizza.\n")
        elif index == 2:
            pizzas_list.append('Mushroom')
            print(f"You have selected for Mushroom your pizza.\n")
        elif index == 3:
            pizzas_list.append('Olive')
            print(f"You have selected for Olive your pizza.\n")
        elif index == 4:
            pizzas_list.append('Anchovy')
            print(f"You have selected for Anchovy your pizza.\n")
        elif index == 5:
            pizzas_list.append('Ham')  
            print(f"You have selected for Ham your pizza.\n")
        elif index < 0 or index > 5:
            print(f"Error: Invalid entry. Please try again.\n")
    
    # making output strings
    if len(pizzas_list) == 1:
        print(f"You have slected a pizza with {pizzas_list[0]}.\n")
    elif len(pizzas_list) == 2:
        print(f"You have slected a pizza with {pizzas_list[0]} and {pizzas_list[1]}.\n")
    elif len(pizzas_list) > 2:
        for i in range(len(pizzas_list) - 1):
            output_str = output_str + pizzas_list[i] + ', '
        output_str = output_str + 'and ' + pizzas_list[-1]
        print(f"You have selected a pizza with {output_str}.\n")
    else:
        print("\n")
        
    return(pizzas_list)
    

#-----------------drinks amount-------------------------

def amt_drinks():
    drinks_list = []
    index = 1
    
    while index != 0:
        
        print(f"\nPlease enter the size of your drink:\n", 
              f"  1) Small     $2.00\n", 
              f"  2) Medium    $3.00\n", 
              f"  3) Large     $3.50\n", 
              f"  0) I am all done.",)
        
        index = int(input('> '))
        
        if index == 1:
            print(f"You have selected a small drink.")
            drinks_list.append('small')
        elif index == 2:
            print(f"You have selected a medium drink.")            
            drinks_list.append('medium')
        elif index == 3:
            print(f"You have selected a large drink.")            
            drinks_list.append('large')
        elif index < 0 or index > 3:
            print(f"Error: Invalid entry. Please try again.")
    
    return drinks_list



#------------------------amount wings----------------------

def amt_wings():
    wings_list = []
    index = 1
    
    while index != 0:
        
        print(f"\nPlease enter the size of your wings\n",
              f"  1) 10pcs     $5.00\n",  
              f"  2) 20pcs     $9.00\n", 
              f"  3) 40pcs    $17.50\n", 
              f"  0) I am all done.",)
        
        index = int(input('> '))
        
        if index == 1:
            print(f"You have selected a 10pcs of wings.")            
            wings_list.append('10pcs')
        elif index == 2:
            print(f"You have selected a 20pcs of wings.")            
            wings_list.append('20pcs')
        elif index == 3:
            print(f"You have selected a 40pcs of wings.")            
            wings_list.append('40pcs')
        elif index < 0 or index > 3:
            print(f"Error: Invalid entry. Please try again.")
            
    return wings_list

# -------------------------main-------------------------

def main():
    
    print(f"\nWelcome to Emerson Pizza!\n")
    
    index = 1
    
    multi_pizzas = []
    multi_drinks = []
    multi_wings = []
    
    while index != 0:
        
        # prints each time after a function is called to order more or end
        print(f"Please enter your order:\n", 
          f"  1) Pizzas\n", 
          f"  2) Drinks\n", 
          f"  3) Wings\n", 
          f"  0) I am done ordering!")
        
        # index is then requested
        index = int(input('> '))
        
        
        if index == 1:
            multi_pizzas.append(amt_pizzas())
        elif index == 2:
            multi_drinks.append(amt_drinks())
        elif index == 3:
            multi_wings.append(amt_wings())
        elif index < 0 or index > 3:
            print(f"Error: Invalid entry. Please try again.\n")
            
    # after while loop is done the '0' stuff will be done
    total_cost(multi_pizzas, multi_drinks, multi_wings)
    
main()
