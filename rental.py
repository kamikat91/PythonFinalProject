class Rental():
	def __init__(self,rental_ID, customer_ID, skies_rented, snowboards_rented, rental_length):
		self.rental_ID = rental_ID
		self.customer_ID = customer_ID
		self.skies_rented = skies_rented
		self.snowboards_rented = snowboards_rented
		self.rental_length = rental_length
		IsClosed = False

	def display(self):
		print(f"rental ID: {self.rental_ID}\nCustomer ID: {self.customer_ID}\nSkies rented: {self.skies_rented}\nSnowboards rented: {self.snowboards_rented}\nRental length: {self.rental_length}")
