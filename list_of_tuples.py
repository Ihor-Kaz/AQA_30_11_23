"""
Homework.

Description:
    Given list of tuples (people list ->
    name, surname, age, profession, City location)
    1- Add your new record with similar random data
    to the beginning of the given list
    2 - In modified list swap elements with indexes 1 and 5
    (1<->5) and print result
    3 - check condition that all people in modified list
    with records indexes 6, 10, 13
    have age >=30 and print result
"""

ALIGN1 = 5
FIRST_IND, SECOND_IND = 1, 5
N1, N2, N3 = 6, 10, 13
AGE = 30
AGE_POS = 2

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix'),
]
random_data = [('test_name', 'test_surname', 99, 'test_prof', 'test_city')]

# Point 1. Add <random_tuple> to the beginning of the given list
new_list = random_data + people_records

# Point 2. In modified list swap elements with indexes 1 and 5
#       (1<->5) and print result

# 2.1 -> cut elements from the modified list
second_cut_item = new_list.pop(SECOND_IND)
first_cut_item = new_list.pop(FIRST_IND)

# 2.2 -> insert elements to the chosen position in modified list
new_list.insert(FIRST_IND, second_cut_item)
new_list.insert(SECOND_IND, first_cut_item)

# 2.3 -> print result
print(f'|{"index": ^{ALIGN1}}|list element')
for el in new_list:
    print(f'|{new_list.index(el): ^{ALIGN1}}|{el}')

# Point 3. Check condition that all people in modified list
#       with records indexes 6, 10, 13 have age >=30 and print result
print(f'list element: {new_list[N1]} have age >=30 is',
      new_list[N1][AGE_POS] >= AGE,
      )
print(f'list element: {new_list[N2]} have age >=30 is',
      new_list[N2][AGE_POS] >= AGE,
      )
print(f'list element: {new_list[N3]} have age >=30 is',
      new_list[N3][AGE_POS] >= AGE,
      )
