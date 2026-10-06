import math
import string
import random
from datetime import datetime, date
from faker import Faker


# ==============================================================================
# 🌟 EXERCISE 1: CURRENCIES
# ==============================================================================
class Currency:
    def __init__(self, currency, amount):
        self.currency = str(currency)
        self.amount = int(amount)

    def _get_plural(self):
        """Helper to handle singular vs plural formatting."""
        return f"{self.currency}s" if self.amount != 1 else self.currency

    def __str__(self):
        return f"{self.amount} {self._get_plural()}"

    def __repr__(self):
        return f"{self.amount} {self._get_plural()}"

    def __int__(self):
        return int(self.amount)

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        elif isinstance(other, (int, float)):
            return self.amount + other
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, (int, float)):
            self.amount += other
        else:
            return NotImplemented
        return self


# ==============================================================================
# 🌟 EXERCISE 2: IMPORT FUNCTION (func.py simulation)
# ==============================================================================
def add_and_print(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")


# ==============================================================================
# 🌟 EXERCISE 3: STRING MODULE
# ==============================================================================
def generate_random_string(length=5):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


# ==============================================================================
# 🌟 EXERCISE 4: CURRENT DATE
# ==============================================================================
def display_current_date():
    today = date.today()
    print("Today's date is:", today.strftime("%B %d, %Y"))


# ==============================================================================
# 🌟 EXERCISE 5: AMOUNT OF TIME LEFT UNTIL JANUARY 1ST
# ==============================================================================
def time_until_next_year():
    now = datetime.now()
    next_year = now.year + 1
    jan_1st = datetime(next_year, 1, 1)
    
    time_left = jan_1st - now
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(f"Time left until January 1st, {next_year}:")
    print(f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")


# ==============================================================================
# 🌟 EXERCISE 6: BIRTHDAY AND MINUTES
# ==============================================================================
def minutes_lived(birthdate_str, date_format="%Y-%m-%d"):
    birthdate = datetime.strptime(birthdate_str, date_format)
    now = datetime.now()
    
    time_lived = now - birthdate
    minutes = int(time_lived.total_seconds() // 60)
    
    print(f"You have lived approximately {minutes:,} minutes in your life!")


# ==============================================================================
# 🌟 EXERCISE 7: FAKER MODULE
# ==============================================================================
fake = Faker()
users = []

def add_fake_users(num_users):
    for _ in range(num_users):
        user = {
            "name": fake.name(),
            "address": fake.address().replace("\n", ", "),
            "language_code": fake.language_code()
        }
        users.append(user)


# ==============================================================================
# TEST RUNNER FOR ALL EXERCISES
# ==============================================================================
if __name__ == "__main__":
    print("--- Exercise 1: Currencies ---")
    c1 = Currency('dollar', 5)
    c2 = Currency('dollar', 10)
    c3 = Currency('shekel', 1)
    c4 = Currency('shekel', 10)

    print(c1)       # '5 dollars'
    print(int(c1))  # 5
    print(repr(c1)) # '5 dollars'
    print(c1 + 5)   # 10
    print(c1 + c2)  # 15
    print(c1)       # 5 dollars

    c1 += 5
    print(c1)       # 10 dollars

    c1 += c2
    print(c1)       # 20 dollars
    # print(c1 + c3) # Uncomment to test TypeError

    print("\n--- Exercise 2: Func Import ---")
    add_and_print(12, 8)

    print("\n--- Exercise 3: Random String ---")
    print("Random 5-letter string:", generate_random_string())

    print("\n--- Exercise 4: Current Date ---")
    display_current_date()

    print("\n--- Exercise 5: Time Until Jan 1st ---")
    time_until_next_year()

    print("\n--- Exercise 6: Birthday and Minutes ---")
    minutes_lived("2000-01-01")

    print("\n--- Exercise 7: Faker Module ---")
    add_fake_users(3)
    for idx, user in enumerate(users, start=1):
        print(f"User {idx}:", user)