class Rental():
	def __init__(self, skies_rented, snowboards_rented, rental_length):
		self.skies_rented = skies_rented
		self.snowboards_rented = snowboards_rented
		self.rental_length = rental_length
		IsClosed = False

	def display(self):
		print(f"Skies rented: {self.skies_rented}\nSnowboards rented: {self.snowboards_rented}\nRental length: {self.rental_length}")
