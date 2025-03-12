import time

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



start = time.time()
for i in range(1,10):
	time.sleep(2)
	print("{} is {} ".format(i,is_prime(i)))

print("\n Execution time : {} seconds".format(time.time()-start))