
drinks=["ice americano","cafe latte","Watermelon juice"]
prices=[2000,3000,4900]
total_price=0
amounts=[0,0,0]

def order_process(idx: int):
    global total_price
    print(f"{drinks[idx]} ordered. Price: {prices[idx]} won")
    total_price += prices[idx]
    amounts[idx] += 1


menu_lists=""
for k in range(len(drinks)):
    menu_lists+=f"{k+1}) {drinks[k]} {prices[k]}won "
menu_lists+=f"{len(drinks)+1}) Exit: "


while True:

    menu = input(menu_lists)
    if menu=="1":
        order_process(0)
    elif menu=="2":
        order_process(1)
    elif menu=="3":
        order_process(2)

    elif menu=="4":
        print("finish order~")
        break
    else:
        print(f"{menu} menu is not exist. pleas choose from above menu.")


print("Product  Price  Amount  Total")
for i in range(len(drinks)):
    if amounts[i]>0:
        print(f"{drinks[i]} {prices[i]} x{amounts[i]} {prices[i] * amounts[i]}")

print(f"total price: {total_price}")
