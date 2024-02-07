#
#
#
truthy_or_falsy = [ 0, "Hello", " ", "!!", 12, True, None, "", "0", False, "False" ]

for i in truthy_or_falsy:
    print(i)
    if i:
           
        print("Truthy")
    else:
        print("Falsy")
