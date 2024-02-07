#
#
#
#
music = "classical"

print(music == "classical")

music = "classical"
shopping_list = []
num = 0
name = ""
my_name = "Dave"


# print("What coat is always wet when you put it on ?")
# # answer = input("   >    ").lower()
               
# if "paint" in answer:
#     print("Correct!")



def add_Up(num1, num2):
    print(num1 + num2)

print(add_Up(4, 7))


def add_Up_2(num1, num2):
    return num1 + num2

print(add_Up_2(4, 7))


dinosaurs = [
"Triceratops",
"Velociraptor",
"Ankylyosaurus",
"Archaopteryx",
"Tyranosaurus Rex",
"Stegosaurus",
"Iguandon"
]

saurus_dicosaurs =[]

for dino in dinosaurs:
    if "saurus" in dino:
        saurus_dicosaurs.append(dino)

print(saurus_dicosaurs)

saurus_dicosaurs_2 = [dino for dino in dinosaurs if "saurus" in dino]

print(saurus_dicosaurs_2)


