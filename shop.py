from customer import *
from rental import *

class Shop():
    def __init__(self, number_of_skis_in_inventory, number_of_snowboards_in_inventory):
        self.number_of_skis_in_inventory = number_of_skis_in_inventory
        self.number_of_snowboards_in_inventory = number_of_snowboards_in_inventory
        self.customer_list = []
        self.rentals_list = []
        total_income = 0

    def find_customer(self, intCustomerIDtoFind):
        for customer in self.customer_list:
            if customer.customer_ID == intCustomerIDtoFind:
                return customer
            else:
                return None

    def find_rental(self, RentalIDtoFind):
        for rental in self.rentals_list:
            if rental.rental_ID == RentalIDtoFind:
                return rental
            else:
                return None

    def find_rentals_for_customer(self, customerID):
        for rental in self.rentals_list:
            if rental.rental_ID == customerID:
                return rental

    def add_customer(self, lname, phonenumber):
        customerIDnumber = 0
        new_customer = Customer(lname, phonenumber)
        customerIDnumber += 1
        self.customer_list.append(new_customer)
        print(f"ID number is {customerIDnumber}")

    def add_rental(self, skies_rented, snowboards_rented, rental_length):
        rentalIDnumber = 0
        new_rental = Rental(skies_rented, snowboards_rented, rental_length)
        rentalIDnumber += 1
        self.customer_list.append(new_rental)
        print(f"ID number is {rentalIDnumber}")

    def complete_rental(self, intRentalID):
        rental = self.find_rental(intRentalID)
        self.IsClosed = True
        self.number_of_skis_in_inventory += self.skies_rented
        self.number_of_snowboards_in_inventory += self.snowboards_rented
        charge = (self.skies_rented * 15) + (self.snowboards_rented * 10)
        print(f"total charge is {charge}")

    def setup_inventory(intNumberOfSkis, intNumberOfSnowboards):





