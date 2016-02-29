import numpy
import wave
from struct import unpack

data = wave.open("data_low.wav", 'r')

print(data.getsampwidth())
print(data.getframerate())


def toArrayIndex(x, y):
  return y * 1024 + x

from PIL import Image
img = Image.new('L', (1024, 256))

mylist = [100 for i in range(1024 * 256)]

for i in range(100):
  frames = data.readframes(1024)

print(len(frames))
for i, frame in enumerate(frames):
  val = unpack("<b", frame)[0]
  for y in range(0, val, 1 if val > 0 else -1):
    mylist[toArrayIndex(i, y + 128)] = 255

img.putdata(mylist)
img.save("image.jpg")

data.close()
