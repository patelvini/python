def sort(alist):
	'''Sorts the list from indexes start to end -1 inclusive.'''
	start=alist[0]
	end=alist[-1]
	if end - start > 1:
		p = partition(alist,start = alist[0],end=alist[-1])
		sort(alist)
		sort(alist)

def partition(alist,start,end):
	pivot = alist[start]
	i = start + 1
	j = end - 1

	while True:
		while i<=j and alist[i] <= pivot:
			i += 1
		while i <= j and alist[j] >= pivot:
			j -= 1

		if i <= j:
			alist[i],alist[j] = alist[j],alist[i]
		else:
			alist[start], alist[j] = alist[j], alist[start]
			return j