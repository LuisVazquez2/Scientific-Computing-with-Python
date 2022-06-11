import difflib
import os
from unicodedata import name


class Category:
    # constructor
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.money = 0
    # special methods

    def __str__(self):
        title = self.name.center(30, "*")
        content = ""
        for current in self.ledger:
            description = f"{current['description']:<23}"
            amount = f"{current['amount']:7.2f}"
            line = f"{description[:23]}{amount[:7]}"
            content += line + "\n"
        total = f"Total: {self.money:.2f}"
        return f"{title}\n{content}{total}"
    # methods of class

    def check_funds(self, amount):
        return self.money >= amount

    def deposit(self, amount, descrition=""):
        self.ledger.append({"amount": amount, "description": descrition})
        self.money += amount

    def withdraw(self, amount, description=""):
        flag = self.check_funds(amount)
        if flag:
            self.ledger.append({"amount": -amount, "description": description})
            self.money -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.money

    def transfer(self, amount, category):
        flag = self.check_funds(amount)
        if flag:
            category.deposit(amount, f"Transfer from {self.name}")
            self.withdraw(amount, f"Transfer to {category.name}")
            return True
        else:
            return False


def create_spend_chart(categories):
    title = "Percentage spent by category"
    chart = ""
    names = "    "
    percent = []
    s_category = []
    t_sum = 0
    for category in categories:
        sum = 0
        for current in category.ledger:
            if current["amount"] < 0:
                sum += abs(current["amount"])
        s_category.append(sum)
        t_sum += sum
    for current in s_category:
        try:
            temp = int(current / t_sum*100)
        except ZeroDivisionError:
            temp = 0
        temp -= 0 if temp % 10 == 0 else temp%10
        percent.append(temp)
    for i in range(100, -1, -10):
        line = f"{i:>3}| "
        for j in range(len(percent)):
            if percent[j] >= i:
                line += "o  "
            else:
                line += "   "
        chart  += line + "\n"
    names += "-" * (len(categories)*3 + 1)
    names += "\n"
    #add names in vertical
    """for x in categories:
        aux = f"{x.name:^30}"
        print(aux)"""
    # aux=1
    # while True:
    #     aux2=False
    #     aux3="     "
    #     for i in range(len(categories)):
    #         if len(categories[i].name) >= aux:
    #             aux2=True
    #             aux3 += f"{categories[i].name[aux-1]}  "
    #         else:
    #             aux3 += "   "
    #     if aux2==False:
    #         break
    #     else:
    #         names += f"{aux3}\n"
    #         aux += 1
    maxi = max(len(x.name) for x in categories)
    flag = False
    for i in range(maxi):
        temp = "     "
        for x in categories:
            if len(x.name) > i:
                temp += f"{x.name[i]}  "
            else:
                temp += "   "
        names += f"{temp}" if i == maxi-1 else f"{temp}\n"
    return f"{title}\n{chart}{names}"

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])
expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
# diferencia = difflib.Differ()
# x = diferencia.compare(actual, expected)
# print("".join(x))
print(actual)
print(expected)