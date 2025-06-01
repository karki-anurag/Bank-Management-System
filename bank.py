# bank.py
import json
import random
import string
from pathlib import Path

class Bank:
    database = 'Database.json'
    data = []

    @classmethod
    def load_data(cls):
        try:
            if Path(cls.database).exists():
                with open(cls.database, encoding="utf-8") as f:
                    cls.data = json.load(f)
            else:
                cls.data = []
        except Exception:
            cls.data = []

    @classmethod
    def save_data(cls):
        with open(cls.database, 'w', encoding="utf-8") as f:
            json.dump(cls.data, f, indent=4)

    @staticmethod
    def generate_account_number():
        alpha = random.choices(string.ascii_uppercase, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id_ = alpha + num + spchar
        random.shuffle(id_)
        return "".join(id_)

    @classmethod
    def create_account(cls, name, age, email, address, tpin):
        if age < 18:
            return False, "Age must be 18+."
        if len(str(tpin)) != 4:
            return False, "TPin must be 4 digits."
        acc_number = cls.generate_account_number()
        user = {
            "name": name,
            "age": age,
            "Email": email,
            "Address": address,
            "Transaction_Pin": tpin,
            "Account_number": acc_number,
            "Balance": 0
        }
        cls.data.append(user)
        cls.save_data()
        return True, acc_number

    @classmethod
    def find_user(cls, acc_num, tpin):
        for user in cls.data:
            if user['Account_number'] == acc_num and user['Transaction_Pin'] == tpin:
                return user
        return None

    @classmethod
    def deposit_money(cls, acc_num, tpin, amount):
        user = cls.find_user(acc_num, tpin)
        if not user:
            return False, "No such account."
        if not (0 < amount <= 10000):
            return False, "Amount must be between 1 and 10000."
        user['Balance'] += amount
        cls.save_data()
        return True, f"Deposited {amount}. New balance: {user['Balance']}"

    @classmethod
    def withdraw_money(cls, acc_num, tpin, amount):
        user = cls.find_user(acc_num, tpin)
        if not user:
            return False, "No such account."
        if not (0 < amount <= 10000):
            return False, "Amount must be between 1 and 10000."
        if user['Balance'] < amount:
            return False, "Insufficient balance."
        user['Balance'] -= amount
        cls.save_data()
        return True, f"Withdrawn {amount}. New balance: {user['Balance']}"

    @classmethod
    def update_details(cls, acc_num, tpin, **updates):
        user = cls.find_user(acc_num, tpin)
        if not user:
            return False, "No such account."
        for key, value in updates.items():
            if value:
                if key == 'Transaction_Pin' and len(str(value)) != 4:
                    return False, "TPin must be 4 digits."
                user[key] = value
        cls.save_data()
        return True, "Details updated."

    @classmethod
    def get_details(cls, acc_num, tpin):
        user = cls.find_user(acc_num, tpin)
        if not user:
            return None
        return user

    @classmethod
    def delete_account(cls, acc_num, tpin):
        user = cls.find_user(acc_num, tpin)
        if not user:
            return False, "No such account."
        cls.data.remove(user)
        cls.save_data()
        return True, "Account deleted."
