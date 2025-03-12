class A:
	def test(self):
		print("A")

class B(A):
	def test(self):
		print("B")
		#super().test()

class C(A):
	def test(self):
		print("C")
		super().test()

class D(B,C):
	def test2(self):
		print("D")

obj = D()
obj.test()
