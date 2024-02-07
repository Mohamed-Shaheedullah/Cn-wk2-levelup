

while True:
    try:
        num_apples = int(input("Please type the number of apples you want to buy "))
        break
    except ValueError:
        print("please use integers only !")    
        
price_1 = num_apples * 25
print(f"The price is {price_1} in pence")


# price_2_pence = (num_apples * 25) % 100
# print(price_2_pence)
# price_2_pounds = (num_apples* 25) - price_2_pence