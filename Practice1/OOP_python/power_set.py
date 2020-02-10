class PowerSet:

	def sub_sets(self,list1):

		sub_list = [[]]

		for i in range(len(list1)+1):
			for j in range(i+1,len(list1)+1):
				sub = list1[i:j]
				sub_list.append(sub)

		return sub_list


if __name__ == '__main__':

	power_set = PowerSet()
	list1 = [1,2,3,4,5]

	print(power_set.sub_sets(list1))





