# names = ["ariel", "adi","eran", "adir","daniel"]
# str1 = "hello world"
# for i in range (5):
#     print(names[i])
# for name in names:
#     print (name)

# a = 0
# while a < 10:
#     a = a+1
#     if a == 5:
#         continue
#     print (a)

for i in range (1, 101):
    if i%7==0 or "7" in str(i):
        continue
    print (i)
