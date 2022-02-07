# print('hello world !')
# ! variables
# x = 10
# x = 30
# print(x)


# name = input('please enter the year')
# print(type(name))

# x = int(input('enter the year'))

# print(type(x))
#  ! date time **


# import datetime

# today = datetime.datetime.today()
# # print(today)

# now = datetime.datetime.now()
# # print(now)

# year = int(input('enter the year  '))
# month = int(input('enter the month  '))
# day = int(input('enter the day  '))


# DOB = datetime.datetime(year, month, day)
# # print(DOB)


# age = now - DOB
# ageInDetails = age.days / 365

# print('the age is ',  age)
# print('the age datails in days ', ageInDetails)


# ! string

# my_str = "I love programming with python! "
# print(my_str[0:10])
# print(my_str[0:-1])
# print(my_str[-1:0])

# my_str = 'Hello there '
# print(my_str[0:3])
# print(my_str[3:])

# print(my_str.lower())
# print(my_str.upper())
# print(my_str.capitalize())

# message = 'thank you'
# print(message[0:5])


# s = 'i love programming\n .. its my life in here ...'
# print(s)


# ! list

# myList = ['koko', 'roro', 'nini']
# grade = ['a', 'b', 'c', 'd']

# numbers = [2, 5, 7]


# print(myList[0])

# ! tuple

# t = (1, 2, 'koko')
# # print(type(t))   tuple

# print(t[2])


# my_list = ['techcampus', 'python', 2019, 20]
# my_tuple = ('techcampus', 'python', 2019, 20)


# # print(my_tuple[1:3])
# # print(my_list[1:3])
# # my_list[1] = 'hello '
# # print(my_list)


# #!  my_tuple[1] = 'hello' !   immutable
# # print(my_tuple)


# ! dictionary


# my_dict = {
#     'name': 'koko',
#     'age': 22,
#     'place': 'los angelos '
# }

# # print(type(my_dict))
# # print(my_dict['name'])

# # print(my_dict['age'])


# my_dict['name'] = 'roro'
# print(my_dict)


# my_dict = {
#     'name': 'koko',
#     'class': 'A',
#     'Std_id': 1000,
#     'Age': 20
# }

# print(my_dict)

# Name = input('enter the name ')
# Class = input('enter the class ')
# Std_id = int(input('enter the id '))
# Age = int(input('enter the age '))

# my_dict = {
#     'Name': Name,
#     'Class': Class,
#     'Std_id': Std_id,
#     'Age': Age

# }


# print(my_dict)


# ! ex
my_str = 'abcd1234'
reverse_str = my_str[::-1]
print(reverse_str)
