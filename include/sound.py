import numpy
import wave
from struct import unpack

def toArrayIndex(x, y):
	return y * 1024 + x
	
def save_waveform(data):
	
	from PIL import Image
	img = Image.new('L', (1024, 256))
	
	mylist = [100 for i in range(1024 * 256)]
	
	for i in range(100):
	  frames = data.readframes(1024)
	
	print(len(frames))
	for i, frame in enumerate(frames):
	  val = unpack("<b", frame)[0]
	  mylist[toArrayIndex(i, val)] = 255
	#  for y in range(0, val, 1 if val > 0 else -1):
	#   mylist[toArrayIndex(i, y + 128)] = 255
	img.putdata(mylist)
	img.save("image.jpg")
	
	data.close()

def read_url(url):

	data = wave.open(url, 'r')
	print("Opening {:s}".format(url))
	print(data.getsampwidth())
	print(data.getframerate())

	return data

