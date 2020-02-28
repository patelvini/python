# Automation script to find all running processes

import psutil

class ProcessMonitor:

	def findProcessList(self):

		list_of_process_names = []

		for process in psutil.process_iter():
			process_info = process.as_dict(attrs = ['pid','name'])

			list_of_process_names.append(process_info)

		return list_of_process_names

if __name__ == '__main__':
	
	p = ProcessMonitor()

	res = p.findProcessList()
	for i in res:
		print(i)