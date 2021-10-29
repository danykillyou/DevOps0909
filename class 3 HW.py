#1-2
try:
    a=1/0
except ZeroDivisionError as e:
    print(e)
#3 legal
try :
    x = 1
finally :
    print("finally")

#4 all exceptions

#5 it's impossible to catch the exception error reason

#6 """ except IOError.It is an error raised when an input/output operation fails,
# such as the print statement or the open() function when trying to open a file that does not exist.
# It is also raised for operating system-related errors.
# except ZeroDivisionError. ZeroDivisionError occurs when a number is divided by a zero.
# In Mathematics, when a number is divided by a zero, the result is an infinite number.
# It is impossible to write an Infinite number physically. Python interpreter throws
# “ZeroDivisionError: division by zero” error if the result is infinite number.
#
# You can divide a number by another number. The division operation divides a number
# into equal parts or groups. Dividing a number into zero pieces or zero groups is meaning less.
# In mathematics, dividing a number by zero is undefined.
#
# If a number is divided by zero, the result wil be infinite number.
# Python can not handle the infinite number because the infinite number is difficult to
# write in concrete form. In this case, Python throws “ZeroDivisionError: division by zero”. """

# 7-10
file = open("words.txt", "w", encoding="utf-8")
file.write(input("something"))
file.close()

file = open("words.txt", "r", encoding="utf-8")
content = file.read()
file.close()

print(content)

# 11
from PIL import Image, ImageDraw

img = Image.new('RGB', (100, 30), color=(73, 109, 137))

d = ImageDraw.Draw(img)
d.text((10, 10), "Hello World", fill=(255, 255, 0))

img.save('pil_text.png')
