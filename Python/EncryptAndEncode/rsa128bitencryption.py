# -*- coding = utf-8 -*-

import math
import random


class RSA:
	def gcd(self, a, b):
		if type(a) != int or type(b) != int:
			return
		a, b = (a, b) if a >= b else (b, a)
		while b:
			a, b = b, a % b
		return a
		
		
	def is_prime(self, n):
		if n <= 1:
			return False
		for i in range(2, int(math.sqrt(n)) + 1):
			if n % i == 0:
				return False
		return True
		
		
	def ext_gcd(self, a, b):
		if b == 0:
			return 1, 0, a
		else:
			x, y, q = self.ext_gcd(b, a % b)
			x, y = y, (x - (a // b) * y)
			return x, y, q
			
			
	def mod_exp(self, b, n, m):
		ret = 1
		tmp = b
		while n:
			if n & 0x1:
				ret = ret * tmp % m
			tmp = tmp * tmp % m
			n >>= 1
		return ret
		
		
	def phi(self, n):
		ret = 1
		i = 2
		n = int(n)
		while i * i <= n:
			if n % i == 0:
				n = n // i
				ret = int(ret * i) - ret
				while n % i == 0:
					n = n // i
					ret = ret * i
			i = i + 1
		if n > 1:
			ret = int(ret * n) - ret
			
		return ret
		
		
	def compute_d(self, fn, e):
		(x, y, r) = self.ext_gcd(fn, e)
		# y maybe < 0, so convert it
		if y < 0:
			return fn + y
		return y
		
		
	def random_prime(self, halfkeylength):
		while True:
			# 选择随机数
			n = random.randint(0, 1 << halfkeylength)
			if n % 2 != 0:
				found = True
				# 随机性测试
				for i in range(0, 5):
					if self.prime_test(n) == 'composite':
						found = False
						break
				if found:
					return n
					
					
	def prime_test(self, n):
		q = n - 1
		k = 0
		while q % 2 == 0:
			k += 1
			q = q // 2
		a = random.randint(2, n - 2)
		if self.mod_exp(a, q, n) == 1:
			return "inconclusive"
		for j in range(0, k):
			if self.mod_exp(a, (2 ** j) * q, n) == n - 1:
				return "inconclusive"
		return "composite"
		
		
	def generate_key(self, key_len):
		p = self.random_prime(key_len // 2)
		q = self.random_prime(key_len // 2)
		n = p * q
		fn = (p - 1) * (q - 1)
		e = 65537
		d = self.compute_d(fn, e)
		return self.int_2_hex(n), self.int_2_hex(e), self.int_2_hex(d)
		
		
	def hex_list(self, intList):
		s = ""
		for elem in intList:
			s += "{:02x}".format(elem) + "+"
		return s
		
		
	def int_2_hex(self, n):
		return "{:02x}".format(n)
		
		
	def hex_2_int(self, h):
		return int(h, 16)
		
		
	def encryption(self, ptext, e, n):
		e, n = self.hex_2_int(e), self.hex_2_int(n)
		encrypt = lambda x: self.mod_exp(x, e, n)
		return self.hex_list([encrypt(ord(c)) for c in ptext])
		
		
	def decryption(self, ctext, d, n):
		ctext, d, n = ctext.split("+"), self.hex_2_int(d), self.hex_2_int(n)
		decrypt = lambda x: self.mod_exp(x, d, n)
		return "".join([chr(decrypt(int(ctext[i], 16))) for i in range(len(ctext) - 1)])
		
		
if __name__ == '__main__':
	# 62, 128, 192, 256, 512, 768, 1024, 2048
	rsa = RSA()
	(n, e, d) = rsa.generate_key(1024)
	print("Private Key Size: ", len(bin(rsa.hex_2_int(d))) - 2, "\n")
	print("-------------- BEGIN MOD ----------------")
	print(n)
	print("-------------- END MOD ------------------\n\n")
	print("-------- BEGIN RSA PUBLIC KEY -----------")
	print(e)
	print("-------- END RSA PUBLIC KEY -------------\n\n")
	print("-------- BEGIN RSA PRIVATE KEY ----------")
	print(d)
	print("-------- END RSA PRIVATE KEY ------------\n\n")
	# text = "Hello World!"
	text = input(":: ")
	C = rsa.encryption(text, e, n)
	M = rsa.decryption(C, d, n)
	print("-------- BEGIN ENCRYPTED MESSAGE --------")
	print(C)
	print("-------- END ENCRYPTED MESSAGE ----------\n\n")
	print(text == M)
