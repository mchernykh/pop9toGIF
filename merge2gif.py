from PIL import Image, ImageSequence
import sys, os, glob
from images2gif import writeGif

# depends on: numpy, PIL, images2gif.py


def main():
	fl = glob.glob(sys.argv[1])
	fl = sorted(fl)
	images = []
	for fn in fl:
		im = Image.open(fn)
		images.append(im)
	writeGif(sys.argv[2], images, duration = 60.0/1000.0)
	return
	
if __name__ == "__main__":
	main()