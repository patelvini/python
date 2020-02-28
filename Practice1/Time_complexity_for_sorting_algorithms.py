import time
import random
from pygorithms import bubble_sort
from pygorithms import insertion_sort
from pygorithms import quick_sort

def timing_decorator(func):
	""" A decorator that times a callable """

	def timing(*args, **kwargs):
		""" The actual timer """
		t_start =  time.time()
		result = func(*args, **kwargs)
		t_end = time.time()

		print("Run time of : {} is {}s".format(func.__name__,(t_end-t_start)))
		return result
	return timing

# @timing_decorator
# def own_bubble_sort(unsorted_list):
# 	print(bubble_sort.sort(unsorted_list))

# @timing_decorator
# def own_insertion_sort(unsorted_list):
# 	print(insertion_sort.sort(unsorted_list))

@timing_decorator
def own_quick_sort(unsorted_list):
	print(quick_sort.sort(unsorted_list))

random.seed(42)
unsorted_list = [random.random() for _ in range(10000)]

# own_bubble_sort(unsorted_list)
# own_insertion_sort(unsorted_list)
own_quick_sort(unsorted_list)
