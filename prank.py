import rotatescreen
import time

screen = rotatescreen.get_primary_display()
# n = int(input("Enter the number of rotation you wanna see!"))
for i in range(13):
    time.sleep(1.75)
    screen.rotate_to(i * 90 % 360)
