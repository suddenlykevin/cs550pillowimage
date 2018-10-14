# Pillow Images
# Kevin Xie CS550
#
# We used the Image library from Pillow to create algorithmically generated images
# My images include a solid red image, the red gradients example from class, two experiments
# with colors, and an HSV color wheel
#
# sources:
# Image modes (learned from processing): https://pillow.readthedocs.io/en/5.3.x/handbook/concepts.html#concept-modes
# converting to RGB: https://stackoverflow.com/questions/21669657/getting-cannot-write-mode-p-as-jpeg-while-operating-on-jpg-image
#
# On My Honor, I have neither given nor received unauthorized aid.

from PIL import Image
# defining image size
imgx=512
imgy=512

image = Image.new("RGB",(imgx,imgy))
# For every pixel in every row and column, fill with color red
for x in range(imgx):
	for y in range(imgy):
		image.putpixel((x,y),(255,0,0))

image.save("demo_image.png") # solid red image
# For every pixel in every row and column, divide x into 8 divisions of red gradients
for x in range(imgx):
	for y in range(imgy):
		image.putpixel((x,y),((x%64)*255//64,0,0)) # 64 is 1/8 of 512, xmod64 divided by 64 is the "darkness" of red for that column (after being multiplied by 255)

image.save("gradient_image.png") # gradients image
# My first attempt at a color wheel, looks more like claws. Divide image in to 3 overlapping columns and make each color peak and decrease in the columns
for x in range(imgx):
	for y in range(imgy):
		r=0
		g=0
		b=0
		if x<=256: 
			if x<=128:
				r=x*2-y//2 # ascending in color as x increases and brightness as y decreases
			else: 
				r=255-(x-128)*2-y//2 # descending in color as x increases and ascending in brightness as y decreases
		if 128<x<=384:
			if x<=256:
				g=(x-128)*2-y//2
			else:
				g=255-(x-256)*2-y//2
		if x>256:
			if x<=384:
				b=(x-256)*2-y//2
			else:
				b=255-(x-384)*2-y//2
		image.putpixel((x,y),(r,g,b))

image.save("neonclaws.png") # COLORFUL CLAWS
# My second attempt at a color wheel, looks like a psychedelic spotlight thing. Just changed y from a subtract to an addition
for x in range(imgx):
	for y in range(imgy):
		r=0
		g=0
		b=0
		if x<=256: 
			if x<=128:
				r=x*2+y//2 # ascending in color as x increases and descending in brightness as y decreases
			else: 
				r=255-(x-128)*2+y//2 # descending in color as x increases and brightness as y decreases
		if 128<x<=384:
			if x<=256:
				g=(x-128)*2+y//2
			else:
				g=255-(x-256)*2+y//2
		if x>256:
			if x<=384:
				b=(x-256)*2+y//2
			else:
				b=255-(x-384)*2+y//2
		image.putpixel((x,y),(r,g,b))

image.save("psycholights.png") # COLORFUL LIGHTS

colorwheel = Image.new("HSV",(imgx,imgy)) # Image modes (learned from processing): https://pillow.readthedocs.io/en/5.3.x/handbook/concepts.html#concept-modes

for x in range(imgx):
	for y in range(imgy):
		colorwheel.putpixel((x,y),(x*255//512,y,255-(y*255//512))) # Hue, Saturation, and Visibility values change corresponding to x and y values

colorwheel.convert("RGB").save("colors.png") # converting to RGB: https://stackoverflow.com/questions/21669657/getting-cannot-write-mode-p-as-jpeg-while-operating-on-jpg-image