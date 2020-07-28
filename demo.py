from PIL import Image
from random import randrange

R, G, B = 0, 1, 2

def mosaicing(img):
	width, height = img.size
	container = img.load()
	for x in range(width):
		for y in range(height):
			if not x % 2 and not y % 2:
				container[x, y] = (0, 0, container[x, y][B])
			elif x % 2 and y % 2:
				container[x, y] = (container[x, y][R], 0, 0)
			else:
				container[x, y] = (0, container[x, y][G], 0)

def demosaic(img):
	width, height = img.size
	container = img.load()
	for x in range(width):
		for y in range(height):
			try:
				red = (container[x - 1, y - 1][R] + container[x + 1, y + 1][R]) // 2
				green = (container[x - 1, y - 1][G] + container[x + 1, y + 1][G]) // 2
				blue = (container[x - 1, y - 1][B] + container[x + 1, y + 1][B]) // 2
			except IndexError:
				red = container[x - 1, y - 1][R]
				green = container[x - 1, y - 1][G]
				blue = container[x - 1, y - 1][B]
			if not x % 2 and not y % 2:
				container[x, y] = (red, green, container[x, y][B])
			elif x % 2 and y % 2:
				container[x, y] = (container[x, y][R], green, blue)
			else:
				container[x, y] = (red, container[x, y][G], blue)

def demosaic2(img):
	width, height = img.size
	container = img.load()
	for x in range(width - 1):
		for y in range(height - 1):
			if not x % 2 and not y % 2:
				red = container[x + 1, y + 1][R]
				green = (container[x, y + 1][G] + container[x + 1, y][G]) // 2
				container[x, y] = (red, green, container[x, y][B])
			elif x % 2 and y % 2:
				green = (container[x, y + 1][G] + container[x + 1, y][G]) // 2
				blue = container[x + 1, y + 1][B]
				container[x, y] = (container[x, y][R], green, blue)
			else:
				red = container[x, y + 1][R]
				blue = container[x + 1, y][B]
				container[x, y] = (red, container[x, y][G], blue)

def bilinear(img):
	width, height = img.size
	container = img.load()
	for x in range(1, width - 1):
		for y in range(1, height - 1):
			if not x % 2 and not y % 2:
				red = (container[x - 1, y - 1][R] + container[x + 1, y + 1][R] + container[x + 1, y - 1][R] + container[x - 1, y + 1][R]) // 4
				green = (container[x, y + 1][G] + container[x + 1, y][G] + container[x, y - 1][G] + container[x - 1, y][G]) // 4
				container[x, y] = (red, green, container[x, y][B])
			elif x % 2 and y % 2:
				green = (container[x, y + 1][G] + container[x + 1, y][G] + container[x, y - 1][G] + container[x - 1, y][G]) // 4
				blue = (container[x - 1, y - 1][B] + container[x + 1, y + 1][B] + container[x + 1, y - 1][B] + container[x - 1, y + 1][B]) // 4
				container[x, y] = (container[x, y][R], green, blue)
			else:
				red = (container[x, y + 1][R] + container[x + 1, y][R] + container[x, y - 1][R] + container[x - 1, y][R]) // 4
				blue = (container[x, y + 1][B] + container[x + 1, y][B] + container[x, y - 1][B] + container[x - 1, y][B]) // 4
				container[x, y] = (red, container[x, y][G], blue)

def resize(img, ratio=0.5):
	width, height = img.size
	container = img.load()
	new_img = Image.new('RGBA', (int(width * ratio), int(height * ratio)))
	new = new_img.load()
	for x in range(int(width * ratio - 1)):
		for y in range(int(height * ratio - 1)):
			new[x, y] = container[x // 2, y // 2]
			new[x + 1, y] = container[x // 2, y // 2]
			new[x, y + 1] = container[x // 2, y // 2]
			new[x + 1, y + 1] = container[x // 2, y // 2]
	return new

def brighten(img, ratio=1.5):
	width, height = img.size
	container = img.load()
	for x in range(width):
		for y in range(height):
			container[x, y] = tuple(int(i * ratio) for i in container[x, y])


if __name__ == '__main__':
	'''
	img = Image.new('RGB', (128, 128))
	bayer_pattern(img)
	img.save("teste.png")'''

	mosaic = Image.open("lenna.png")
	mosaicing(mosaic)
	mosaic.save("teste2.png")

	'''demo = Image.open("teste2.png")
	demosaic(demo)
	demo.save("teste3.png")'''

	demo2 = Image.open("teste2.png")
	bilinear(demo2)
	demo2.save("teste4.png")

	demo = Image.open("teste2.png")
	demosaic(demo)
	demo.save("teste3.png")

	'''lenna = Image.open("lenna.png")
	brighten(lenna, ratio=0.8)
	lenna.save("brightened.png")'''

	lenna = Image.open("lenna.png")
	resize(lenna)
	lenna.save("brightened.png")