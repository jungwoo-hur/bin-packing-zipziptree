# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file

#from __future__ import annotations
#project 2

from typing import TypeVar
from dataclasses import dataclass
import random
import math


KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')


@dataclass(order=True)
class Rank:
	geometric_rank: int
	uniform_rank: int

@dataclass
class Node:
	key: KeyType
	val: ValType
	rank: Rank
	left: 'Node' = None
	right: 'Node' = None

class ZipZipTree:
	def __init__(self, capacity: int): # capacity 왜 필요함?
		self.root = None
		self.size = 0
		self.capacity = capacity


###########################################################################
		
	def get_random_rank(self) -> Rank: # 리턴값 Rank 객체 반환

		geometric = 0
		while random.random() < 0.5:
			geometric += 1


		uniformMax = int(math.log(self.capacity) ** 3) - 1
		uniform = random.randint(0, uniformMax)

		return Rank(geometric_rank=geometric, uniform_rank=uniform)

###########################################################################


	def insert(self, key: KeyType, val: ValType, rank: Rank = None):


		if rank is None:
			rank = self.get_random_rank();

		self.size += 1

		new_node = Node(key, val, rank)


		p_node = None
		c_node = self.root
		

		# find node to be replaced
		
		while c_node is not None and (new_node.rank < c_node.rank or (new_node.rank == c_node.rank and new_node.key > c_node.key)):


			p_node = c_node
			if new_node.key < c_node.key:
					c_node = c_node.left
			else:
					c_node = c_node.right

		# insert new node
		if c_node == self.root:
			self.root = new_node

		elif new_node.key < p_node.key:
			p_node.left = new_node

		else:
			p_node.right = new_node

		# preserving replaced node
		if c_node is None:
			return
		if new_node.key < c_node.key:
			new_node.right = c_node

		else:
			new_node.left = c_node
		p_node = new_node

		tmp_node = None

		while c_node is not None:
			tmp_node = p_node

			if c_node.key < new_node.key:
					while c_node is not None and c_node.key < new_node.key:
						p_node = c_node
						c_node = c_node.right

			else:
					while c_node is not None and c_node.key > new_node.key:
						p_node = c_node
						c_node = c_node.left

			if tmp_node.key > new_node.key or (tmp_node == new_node and p_node.key > new_node.key):
					
					tmp_node.left = c_node
			
			else:
					tmp_node.right = c_node
		
		
		
	
	###########################################################################


	def remove(self, key: KeyType):
		
		
		c_node = self.root
		l_node = None
		r_node = None
		p_node = None
		


		self.size -= 1

		while key != c_node.key:
			p_node = c_node
			if key < c_node.key:
					c_node = c_node.left
			else:
					c_node = c_node.right

		if not c_node:
			return  


		l_node = c_node.left
		r_node = c_node.right

		
		if l_node is None:
			c_node = r_node
		elif r_node is None:
			c_node = l_node
	
		elif l_node.rank >= r_node.rank:
			c_node = l_node
		else:
			c_node = r_node

		if self.root.key == key:
			self.root = c_node
		elif key < p_node.key:
			p_node.left = c_node
		else:
			p_node.right = c_node

		
		while r_node is not None and l_node is not None:

			if l_node.rank >= r_node.rank:
					while l_node is not None and l_node.rank >= r_node.rank:
						p_node = l_node
						l_node = l_node.right
					p_node.right = r_node
			else:
					while r_node is not None and l_node.rank < r_node.rank:
						p_node = r_node
						r_node = r_node.left
					p_node.left = l_node

	###########################################################################
		
	# def zip(self, left: Node, right: Node) -> Node:

	# 	if left is None:
	# 		return right
		
	# 	if right is None:
	# 		return left
		
	# 	if left.rank > right.rank or (left.rank == right.rank and left.key < right.key):
	# 		left.right = self.zip(left.right, right)
	# 		return left
		
	# 	else:
	# 		right.left = self.zip(left, right.left)
	# 		return right


	###########################################################################	

	def find(self, key: KeyType) -> ValType:
		
		c_node = self.root

		while c_node is not None:
			
			if key == c_node.key:
				return c_node.val
			
			elif key < c_node.key:
				c_node = c_node.left

			else:
				c_node = c_node.right

			
		# raise ValueError("Key not found")
		return None
	

	###########################################################################

	def get_size(self) -> int:
		return self.size
	
	###########################################################################

	def get_height(self) -> int:

		if self.root is None:
			return -1
		
		def height_helper(node: Node) -> int:

			if node is None:
				return -1
			

			left_height = height_helper(node.left)
			right_height = height_helper(node.right)

			return max(left_height, right_height) + 1
		
		return height_helper(self.root)
		

	###########################################################################

	def get_depth(self, key: KeyType):
		
		
		if self.root is None:
			return -1
		
		c_node = self.root
		depth = 0

		while c_node is not None:
			if key == c_node.key:
				return depth
			
			elif key < c_node.key:
				c_node = c_node.left
				depth += 1

			else:
				c_node = c_node.right
				depth += 1

		return -1




	###########################################################################

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define