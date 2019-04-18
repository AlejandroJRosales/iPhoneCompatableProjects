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
	except :
		print("Import Photos may not be working")
		print("Trying to open file")
		try: 
			infile = "Chelsey.jpg"
		except :
			print("Failed")
		
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
		
		# Image Manipulations
		img.thumbnail(maxsize, Image.ANTIALIAS)
		sharpness = ImageEnhance.Sharpness(img)
		
		#sharpness.enhance(2).show()
		return sharpness.enhance(2)
		
	except IOError:
		print("Unable to load image")
		sys.exit()
		
		
def value(pixel_value):
	smallest = 255
	index = 0
	for i in range(len(pixel_value)):
		if pixel_value[i] < smallest:
			smallest = pixel_value[i]
			index = i
	return index, smallest
	
	
def check(img, new_image):
	row_sum = 0
	for i in range(img.size[0] * img.size[1]):
		row_sum += new_image[i][0]
		if (i % img.size[0] == 0) & (i != 0):
			if row_sum % 255  == 0:
				return True
			else:
				row_sum = 0
				
	col_sum = 0
	for i in range(img.size[0]):
		for a in range(img.size[1]):
			
			col_sum += new_image[a * img.size[0] + i][0]
		if col_sum % 255 == 0:
			return True
		else:
			col_sum = 0
			
	return False
	
	
# Points of intensity
def poi(img):
	new_image = [(255, 255)] * (img.size[0] * img.size[1])
	pixels = []
	pixels_list = list(img.getdata())
	for pixel in pixels_list:
		pixels.append(pixel[0])
	while check(img, new_image):
		index, smallest = value(pixels)
		pixels.pop(index)
		pixels.insert(index, 255)
		new_image.pop(index)
		new_image.insert(index, (smallest, 255))
	im2 = Image.new(img.mode, img.size)
	im2.putdata(new_image)
	im2.show()
	
	
if __name__ == '__main__':
	img = process_img()
	poi(img)

