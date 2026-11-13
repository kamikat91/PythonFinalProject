from customer import *
from rental import *
from shop import *

def main():
    menu_open = True

    the_shop = Shop(25, 40)
    customer_1 = Customer("Jones",123-456-7890)
    customer_2 = Customer("Perry",513-348-1256)
    customer_3 = Customer("kreek",891-222-5558)

    while menu_open == True:

        choice = int(input("Welcome to the shop menu! please select and action\n1 for make a new customer"
                            "\n2 for customer information\n3 for customer rentals\n4 for all open rentals"
                            "\n5 to make a new rental\n6 to return a rental\n7 to display current inventory"
                            "\n8 to see aggregate statistics\n9 to close the menu "))
        if choice == 1:
            new_customer(the_shop)
        elif choice == 2:
            display_customer(the_shop)
        elif choice == 3:
            display_customer_rentals(the_shop)
        elif choice == 9:
            menu_open = False


        def tests(the_shop):
            the_shop.add_customer("smith", "111-111-1111")
            the_shop.add_customer("perry", "444-444-4444")
            the_shop.add_customer("kreek", "666-111-1111")
            the_shop.add_rental(2, 4, 5, 1)
            test_customer = the_shop.find_customer(1)
            test_customer.display()
            test_rental = the_shop.find_rental(1)
            test_rental.display()
            the_shop.complete_rental(1)
            the_shop.setup_inventory()


        def new_customer(the_shop):
            last_name = input("Whats the last name? ")
            phone_number = input("Whats the phone number? ")
            the_shop.add_customer(last_name, phone_number)


        def display_customer(the_shop):
            the_ID = int(input("Whats the ID number? "))
            the_customer = the_shop.find_customer(the_ID)
            the_customer.display()

        def display_customer_rentals(the_shop):
            the_ID = int(input("Whats the ID number? "))
            the_customer = the_shop.find_customer(the_ID)
            the_customer.display()


main()