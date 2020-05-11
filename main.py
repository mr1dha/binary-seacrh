#Author : Muhammad Ridha
#NIM : 180810701023
#Last Modified : May 10th 2020

class BinarySearch():
	
	#Constructor Method
	def __init__(self): 
		self.arr = []
		self.l = 0;
		self.r = 0

	#Method untuk inser data
	def insert(self, data):
		self.arr = data
		self.r = len(self.arr)-1

	# Method Mengembalikan nilai index jika data ditemukan 
	# Dan mengembalikan -1 Jika 404
	def search(self, x):

		while self.l <= self.r: 
			#Mengecek dan memperbarui nilai tengah
			mid = self.l + (self.r - self.l) // 2; 
			
			# Cek apakah data berada di tengah
			if self.arr[mid] == x: 
				return mid 

			# Cek apakah data berada di kanan
			elif self.arr[mid] < x: 
				self.l = mid + 1

			# Cek apakah data berada di kiri 
			else: 
				self.r = mid - 1
		 
		# Mengembalikan -1 jika elemen tidak ada 
		return -1


########### TESTING ##########

#membuat objek dari class BinarySearch
binarySearch = BinarySearch();

#melakukan insert data
binarySearch.insert([1,5,9,12,23,24,33,90])

#search data
result = binarySearch.search(23) 

if result > -1: 
	print ("Data ditemukan pada index ke- % d" % result) 
else: 
	print ("Data tidak ada dalam array") 
