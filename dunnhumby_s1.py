# Section 1: general Python



# 1. Given the list of basket values, do the following:  
# a. Print out whether each basket is small (basket value < £5), medium (£5 ≤ basket value < £10) or large (basket value ≥ £10); 
# b. Sum and print the value of the medium value baskets. 
# basket_values = [3.43,9.73,7.56,9.52,15.23,2.25,6.44,7.38]

basket_values = [3.43,9.73,7.56,9.52,15.23,2.25,6.44,7.38]
basket_size = []
medium_basket = []
medium_sum = 0

for x in basket_values:
    if x < 5:
        basket_size.append('small')
    elif x >= 5 and x < 10:
        basket_size.append('medium')
        medium_basket.append(x)
        medium_sum += x
    else:
        basket_size.append('large')
    

print('1.a: the size of each basket is: ', basket_size)
print(f'1.b: the sum of the medium size basket: {medium_basket} is: {medium_sum}')





# 2.	You are given the following nested dictionaries, which represent items in a basket.  Do the following:  
# a.	Return the product name for item 7527. 
# b.	Return the total value of this basket. 
# c.	Add another entry for a product that costs £4.95, has ID 7524 and name ‘poppy seeds’. 
# basket = {'2624': {'price': 0.5, 'prod_name': 'salt'},
# '2894': {'price': 3.25, 'prod_name': 'yeast'},
# '7527': {'price': 2.5, 'prod_name': 'flour'}}

basket = {'2624': {'price': 0.5, 'prod_name': 'salt'},
'2894': {'price': 3.25, 'prod_name': 'yeast'},
'7527': {'price': 2.5, 'prod_name': 'flour'}}


def product_name(product, item_id):
    return product[item_id]['prod_name']

def total_value(product):
    values = 0
    for x in product:
        values += product[x]['price']
    return values

def add_item(product, product_cost, product_id, product_name):
    new_product = {}
    new_product = product
    new_product[product_id] = {'price': product_cost, 'prod_name': product_name}
    return new_product
    
product_name(basket, '7527')
total_value(basket)
print(add_item(basket, 4.95, '7524', 'poppy seeds'))




# 3.	Below is the source code for a function called ‘get_sql_string’. 
# 1   def get_sql_string(stores):
# 2      store_names = [x.split(', ')[0] for x in stores]
# 3      store_names = [x.replace(' ', '_') for x in store_names]
# 4      store_regions = [x.split(',')[1] for x in stores]
# 5      locations = store_names + store_regions
# 6      columns = ['sales_' + x.lower() for x in locations]
# 7      return ', '.join(columns)
 
# a.	There is a bug in line 4. What should the line be? 
# b.	Assuming this bug was fixed, what would be returned if the following command was executed: 
# my_stores = ['Fulham Palace Rd, Hammersmith', 'Crown St, Reading', 'Leavesden Green, Watford'] 
# get_sql_string(my_stores) 

def get_sql_string(stores):
    store_names = [x.split(', ')[0] for x in stores]
    store_names = [x.replace(' ', '_') for x in store_names]
    store_regions = [x.split(', ')[1] for x in stores]
    locations = store_names + store_regions
    columns = ['sales_' + x.lower() for x in locations]
    return ', '.join(columns)

my_stores = ['Fulham Palace Rd, Hammersmith', 'Crown St, Reading', 'Leavesden Green, Watford'] 
get_sql_string(my_stores)

# 4.	Write a function that: 
# a.	accepts a list of strings as input. 
# b.	returns an alphabetically ordered list of unique strings. 
# c.	prints the string(s) with maximum length in the console. 

def alpha_ordered(inputList):
    max_len = 0
    for x in inputList:
        if len(x) > max_len:
            max_len = x
            
    max_strs = []
    for x in inputList:
        if len(x) = max_len:
            max_strs.append(x)
            
    print(max_strs)
    return sorted(inputList)
    