import pygame
import math, random, fractions
pygame.init()

def sin (angle):
	# Degree sine
	return math.sin(math.radians(angle))

def cos (angle):
	# Degree cosine
	return math.cos(math.radians(angle))

def cyclolist(imgsize, radii):
	# Function generates a set of image coordinates to approximate a spirograph with the given dimensions.

	# Center offset so the spirograph is properly centered on the image.
	cenx, ceny = imgsize[0] / 2, imgsize[1] / 2
	# Fixed radius, moving radius, and pen offset.
	# Fixed radius can be any value. Negative values just flip the spirograph, and zero values create circles.
	# Positive values for moving radius creates epicycloids, while negative values creates hypocycloids. r = 0 is undefined.
	# Pen offset can be any value. Negative values, again, will just flip the spirograph.
	fixrad, movrad, offset = radii[:3]
	if movrad == 0: raise ZeroDivisionError('The moving circle\'s radius cannot be zero!')
	# Scale makes sure that the spirograph fits the image dimensions properly.
	# The scale factor is ideally half the side length of a square image.
	# The furthest points from the center of a spirograph are at a distance abs(R + o) + r from the center.
	scalefac = (cenx if cenx < ceny else ceny) / ((abs(fixrad + offset) + movrad) * 1.2)
	# Number of revolutions around the fixed circle to perform.
	# The number of revolutions required to complete a spirograph is equal to the LCM of R and r divided by R.
	max_rotations = float(movrad) / fractions.gcd(fixrad, movrad)
	# Returns a list of points on the image that correspond to vertices on the spirograph.
	phi = random.randint(0, 360)
	return [
		[
			((fixrad + movrad) * cos(t + phi) + offset * cos(((fixrad + movrad) * (t + phi) / movrad))) * scalefac + cenx, 
			((fixrad + movrad) * sin(t + phi) + offset * sin(((fixrad + movrad) * (t + phi) / movrad))) * scalefac + ceny
		] for t in range(int(max_rotations * 360))
		]

_ssurf = pygame.Surface((100, 100))
pygame.draw.aalines(_ssurf, (0, 255, 0), True, cyclolist(_ssurf.get_size(), (10, 7, 7)))
pygame.image.save(_ssurf, 'spiro.png')