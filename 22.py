def input_names():
    names_txt = open("names.txt","a+")
    input_from_user = input("enter your name: ")
    names_txt.write(input_from_user + "\n")
    names_txt.close()

def print_names():
    names_txt = open ("names.txt", "r")
    for name in names_txt.readlines():
        print(f"hello {name}", end='')
    names_txt.close()
input_names()
input_names()
input_names()
print_names()