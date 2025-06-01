"""Module for using json Liabries"""
import json
import random
from pathlib import Path
import string


#json is a light weight file that stores data in form of list and dictionary
#our database that is json file is outside our code base,
# in that case we need to go to the path of the json file each time we want to intreact with the json file.
# so, we are creating a dummy data variable o store or fetch that data automatically when the code starts.

#json.load,It reads JSON data from a file object (like a .json file)
# and converts it into a Python data structure (like a dictionary or list)


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
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except PermissionError:
        print("Permission denied while reading the file.")
    except OSError as e:
        print(f"OS error: {e}")

    @classmethod
    def __update(cls):
        """create to link information of the user to the json file"""
        with open(cls.database, 'w', encoding = "utf-8") as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        """create a account generation function to create random account number"""
        alpha = random.choices(string.ascii_letters, k = 3)
        num = random.choices(string.digits, k = 3)
        spchar = random.choices("!@#$%^&*", k =1)
        id_ = alpha + num + spchar
        random.shuffle(id_)
        return "".join(id_)



    def createaccount(self):
        """Function used for creating accounts"""
        info = {
            "name": input("Please, Tell me your name:- "),
            "age" : int(input("Please, Tell me your age:- ")),
            "Email": input("Please, Tell me your email:- "),
            "Address":input("Please, Tell me Your Address:- "),
            "Transaction_Pin": int(input("Please Setup 4 digit TPin:- ")),
            "Account_number": Bank.__accountgenerate(),
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
                print(f"{i}: {values}")
            Bank.data.append(info) #appending the info into the data variable(dummy data)
            Bank.__update()
        
    def depositemoney(self):
        """This function helps the user to deposite money."""
        accnumber = input("Please, Tell me your account number:- ")
        tpin = int(input("please, Tell me your Transaction Pin :- "))
        deepcopy = [i for i in Bank.data if i['Account_number'] == accnumber and i['Transaction_Pin'] == tpin ]
        if deepcopy == []:
            print("no such data found")
        else:
            amount = int(input("How much you want to Deposite:- "))
            if amount >10000 and amount < 0:
                print("Please enter valid amount within 10000 range")
            else:
                deepcopy[0]['Balance'] += amount
                Bank.__update()
                print(f"{amount} Amount Deposited successfully")
    def withdrarmoney(self):
        """This function helps to withdraw money."""
        accnum = input("Please, tell me your account number:- ")
        tpin = int(input("Please Tell me yout Transaction pin:- "))

        deepcopy = [i for i in Bank.data if i['Account_number']== accnum and i['Transaction_Pin'] == tpin]

        if deepcopy == []:
            print("No such data found")
        else:
            print(f"Your Balance is :- {deepcopy[0]['Balance']} ")
            withdraw = int(input("How much you want to withdraw:-"))
            if withdraw > 10000 and withdraw < 0:
                print("please enter a valid amount between 0 to 10000")
            else:
                deepcopy[0]['Balance'] -= withdraw
                Bank.__update()
                print(f"Amount {withdraw} Withdrawed Successfully")
    def details(self):
        """This function will help the user to see their details"""
        accnum = input("Please, tell me your account number:- ")
        tpin = int(input("Please Tell me yout Transaction pin:- "))

        deepcopy = [i for i in Bank.data if i['Account_number']== accnum and i['Transaction_Pin'] == tpin]
        if deepcopy == []:
            print("No Such Data Found")
            
        else:
            for i in deepcopy[0]:
                print(f"{i}: {deepcopy[0][i]}")
            



user = Bank()

print("Welcome to Sunrise Bank Limited\n")
print("Press 1 to Create an Account With us")
print("Press 2 to Deposite Money")
print("Press 3 to Withdraw Money")
print("Press 4 to check your Details")
print("press 5 to update Your Detail")
print("Press 6 to delete Your Account\n")

check = int(input("What would you like to do, sir/mam ? :- "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositemoney()

if check == 3:
    user.withdrarmoney()

if check == 4:
    user.details()