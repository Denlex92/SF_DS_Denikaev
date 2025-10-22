from hidden import center, south, north
from collections import Counter



center = [item for sublist in center for item in sublist]
south = [item for sublist in south for item in sublist]
north = [item for sublist in north for item in sublist]

center_count = len(center)
south_count = len(south)
north_count = len(north)

max_count = max(center_count, south_count, north_count)

if center_count == max_count:
    print('center')
elif south_count == max_count:
    print('south')
else:
    print('north')
    
    
center_counter = Counter(center)
south_counter = Counter(south)
north_counter = Counter(north)
rarest_item_north = north_counter.most_common()[-1]
rarest_item_center = center_counter.most_common()[-1]
print(rarest_item_north)
print(rarest_item_center)
rarest_count_north = rarest_item_north[1]
rarest_count_center = rarest_item_center[1]
print(rarest_count_north)
print(rarest_count_center)
print(center_counter)
print(south_counter)
print(north_counter)


# Ваш код здесь

print ("1")

#Counter({'Bread': 95, 'Beer': 81, 'Chips': 61, 'Cola': 60, 'Meat': 46, 'Milk': 43, 'Cheese': 39, 'Chocolate': 35, 'Ketchup': 33, 'Soap': 28, 'Yoghurt': 27})
#Counter({'Bread': 73, 'Meat': 60, 'Beer': 60, 'Cola': 55, 'Milk': 46, 'Chocolate': 39, 'Yoghurt': 33, 'Cheese': 30, 'Ketchup': 30, 'Chips': 28, 'Soap': 24})
#Counter({'Cola': 121, 'Beer': 116, 'Bread': 72, 'Chips': 39, 'Chocolate': 33, 'Yoghurt': 30, 'Soap': 28, 'Milk': 22, 'Meat': 15, 'Ketchup': 14, 'Cheese': 10})