from pyautogui import *
from PIL import Image

def draw(img):
	width, height = img.size
	container = img.load()
	line = 0
	m = position()
	for x in range(width):
		for y in range(height):
			if sum(container[x, y]) // 3 > 128:
				click()
			moveTo(position()[0] + 1, position()[1] + line)
		line += 1

if __name__ == '__main__':
	file = Image.open("lenna.png")
	#file.convert('L')
	draw(file)