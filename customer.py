class Customer():
    def __init__(self, lname, phonenumber):
        self.last_name = lname
        self.phone_number = phonenumber

    def display(self):
        print(f"Last name: {self.last_name}\nPhone number: {self.phone_number}")