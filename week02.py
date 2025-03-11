#1) ice americano : 2000 2) cafe latte : 3000
prices=[2000,3000]
drinks=["ice americano","cafe latte"]
while True:

    menu = input(f"1) {drinks[0]} {prices[0]}  2) {drinks[1]} {prices[1]}  3) exit : ")
    if menu=="1":
        print(f"{drinks[0]} ordered. Price: {prices[0]} won")

    elif menu=="2":
        print(f"{drinks[1]} ordered. Price: {prices[1]} won")

    elif menu=="3":
        print("finish order~")
        break
    else:
        print(f"{menu} menu is not exist. pleas choose from above menu.")
