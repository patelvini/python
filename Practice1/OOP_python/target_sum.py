class Target:

	def get_indices(self,list1,target):

		for i,num in enumerate(list1):
			if list1[i]+list1[i+1] == target:
				return i,i+1

if __name__ == '__main__':
	
	target = Target()

	list1 = [5,6,10,20,60]
	print(target.get_indices(list1,30))




