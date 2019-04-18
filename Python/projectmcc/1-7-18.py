#Alejandro Rosales

import os
from PIL import Image, ImageEnhance
import sys


# Set maxsize of image
maxsize = (80, 80)


# Take a picture
def take_photo(filename='pic.jpg'):
	import photos
	img = photos.capture_image()
	if img:
		img.save(filename)
		return filename
		
		
# Imports image and manipulates it
def process_img():
	try:
		infile = take_photo()
	except IOError:
		infile = "Chelsey.jpg"
		
	f, e = os.path.splitext(infile)
	outfile = f + ".jpg"
	
	# If file is not the proper format then convert file
	if infile != outfile:
		try:
			Image.open(infile).save(outfile)
		except IOError:
			print("Cannot convert file")
			sys.exit()
			
	# Try opening file
	try:
		img = Image.open(infile).convert('LA')
		
		# Print size before
		print(img.format, img.size, img.mode)
		
		# Image Manipulations
		img.thumbnail(maxsize, Image.ANTIALIAS)
		sharpness = ImageEnhance.Sharpness(img)
		
		# Print size after
		print(img.format, img.size, img.mode)
		
		#sharpness.enhance(2).show()
		return sharpness.enhance(2)
		
	except IOError:
		print("Unable to load image")
		sys.exit()
		
		
def max_value(pixels):
	single_array = []
	for pixel in pixels:
		single_array.append(pixel[0])
	return max(single_array)
	
	
# Points of intensity
def poi(img):
	max_values = [[]]
	pixels = list(img.getdata())
	while True:
		max_values.append(max_value(pixels))
		
		
if __name__ == '__main__':
	img = process_img()
	print(poi(img))
