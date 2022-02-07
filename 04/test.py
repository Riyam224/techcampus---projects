# !


# class Customers:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance

#     def withdraw(self, amount):
#         self.balance -= amount
#         return self.balance

#     def getBalance(self):
#         return self.balance


# if __name__ == '__main__':
#     customer1 = Customers('koko', 1000000)

#     while True:
#         option = int(input('please enter ur choice \n 1-press #1 for deposit \n 2-press #2 for withdraw  \n 3-press #3 for checking the balance \n 4-press #4 for exit the application ....'))

#         # !
#         if option == 1:
#             deposit_amount = float(input('enter the deposit amount '))
#             current_balance = customer1.deposit(deposit_amount)
#             print('the current balance is ', current_balance)

#         elif option == 2:
#             withdraw_amount = float(input('enter the withdraw amount ...'))
#             current_balance = customer1.getBalance()
#             if withdraw_amount >= 0:
#                 if current_balance >= withdraw_amount:
#                     new_balance = customer1.withdraw(withdraw_amount)
#                     print('the current balance after withdraw os ', new_balance)
#                 else:
#                     print(
#                         'the current balance should be less or equal the withdraw amount ...')

#         elif option == 3:
#             current_balance = customer1.getBalance()
#             print('the current balance is ', current_balance)
#         else:
#             print('please enter correct choice ')


# ! Graphical user interface  GUI


from tkinter import *


top = Tk()
top.title('Calc')
top.minsize(200, 200)


num1 = Label(text="First number ")
num1.pack()

num1Box = Entry()
num1Box.pack()


num2 = Label(text="Second number ")
num2.pack()

num2Box = Entry()
num2Box.pack()


def addNumbers():
    number1 = float(num1Box.get())
    number2 = float(num2Box.get())
    res = number1 + number2
    resLabel = Label(text="the result is "+str(res))
    resLabel.pack()


but = Button(text="add", command=addNumbers)
but.pack()


top.mainloop()
