from PIL import Image, ImageSequence
import sys, os
from images2gif import writeGif

# depends on: numpy, PIL, images2gif.py




def get9boxes((width, height),vertical_gap = 20, gorizontal_gap = 8):	
	width_step = (width - 2 * gorizontal_gap) / 3
	height_step = (height - 2 * vertical_gap) / 3
	boxes = [(i * (width_step + gorizontal_gap), j * (height_step + vertical_gap), i * (width_step + gorizontal_gap) + width_step, j * (height_step + vertical_gap) + height_step) for i in range(0,3) for j in range(0,3)]
	return sorted(boxes, key = lambda t: [t[1], t[0]])
	
def main():
	if len(sys.argv) <= 1:
		print "Usage python pop9toGIF.py target_image.jpg"
		return
	
	im = Image.open(sys.argv[1])
	im_enlarged = im.resize((3*im.size[0], 3 * im.size[1]))
	boxes = get9boxes(im_enlarged.size)
	images = [im_enlarged.crop(box) for box in boxes]
	images_small = [i.resize((im.size[0] / 3, im.size[1] / 3)) for i in images]
	preorder = [1,2,3,6,9,8,7,4]
	# preorder = [4,5, 6, 5]
	# preorder = [1,2,3,6,9,8,7,4, 7, 8, 9, 6, 3, 2, 1]
	# 123
	# 456
	# 789
	order = [i - 1 for i in preorder]
	images_reordered = [images_small[i] for i in order]
	writeGif(os.path.splitext(sys.argv[1])[0] + ".gif", images_reordered, duration = 0.1)
	return
	
if __name__ == "__main__":
	main()