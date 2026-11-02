from customer import *
from rental import *

class Shop():
    def __init__(self, number_of_skis_in_inventory, number_of_snowboards_in_inventory):
        self.number_of_skis_in_inventory = number_of_skis_in_inventory
        self.number_of_snowboards_in_inventory = number_of_snowboards_in_inventory
        customer_list = []
        rentals_list = []
        total_income = 0

    def find_customer(self, intCustomerIDtoFind):
        for customer in customer_list:
            if customer.customer_ID == intCustomerIDtoFind:
                return customer
            else:
                return None

    def find_rental(self, RentalIDtoFind):
        for rental in rentals_list:
            if rental.rental_ID == RentalIDtoFind:
                return rental
            else:
                return None

    def find_rentals_for_customer(self, customerID):
        for rental in rentals_list:
            if rental.rental_ID == customerID:
                return rental

    def add_customer(self, IDnumber, lname, phonenumber):
        new_customer = Customer(IDnumber, lname, phonenumber)
        customer_list.append(new_customer)

