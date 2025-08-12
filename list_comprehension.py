#Python List Comprehension -> a concise way to create list in python

# Formula = [Expression for value in iterable]


# doubles = []

# for x in range(1,11):
#     doubles.append(x * 2)

# print(doubles)


# doubles = [x * 2 for x in range(1, 11)]
# print(doubles)


# triples = [x * 3 for x in range(1, 11)]
# print(triples)


# square = [x**2 for x in range(1, 11)]
# print(square)


# fruits = ["apple", "orange", "banana","coconut"]
# fruits =[fruit.capitalize() for fruit in fruits]
# fruits =[fruit[0] for fruit in fruits]
# print(fruits)


# numbers = [1, -2, 3, -4, 5, -6, -7, 8]
# positive_num = [num for num in numbers if num > 0]
# negative_num = [num for num in numbers if num < 0]
# even_num = [num for num in numbers if num % 2== 0]
# odd_num = [num for num in numbers if num % 2== 1]

# print(odd_num)


grades = [85, 42, 79, 90, 56, 61, 30]
passing_grade =  [grade for grade in grades if grade >= 60]

print(passing_grade)
