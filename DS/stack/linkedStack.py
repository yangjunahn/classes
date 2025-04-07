from DS.list.linkedListBasic import *

class LinkedStack:
	def __init__(self):
		self.__list = LinkedListBasic()

	def push(self, newItem):
		self.__list.insert(0, newItem)

	def pop(self):
		return self.__list.pop(0)

	def top(self):
		if self.isEmpty():
			return None
		else:
			return self.__list.get(0)

	def isEmpty(self) -> bool:
		return self.__list.isEmpty()

	def popAll(self):
		self.__list.clear()

	def printStack(self):
		print("Stack from top:", end = '')
		for i in range(self.__list.size()):
			print(self.__list.get(i), end = '')
		print()

	## Problem 04 구현을 위해 추가 구현한 함수
	def num_Items(self):
		return self.__list.size()	
# 코드 6-13