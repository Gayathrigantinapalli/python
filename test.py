# import random
# print(random.randint(0,9))



# import random
# print (random.randint(20,2)




# import random
# num=random.randint(4,99)
# print(num)


# import random
# char="abcdefghijklmnopqrstuvwxyz123456789"
# password=""
# for i in range(8):
#     password+=random.chice(char)
# print("possword:" ,password)



import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890"
password = ""

for i in range(8):
    password += random.choice(chars)

print("Password:", password)






