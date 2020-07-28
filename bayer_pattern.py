def bayer_pattern(img, randomize=True):
	width, height = img.size
	container = img.load()
	start = 0

	if not randomize:
		start = 255

	for x in range(width):
		for y in range(height):
			if not x % 2 and not y % 2:
				container[x, y] = (0, 0, randrange(start, 256))
			elif x % 2 and y % 2:
				container[x, y] = (randrange(start, 256), 0, 0)
			else:
				container[x, y] = (0, randrange(start, 256), 0)