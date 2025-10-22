from collections import Counter
cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow)
print(counter_spb)
print(counter_moscow + counter_spb)
counter_moscow.subtract(counter_spb)
print(counter_moscow)