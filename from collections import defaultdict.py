from collections import defaultdict
students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]
groups = defaultdict(list)
for student, group in students:
    groups[group].append(student)
 
print(groups)
print(groups[3])