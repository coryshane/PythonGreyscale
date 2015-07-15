"""
Image converter 
from color to black and white
luminosity
and sepia
"""
#Cory Stephens


from PIL import Image

def greyscale(fileName):
	image = Image.open(fileName)
	location = image.size
	#size returns a 2-tuple, width and height
	newImage = Image.new("RGB", location, "white")
	pixelMap = newImage.load()

	for x in range(location[0]):
		for y in range(location[1]):
			pixel = pixelToGreyscale(image.getpixel((x,y)))
			pixelMap[x,y] = (pixel, pixel, pixel)
			
		
	newImage.save("gray_" + fileName)

def luminosity(fileName):
	image = Image.open(fileName)
	location = image.size
	
	newImage = Image.new("RGB", location, "white")
	pixelMap = newImage.load()

	for x in range(location[0]):
		for y in range(location[1]):
			pixel = pixelToLuminosity(image.getpixel((x,y)))
			pixelMap[x,y] = (pixel, pixel, pixel)
			
		
	newImage.save("luminosity_" + fileName)

def sepia(fileName):
	image = Image.open(fileName)
	location = image.size
	
	newImage = Image.new("RGB", location, "white")
	pixelMap = newImage.load()

	for x in range(location[0]):
		for y in range(location[1]):
			red = sepiaRed(image.getpixel((x,y)))
			green = sepiaGreen(image.getpixel((x,y)))
			blue = sepiaBlue(image.getpixel((x,y)))
			
			pixelMap[x,y] = (red, green, blue)
			
		
	newImage.save("sepia_" + fileName)
	
def pilBlackAndWhite(fileName):
	image = Image.open(fileName)
	image = image.convert('1')
	image.save('pil_' + fileName)
	
#The numbers here are Microsoft's recommended calculations for sepia
def sepiaRed(pixel):
	red = (pixel[0] * .393) + (pixel[1] * .769) + (pixel[2] * .189)
	return int(red)
	
def sepiaGreen(pixel):
	green = (pixel[0] * .349) + (pixel[1] * .686) + (pixel[2] * .168)
	return int(green)
	
def sepiaBlue(pixel):
	blue = (pixel[0] * .272) + (pixel[1] * .534) + (pixel[2] * .131)
	return int(blue)

#The author of GIMP wrote an article on types of greyscale conversion. The numbers can be accredited to his work	
def pixelToLuminosity(pixel):
	#RGB, humans are more sensitive to green, so the formula is weighted for green heavily
	newPixel = 0.21*(pixel[0]) + 0.72*(pixel[1]) + 0.07*(pixel[2])
	return int(newPixel)

def pixelToGreyscale(pixel):
	newPixel = (pixel[0] + pixel[1] + pixel[2]) / 3
	return int(newPixel)

def mainMenu():
	userInput = raw_input("Please type the file name to convert, or type QUIT to quit: ")
	
	if userInput != "QUIT":
		print"""
Convert to:
1. Greyscale
2. Luminosity B&W
3. Sepia
4. PIL Built-In B&W
	
5. Quit Program
		
"""
		keepGoing = True
		while keepGoing:
			choice = raw_input("> ")
			if choice == "1":
				greyscale(userInput)
				print "Any other conversions for this image?"
				
			elif choice == "2":
				luminosity(userInput)
				print "Any other conversions for this image?"
				
			elif choice == "3":
				sepia(userInput)
				print "Any other conversions for this image?"
				
			elif choice == "4":
				pilBlackAndWhite(userInput)
				print "Any other conversions for this image?"
			
			elif choice == "5":
				print "Thanks for using this program. Bye!"
				keepGoing = False
				
			else:
				print "I'm not sure what you mean, try again"

	
if __name__ == "__main__":
	print "Welcome to the Image Conversion Program"
	print ""
	print ""
	
	mainMenu()