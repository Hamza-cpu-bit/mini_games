import json
from datetime import datetime
import os

DATA_FILE = "account_data.json"

def load_accounts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_accounts(accounts):
    with open(DATA_FILE, 'w') as f:
        json.dump(accounts, f, indent=4)

def calculate_days_until_birthday(dob):
    today = datetime.today().date()
    next_birthday = dob.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    return (next_birthday - today).days

def calculate_age(dob):
    today = datetime.today().date()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age

def main():
    accounts = load_accounts()
    name = input("Enter your name: ").strip()

    if name in accounts:
        dob_str = accounts[name]
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        age = calculate_age(dob)
        days_left = calculate_days_until_birthday(dob)
        print(f"👋 Welcome back, {name}!")
        print(f"🎉 You are {age} years old.")
        print(f"📆 {days_left} day(s) left until your next birthday.")
    else:
        print("👤 New user detected.")
        dob_str = input("Enter your birthday (YYYY-MM-DD): ")
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
            accounts[name] = dob_str
            save_accounts(accounts)
            print(f"✅ Account for {name} saved.")
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
