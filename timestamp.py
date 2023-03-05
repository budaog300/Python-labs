import time

leapDays = 13
start = 1970
S = int(time.time())
g = S / 31536000
v = (g % 4 == 0 and g % 100 != 0 or g % 400 == 0) if g else False
Y = S / (31622400 if v else 31536000)
M = (S / (2635200 if v else 2628000)) % 12
D = (S / 86400) % ((28 + ((0x3bbeecc >> int(2 * M)) & 3)) if M else 31) - leapDays + 1
h = (S / 3600) % 24 + 4
m = (S / 60) % 60
s = S % 60
Output = (str(int(start + Y)) + "-" + str('{:02}'.format(int(M + 1))) + "-" + str('{:02}'.format(int(D))) + " "
          + str('{:02}'.format(int(h))) + ":" + str('{:02}'.format(int(m))) + ":" + str('{:02}'.format(int(s))))
print(Output)
