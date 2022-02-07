# ! files

# file_obj = open('foo.txt', 'w')
# file_obj.write('first line\nsecond line\nthird line')
# file_obj.close()


# ! exception

# try:
#     num = input('enter number ')
#     res = num / 3
#     print(res)

#     fo_obj = open('f.txt', 'r')
#     data = fo_obj.read()
#     fo_obj.close()

# except FileNotFoundError:
#     print('file not fount ')
# except TypeError:
#     print('type error ')

# except Exception as f:
#     print(f)


# try:
#     num = int(input('enter your number !'))
#     res = num * 100
#     print(res)

# except Exception as f:
#     print('invalid input! ', f)


# try:
#     num = int(input('enter number '))
#     res = num * num
#     print(res)

#     fo = open('foo.txt', 'r')
#     data = fo.read()
#     print(data)

# except TypeError:
#     print('type error')

# except FileExistsError:
#     print('file not found')

# except Exception as e:
#     print(e)

# else:
#     print('no error ')


# !

# try:
#     test_file = open('foo.txt', 'r')
#     data = test_file.read()
#     print(data)
#     test_file.close()

# except FileNotFoundError:
#     print('sorry the file not found ')

# except Exception as e:
#     print(e)

# else:
#     print(2 * 10)

# finally:
#     print('it worked ')


# ! reg

import re

# pattern = "^[a-zA-Z]*$"


# name = input('enter the name ')
# if re.match(pattern, name):
#     print('match ')
# else:
#     print('not ')


# pattern = "^[0-9]*$"
# name = input('enter the name ')
# if re.match(pattern, name):
#     print('match ')
# else:
#     print('not ')


# pattern = ["java", "python", "c"]
# text = "i love python"

# for item in pattern:
#     if re.search(item, text):
#         print('found')
#     else:
#         print('not found')


# !

# def add(num1, num2):
#     res = num1 + num2
#     return res


# def sub(num1, num2):
#     res = num1 - num2
#     return res


# if __name__ == '__main__':
#     num1 = int(input('enter the number 1'))
#     num2 = int(input('enter the number 2'))
#     res = add(num1, num2)
#     res2 = sub(num1, num2)
#     print(res, res2)


# !
# class Car:
#     def __init__(self, name, color, model, energy):
#         self.name = name
#         self.color = color
#         self.model = model
#         self.energy = energy

#     def goBack(self):
#         print('the car is going back')

#     def goForward(self):
#         print('the car is going forward')


# if __name__ == '__main__':
#     red_car = Car('toyota', 'red', 2019, 'gaz')
#     print(red_car.name)
#     print(red_car.model)
#     print(red_car.goBack())


# !
# import datetime


# class Employee:
#     def __init__(self, name, surname, yearOfBirth, job_title, salary, email):
#         self.name = name
#         self.surname = surname
#         self.yearOfBirth = yearOfBirth
#         self.job_title = job_title
#         self.salary = salary
#         self.email = email

#     def age(self):
#         age = datetime.datetime.now() - (self.yearOfBirth)
#         return age


# koko = Employee('koko', 'dede', 2000, 'eng', 1000, 'koko.gmail.com')

# print(koko.salary)
# print(koko.age())


# !

class Student:
    def __init__(self, fname, lname, std_id):
        self.fname = fname
        self.lname = lname
        self.std_id = std_id
        self.email = fname + '.'+lname + '@udemy.com'

    def getFullName(self):
        return self.fname + ' ' + self.lname

    def getEmail(self):
        return self.email


if __name__ == '__main__':

    std1 = Student('koko', 'dede', 1000)

    print(std1.getEmail())
    print(std1.getFullName())
