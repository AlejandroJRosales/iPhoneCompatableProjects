# -*- coding = utf-8 -*-

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
		for i in range(2, int((n ** .5) + 1)):
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
			n = random.randint(0, 1 << halfkeylength)
			if n % 2 != 0:
				found = True
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
		if pow(a, q, n) == 1:
			return "inconclusive"
		for j in range(0, k):
			if pow(a, (2 ** j) * q, n) == n - 1:
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
		bytes = ptext.encode("utf-8")
		h = ""
		for b in bytes:
			h += self.int_2_hex(b)
		num = int(h, 16)
		encrypt = lambda x: pow(x, e, n)
		return self.int_2_hex(encrypt(num))
		
	def decryption(self, ctext, d, n):
		ctext, d, n = int(ctext, 16), self.hex_2_int(d), self.hex_2_int(n)
		decrypt = lambda x: pow(x, d, n)
		num = decrypt(ctext)
		h = self.int_2_hex(num)
		i = 0
		bytes = []
		while i < len(h):
			bytes.append(int(h[i: i + 2], 16))
			i += 2
		return "".join([chr(byte) for byte in bytes])
		
	def clean_print(self, string):
		for i, c in enumerate(string):
			if i % 41 == 0 and i != 0:
				print()
			print(c, end="")
		print()
		
		
if __name__ == '__main__':
	# 62, 128, 192, 256, 512, 768, 1024, 2048
	rsa = RSA()
	(n, e, d) = rsa.generate_key(1024)
	key_size = len(bin(rsa.hex_2_int(d))) - 2
	mod_size = len(bin(rsa.hex_2_int(n))) - 2
	print(f"Private Key Size In Bits: {key_size} \n")
	print("-------------- BEGIN MOD ----------------")
	rsa.clean_print(n)
	print("-------------- END MOD ------------------\n\n")
	print("-------- BEGIN RSA PUBLIC KEY -----------")
	rsa.clean_print(e)
	print("-------- END RSA PUBLIC KEY -------------\n\n")
	print("-------- BEGIN RSA PRIVATE KEY ----------")
	rsa.clean_print(d)
	print("-------- END RSA PRIVATE KEY ------------\n\n")
	# text = "Hello World!"
	print(f"Max Character Size is {int(.12 * mod_size)}")
	text = input("Input:: ")
	print(f"Your Character Size is {len(text)}\n\n")
	# print(len(bin(rsa.text)) - 2)
	C = rsa.encryption(text, e, n)
	M = rsa.decryption(C, d, n)
	print("-------- BEGIN ENCRYPTED MESSAGE --------")
	rsa.clean_print(C)
	print("-------- END ENCRYPTED MESSAGE ----------\n\n")
	print("Successful") if text == M else print("Failed")

