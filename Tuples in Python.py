# Tuples look like lists,
Fruit = ('Apples', 4, 'Bananas', 5, 'Oranges', 6)

List_of_fruit = ['Apples', 4, 'Bananas', 5, 'Oranges', 6]

List_of_fruit[0] = 'Strawberries'
print(List_of_fruit)

# Can't modify elements within a tuple
# Slicing tuples
print(Fruit[0:3])

# You can concatenate and recall elements within a tuple

# Tuples have () and Lists have []

# Tuple with one element must have a comma i.e (5 ,) otherwise it will think it is a integer

# finding the length of the tuple
print(len(Fruit))

# creating a tuple
another_tuple = tuple(('Hello', 18, True))
print(type(another_tuple))

# converting a tuple to a list then back to a tuple
Fruit = list(Fruit)
Fruit.append('Pears')
Fruit = tuple(Fruit)
print(Fruit)

# Unpacking tuples
Fruit = ('Apples', 'Bananas', 'Pears', 'Oranges', 'Strawberries')
(one, two, *three) = Fruit
print(one)
print(two)
print(three)

# Incorporate loops within tuples

for i in range(len(Fruit)):
    print(Fruit[i])