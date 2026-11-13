from customer import *
from rental import *

class Shop():
    def __init__(self, number_of_skis_in_inventory, number_of_snowboards_in_inventory):
        self.setup_inventory(number_of_skis_in_inventory, number_of_snowboards_in_inventory)
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

    def find_rentals_for_customer(self, customerIDnumber):
        customers_rentals = []
        for rental in self.rentals_list:
            if rental.rental_ID == customerIDnumber:
                customers_rentals.append(rental)
        return customers_rentals

    def add_customer(self, lname, phonenumber):
        new_customer = Customer(lname, phonenumber)
        self.customer_list.append(new_customer)
        print(f"ID number is {new_customer.customerIDnumber}")

    def add_rental(self, skies_rented, snowboards_rented, rental_length, customerIDnumber):
        new_rental = Rental(skies_rented, snowboards_rented, rental_length)
        self.customer_list.append(new_rental)
        print(f"ID number is {new_rental.rentalIDnumber}")

    def complete_rental(self, intRentalID):
        rental = self.find_rental(intRentalID)
        rental.IsClosed = True
        self.number_of_skis_in_inventory += rental.skies_rented
        self.number_of_snowboards_in_inventory += rental.snowboards_rented
        charge = (rental.skies_rented * 15) + (rental.snowboards_rented * 10)
        print(f"total charge is {charge}")

    def setup_inventory(self, intNumberOfSkis, intNumberOfSnowboards):
        self.number_of_skis_in_inventory = intNumberOfSkis
        self.number_of_snowboards_in_inventory = intNumberOfSnowboards





