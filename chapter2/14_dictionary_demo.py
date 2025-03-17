# populate a dictionary (dict)
products = {
    1:"apples" ,
    2:"bananas" ,
    3:"eggs" ,
    4:"melons"
}
print("----------------")
print("Initial products " , products)
print("----------------")
# insert/update a new product
products[15] = "oranges"
print("Products after insert/update " , products)
print("----------------")
# get the product with id = 3
product_to_find = products[15] ## 3 --> key
print("Product in position 3, is" , product_to_find)
print("----------------")
# Delete
# del products[4]
# print(f"Products after deletion {products}")
print("----------------")

# Delete with pop
removed_product = products.pop(3)
print(f"Removed product {removed_product} " , products)
print("----------------")

# Delete with pop , for a non-existing item
removed_product2 = products.pop(25 , "NOT FOUND")
print(f"Removed product {removed_product} " , products)
print("----------------")

key , value = products.popitem()
print(f"Removed key : {key} , Removed value : {value}")
print(products)

print("----------------")
key_to_check = 2

# find key
if key_to_check in products: # search in keys
    print(f"Key {key_to_check} is present in the list of products")
else:
    print(f"Key {key_to_check} is not present in the list of products")

print("----------------")
# get keys from a dictionary
for key in products.keys():
    print(key)
# get values from a dictionary
for value in products.values():
    print(value)
# iterate a dictionary
for key in products.keys():
    print(f"{key} : {products[key]}")

print("----------------")

for key , value in products.items():
    print(f"{key} : {value}")
