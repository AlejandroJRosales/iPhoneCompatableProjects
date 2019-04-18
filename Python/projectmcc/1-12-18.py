#Alejandro Rosales

import math
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
def proccess_img():
	try:
		infile = take_photo()
	except: 
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
		
		sharpness.enhance(2).show()
		return sharpness.enhance(2)
		
	except IOError:
		print("Unable to load image")
		sys.exit()
		
		
#Persons correlation coefficent r
def r(X, Y):
	x_sum = 0
	for x in X:
		x_sum += x
	x_bar = x_sum/len(X)
	
	y_sum = 0
	for y in Y:
		y_sum += y
	y_bar = y_sum/len(Y)
	
	top_part = 0
	x_sqrd = 0
	y_sqrd = 0
	for n in range(len(X)):
		top_part += (float(X[n]) - x_bar) * (float(Y[n]) - y_bar)
		x_sqrd += (float(X[n]) - x_bar) ** 2
		y_sqrd += (float(Y[n]) - y_bar) ** 2
		return top_part/math.sqrt(x_sqrd * y_sqrd)


#Points of intensity
def poi(img):
	pixels = list(img.getdata())
	correlations = []
	return correlations
	
	
#Find highest points of correlation
def my_sort(arr, limit):
	new_arr = []
	for i in range(limit):
		largest = 0
		for c in range(len(arr)):
			if abs(arr[c]) > largest: 
				largest = abs(arr[c])
				actual = arr[c]
				position = c
		new_arr.append(actual)
		arr.pop(position)
	return new_arr

if __name__ == '__main__':
	img = proccess_img()
	print(len(poi(img)))
