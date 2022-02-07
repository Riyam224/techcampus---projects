# ! HW 01

# my_str = "abcd1234"
# reverse_str = my_str[::-1]
# print('Reverse the string is ', reverse_str)

# ! if  oondition

# ! q1
# num = int(input('please enter the number ! '))

# if num % 2 == 0:
#     print('the number is even')
# else:
#     print('the number is odd ')

# ! q2

# amount = float(input('enter the amonnt of money '))
# discount = 0
# final_amount = 0

# if amount > 0 and amount < 1000:
#     discount = amount*(5/100)
#     final_amount = amount - discount
# elif amount >= 1000 and amount <= 5000:
#     discount = amount*(10/100)
#     final_amount = amount - discount
# elif amount >= 5000:
#     discount = amount*(15/100)
#     final_amount = amount - discount
# else:
#     print('please enter correct number ')
# print('the discount amount ', discount)
# print('the final amount ', final_amount)


# ! q3

# final_res = int(input('enter the student result '))
# if final_res >= 50:
#     print('congrats ... u succed ')
# else:
#     print('Iam sorry .. u faild ')


# ! q4


# pass_grad = ['a', 'b', 'c', 'd']
# failed_grad = 'f'
# grade = input('enter your grade ')

# if grade.upper() in pass_grad or grade.lower():
#     print('pass')

# elif grade.upper() == failed_grad or grade.lower() == failed_grad:
#     print('good luck next year ')
# else:
#     print('please enter correct grade ')


# name = 'koko'

# if name != 'techcamous':
#     if name == 'koko':
#         print('its koko')
#     else:
#         print('not koko ')


# ! for

# # my_list = [1, 2, 3, 4]
# # for item in my_list:
# #     print(item)

# # print(range(5))

# # for i in range(5):
# #     print(i)

# # !
# # for i in range(11):
# #     print('I love python')

# # for i in range(0, 11):
# #     print(i, '* 10 = ', i*10)


# # !
# dollar_list = []
# ryal_list = []

# for item in range(1, 101):
#     dollar_list.append(item)


# converted_rate = float(input('please enter converted rate '))

# while True:
#     if converted_rate > 0 and compile < 10:
#         for item in dollar_list:
#             ryal_val = item * converted_rate
#             ryal_list.append(ryal_val)
#         print('the ryal list is \n', ryal_list)
#         break
#     else:
#         converted_rate = float(
#             input('please enter converted  should be greated than 0 and less than 10 '))
# print('the dollar list is \n ', dollar_list)


# !


# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# sum = 0
# for i in numbers:
#     sum = sum + i
# print('the sum is ', sum)


# !

# num_list = [1, 2, 3]
# alpha_list = ['a', 'b', 'c']

# for num in num_list:
#     for char in alpha_list:
#         print(char,  num)


# ! files

# fo = open('test.txt', 'r')
# str = fo.read()
# print(str)
# fo.close()


# ! prime

for x in range(0, 11):
    for y in range(0, 11):
        print('product', y*x)
