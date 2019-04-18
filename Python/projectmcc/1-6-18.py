from PIL import Image, ImageFilter
import os


# Set maxsize of image(s)
maxsize = (100, 100)


# IMPORTS IMAGE THEN APPLIES GRAYSCALE AND SIZES IMAGE
def proccess_img():
	infile = "Chelsey1.png"
	f, e = os.path.splitext(infile)
	outfile = f + ".png"
	
	# If file is not the proper format then convert files
	if infile != outfile:
		try:
			Image.open(infile).save(outfile)
		except:
			raise IOError("cannot convert")
			
	try:
		img = Image.open(infile).convert('LA')
		
		# Print size before
		print(img.format, img.size, img.mode)
		img.thumbnail(maxsize, Image.ANTIALIAS)
		
		# Print size after
		print(img.format, img.size, img.mode)
		
		img.show()
		return img
		
	except:
		raise IOError("Unable to load image")
		
		
def pixel_intensities(img):
	#count = 0
	for pixel in img.getdata():
		print(pixel)
		#if count % 1000 == 0:
			#print("")
		#count += 1
		
if __name__ == '__main__':
	pixel_intensities(proccess_img())
	
	
# img.save('grayscale.png')
# img = img.filter(ImageFilter.SHARPEN)
# img = img.filter(ImageFilter.EDGE_ENHANCE)

