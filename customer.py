class Customer():
    customerIDnumber = 0
    def __init__(self, lname, phonenumber):
        self.last_name = lname
        self.phone_number = phonenumber
        Customer.customerIDnumber += 1

    def display(self):
        print(f"Last name: {self.last_name}\nPhone number: {self.phone_number}")