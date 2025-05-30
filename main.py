"""Module for using json Liabries"""
import json
import random
from pathlib import Path

#json is a light weight file that stores data in form of list and dictionary

"""
our database that is json file is outside our code base, 
in that case we need to go to the path of the json file each time we want to intreact with the json file.
so, we are creating a dummy data variable o store or fetch that data automatically when the code starts.
"""
"""json.load,It reads JSON data from a file object (like a .json file) 
and converts it into a Python data structure (like a dictionary or list)"""


class Bank:
    """Class representing a bank"""

    data = []
    database = 'Database.json'

    try:
        if Path(database).exists():
            with open(database, encoding="utf-8") as fs:
                read = fs.read()
                data = json.loads(read)
        else:
            print("No Such File Exists")
    except Exception as err:
        print(f"error : {err}")

    @staticmethod
    def update():
        """create to link information of the user to the json file"""
        with open(Bank.database, 'w', encoding = "utf-8") as fs:
            fs.write(json.dumps(Bank.data))


    def createaccount(self):
        """Function used for creating accounts"""
        info = {
            "name": input("Please, Tell me your name:- "),
            "age" : int(input("Please, Tell me your age:- ")),
            "Email": input("Please, Tell me your email:- "),
            "Address":input("Please, Tell me Your Address:- "),
            "Transaction_Pin": int(input("Please Setup 4 digit TPin:- ")),
            "Account_number": 8894,
            "Balance": 0
        }
        if info["age"] < 18:
            print("Your age must be above 18.")
            print("Try again")
        if len(str(info["Transaction_Pin"])) != 4:
            print("The length of the Tpin must be 4")
            print("Try again")
        else:
            print("Account Created Successfully, Please Note Down your Account Number")
            for i, values in info.items():
                print(f"Your Details are {i}: {values}")
            Bank.data.append(info) #appending the info into the data variable(dummy data)
            Bank.update()

user = Bank()

print("Welcome to Sunrise Bank Limited\n")
print("Press 1 to Create an Account With us")
print("Press 2 to Deposite Money")
print("Press 3 to Withdraw Money")
print("Press 4 to check your Details")
print("press 5 to update Your Detail")
print("Press 6 to delete Your Account\n")

check = int(input("What would you like to do, sir ? :- "))

if check == 1:
    user.createaccount()