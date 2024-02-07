#
#
#
#
guest_list = ["Alice",
"James",
"Lucy",
"Henry",
"Emma"
]

barred_list = [
"George",
"Olivia",
"William",
"Grace",
"Edward"
]

person = input("Please enter name of guest:   ")

if person in guest_list:
    print(f"{person} can enter")
elif person in barred_list:
    print(f"{person} cannot enter")
else:
    print(f"{person} must wait")


