from collections import Counter


center_counter = Counter({'Bread': 95, 'Beer': 81, 'Chips': 61, 'Cola': 60, 'Meat': 46, 'Milk': 43, 'Cheese': 39, 'Chocolate': 35, 'Ketchup': 33, 'Soap': 28, 'Yoghurt': 27})
south_counter = Counter({'Bread': 73, 'Meat': 60, 'Beer': 60, 'Cola': 55, 'Milk': 46, 'Chocolate': 39, 'Yoghurt': 33, 'Cheese': 30, 'Ketchup': 30, 'Chips': 28, 'Soap': 24})
north_counter = Counter({'Cola': 121, 'Beer': 116, 'Bread': 72, 'Chips': 39, 'Chocolate': 33, 'Yoghurt': 30, 'Soap': 28, 'Milk': 22, 'Meat': 15, 'Ketchup': 14, 'Cheese': 10})

all_counts = center_counter + south_counter + north_counter

test_1 = all_counts.most_common(1)

print(all_counts)
print(test_1)