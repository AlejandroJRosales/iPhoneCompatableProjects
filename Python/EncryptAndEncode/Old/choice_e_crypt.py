import random


# Method for finding the greatest common denominator of two numbers
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a
	
	
# Method for finding least common multiple of two numbers
def lcm(x, y):
	if x > y:
		z = x
	else:
		z = y
		
	while True:
		if z % x == 0 and z % y == 0:
			answer = z
			break
		z += 1
		
	return answer
	
	
# Modular multiplicative inverse
def mod_inv(e, totient):
	for d in range(1, totient):
		if (d * e) % totient == 1:
			return d
	return None
	
	
# Method for finding coprime of number
def coprimes(x):
	primes = []
	for i in range(2, x):
		if gcd(i, x) == 1:
			primes.append(i)
	return primes
	
	
def not_divisor(arr, x):
	return [num for num in arr if x % num != 0]
	
	
# Generate Prime numbers
def get_primes():
	primes = []
	for i in range(100, 999):
		k = 0
		for a in range(2, i // 2 + 1):
			if i % a == 0:
				k += 1
		if k <= 0:
			primes.append(i)
	return primes
	
	
# Generate Private and Public Keys
def get_keys():
	# Generating Public Key
	primes = get_primes()
	p, q = primes.pop(random.randint(0, len(primes) - 1)), primes.pop(random.randint(0, len(primes) - 1))
	n = p * q
	
	# Generating Private Key
	totient = lcm((p - 1), (q - 1))
	e = random.choice(not_divisor(coprimes(totient), totient))
	d = mod_inv(e, totient)
	
	return n, e, d
	
selection = ""
while selection != "e" and selection != "d":
	# private key (n, d) is to decrypt messages going in for who u gave ur public key too
	# public key (n, e) is what you gave to someone so they can encrypt their messages so only you can read them
	selection = input("Encrypt/Decrypt (e/d): ")
	if selection == "e":
		usr_input = ""
		while usr_input != "y" and usr_input != "n":
			usr_input = input("Do you already have a public and/or private key (y/n): ")
			if usr_input == "y":
				print("Enter in public key. Looks like \"Public Key = (n, e) = (12, 34)\"")
				run = False
				while run is False:
					try:
						n, e = (int(num) for num in input("Enter in your public key | ex. -> 12, 34: ").split(","))
						run = True
					except ValueError:
						print("Hmm, does not look right. Example -> 12, 34")
						
				msg = input("Message: ")
				encrypt = lambda x: x ** e % n
				e_crypt = "".join([chr(encrypt(ord(c))) for c in msg])
				print(f"Encrypted - {e_crypt}")
				pass
			elif usr_input == "n":
				n, e, d = get_keys()
				print(f"\nPublic key = (n, e) = ({n}, {e}) Private key = (n, d) = ({n}, {d})\n")
				msg = input("Message: ")
				encrypt = lambda x: x**e % n
				e_crypt = "".join([chr(encrypt(ord(c))) for c in msg])
				print(f"Encrypted - {e_crypt}")
			else:
				print("*Please enter in \"y\" or \"n\" for yes or no, respectively*")
				
	elif selection == "d":
		print("Enter in private key. Looks like \"Private Key = (n, e) = (12, 34)\"")
		# Public key = (n, e) = (511, 59) Private key = (n, d) = (511, 11)
		run = False
		while run is False:
			try:
				n,d  = (int(num) for num in input("Enter in your private key | ex. -> 12, 34: ").split(","))
				run = True
			except ValueError:
				print("Hmm, does not look right. Example -> 12, 34")
				
		e_crypt = input("Encrypted Message: ")
		decrypt = lambda x: x**d % n
		d_crypt = "".join([chr(decrypt(ord(c))) for c in e_crypt])
		print(f"Decrypted - {d_crypt}")
		
	else:
		print("*Please enter in \"e\" or \"d\" for \"Encrypt\" or \"Decrypt\", respectively*")
		
		# Public key = (n, e) = (2183, 223) Private key = (n, d) = (2183, 103)
		# әߔǏχđχ܋ϤǏߔ̝Ǐׂ͌ߔׇࡅǏ̝ǆǏԴǙׇǏ܋ׇҗőǆѼ̛ߔԴׇǏ͌Դࡒ̛Ǚđő܋ӕǏǠǏߡׂ̛͌ǏǙđׇ̛܋ԄǏ̛ԴǏ̛܋ɱɱǏׂǏׂőǏ̝ǆǏχ܋̛͌Ǐࡒőߔ܋ׇԄǏđׇԄǏǠǏǙđׇ̛Ǐ̛ԴǏ̛͌đׇԄǏǙߔ̛љǏׂǏࡒԴő܋͵܋őӕǏǠǏǙđׇ̛Ǐ̛ԴǏљ͵ǏχđχǆǏχׂԄ͌ǏđׇԄǏљ͵ǏׂǏχ܋Ǐ̛љ܋ő܋Ǐ̝Դ̝̝đǏχׂԄӕǏǠǏǙđׇ̛Ǐ̛ԴǏࡅőԴǙǏԴɱԄǏǙߔ̛љǏǆԴׂӕǏǠǏǙđׇ̛ǏǆԴׂǏ̛ԴǏχ܋Ǐ̛љ܋ő܋ǏࡒԴőǏ̝ǆǏɱđ̛͌Ǐχő܋đ̛љϤǏԴőǏǠǏǙđׇ̛Ǐ̛ԴǏχ܋Ǐ̛љ܋ő܋ǏࡒԴőǏׂő͌ӕǏǠǏɱԴ͵܋ǏǆԴׂӕǏ̍ǙđљӕǏ\̛ߔࡅљ̛܋̛͌Ǐχߔࡅࡅ܋̛͌Ǐχ܋đőǏљׂࡅ\

