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

    def updatedetails(self):
        """This function helps to update details of the users"""
        accnum = input("Please, tell me your account number:- ")
        tpin = int(input("Please Tell me yout Transaction pin:- "))
        deepcopy = [i for i in Bank.data if i['Account_number']== accnum and i['Transaction_Pin'] == tpin]
        if deepcopy == []:
            print("No Such Data Found")
        else:
            for i in deepcopy[0]:
                print(f"{i}: {deepcopy[0][i]}")
        #this will update data on by one
        # update = input("What do you want to update :- ")
        # print(update)
        # if update == 'name' or update == 'Name':
        #     name_update = input("What do you want as your new name:- ")
        #     deepcopy[0]['name'] = name_update
        #     Bank.__update()
        #     print("Updated successfully")
        # elif update == 'Address' or update == 'address':
        #     address_update = input("What do you want as your new Address:- ")
        #     deepcopy[0]['Address'] = address_update
        #     Bank.__update()
        #     print("Updated successfully")
        # elif update == 'Email' or update == 'email':
        #     email_update = input("What do you want as your new Email:- ")
        #     deepcopy[0]['Email'] = email_update
        #     Bank.__update()
        #     print("Updated successfully")
        # elif update == 'Transaction_Pin' or update == 'Tpin':
        #     tpin_update = int(input("What do you want as your new Tpin:- "))
        #     deepcopy[0]['Transaction_Pin'] = tpin_update
        #     Bank.__update()
        #     print("Updated successfully")
        # else:
        #     print("Please Follow the Naming convenction")

        #For updating data all by once
        print("Please update you inforamtion as you need")
        newdata = {
            "name" : input("please enter the new name or press enter to skip:- "),
            "Email": input("Please Enter the new Email or press enter to skip:-"),
            "Address" : input("Please enter the new address or press enter to skip:- "),
            "Transaction_Pin": int(input("please enter the new Tpin or press enter to skip:- "))
        }
        if newdata['name'] == "":
            newdata['name'] = deepcopy[0]['name']
        if newdata['Email'] == "":
            newdata['Email'] = deepcopy[0]['Email']
        if newdata['Address'] == "":
            newdata['Address'] = deepcopy[0]['Address']
        if newdata['Transaction_Pin'] == "":
            newdata['Transaction_Pin'] = deepcopy[0]['Transaction_Pin']
        newdata['age'] = deepcopy[0]['age']
        newdata['Balance'] = deepcopy[0]['Balance']
        newdata['Account_number'] = deepcopy[0]['Account_number']
        #we are doing this because, we are passing  newdata as dummy data during update

        if type(newdata['Transaction_Pin']) == str:
            newdata['Transaction_Pin'] = int(newdata['Transaction_Pin'])

        #This goes through each key and value in the newdata dictionary.
        #First round: key is 'name', value is 'roheet'
        for key, value in newdata.items():
            if value == deepcopy[0][key]:
                continue
            else:
                deepcopy[0][key] = value
            Bank.__update()
            print("Details Update successfully")
    
    def acc_delete(self):
        """This Function will delete the user data"""
        accnum = input("Please, tell me your account number:- ")
        tpin = int(input("Please Tell me yout Transaction pin:- "))
        deepcopy = [i for i in Bank.data if i['Account_number']== accnum and i['Transaction_Pin'] == tpin]
        if deepcopy == []:
            print("No Such Data Found")
        else:
            conform = input("press 'Y' to delete or 'N' for ternimation of the process :-")
            if conform == 'n' or conform == 'N':
                print("Process Terminated successfully")
            else:
                index_of_data = Bank.data.index(deepcopy[0])
                Bank.data.pop(index_of_data)
                Bank.__update()
                print("data deleted successfully")

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

if check == 5:
    user.updatedetails()

if check == 6:
    user.acc_delete()
