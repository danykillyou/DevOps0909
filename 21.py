my_file = open("read_my_contents.txt","r")
#print(list(my_file.readlines()))
for line in my_file.readlines():
    if "error" in line:
        print("*"+line+"*", end='')
    else:
        print ("no")