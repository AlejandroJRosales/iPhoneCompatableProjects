import random
from PIL import Image
import photos
import dialogs

from random import randrange, getrandbits
from itertools import repeat
from functools import reduce
from math import log10
from time import time
	


def getPrime(n):
	"""Get a n-bit pseudo-random prime"""
	
	def isProbablePrime(n, t=7):
		"""Miller-Rabin primality test"""
		
		def isComposite(a):
			"""Check if n is composite"""
			if pow(a, d, n) == 1:
				return False
			for i in range(s):
				if pow(a, 2 ** i * d, n) == n - 1:
					return False
			return True
			
		assert n > 0
		if n < 3:
			return [False, False, True][n]
		elif not n & 1:
			return False
		else:
			s, d = 0, n - 1
			while not d & 1:
				s += 1
				d >>= 1
		for _ in repeat(None, t):
			if isComposite(randrange(2, n)):
				return False
		return True
		
	p = getrandbits(n)
	while not isProbablePrime(p):
		p = getrandbits(n)
	return p
	
	
def inv(p, q):
	"""Multiplicative inverse"""
	
	def xgcd(x, y):
		"""Extended Euclidean Algorithm"""
		s1, s0 = 0, 1
		t1, t0 = 1, 0
		while y:
			q = x // y
			x, y = y, x % y
			s1, s0 = s0 - q * s1, s1
			t1, t0 = t0 - q * t1, t1
		return x, s0, t0
		
	s, t = xgcd(p, q)[0:2]
	assert s == 1
	if t < 0:
		t += q
	return t
	
	
def genRSA(p, q):
	"""Generate public and private keys"""
	phi, mod = (p - 1) * (q - 1), p * q
	if mod < 65537:
		return (3, inv(3, phi), mod)
	else:
		return (65537, inv(65537, phi), mod)
		
		
def text2Int(text):
	"""Convert a text string into an integer"""
	return reduce(lambda x, y: (x << 8) + y, map(ord, text))
	
	
def int2Text(number, size):
	"""Convert an integer into a text string"""
	text = "".join([chr((number >> j) & 0xff)
	for j in reversed(range(0, size << 3, 8))])
	return text.lstrip("\x00")
	
	
def int2List(number, size):
	"""Convert an integer into a list of small integers"""
	return [(number >> j) & 0xff
	for j in reversed(range(0, size << 3, 8))]
	
	
def list2Int(listInt):
	"""Convert a list of small integers into an integer"""
	return reduce(lambda x, y: (x << 8) + y, listInt)
	
	
def modSize(mod):
	"""Return length (in bytes) of modulus"""
	modSize = len("{:02x}".format(mod)) // 2
	return modSize
	
	
def encrypt(ptext, pk, mod):
	"""Encrypt message with public key"""
	size = modSize(mod)
	output = []
	while ptext:
		nbytes = min(len(ptext), size - 1)
		aux1 = text2Int(ptext[:nbytes])
		assert aux1 < mod
		aux2 = pow(aux1, pk, mod)
		output += int2List(aux2, size + 2)
		ptext = ptext[size:]
	return output
	
	
def decrypt(ctext, sk, p, q):
	"""Decrypt message with private key
	using the Chinese Remainder Theorem"""
	mod = p * q
	size = modSize(mod)
	output = ""
	while ctext:
		aux3 = list2Int(ctext[:size + 2])
		assert aux3 < mod
		m1 = pow(aux3, sk % (p - 1), p)
		m2 = pow(aux3, sk % (q - 1), q)
		h = (inv(q, p) * (m1 - m2)) % p
		aux4 = m2 + h * q
		output += int2Text(aux4, size)
		ctext = ctext[size + 2:]
	return output

	
def hexList(intList):
	"""Print ciphertext in hex"""
	clist = ""
	for index, elem in enumerate(intList):
		if index % 32 == 0:
			clist += ""
		clist += "{:02x}".format(elem) + " "
	return clist


# Convert encoding data into 8-bit binary
# form using ASCII value of characters
def genData(data):
	# list of binary codes
	# of given data
	newd = []
	
	for i in data:
		newd.append(format(ord(i), '08b'))
	return newd
	
	
# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):
	datalist = genData(data)
	lendata = len(datalist)
	imdata = iter(pix)
	
	for i in range(lendata):
	
		# Extracting 3 pixels at a time
		pix = [value for value in imdata.__next__()[:3] +
		imdata.__next__()[:3] +
		imdata.__next__()[:3]]
		
		# Pixel value should be made
		# odd for 1 and even for 0
		for j in range(0, 8):
			if (datalist[i][j] == '0') and (pix[j] % 2 != 0):
			
				if (pix[j] % 2 != 0):
					pix[j] -= 1
					
			elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
				pix[j] -= 1
				
		# Eigh^th pixel of every set tells
		# whether to stop ot read further.
		# 0 means keep reading; 1 means the
		# message is over.
		if (i == lendata - 1):
			if (pix[-1] % 2 == 0):
				pix[-1] -= 1
		else:
			if (pix[-1] % 2 != 0):
				pix[-1] -= 1
				
		pix = tuple(pix)
		yield pix[0:3]
		yield pix[3:6]
		yield pix[6:9]
		
		
def encode_enc(newimg, data):
	w = newimg.size[0]
	(x, y) = (0, 0)
	
	for pixel in modPix(newimg.getdata(), data):
	
		# Putting modified pixels in the new image
		newimg.putpixel((x, y), pixel)
		if (x == w - 1):
			x = 0
			y += 1
		else:
			x += 1
			
			
# Encode data into image
def encode(msg):
	i = dialogs.alert('Image', '', 'Take Photo', 'Load Image', 'Select from Photos')
	if i == 1:
		im = photos.capture_image()
	elif i == 2:
		im = Image.open(input("Name (example.png): "))
	else:
		im = photos.pick_image()
		
	newimg = im.copy()
	encode_enc(newimg, msg)
	newimg.show()
	new_img_name = input("Name (example.png): ")
	newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
	print("Image saved")
	
	
# Decode the data in the image
def decode():
	i = dialogs.alert('Image', '', 'Load Image', 'Select from Photos')
	if i == 1:
		im = Image.open(input("Name (example.png): "))
	else:
		im = photos.pick_image()
	
	data = ''
	imgdata = iter(im.getdata())
	
	while (True):
		pixels = [value for value in imgdata.__next__()[:3] +
		imgdata.__next__()[:3] +
		imgdata.__next__()[:3]]
		# string of binary data
		binstr = ''
		
		for i in pixels[:8]:
			if (i % 2 == 0):
				binstr += '0'
			else:
				binstr += '1'
				
		data += chr(int(binstr, 2))
		if (pixels[-1] % 2 != 0):
			return data
			
		# Main Function


def main():
	selection = dialogs.alert('Type', '', 'Encode', 'Decode')
	
	if (selection == 1):		
		p = dialogs.alert('Do you already have a public and/or private key (y/n)', '', 'Yes', 'No')
		if p == 1:
			print("Enter in public key. Looks like \"Public Key = (n, e) = (12, 34)\"")
			run = False
			while run is False:
				try:
					n, e = (int(num) for num in input("Enter in your public key | ex. -> 12, 34: ").split(","))
					run = True
				except ValueError:
					print("Hmm, does not look right. Example -> 12, 34")
		else:
				
			n = 256
			p = getPrime(n)
			q = getPrime(n)
			pk, sk, mod = genRSA(p, q)
			print("\nPublic Key: ", pk)
			print("Private Key: ", sk)
			msg = input("\nMessage: ")
			ctext = encrypt(msg, pk, mod)
			ctext = hexList(ctext)
			print("Ciphertext:", ctext)
			encode(ctext)
		
	else:
		decoded_message = decode()
		print("Decoded word:\n\n" + decoded_message)
		
		usr_input = ""
		while usr_input != "y" or usr_input != "n":
			usr_input = input("\nDecrypt (y/n):")
		
			if usr_input == "y":
				run = False
				while run is False:
					try:
						sk, p, q  = (int(num) for num in input("Enter in your private key, p, and q seperated by commas: ").split(","))
						run = True
					except ValueError:
						print("Hmm, does not look right. Example -> 12, 34")
				
				ptext = decrypt(decoded_message, sk, p, q)
				print(f"Decrypted - \n\n{ptext}")
				break
			if usr_input == "n":
				break
				
			else:
				print("*Please enter in \"y\" or \"n\" for yes or no, respectively*")
		
	# Driver Code
	
	
if __name__ == '__main__':
	# Calling main function
	main()
