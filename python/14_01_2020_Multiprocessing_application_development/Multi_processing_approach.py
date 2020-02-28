# using process class

import time
import multiprocessing

def is_prime(n):
	if n == 1:
		return "Composite number"
	elif n > 1:
		flag = 0
		for i in range(2,n):
			if n % i == 0:
				flag = 1
	if flag == 1:
		return "Not prime"
	else:
		return "Prime"

def multiprocessing_func(x):
	time.sleep(2)
	print('{} is {} number'.format(x, is_prime(x)))
    
if __name__ == '__main__':
    starttime = time.time()
    processes = []
    for i in range(1,10):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()
        
    print()    
    print('Time taken = {} seconds'.format(time.time() - starttime))
