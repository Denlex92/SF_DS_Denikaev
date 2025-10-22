from collections import Counter


center_counter = Counter({'Bread': 95, 'Beer': 81, 'Chips': 61, 'Cola': 60, 'Meat': 46, 'Milk': 43, 'Cheese': 39, 'Chocolate': 35, 'Ketchup': 33, 'Soap': 28, 'Yoghurt': 27})
south_counter = Counter({'Bread': 73, 'Meat': 60, 'Beer': 60, 'Cola': 55, 'Milk': 46, 'Chocolate': 39, 'Yoghurt': 33, 'Cheese': 30, 'Ketchup': 30, 'Chips': 28, 'Soap': 24})
north_counter = Counter({'Cola': 121, 'Beer': 116, 'Bread': 72, 'Chips': 39, 'Chocolate': 33, 'Yoghurt': 30, 'Soap': 28, 'Milk': 22, 'Meat': 15, 'Ketchup': 14, 'Cheese': 10})

print("Checking for center")
for item in center_counter:
    center_count = center_counter[item]
    other_count = south_counter[item] + north_counter[item]
    if center_count > other_count:
        print(f"{item}: {center_count} > {other_count}({south_counter[item]} + {north_counter[item]})")
        found = True

print("Cheking for south")
for item in south_counter:
    south_count = south_counter[item]
    other_count = center_counter[item] + north_counter[item]
    if south_count > other_count:
        print(f"{item}: {south_count} > {other_count} ({center_counter[item]} + {north_counter[item]})")
        found = True
        
print("Cheking for north")
for item in north_counter:
    north_count = north_counter[item]
    other_count = center_counter[item] + south_counter[item]
    if north_count > other_count:
        print(f"{item}: {north_count} > {other_count} ({center_counter[item]} + {south_counter[item]})")
        found = True
        
        
if not found:
    print("No such goods")
        


#Counter({'Bread': 95, 'Beer': 81, 'Chips': 61, 'Cola': 60, 'Meat': 46, 'Milk': 43, 'Cheese': 39, 'Chocolate': 35, 'Ketchup': 33, 'Soap': 28, 'Yoghurt': 27})
#Counter({'Bread': 73, 'Meat': 60, 'Beer': 60, 'Cola': 55, 'Milk': 46, 'Chocolate': 39, 'Yoghurt': 33, 'Cheese': 30, 'Ketchup': 30, 'Chips': 28, 'Soap': 24})
#Counter({'Cola': 121, 'Beer': 116, 'Bread': 72, 'Chips': 39, 'Chocolate': 33, 'Yoghurt': 30, 'Soap': 28, 'Milk': 22, 'Meat': 15, 'Ketchup': 14, 'Cheese': 10})