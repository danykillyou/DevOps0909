# try:
#     f = open("asd.txt")
# except FileNotFoundError as e:
#     print(e.args)
#
import io

try:
    f = open("7.py","r")
    f.write("a")
except io.UnsupportedOperation as e:
    print(e.args)

