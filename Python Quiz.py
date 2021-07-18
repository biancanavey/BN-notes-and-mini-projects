# Q1 creating two variables X=? Y= ?
# Find the sum, division, subtraction, multiplication
x = 10
y = 15

print(x + y)
print(x / y)
print(x - y)
print(x * y)

# Q2- Lists - Create a List with all even numbers from 0 - 100.
# print the first 10 elements in the less and find the length of the list.
# Append any value to this list

my_list = list(range(0, 101, 10))
print(my_list)

print(my_list[0:10])

print(len(my_list))

my_list.append(True)
print(my_list)

# Q3 Assign variable to any number that you want
# Then use an if statement to find out whether the integer is divisible by 5.
# print if it is or isn't

number = 69445
if number % 5 == 0:
    print('a is divisible by 5')
else:
    print('a is not divisible by 5')

# Q4 using a for loop, get python to print the numbers 0 to 5
for i in range(6):
    print(i)

# Q5 Draw a pentagon in turtle
# import turtle
#
# for i in range(5):
#     turtle.right(72)
#     turtle.forward(100)


# turtle.done()

# Q6 create a function that tests if 3 numbers (a,b,c) are a pythagorean triple,

def pythagorean_triple(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return print(' These three value are a pythagorean triple')
    else:
        return print('These three value are not a pythagorean triple')


print(pythagorean_triple(3,4,5))
print(pythagorean_triple(3,8,5))


# q7 where is the error
n = 5
while n > 0:
    n = n + 1
    print(n)

# Q8 create two lists( of size 5 or any size you want0 and plot these against each other using matplotlib

import matplotlib.pyplot as plt #import the relevant modules

list1 = [1, 2, 3, 4, 5, 6]
list2 = [3, 4, 5 , 65, 5]
plt.plot(list1, list2, c='Green', linewidth=2, label='line 2')
plt.xlabel('X- axis')
plt.ylabel('Y- axis')
plt.title('Two Lines')
plt.legend()
plt.show()