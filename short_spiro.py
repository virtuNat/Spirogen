import pygame as P, math
from fractions import gcd as g
P.init()
_s=lambda t:math.sin(math.radians(t))
_c=lambda t:math.cos(math.radians(t))
def G(s,_r):
	h,k=[d/2 for d in s];R,r,o=_r[:3]
	if r==0:raise ZeroDivisionError
	f=(h if h<k else k)/((abs(R+o)+r)*1.2)
	return[[((R+r)*_c(t)+o*_c(((R+r)*(t)/r)))*f+h,((R+r)*_s(t)+o*_s(((R+r)*(t)/r)))*f+k]for t in range(int(360*float(r)/g(R,r)))]
_S = P.Surface((100,100))
P.draw.aalines(_S,(0, 255, 0),True,G(_S.get_size(),(10,7,7)))
P.image.save(_S,'spiro.png')