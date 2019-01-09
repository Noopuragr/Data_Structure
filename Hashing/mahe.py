#Design a multilevel hash table to store student information of 
#Manipal University. Assume University has many colleges ( SOIS, MIT, KMC, SOAHS, SOLS,…….). 
#Student information is stored under respective colleges. 
#Each college can have multiple streams ( Big Data, VLSI, ES, MS, CTV etc….). Design hash table such that student should be stored under respective college and corresponding stream. 
#Information need to store is student registration number, name, phone number, mail id, Grade. 
#Provide following methods to end users:
#a.      add_student()
#b.      delete_student()
#c.      search_student()
#d.      edit_student_details()
#e.      count_no_students_college()
#f.       count_no_students_stream()
#              User need to input college name and stream name to ease the operations.



import numpy as py

class OpenHash:
	table_size = 11
	def __init_(self):
		self.hashtable1 = []
		self.hashtable2 = []
		self.hashtable3 = []
			# self.p = 13
			# self.a = np.random.randint(1,self.p)
			# self.b = np.random.randint(0,self.p)
		self.initialize_hashtable(hashtable1)
		self.initialize_hashtable(hashtable1)
		self.initialize_hashtable(hashtable1)




	def _initialize_hashtable(self,hashtable):
		self.hashtable = [None] * OpenHash.table_size
	class subHash:
		table_size = 11
		class Node:
			def __init__(self, ssid, name=[]):
				self.ssid = ssid
				self.name = name
				self.next = None
		def __init__(self):
			self.hashtable = []
			# self.p = 13
			# self.a = np.random.randint(1,self.p)
			# self.b = np.random.randint(0,self.p)
			self.initialize_hashtable()
		def _initialize_hashtable(self):
			self.hashtable = [None] * OpenHash.table_size
		def _hash_number(self,element):
			hash_code = 0
			for ch in str(element):
				hash_code = hash_code + ord(ch)
			return hash_code

		def _compress(self, number):
			return((self.a*number + self.b) % self.p) % OpenHash.table_size)

		def _hash_(self, element):
			number = self._hash_number(element)
			hash_code = self._compress(number)
			return hash_code
		def is_member(self, element):
			bucket = self._hash_(element)
			cur = self.hashtable[bucket]
			while(cur != None):
				if cur.ssid == element:
					return True
				else:
					cur = cur.next
			return False

		def add_element(self,element, name):
			if not self.is_member(element):
				bucket = self._hash_(element):
				new_node = self.Node(element,name)
				new_node.next = self.hashtable[bucket]
				self.hashtable[bucket] = new_node

		def delete_data(self, element):
			bucket = self._hash_(element)
			if self.hashtable[bucket] != None:
				if self.hashtable[bucket].ssid == element:
					self.hashtable[bucket] = self.hashtable[bucket].next
				else:
					cur = self.hashtable[bucket]
					while cur.next!= None:
						if cur.next.ssid == element:
							cur.next = cur.next.next
						else:
							cur = cur.next


	def add_tables(self, coll, branch, s_details):
		sid = s_details[0]
		bucket = self.subHash._hash_(coll)
		if self.hashtable1[bucket] == None:
			if coll is 'SOIS':
				new_node = self.subHash.Node(coll)
				new_node.next = hashtable2
				self.hashtable1[bucket] = new_node

				bucket1 = self.subHash._hash_(branch)
				new_node = self.subHash.Node(branch)
				self.hashtable2[bucket1] = new_node

				bucket2 = self.subHash._hash_(sid)
				new_node = self.subHash.Node(branch)
				new_node.next = self.hashtable2[bucket1].next
				self.hashtable2[bucket1].next = new_node

		cur = self.hashtable1[bucket]
		branch_table = cur.next

		branch_bucket = self.subHash._hash_(branch)
		# branch = self.hashtable2[branch_bucket]

		# bucket2 = self.subHash._hash_(sid)
		new_node = self.subHash.Node(sid)
		new_node.next = branch_table[branch_bucket].next
		branch_table[branch_bucket].next = new_node








h1=hashtable()
h2=hashtable()
h3=hashtable()

def add(coll,branch, s_details):





