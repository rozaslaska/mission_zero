from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(270)
purple = (144, 1, 255)
sense.show_message("Hi from: Roza, Asia and Natalia",text_colour=purple, scroll_speed=0.06)

r = (255, 0, 68)
b = (166,60,3)
p = (119, 30, 47)
n = (0,181,228)
z = (27, 73, 47)
f = (71, 0, 68)
picture = [
    n, n, n, n, n, n, n, n,
    n, n, r, p, r, n, p, r,
    n, f, r, f, r, r, r, p,
    n, r, r, b, p, f, p, r,
    n, p, b, b, p, b, b, f,
    n, r, p, b, b, b, p, f,
    n, n, n, b, b, n, n, n,
    z, z, b, b, b, z, z, z
]
sense.set_pixels(picture)
sleep(2)

z = (252,244,2)
b = (0,181,228)
f = (71,0,68)
k = (217,162,132)
picture = [
b, b, b, b, b, b, b, b,
b, z, z, z, z, z, b, b,
b, z, z, k, z, z, b, b,
b, z, k, k, k, z, b, b,
b, z, k, k, k, z, b, b,
b, z, z, k, z, z, b, b,
b, z, f, f, f, z, b, b, 
b, b, k, f, k, b, b, b,
]
sense.set_pixels(picture)
sleep(2)

b = (102, 57, 3)
n = (0,181,228)
z = (1, 65, 3)
k = (217,162,132)
picture = [
n, n, n, n, n, n, n, n,
n, b, b, b, b, b, n, n,
n, b, b, k, b, b, n, n,
n, b, k, k, k, b, n, n,
n, b, k, k, k, b, n, n,
n, b, b, k, b, b, n, n,
n, b, z, z, z, b, n, n, 
n, b, k, z, k, b, n, n,
]
sense.set_pixels(picture)
sleep(2)

b = (102, 57, 3)
n = (0,181,228)
r = (254, 50, 198)
k = (217,162,132)
picture = [
n, n, n, n, n, n, n, n,
n, b, b, b, b, b, n, n,
n, b, b, k, b, b, n, n,
n, b, k, k, k, b, n, n,
n, b, k, k, k, b, n, n,
n, b, b, k, b, b, n, n,
n, n, r, r, r, n, n, n, 
n, n, k, r, k, n, n, n,
]
sense.set_pixels(picture)
sleep(2)

humid = round (sense.humidity)
blue = (0, 0, 104)
white = (255, 254, 255)
sense.show_message( "Jest " + str(humid) + " %",text_colour=blue, back_colour=white, scroll_speed=0.05)
