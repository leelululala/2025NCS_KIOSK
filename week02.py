#1) ice americano : 2000 2) cafe latte : 3000
prices=[2000,3000]
while True:

    menu = input(f"1) ice americano {prices[0]}  2) cafe latte {prices[1]}  3) exit : ")
    if menu=="1":
        print(f"ice americano ordered. Price: {prices[0]} won")

    elif menu=="2":
        print(f"cafe latte ordered. Price: {prices[1]} won")

    elif menu=="3":
        print("finish order~")
        break
