import cv2
from PIL import Image 
import random 
import os, sys


def get_preview(file_name):
	cap = cv2.VideoCapture(file_name)
	fps = cap.get(cv2.CAP_PROP_FPS)
	duration = cap.get(cv2.CAP_PROP_FRAME_COUNT)

	frames_read = 0 
	frame_to_take = int(duration / 2)
	ret, frame = cap.read()
	while ret:
		if frames_read == frame_to_take:
			ret, frame = cap.read()
			return Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR), 'RGB')

		frames_read +=1
		ret, _ = cap.read() 


def main():
	for file in os.scandir(sys.argv[1]):
		image = get_preview(file.path).resize((364, 205))
		print(file.name)
		print(file.name[0:file.name.rfind('.')] + '.jpg')
		image.save(sys.argv[2] + '\\' + file.name[0:file.name.rfind('.')] + '.jpg')



if __name__ == '__main__':
	if not len(sys.argv) > 2:
		print('Error: you need to specify to directories: <directory_from> <directory_to>')
		exit()
	main()

