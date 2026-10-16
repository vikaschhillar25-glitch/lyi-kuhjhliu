items =["pencil","eraser","notbook","sharpener","glue"]
stock_counts=[12,0,8,5,3]

inventory = {item: count for item,count in zip (items ,stock_counts)}
print("Full Invenntory:",inventory)

in_stock_item =[item for item in items if inventory [item]>0]
print("in stock item:", in_stock_item)

chosen_item = input("which item you want to bay!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!?")

if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item, "is out stock!")
    exit()

price =[10,5,40,15,20]
markup = int(input("enter amount:"))

markup_up_price = list(map(lambda p: p +markup,price))
print("mack up price:",markup_up_price)

item_index = items.index(chosen_item)
chosen_price = markup_up_price[item_index]
print("price of",chosen_item,"after markup",chosen_price)

inventory[chosen_item] = inventory[chosen_item] -1

print(chosen_item,"purchased!",inventory[chosen_item])

print("")
print("======================= school  ========================")
print("Item bought:",chosen_item)
print("price pade",chosen_price)
print("inventory",inventory)
print("==================")

