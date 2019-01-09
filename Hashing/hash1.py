#Implement External hashing technique with bit-representation hash function

import OpenHash:
	table_size = 11
	class Node:
		def __init__(self, ssid, name):
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
	def is_number(self, element):
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
	