#!/usr/bin/python

import click
from include import sound

@click.command()
@click.option('--url', help='Sound source', prompt='Enter .wav file: ', default='sampleset/data_low.wav')
@click.option('-o', default='image.jpg', prompt='Enter output file: ', help='File output')

def main(url, o):
	data = sound.read_url("sampleset/data_low.wav")
	# sound.save_waveform(data)
	sound.fft(url)

if __name__ == '__main__':
	main()	
